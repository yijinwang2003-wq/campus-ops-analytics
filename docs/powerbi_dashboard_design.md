# Power BI Dashboard Design

## Design Intent

This dashboard package is designed for a university Finance division and Finance & Business Information Services team. The pages emphasize fiscal stewardship, operational bottlenecks, service risk, and workforce context. The design should feel executive-ready but still useful for analysts and department managers who need to investigate exceptions.

Primary datasets:

- `data/powerbi/budget_summary.csv`
- `data/powerbi/budget_monthly_dashboard.csv`
- `data/powerbi/procurement_dashboard.csv`
- `data/powerbi/maintenance_dashboard.csv`
- `data/powerbi/hr_workforce_dashboard.csv`
- `data/powerbi/dim_department.csv`
- `data/powerbi/dim_date.csv`

Recommended visual style:

- White or very light gray canvas.
- University finance palette: navy, slate, teal, gold, and restrained red for exceptions.
- KPI cards across the top of each page.
- Left-side or top filter bar for fiscal year, department, and operational dimensions.
- Exception colors should be consistent: red for over budget or overdue critical items, gold for warning thresholds, green for within target.

## Page 1: Executive Overview

### Page Title

**Executive Overview**

### Business Purpose

Provide senior finance and administrative leaders with a single-page view of enterprise risk across budget utilization, procurement delays, critical facilities backlog, and workforce capacity.

### KPI Cards

| KPI Card | Dataset | Definition |
|---|---|---|
| FY2025 Total Budget | `budget_summary.csv` | Sum of `total_budget` for selected fiscal year. Current FY2025 total: $59.2M. |
| FY2025 Actual Spend | `budget_summary.csv` | Sum of `total_actual_spend`. Current FY2025 actual spend: $57.35M. |
| Departments Over Budget | `budget_summary.csv` | Count of departments where `is_over_budget = TRUE`. Current count: 1. |
| Departments at 95%+ Utilization | `budget_summary.csv` | Count of departments with `budget_utilization_pct >= 95`. Current count: 5. |
| Avg Procurement Approval Days | `procurement_dashboard.csv` | Average `days_to_approve`. Current average: 8.09 days. |
| Critical Facilities Over 48h | `maintenance_dashboard.csv` | Count where `is_critical_over_48h = TRUE`. Current count: 4. |
| Current Headcount | `hr_workforce_dashboard.csv` | Sum of latest month `total_headcount`. Current June 2025 headcount: 680. |
| Open Vacancies | `hr_workforce_dashboard.csv` | Sum of latest month `vacancies`. Current June 2025 vacancies: 25. |

### Charts

| Visual | Chart Type | Fields |
|---|---|---|
| Budget Utilization by Department | Horizontal bar chart | Axis: `department_name`; Value: `budget_utilization_pct`; Conditional color: over 100%, 95-100%, below 95%. |
| Enterprise Risk Matrix | Matrix / table | Rows: `department_name`; Columns: budget utilization, delayed procurement count, critical work orders, vacancies. |
| Procurement Approval Trend | Line chart | Axis: `approval_month`; Value: average `days_to_approve`; Legend: optional department. |
| Critical Backlog by Priority | Stacked bar | Axis: `priority`; Value: count of `work_order_number`; Legend: `status`. |
| Workforce by Department | Column chart | Axis: `department_name`; Value: latest `total_headcount`; Tooltip: vacancies and salary expense. |

### Filters

- Fiscal Year
- Department
- Division
- Department Type
- Academic / Administrative flag

### Business Insights

- Information Technology is the primary FY2025 budget exception at 107.00% utilization, approximately $504,000 over budget.
- Student Affairs is not over budget but is close to its limit at 98.00% utilization.
- IT procurement cycle time is a cross-functional concern, averaging 14.24 days versus the 8.09-day university average.
- Four critical maintenance requests remain unresolved for more than 48 hours, creating operational risk that should be reviewed by Facilities leadership.
- Workforce context is important when interpreting service delays and budget pressure; latest generated data shows 680 total headcount and 25 vacancies.

