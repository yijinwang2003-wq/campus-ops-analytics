"""Generate synthetic higher education enterprise analytics source data.

The data intentionally includes realistic management stories for FY2024-FY2025:
- IT exceeds FY2025 budget by about 7%.
- Student Affairs is near its FY2025 budget limit at about 98% utilization.
- IT procurement approvals average about 14 days, roughly twice the university average.
- Facilities has critical unresolved maintenance requests older than 48 hours.
- HR trends include monthly headcount, salary, vacancy, and turnover measures.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
RANDOM_SEED = 20250615
SNAPSHOT_DATE = pd.Timestamp("2025-06-30")


@dataclass(frozen=True)
class Department:
    department_id: int
    department_name: str
    division: str
    department_type: str
    vp_owner: str
    is_academic: bool
    annual_budget_fy2025: float
    target_utilization_fy2025: float
    base_headcount: int


DEPARTMENTS = [
    Department(1, "Finance & Accounting", "Finance and Administration", "Administrative", "VP Finance", False, 4_800_000, 0.94, 44),
    Department(2, "Human Resources", "Finance and Administration", "Administrative", "VP Human Resources", False, 3_900_000, 0.93, 38),
    Department(3, "Facilities Management", "Finance and Administration", "Operations", "VP Operations", False, 8_600_000, 0.96, 118),
    Department(4, "Information Technology", "Information Services", "Administrative", "CIO", False, 7_200_000, 1.07, 82),
    Department(5, "College of Liberal Arts", "Academic Affairs", "Academic", "Provost", True, 11_500_000, 0.95, 156),
    Department(6, "College of Engineering", "Academic Affairs", "Academic", "Provost", True, 13_200_000, 0.97, 142),
    Department(7, "Student Affairs", "Student Success", "Student Services", "VP Student Affairs", False, 5_400_000, 0.98, 64),
    Department(8, "Research Administration", "Research", "Administrative", "VP Research", False, 4_600_000, 0.92, 41),
]

BUDGET_CATEGORIES = {
    "Finance & Accounting": ["Personnel", "Professional Services", "Systems", "Training"],
    "Human Resources": ["Personnel", "Recruiting", "Benefits Administration", "Training"],
    "Facilities Management": ["Personnel", "Maintenance Supplies", "Utilities", "Contract Services"],
    "Information Technology": ["Personnel", "Software", "Hardware", "Cloud Services"],
    "College of Liberal Arts": ["Personnel", "Instructional Supplies", "Travel", "Student Support"],
    "College of Engineering": ["Personnel", "Lab Equipment", "Research Support", "Travel"],
    "Student Affairs": ["Personnel", "Student Programming", "Counseling Services", "Athletics Support"],
    "Research Administration": ["Personnel", "Compliance", "Grant Systems", "Training"],
}


def fiscal_year_for_date(date_value: pd.Timestamp) -> int:
    return date_value.year + 1 if date_value.month >= 7 else date_value.year


def fiscal_month_for_date(date_value: pd.Timestamp) -> int:
    return date_value.month - 6 if date_value.month >= 7 else date_value.month + 6


def date_key(date_value: pd.Timestamp) -> int:
    return int(date_value.strftime("%Y%m%d"))


def build_departments() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "department_id": dept.department_id,
                "department_name": dept.department_name,
                "division": dept.division,
                "department_type": dept.department_type,
                "vp_owner": dept.vp_owner,
                "is_academic": dept.is_academic,
            }
            for dept in DEPARTMENTS
        ]
    )


def build_date_dimension() -> pd.DataFrame:
    dates = pd.date_range("2023-07-01", "2025-06-30", freq="D")
    records = []
    for date_value in dates:
        fy_month = fiscal_month_for_date(date_value)
        records.append(
            {
                "date_key": date_key(date_value),
                "calendar_date": date_value.date().isoformat(),
                "calendar_year": date_value.year,
                "calendar_quarter": ((date_value.month - 1) // 3) + 1,
                "calendar_month": date_value.month,
                "month_name": date_value.strftime("%B"),
                "fiscal_year": fiscal_year_for_date(date_value),
                "fiscal_quarter": ((fy_month - 1) // 3) + 1,
                "fiscal_month": fy_month,
                "month_start_date": date_value.to_period("M").start_time.date().isoformat(),
                "month_end_date": date_value.to_period("M").end_time.date().isoformat(),
                "is_month_end": date_value.is_month_end,
            }
        )
    return pd.DataFrame(records)


def build_budget(rng: np.random.Generator) -> pd.DataFrame:
    records = []
    month_starts = pd.date_range("2023-07-01", "2025-06-01", freq="MS")
    category_weights = np.array([0.62, 0.16, 0.12, 0.10])

    for dept in DEPARTMENTS:
        for fiscal_year in [2024, 2025]:
            annual_budget = dept.annual_budget_fy2025 * (0.965 if fiscal_year == 2024 else 1.0)
            target_utilization = dept.target_utilization_fy2025 if fiscal_year == 2025 else min(dept.target_utilization_fy2025 - 0.025, 0.96)
            categories = BUDGET_CATEGORIES[dept.department_name]
            annual_actual = annual_budget * target_utilization

            for category, weight in zip(categories, category_weights):
                category_budget = annual_budget * weight
                monthly_pattern = np.array([0.074, 0.078, 0.080, 0.081, 0.083, 0.087, 0.079, 0.081, 0.084, 0.086, 0.090, 0.097])
                monthly_pattern = monthly_pattern / monthly_pattern.sum()
                spend_noise = rng.normal(1.0, 0.035, size=12)
                spend_pattern = monthly_pattern * spend_noise
                spend_pattern = spend_pattern / spend_pattern.sum()

                for period in range(1, 13):
                    month_start = month_starts[(fiscal_year - 2024) * 12 + period - 1]
                    monthly_budget = category_budget * monthly_pattern[period - 1]
                    actual_spend = annual_actual * weight * spend_pattern[period - 1]
                    committed_amount = monthly_budget * rng.uniform(0.02, 0.09)
                    if dept.department_name == "Information Technology" and fiscal_year == 2025 and category in {"Software", "Cloud Services"}:
                        committed_amount = monthly_budget * rng.uniform(0.12, 0.20)

                    records.append(
                        {
                            "department_id": dept.department_id,
                            "department_name": dept.department_name,
                            "date_key": date_key(month_start),
                            "fiscal_year": fiscal_year,
                            "fiscal_period": period,
                            "budget_category": category,
                            "monthly_budget": round(monthly_budget, 2),
                            "actual_spend": round(actual_spend, 2),
                            "committed_amount": round(committed_amount, 2),
                            "funding_source": "Operating Fund" if not dept.is_academic else "Academic Operating Fund",
                            "last_updated_date": SNAPSHOT_DATE.date().isoformat(),
                        }
                    )
    return pd.DataFrame(records)


def build_procurement(rng: np.random.Generator) -> pd.DataFrame:
    vendors = {
        "Information Technology": ["Cloudbridge Systems", "Northstar Software", "Campus Network Supply", "SecureEd Platforms"],
        "Facilities Management": ["Metro Mechanical", "Capital Electric", "GreenWorks Services", "Facilities Parts Co."],
        "College of Engineering": ["LabSource Scientific", "Precision Instruments", "Academic Robotics LLC", "Research Supply Group"],
        "Student Affairs": ["Campus Events Co.", "Wellness Partners", "Athletic Supply House", "Student Engagement LLC"],
        "default": ["OfficeSource", "Professional Services Group", "Campus Supply Co.", "EduConsult Partners"],
    }
    categories = ["Software", "Equipment", "Professional Services", "Supplies", "Maintenance", "Events"]
    records = []
    request_id = 10001

    for dept in DEPARTMENTS:
        request_count = 38 if dept.department_name == "Information Technology" else 22
        for _ in range(request_count):
            request_date = pd.Timestamp(rng.choice(pd.date_range("2024-07-01", "2025-06-10", freq="D")))
            if dept.department_name == "Information Technology":
                approval_days = int(np.clip(round(rng.normal(14, 2.4)), 9, 21))
                amount = rng.uniform(18_000, 175_000)
                category = rng.choice(["Software", "Equipment", "Professional Services"])
            else:
                approval_days = int(np.clip(round(rng.normal(6.5, 2.1)), 2, 13))
                amount = rng.uniform(1_500, 85_000)
                category = rng.choice(categories)

            approval_date = request_date + pd.Timedelta(days=approval_days)
            po_date = approval_date + pd.Timedelta(days=int(rng.integers(1, 4)))
            invoice_date = po_date + pd.Timedelta(days=int(rng.integers(7, 35)))
            status = "Closed" if invoice_date <= SNAPSHOT_DATE else "Approved"

            dept_vendors = vendors.get(dept.department_name, vendors["default"])
            records.append(
                {
                    "request_number": f"REQ-{request_id}",
                    "department_id": dept.department_id,
                    "department_name": dept.department_name,
                    "request_date": request_date.date().isoformat(),
                    "request_date_key": date_key(request_date),
                    "approval_date": approval_date.date().isoformat(),
                    "approval_date_key": date_key(approval_date),
                    "po_date": po_date.date().isoformat(),
                    "po_date_key": date_key(po_date),
                    "invoice_date": invoice_date.date().isoformat() if invoice_date <= SNAPSHOT_DATE else "",
                    "invoice_date_key": date_key(invoice_date) if invoice_date <= SNAPSHOT_DATE else "",
                    "vendor_name": rng.choice(dept_vendors),
                    "procurement_category": category,
                    "request_amount": round(amount, 2),
                    "approved_amount": round(amount * rng.uniform(0.96, 1.0), 2),
                    "request_status": status,
                    "approval_level": "Cabinet Review" if amount >= 100_000 else "Director Review" if amount >= 25_000 else "Manager Review",
                    "finance_reviewer": rng.choice(["A. Chen", "M. Rivera", "S. Patel", "J. Morgan"]),
                    "is_competitive_bid": amount >= 50_000,
                }
            )
            request_id += 1
    return pd.DataFrame(records)


def build_maintenance(rng: np.random.Generator) -> pd.DataFrame:
    buildings = ["Administration Hall", "Science Center", "Engineering Complex", "Student Union", "Library", "Residence Hall A", "Central Plant"]
    request_types = ["HVAC", "Electrical", "Plumbing", "Custodial", "Life Safety", "General Repair"]
    teams = ["Mechanical", "Electrical", "Building Services", "Life Safety", "Grounds"]
    records = []
    work_order_id = 70001

    for dept in DEPARTMENTS:
        request_count = 34 if dept.department_name == "Facilities Management" else 10
        for _ in range(request_count):
            request_date = pd.Timestamp(rng.choice(pd.date_range("2024-07-01", "2025-06-27", freq="D")))
            priority = rng.choice(["Low", "Medium", "High", "Critical"], p=[0.38, 0.38, 0.18, 0.06])
            completion_days = {"Low": 12, "Medium": 7, "High": 3, "Critical": 1}[priority] + int(rng.integers(0, 4))
            completed_date = request_date + pd.Timedelta(days=completion_days)
            is_completed = completed_date <= SNAPSHOT_DATE and rng.random() > 0.08
            estimated_cost = rng.uniform(150, 18_000)

            records.append(
                {
                    "work_order_number": f"WO-{work_order_id}",
                    "department_id": dept.department_id,
                    "department_name": dept.department_name,
                    "request_date": request_date.date().isoformat(),
                    "request_date_key": date_key(request_date),
                    "completed_date": completed_date.date().isoformat() if is_completed else "",
                    "completed_date_key": date_key(completed_date) if is_completed else "",
                    "building_name": rng.choice(buildings),
                    "request_type": rng.choice(request_types),
                    "priority": priority,
                    "status": "Completed" if is_completed else "Open",
                    "estimated_cost": round(estimated_cost, 2),
                    "actual_cost": round(estimated_cost * rng.uniform(0.85, 1.25), 2) if is_completed else "",
                    "assigned_team": rng.choice(teams),
                }
            )
            work_order_id += 1

    for request_date, building, request_type in [
        ("2025-06-24", "Science Center", "HVAC"),
        ("2025-06-25", "Student Union", "Life Safety"),
        ("2025-06-26", "Residence Hall A", "Electrical"),
        ("2025-06-20", "Central Plant", "Plumbing"),
    ]:
        records.append(
            {
                "work_order_number": f"WO-{work_order_id}",
                "department_id": 3,
                "department_name": "Facilities Management",
                "request_date": request_date,
                "request_date_key": int(request_date.replace("-", "")),
                "completed_date": "",
                "completed_date_key": "",
                "building_name": building,
                "request_type": request_type,
                "priority": "Critical",
                "status": "Open",
                "estimated_cost": round(rng.uniform(8_000, 32_000), 2),
                "actual_cost": "",
                "assigned_team": rng.choice(["Mechanical", "Electrical", "Life Safety"]),
            }
        )
        work_order_id += 1

    return pd.DataFrame(records)


def build_hr(rng: np.random.Generator) -> pd.DataFrame:
    records = []
    month_starts = pd.date_range("2023-07-01", "2025-06-01", freq="MS")
    employee_groups = [("Faculty", 0.46), ("Staff", 0.42), ("Student Workers", 0.12)]

    for dept in DEPARTMENTS:
        for month_index, month_start in enumerate(month_starts):
            fiscal_year = fiscal_year_for_date(month_start)
            fiscal_period = fiscal_month_for_date(month_start)
            growth = 1 + (0.018 * (month_index / 23))
            if dept.department_name == "Information Technology" and fiscal_year == 2025:
                growth += 0.035
            if dept.department_name == "Student Affairs" and fiscal_year == 2025:
                growth += 0.02

            total_headcount = max(1, round(dept.base_headcount * growth + rng.normal(0, 1.5)))
            for group, share in employee_groups:
                if group == "Faculty" and not dept.is_academic:
                    group_share = 0.0
                elif group == "Student Workers" and dept.department_name in {"Student Affairs", "College of Engineering", "College of Liberal Arts"}:
                    group_share = share + 0.06
                else:
                    group_share = share

                headcount = int(round(total_headcount * group_share))
                if group == "Staff" and not dept.is_academic:
                    headcount = max(headcount, int(total_headcount * 0.78))
                if headcount == 0:
                    continue

                salary_rate = {"Faculty": 9_600, "Staff": 6_450, "Student Workers": 1_650}[group]
                salary_modifier = 1.12 if dept.department_name in {"Information Technology", "College of Engineering"} else 1.0
                fte = headcount * (0.96 if group != "Student Workers" else 0.45)
                salary_expense = headcount * salary_rate * salary_modifier * rng.uniform(0.985, 1.025)

                records.append(
                    {
                        "department_id": dept.department_id,
                        "department_name": dept.department_name,
                        "date_key": date_key(month_start),
                        "month_start_date": month_start.date().isoformat(),
                        "fiscal_year": fiscal_year,
                        "fiscal_period": fiscal_period,
                        "employee_group": group,
                        "headcount": headcount,
                        "fte": round(fte, 2),
                        "total_salary_expense": round(salary_expense, 2),
                        "overtime_expense": round(salary_expense * rng.uniform(0.005, 0.035), 2),
                        "vacancies": int(rng.integers(0, 4)),
                        "turnover_count": int(rng.choice([0, 0, 0, 1, 1, 2], p=[0.45, 0.2, 0.1, 0.15, 0.07, 0.03])),
                    }
                )
    return pd.DataFrame(records)


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(RANDOM_SEED)

    outputs = {
        "departments.csv": build_departments(),
        "date_dimension.csv": build_date_dimension(),
        "budget_monthly.csv": build_budget(rng),
        "procurement_requests.csv": build_procurement(rng),
        "maintenance_requests.csv": build_maintenance(rng),
        "hr_monthly.csv": build_hr(rng),
    }

    for filename, dataframe in outputs.items():
        dataframe.to_csv(RAW_DIR / filename, index=False)
        print(f"Wrote {filename}: {len(dataframe):,} rows")


if __name__ == "__main__":
    main()
