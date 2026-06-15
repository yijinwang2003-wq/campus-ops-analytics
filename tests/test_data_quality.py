from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
POWERBI_DIR = PROJECT_ROOT / "data" / "powerbi"


def setup_module() -> None:
    subprocess.run([sys.executable, str(PROJECT_ROOT / "src" / "generate_data.py")], check=True)
    subprocess.run([sys.executable, str(PROJECT_ROOT / "src" / "transform_data.py")], check=True)


def test_no_missing_department_ids() -> None:
    departments = pd.read_csv(RAW_DIR / "departments.csv")
    valid_ids = set(departments["department_id"])

    for filename in [
        "budget_summary.csv",
        "budget_monthly_dashboard.csv",
        "procurement_dashboard.csv",
        "maintenance_dashboard.csv",
        "hr_workforce_dashboard.csv",
    ]:
        dataframe = pd.read_csv(POWERBI_DIR / filename)
        assert dataframe["department_id"].notna().all()
        assert set(dataframe["department_id"]) <= valid_ids


def test_dates_are_valid() -> None:
    date_dimension = pd.read_csv(RAW_DIR / "date_dimension.csv")
    procurement = pd.read_csv(POWERBI_DIR / "procurement_dashboard.csv")
    maintenance = pd.read_csv(POWERBI_DIR / "maintenance_dashboard.csv")
    hr = pd.read_csv(POWERBI_DIR / "hr_workforce_dashboard.csv")

    assert pd.to_datetime(date_dimension["calendar_date"], errors="coerce").notna().all()
    assert pd.to_datetime(procurement["request_date"], errors="coerce").notna().all()
    assert pd.to_datetime(procurement["approval_date"], errors="coerce").notna().all()
    assert pd.to_datetime(maintenance["request_date"], errors="coerce").notna().all()
    assert pd.to_datetime(hr["month_start_date"], errors="coerce").notna().all()


def test_budget_utilization_calculations_are_correct() -> None:
    budget = pd.read_csv(POWERBI_DIR / "budget_summary.csv")
    expected_utilization = (budget["total_actual_spend"] / budget["total_budget"] * 100).round(2)
    expected_variance = (budget["total_budget"] - budget["total_actual_spend"]).round(2)
    expected_variance_pct = (expected_variance / budget["total_budget"] * 100).round(2)

    pd.testing.assert_series_equal(budget["budget_utilization_pct"].round(2), expected_utilization, check_names=False)
    pd.testing.assert_series_equal(budget["budget_variance"].round(2), expected_variance, check_names=False)
    pd.testing.assert_series_equal(budget["budget_variance_pct"].round(2), expected_variance_pct, check_names=False)


def test_it_budget_utilization_is_greater_than_100_percent() -> None:
    budget = pd.read_csv(POWERBI_DIR / "budget_summary.csv")
    it_budget = budget[(budget["department_name"] == "Information Technology") & (budget["fiscal_year"] == 2025)].iloc[0]
    assert it_budget["budget_utilization_pct"] > 100
    assert 105 <= it_budget["budget_utilization_pct"] <= 109


def test_it_approval_days_are_greater_than_university_average() -> None:
    procurement = pd.read_csv(POWERBI_DIR / "procurement_dashboard.csv")
    approved = procurement.dropna(subset=["days_to_approve"])
    it_avg = approved.loc[approved["department_name"] == "Information Technology", "days_to_approve"].mean()
    university_avg = approved["days_to_approve"].mean()

    assert it_avg > university_avg
    assert 12 <= it_avg <= 16


def test_critical_overdue_maintenance_requests_exist() -> None:
    maintenance = pd.read_csv(POWERBI_DIR / "maintenance_dashboard.csv")
    critical_overdue = maintenance[maintenance["is_critical_over_48h"] == True]
    assert len(critical_overdue) >= 3