### Layout Sketch

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ Executive Overview                                      Fiscal Year Filter │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────┤
│ Total Budget │ Actual Spend │ Over Budget  │ Avg Approval │ Critical 48h  │
│ $59.2M       │ $57.35M      │ 1 Dept       │ 8.09 Days    │ 4 Requests    │
├─────────────────────────────┬──────────────────────────────────────────────┤
│ Budget Utilization by Dept  │ Enterprise Risk Matrix                       │
│ Horizontal Bar              │ Dept x Budget / Procurement / Facilities /HR │
├─────────────────────────────┼──────────────────────────────────────────────┤
│ Procurement Approval Trend  │ Workforce by Department                      │
│ Line Chart                  │ Column Chart                                 │
└─────────────────────────────┴──────────────────────────────────────────────┘
```

## Page 2: Budget Analytics

### Page Title

**Budget Analytics**

### Business Purpose

Support Finance leadership, budget analysts, and department managers with budget-to-actual monitoring, variance review, category analysis, and identification of departments requiring fiscal intervention.

### KPI Cards

| KPI Card | Dataset | Definition |
|---|---|---|
| Total Budget | `budget_summary.csv` | Sum of `total_budget`. |
| Actual Spend | `budget_summary.csv` | Sum of `total_actual_spend`. |
| Remaining Budget | `budget_summary.csv` | Sum of `budget_variance`. |
| Budget Utilization % | `budget_summary.csv` | Actual spend divided by budget. |
| Over-Budget Departments | `budget_summary.csv` | Count where `is_over_budget = TRUE`. |
| Watchlist Departments | `budget_summary.csv` | Count where `budget_utilization_pct >= 95`. |

### Charts

| Visual | Chart Type | Fields |
|---|---|---|
| Budget vs Actual by Department | Clustered bar chart | Axis: `department_name`; Values: `total_budget`, `total_actual_spend`. |
| Budget Variance by Department | Waterfall chart | Category: `department_name`; Value: `budget_variance`. |
| Monthly Budget Utilization | Line chart | Axis: `fiscal_period`; Value: average or weighted `budget_utilization_pct`; Legend: `department_name`. |
| Spend by Budget Category | Treemap or stacked column | Group: `budget_category`; Value: `actual_spend`. |
| Department Budget Exception Table | Table | `department_name`, `total_budget`, `total_actual_spend`, `budget_variance`, `budget_utilization_pct`, `is_over_budget`. |

### Filters

- Fiscal Year
- Fiscal Period
- Department
- Division
- Budget Category
- Funding Source

### Business Insights

- IT is the only generated FY2025 over-budget department, with 107.00% utilization and a negative variance of about $504,000.
- Student Affairs should be treated as a watchlist department at 98.00% utilization even though it remains within budget.
- College of Engineering, Facilities Management, and College of Liberal Arts are also above or near the 95% monitoring threshold.
- Monthly budget and category views help distinguish recurring cost pressure from year-end timing issues.

### Layout Sketch

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ Budget Analytics                    FY | Period | Department | Category   │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────┤
│ Total Budget │ Actual Spend │ Remaining    │ Utilization  │ Watchlist     │
├─────────────────────────────┬──────────────────────────────────────────────┤
│ Budget vs Actual by Dept    │ Budget Variance Waterfall                    │
│ Clustered Bar               │ Waterfall                                    │
├─────────────────────────────┼──────────────────────────────────────────────┤
│ Monthly Utilization Trend   │ Spend by Budget Category                     │
│ Line Chart                  │ Treemap / Stacked Column                     │
├────────────────────────────────────────────────────────────────────────────┤
│ Department Budget Exception Table                                          │
└────────────────────────────────────────────────────────────────────────────┘
```

## Page 3: Procurement Operations

### Page Title

**Procurement Operations**

### Business Purpose

Help Procurement Services and Finance identify approval delays, category bottlenecks, high-value requests, competitive bid workload, and departments with above-average approval cycle time.

### KPI Cards

