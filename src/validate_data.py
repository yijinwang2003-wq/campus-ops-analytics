"""Validate generated and transformed analytics datasets."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
POWERBI_DIR = PROJECT_ROOT / "data" / "powerbi"


def load_datasets() -> dict[str, pd.DataFrame]:
    return {
        "departments": pd.read_csv(RAW_DIR / "departments.csv"),
        "date_dimension": pd.read_csv(RAW_DIR / "date_dimension.csv"),
        "budget_summary": pd.read_csv(POWERBI_DIR / "budget_summary.csv"),
        "budget_monthly": pd.read_csv(POWERBI_DIR / "budget_monthly_dashboard.csv"),
        "procurement": pd.read_csv(POWERBI_DIR / "procurement_dashboard.csv"),
        "maintenance": pd.read_csv(POWERBI_DIR / "maintenance_dashboard.csv"),
        "hr": pd.read_csv(POWERBI_DIR / "hr_workforce_dashboard.csv"),
    }


def validate_no_missing_department_ids(data: dict[str, pd.DataFrame]) -> None:
    valid_ids = set(data["departments"]["department_id"])
    for name in ["budget_summary", "budget_monthly", "procurement", "maintenance", "hr"]:
        ids = set(data[name]["department_id"].dropna())
        missing = ids - valid_ids
        assert not missing, f"{name} contains invalid department IDs: {sorted(missing)}"
        assert data[name]["department_id"].notna().all(), f"{name} contains missing department IDs"


def validate_dates(data: dict[str, pd.DataFrame]) -> None:
    date_checks = {
        "date_dimension": ["calendar_date", "month_start_date", "month_end_date"],
        "procurement": ["request_date", "approval_date", "po_date"],
        "maintenance": ["request_date"],
        "hr": ["month_start_date"],
    }
    for dataset_name, columns in date_checks.items():
        for column in columns:
            parsed = pd.to_datetime(data[dataset_name][column], errors="coerce")
            assert parsed.notna().all(), f"{dataset_name}.{column} contains invalid dates"


def validate_budget_calculations(data: dict[str, pd.DataFrame]) -> None:
    budget = data["budget_summary"].copy()
    expected_utilization = (budget["total_actual_spend"] / budget["total_budget"] * 100).round(2)
    expected_variance = (budget["total_budget"] - budget["total_actual_spend"]).round(2)
    expected_variance_pct = (expected_variance / budget["total_budget"] * 100).round(2)

    pd.testing.assert_series_equal(budget["budget_utilization_pct"].round(2), expected_utilization, check_names=False)
    pd.testing.assert_series_equal(budget["budget_variance"].round(2), expected_variance, check_names=False)
    pd.testing.assert_series_equal(budget["budget_variance_pct"].round(2), expected_variance_pct, check_names=False)


def validate_business_stories(data: dict[str, pd.DataFrame]) -> None:
    budget = data["budget_summary"]
    procurement = data["procurement"]
    maintenance = data["maintenance"]

    it_budget = budget[(budget["department_name"] == "Information Technology") & (budget["fiscal_year"] == 2025)].iloc[0]
    assert it_budget["budget_utilization_pct"] > 100, "IT FY2025 budget utilization should be over 100%"

    student_affairs = budget[(budget["department_name"] == "Student Affairs") & (budget["fiscal_year"] == 2025)].iloc[0]
    assert 96 <= student_affairs["budget_utilization_pct"] <= 100, "Student Affairs should be close to budget limit"

    approved = procurement.dropna(subset=["days_to_approve"])
    it_avg = approved.loc[approved["department_name"] == "Information Technology", "days_to_approve"].mean()
    university_avg = approved["days_to_approve"].mean()
    assert it_avg > university_avg, "IT approval days should exceed university average"
    assert 12 <= it_avg <= 16, f"IT approval cycle should be around 14 days, got {it_avg:.2f}"

    critical_overdue = maintenance[maintenance["is_critical_over_48h"] == True]
    assert len(critical_overdue) >= 3, "Expected critical overdue maintenance requests"


def run_all_validations() -> None:
    data = load_datasets()
    validate_no_missing_department_ids(data)
    validate_dates(data)
    validate_budget_calculations(data)
    validate_business_stories(data)
    print("All data validations passed.")


if __name__ == "__main__":
    run_all_validations()
