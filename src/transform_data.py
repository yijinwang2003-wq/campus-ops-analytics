"""Transform raw synthetic source data into Power BI-ready CSV outputs."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
POWERBI_DIR = PROJECT_ROOT / "data" / "powerbi"
SNAPSHOT_DATE = pd.Timestamp("2025-06-30")


def read_csv(filename: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / filename, **kwargs)


def transform_budget() -> pd.DataFrame:
    budget = read_csv("budget_monthly.csv")
    grouped = (
        budget.groupby(["department_id", "department_name", "fiscal_year"], as_index=False)
        .agg(
            total_budget=("monthly_budget", "sum"),
            total_actual_spend=("actual_spend", "sum"),
            total_committed_amount=("committed_amount", "sum"),
        )
    )
    grouped["budget_variance"] = grouped["total_budget"] - grouped["total_actual_spend"]
    grouped["budget_utilization_pct"] = grouped["total_actual_spend"] / grouped["total_budget"] * 100
    grouped["budget_variance_pct"] = grouped["budget_variance"] / grouped["total_budget"] * 100
    grouped["is_over_budget"] = grouped["total_actual_spend"] > grouped["total_budget"]
    numeric_cols = ["total_budget", "total_actual_spend", "total_committed_amount", "budget_variance", "budget_utilization_pct", "budget_variance_pct"]
    grouped[numeric_cols] = grouped[numeric_cols].round(2)
    return grouped


def transform_budget_monthly() -> pd.DataFrame:
    budget = read_csv("budget_monthly.csv")
    budget["budget_variance"] = budget["monthly_budget"] - budget["actual_spend"]
    budget["budget_utilization_pct"] = budget["actual_spend"] / budget["monthly_budget"] * 100
    budget["budget_variance_pct"] = budget["budget_variance"] / budget["monthly_budget"] * 100
    budget["is_over_budget"] = budget["actual_spend"] > budget["monthly_budget"]
    numeric_cols = ["monthly_budget", "actual_spend", "committed_amount", "budget_variance", "budget_utilization_pct", "budget_variance_pct"]
    budget[numeric_cols] = budget[numeric_cols].round(2)
    return budget


def transform_procurement() -> pd.DataFrame:
    procurement = read_csv("procurement_requests.csv")
    date_columns = ["request_date", "approval_date", "po_date", "invoice_date"]
    for column in date_columns:
        procurement[column] = pd.to_datetime(procurement[column], errors="coerce")

    procurement["days_to_approve"] = (procurement["approval_date"] - procurement["request_date"]).dt.days
    procurement["days_to_complete"] = (procurement["invoice_date"] - procurement["request_date"]).dt.days
    procurement["is_approval_delayed"] = procurement["days_to_approve"] > 10
    procurement["approval_month"] = procurement["approval_date"].dt.to_period("M").astype(str)
    return procurement


def transform_maintenance() -> pd.DataFrame:
    maintenance = read_csv("maintenance_requests.csv")
    maintenance["request_date"] = pd.to_datetime(maintenance["request_date"], errors="coerce")
    maintenance["completed_date"] = pd.to_datetime(maintenance["completed_date"], errors="coerce")
    maintenance["days_to_resolve"] = (maintenance["completed_date"].fillna(SNAPSHOT_DATE) - maintenance["request_date"]).dt.days
    maintenance["is_critical_over_48h"] = (
        (maintenance["priority"] == "Critical")
        & (maintenance["status"] != "Completed")
        & (maintenance["days_to_resolve"] > 2)
    )
    maintenance["actual_cost"] = pd.to_numeric(maintenance["actual_cost"], errors="coerce")
    return maintenance


def transform_hr() -> pd.DataFrame:
    hr = read_csv("hr_monthly.csv")
    hr["month_start_date"] = pd.to_datetime(hr["month_start_date"], errors="coerce")
    grouped = (
        hr.groupby(["department_id", "department_name", "fiscal_year", "fiscal_period", "month_start_date"], as_index=False)
        .agg(
            total_headcount=("headcount", "sum"),
            total_fte=("fte", "sum"),
            total_salary_expense=("total_salary_expense", "sum"),
            overtime_expense=("overtime_expense", "sum"),
            vacancies=("vacancies", "sum"),
            turnover_count=("turnover_count", "sum"),
        )
        .sort_values(["department_id", "month_start_date"])
    )
    grouped["avg_salary_per_headcount"] = grouped["total_salary_expense"] / grouped["total_headcount"]
    grouped["headcount_prior_month"] = grouped.groupby("department_id")["total_headcount"].shift(1)
    grouped["headcount_change"] = grouped["total_headcount"] - grouped["headcount_prior_month"]
    numeric_cols = ["total_fte", "total_salary_expense", "overtime_expense", "avg_salary_per_headcount"]
    grouped[numeric_cols] = grouped[numeric_cols].round(2)
    return grouped


def main() -> None:
    POWERBI_DIR.mkdir(parents=True, exist_ok=True)

    outputs = {
        "budget_summary.csv": transform_budget(),
        "budget_monthly_dashboard.csv": transform_budget_monthly(),
        "procurement_dashboard.csv": transform_procurement(),
        "maintenance_dashboard.csv": transform_maintenance(),
        "hr_workforce_dashboard.csv": transform_hr(),
        "dim_department.csv": read_csv("departments.csv"),
        "dim_date.csv": read_csv("date_dimension.csv"),
    }

    for filename, dataframe in outputs.items():
        dataframe.to_csv(POWERBI_DIR / filename, index=False)
        print(f"Wrote {filename}: {len(dataframe):,} rows")


if __name__ == "__main__":
    main()