| KPI Card | Dataset | Definition |
|---|---|---|
| Total Requests | `procurement_dashboard.csv` | Count of `request_number`. Current generated count: 192. |
| Total Approved Amount | `procurement_dashboard.csv` | Sum of `approved_amount`. |
| Avg Days to Approve | `procurement_dashboard.csv` | Average `days_to_approve`. Current average: 8.09 days. |
| Delayed Approvals | `procurement_dashboard.csv` | Count where `is_approval_delayed = TRUE`. Current count: 43. |
| IT Avg Approval Days | `procurement_dashboard.csv` | Average IT `days_to_approve`. Current average: 14.24 days. |
| Competitive Bid Requests | `procurement_dashboard.csv` | Count where `is_competitive_bid = TRUE`. |

### Charts

| Visual | Chart Type | Fields |
|---|---|---|
| Avg Approval Days by Department | Horizontal bar chart | Axis: `department_name`; Value: average `days_to_approve`; reference line: university average. |
| Delayed Approval Count by Department | Bar chart | Axis: `department_name`; Value: count of delayed requests. |
| Approval Cycle Trend | Line chart | Axis: `approval_month`; Value: average `days_to_approve`; Legend: `approval_level` or department. |
| Requests by Category and Status | Stacked column | Axis: `procurement_category`; Value: count of requests; Legend: `request_status`. |
| Vendor Spend Table | Table | `vendor_name`, request count, sum of `approved_amount`, average `days_to_approve`. |
| Approval Level Mix | Donut or 100% stacked bar | Legend: `approval_level`; Value: count of requests. |

### Filters

- Department
- Procurement Category
- Vendor
- Request Status
- Approval Level
- Finance Reviewer
- Competitive Bid Flag
- Approval Month

### Business Insights

- IT procurement is the main cycle-time exception, averaging 14.24 days compared with the university average of 8.09 days.
- Delayed approvals should be triaged by approval level and category to determine whether delays are due to contract review, competitive bid requirements, finance review, or missing documentation.
- Vendor and category views help identify repeat sourcing areas that may benefit from blanket agreements or improved intake standards.
- Finance reviewer filters help separate individual workload from process design issues.

### Layout Sketch

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ Procurement Operations       Dept | Category | Vendor | Status | Reviewer │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────┤
│ Requests     │ Approved Amt │ Avg Approval │ Delayed      │ IT Approval   │
│ 192          │              │ 8.09 Days    │ 43           │ 14.24 Days    │
├─────────────────────────────┬──────────────────────────────────────────────┤
│ Avg Approval Days by Dept   │ Approval Cycle Trend                         │
│ Bar + Avg Reference Line    │ Line Chart                                   │
├─────────────────────────────┼──────────────────────────────────────────────┤
│ Requests by Category/Status │ Approval Level Mix                           │
│ Stacked Column              │ Donut / Stacked Bar                          │
├────────────────────────────────────────────────────────────────────────────┤
│ Vendor Spend and Cycle-Time Table                                          │
└────────────────────────────────────────────────────────────────────────────┘
```

## Page 4: Facilities & Workforce

### Page Title

**Facilities & Workforce**

### Business Purpose

Connect facilities service risk with workforce capacity. This page supports Facilities, HR, Finance, and executive leadership by showing maintenance backlog, critical unresolved work, staffing levels, vacancies, and salary context.

### KPI Cards

| KPI Card | Dataset | Definition |
|---|---|---|
| Open Work Orders | `maintenance_dashboard.csv` | Count where `status != Completed`. Current generated count: 11. |
| Critical Over 48h | `maintenance_dashboard.csv` | Count where `is_critical_over_48h = TRUE`. Current count: 4. |
| Avg Days to Resolve | `maintenance_dashboard.csv` | Average `days_to_resolve`. Current generated average: 17.46 days. |
| Estimated Maintenance Cost | `maintenance_dashboard.csv` | Sum of `estimated_cost`. |
| Current Headcount | `hr_workforce_dashboard.csv` | Latest month sum of `total_headcount`. Current generated value: 680. |
| Open Vacancies | `hr_workforce_dashboard.csv` | Latest month sum of `vacancies`. Current generated value: 25. |
| Monthly Salary Expense | `hr_workforce_dashboard.csv` | Latest month sum of `total_salary_expense`. |

### Charts

| Visual | Chart Type | Fields |
|---|---|---|
| Work Orders by Priority and Status | Stacked bar | Axis: `priority`; Value: count of `work_order_number`; Legend: `status`. |
| Critical Overdue Work Orders | Table | `work_order_number`, `building_name`, `request_type`, `assigned_team`, `days_to_resolve`, `estimated_cost`. |
| Avg Days to Resolve by Request Type | Bar chart | Axis: `request_type`; Value: average `days_to_resolve`. |
| Maintenance Cost by Building | Column chart | Axis: `building_name`; Values: sum of `estimated_cost`, sum of `actual_cost`. |
| Headcount and Vacancies by Department | Combo chart | Axis: `department_name`; Column: `total_headcount`; Line: `vacancies`. |
| Salary Expense Trend | Line chart | Axis: `month_start_date`; Value: `total_salary_expense`; Legend: optional department. |

### Filters

- Department
- Building
- Priority
- Maintenance Status
- Request Type
- Assigned Team
- Fiscal Year
- Fiscal Period
- Employee Group, if connected from raw HR detail in later model versions

### Business Insights

- The generated dataset contains four critical maintenance requests unresolved for more than 48 hours, requiring daily operational review.
- Facilities backlog should be reviewed with staffing and vacancy data to determine whether service delays are related to workload, staffing capacity, vendor constraints, or parts availability.
- June 2025 generated workforce data shows 680 total headcount and 25 vacancies across the university.
- Combining facilities and workforce information gives Finance leadership better context for overtime, service delays, and resource planning.

### Layout Sketch

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ Facilities & Workforce       Dept | Building | Priority | Status | Period │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────┤
│ Open Orders  │ Critical 48h │ Avg Resolve  │ Headcount    │ Vacancies     │
│ 11           │ 4            │ 17.46 Days   │ 680          │ 25            │
├─────────────────────────────┬──────────────────────────────────────────────┤
│ Work Orders by Priority     │ Critical Overdue Work Order Table            │
│ Stacked Bar                 │ Exception Table                              │
├─────────────────────────────┼──────────────────────────────────────────────┤
│ Avg Resolve by Request Type │ Headcount and Vacancies by Department        │
│ Bar Chart                   │ Combo Chart                                  │
├─────────────────────────────┴──────────────────────────────────────────────┤
│ Salary Expense Trend / Maintenance Cost by Building                         │
└────────────────────────────────────────────────────────────────────────────┘
```

## Cross-Page Navigation

Recommended navigation:

- Executive Overview
- Budget Analytics
- Procurement Operations
- Facilities & Workforce

Use consistent slicer placement and a small reset-filters button on each page. Keep department and fiscal year filters available globally because they are the primary management dimensions for a university finance audience.

## Recommended Measures

```text
Budget Utilization % = DIVIDE(SUM(actual_spend), SUM(monthly_budget))
Budget Variance = SUM(monthly_budget) - SUM(actual_spend)
Over Budget Department Count = COUNTROWS(FILTER(BudgetSummary, BudgetSummary[is_over_budget] = TRUE()))
Average Days to Approve = AVERAGE(Procurement[days_to_approve])
Delayed Approval Count = COUNTROWS(FILTER(Procurement, Procurement[is_approval_delayed] = TRUE()))
Critical Over 48h Count = COUNTROWS(FILTER(Maintenance, Maintenance[is_critical_over_48h] = TRUE()))
Open Work Orders = COUNTROWS(FILTER(Maintenance, Maintenance[status] <> "Completed"))
Current Headcount = SUM(LatestHR[total_headcount])
Open Vacancies = SUM(LatestHR[vacancies])
```

## Implementation Notes

- Use `dim_department` as the common slicer table for department, division, department type, and academic flag.
- Use `dim_date` for fiscal year and fiscal period filtering where possible.
- The current CSV outputs are dashboard-ready and can be loaded directly into Power BI.
- For a production semantic model, create explicit relationships from fact tables to `dim_department` and role-playing date relationships from procurement and maintenance lifecycle date keys to `dim_date`.
- HR salary fields should be secured for approved HR, Finance leadership, and executive users.
