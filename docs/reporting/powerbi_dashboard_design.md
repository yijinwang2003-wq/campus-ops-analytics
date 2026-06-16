# Power BI Dashboard Specification

## Portfolio Context

This dashboard specification is based on the generated CSV datasets in `data/powerbi/`. It is designed for a university Finance & Business Information Services department that needs integrated visibility across Finance, Procurement, Facilities, and HR operations.

The reporting design prioritizes executive financial stewardship, budget exception management, procurement cycle-time monitoring, critical facilities backlog, and workforce capacity context.

## Source Files Reviewed

| CSV File | Rows | Primary Use |
|---|---:|---|
| `budget_summary.csv` | 16 | Annual budget-to-actual summary by department and fiscal year. |
| `budget_monthly_dashboard.csv` | 768 | Monthly budget, actual spend, commitments, variance, and category trends. |
| `procurement_dashboard.csv` | 192 | Procurement request lifecycle, approval cycle time, status, vendor, category, and delay flags. |
| `maintenance_dashboard.csv` | 108 | Facilities work orders, priority, status, building, cost, resolution days, and critical overdue flags. |
| `hr_workforce_dashboard.csv` | 192 | Monthly headcount, FTE, salary expense, overtime, vacancies, turnover, and headcount change. |
| `dim_department.csv` | 8 | Department, division, department type, VP owner, and academic flag. |
| `dim_date.csv` | 731 | Calendar and fiscal date attributes. |

## Shared Design Standards

- **Audience:** university Finance division, Finance & Business Information Services, budget analysts, procurement leadership, facilities leadership, HR leadership, and executive sponsors.
- **Canvas:** 16:9 Power BI report page.
- **Theme:** white background, navy headers, slate text, teal accents, gold warning states, red exception states.
- **Global slicers:** fiscal year, department, division, department type.
- **Exception colors:** red for over budget or critical overdue, gold for watchlist, green for within target.
- **Navigation:** four-page report with left-side vertical navigation or top tab-style navigation.
- **Data grain:** use aggregated fields for KPI cards and drillable tables for operational exceptions.

## Page 1: Executive Overview

### Business Purpose

Provide executive leadership with a consolidated enterprise view of financial risk, procurement bottlenecks, facilities service exposure, and workforce capacity. This page should answer: "Where does leadership need to intervene this month?"

### KPIs

| KPI | Definition | Required Fields | Current Dataset Value |
|---|---|---|---:|
| FY2025 Total Budget | Sum of approved annual budget. | `budget_summary.total_budget`, `budget_summary.fiscal_year` | $59.20M |
| FY2025 Actual Spend | Sum of actual annual spend. | `budget_summary.total_actual_spend`, `budget_summary.fiscal_year` | $57.35M |
| FY2025 Budget Utilization | Actual spend divided by total budget. | `total_actual_spend`, `total_budget` | 96.88% |
| Departments Over Budget | Count of departments where over-budget flag is true. | `department_name`, `is_over_budget`, `fiscal_year` | 1 |
| Departments at 95%+ Utilization | Count of departments at or above watchlist threshold. | `department_name`, `budget_utilization_pct`, `fiscal_year` | 5 |
| Avg Procurement Approval Days | Average days from request to approval. | `procurement_dashboard.days_to_approve` | 8.09 |
| Critical Facilities Over 48h | Count of critical open requests older than 48 hours. | `maintenance_dashboard.is_critical_over_48h` | 4 |
| Current Headcount | Latest-month total headcount. | `hr_workforce_dashboard.month_start_date`, `total_headcount` | 680 |

### Charts

| Chart | Exact Power BI Visual Type | Required Fields | Configuration |
|---|---|---|---|
| Budget Utilization by Department | Clustered bar chart | `department_name`, `budget_utilization_pct`, `fiscal_year` | Sort descending by utilization; conditional color red above 100%, gold 95-100%, teal below 95%. |
| Enterprise Exception Matrix | Matrix | `department_name`, `budget_utilization_pct`, `budget_variance`, delayed approval count, critical overdue count, `vacancies` | Use conditional formatting on utilization, variance, delayed approvals, and critical backlog. |
| Procurement Approval Trend | Line chart | `approval_month`, `days_to_approve`, `department_name` | Average days to approve by approval month; optional department legend. |
| Facilities Backlog by Priority | Stacked column chart | `priority`, `status`, `work_order_number` | Count work orders by priority and status. |
| Workforce by Department | Clustered column chart | `department_name`, latest `total_headcount`, latest `vacancies` | Headcount as columns; vacancies as tooltip or secondary line if using combo chart. |

### Required Fields

- `budget_summary`: `department_id`, `department_name`, `fiscal_year`, `total_budget`, `total_actual_spend`, `budget_variance`, `budget_utilization_pct`, `is_over_budget`
- `procurement_dashboard`: `department_id`, `department_name`, `approval_month`, `days_to_approve`, `is_approval_delayed`
- `maintenance_dashboard`: `department_id`, `department_name`, `priority`, `status`, `work_order_number`, `is_critical_over_48h`
- `hr_workforce_dashboard`: `department_id`, `department_name`, `month_start_date`, `total_headcount`, `vacancies`
- `dim_department`: `department_id`, `division`, `department_type`, `vp_owner`, `is_academic`

### Filters

- Fiscal Year
- Department
- Division
- Department Type
- Academic / Administrative flag

### Layout Wireframe

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ EXECUTIVE OVERVIEW                         Fiscal Year | Division | Dept     │
├────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤
│ Budget     │ Actual     │ Util %     │ Over Budget│ Avg Approve│ Critical   │
│ $59.20M    │ $57.35M    │ 96.88%     │ 1 Dept     │ 8.09 Days  │ 4 Over 48h │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ Budget Utilization by Dept    │ Enterprise Exception Matrix                  │
│ Clustered bar chart           │ Matrix with conditional formatting           │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ Procurement Approval Trend    │ Facilities Backlog by Priority               │
│ Line chart                    │ Stacked column chart                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Workforce by Department - clustered column chart                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Expected Insights

- Information Technology is the only FY2025 over-budget department, with 107.00% budget utilization and a negative variance of approximately $504,000.
- Student Affairs is a near-limit budget watch item at 98.00% utilization.
- Five departments are at or above 95% utilization and should be monitored by Finance.
- Procurement approval time is materially elevated for IT compared with the university average.
- Critical facilities backlog requires executive visibility because four critical requests are unresolved beyond 48 hours.

## Page 2: Budget Analytics

### Business Purpose

Support Finance leadership and budget analysts with budget-to-actual monitoring, category-level spend analysis, monthly variance review, and department exception management.

### KPIs

| KPI | Definition | Required Fields | Current Dataset Value |
|---|---|---|---:|
| Total Budget | Sum of selected budget. | `total_budget` or `monthly_budget` | $59.20M for FY2025 |
| Actual Spend | Sum of selected actual spend. | `total_actual_spend` or `actual_spend` | $57.35M for FY2025 |
| Budget Variance | Budget minus actual spend. | `budget_variance` | $1.85M remaining for FY2025 |
| Budget Utilization % | Actual spend divided by budget. | `budget_utilization_pct` | 96.88% for FY2025 |
| Over-Budget Departments | Count where `is_over_budget = TRUE`. | `is_over_budget`, `department_name` | 1 |
| Watchlist Departments | Count where utilization is at least 95%. | `budget_utilization_pct`, `department_name` | 5 |
| Committed Amount | Sum of open commitments. | `total_committed_amount`, `committed_amount` | Use selected filter context |

### Charts

| Chart | Exact Power BI Visual Type | Required Fields | Configuration |
|---|---|---|---|
| Budget vs Actual by Department | Clustered column chart | `department_name`, `total_budget`, `total_actual_spend`, `fiscal_year` | Compare approved budget and actual spend by department. |
| Budget Variance by Department | Waterfall chart | `department_name`, `budget_variance`, `fiscal_year` | Show favorable and unfavorable variances; red for negative variance. |
| Monthly Utilization Trend | Line chart | `fiscal_period`, `budget_utilization_pct`, `department_name`, `fiscal_year` | Use `budget_monthly_dashboard`; show trend by selected department or all departments. |
| Actual Spend by Budget Category | Treemap | `budget_category`, `actual_spend`, `department_name`, `fiscal_year` | Size by actual spend; drill by department. |
| Budget Exception Detail | Table | `department_name`, `budget_category`, `monthly_budget`, `actual_spend`, `committed_amount`, `budget_variance`, `budget_utilization_pct`, `is_over_budget` | Add conditional formatting for over-budget rows and high utilization. |

### Required Fields

- `budget_summary`: `department_id`, `department_name`, `fiscal_year`, `total_budget`, `total_actual_spend`, `total_committed_amount`, `budget_variance`, `budget_utilization_pct`, `budget_variance_pct`, `is_over_budget`
- `budget_monthly_dashboard`: `department_id`, `department_name`, `fiscal_year`, `fiscal_period`, `budget_category`, `monthly_budget`, `actual_spend`, `committed_amount`, `funding_source`, `budget_variance`, `budget_utilization_pct`, `budget_variance_pct`, `is_over_budget`
- `dim_department`: `department_id`, `division`, `department_type`, `vp_owner`, `is_academic`
- `dim_date`: `date_key`, `fiscal_year`, `fiscal_quarter`, `fiscal_month`

### Filters

- Fiscal Year
- Fiscal Quarter
- Fiscal Period
- Department
- Division
- Budget Category
- Funding Source
- Over-Budget Flag

### Layout Wireframe

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ BUDGET ANALYTICS           FY | Quarter | Period | Department | Category     │
├────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤
│ Budget     │ Actual     │ Variance   │ Util %     │ Over Budget│ Watchlist  │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ Budget vs Actual by Dept      │ Budget Variance Waterfall                    │
│ Clustered column chart        │ Waterfall chart                              │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ Monthly Utilization Trend     │ Actual Spend by Budget Category              │
│ Line chart                    │ Treemap                                      │
├──────────────────────────────────────────────────────────────────────────────┤
│ Budget Exception Detail - table with conditional formatting                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Expected Insights

- IT budget pressure should be the first Finance follow-up item because it exceeds approved FY2025 budget by 7%.
- Student Affairs should be monitored closely because only about $108,000 remains in FY2025 budget capacity.
- Category-level analysis can isolate whether pressure is driven by personnel, software, cloud services, student programming, or contract services.
- Monthly trends help determine whether budget risk is structural or caused by fiscal-year timing.

## Page 3: Procurement Operations

### Business Purpose

Enable Procurement Services, Finance Office reviewers, and department leadership to monitor approval cycle time, delayed approvals, sourcing workload, and vendor/category concentration.

### KPIs

| KPI | Definition | Required Fields | Current Dataset Value |
|---|---|---|---:|
| Total Requests | Count of procurement requests. | `request_number` | 192 |
| Total Approved Amount | Sum of approved request amount. | `approved_amount` | $10.85M |
| Avg Days to Approve | Average request-to-approval cycle time. | `days_to_approve` | 8.09 |
| Delayed Approvals | Count where approval delay flag is true. | `is_approval_delayed` | 43 |
| IT Avg Days to Approve | IT average request-to-approval cycle time. | `department_name`, `days_to_approve` | 14.24 |
| Competitive Bid Requests | Count where competitive bid flag is true. | `is_competitive_bid` | 103 |
| Avg Days to Complete | Average request-to-invoice completion time. | `days_to_complete` | Use completed/invoiced records |

### Charts

| Chart | Exact Power BI Visual Type | Required Fields | Configuration |
|---|---|---|---|
| Avg Approval Days by Department | Clustered bar chart | `department_name`, `days_to_approve` | Average days by department; add constant line for university average of 8.09 days. |
| Delayed Approval Count by Department | Clustered column chart | `department_name`, `is_approval_delayed`, `request_number` | Count delayed requests; sort descending. |
| Approval Cycle Trend | Line chart | `approval_month`, `days_to_approve` | Average days by month; optional legend by `approval_level`. |
| Requests by Category and Status | Stacked column chart | `procurement_category`, `request_status`, `request_number` | Count requests by category and status. |
| Approved Amount by Vendor | Bar chart | `vendor_name`, `approved_amount` | Top 10 vendors by approved amount. |
| Procurement Detail | Table | `request_number`, `department_name`, `vendor_name`, `procurement_category`, `approval_level`, `request_status`, `approved_amount`, `days_to_approve`, `is_approval_delayed` | Conditional formatting on delayed approvals and high amounts. |

### Required Fields

- `procurement_dashboard`: `request_number`, `department_id`, `department_name`, `request_date`, `approval_date`, `po_date`, `invoice_date`, `vendor_name`, `procurement_category`, `request_amount`, `approved_amount`, `request_status`, `approval_level`, `finance_reviewer`, `is_competitive_bid`, `days_to_approve`, `days_to_complete`, `is_approval_delayed`, `approval_month`
- `dim_department`: `department_id`, `division`, `department_type`, `vp_owner`, `is_academic`
- `dim_date`: `date_key`, `calendar_date`, `fiscal_year`, `fiscal_month`

### Filters

- Department
- Division
- Procurement Category
- Vendor
- Request Status
- Approval Level
- Finance Reviewer
- Competitive Bid Flag
- Approval Month
- Delayed Approval Flag

### Layout Wireframe

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ PROCUREMENT OPERATIONS       Dept | Category | Vendor | Status | Reviewer   │
├────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤
│ Requests   │ Approved $ │ Avg Approve│ Delayed    │ IT Avg     │ Comp Bid   │
│ 192        │ $10.85M    │ 8.09 Days  │ 43         │ 14.24 Days │ 103        │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ Avg Approval Days by Dept     │ Approval Cycle Trend                         │
│ Clustered bar + avg line      │ Line chart                                   │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ Delayed Count by Dept         │ Requests by Category and Status              │
│ Clustered column chart        │ Stacked column chart                         │
├───────────────────────────────┴──────────────────────────────────────────────┤
│ Procurement Detail - request-level table                                      │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Expected Insights

- IT procurement is the key operational bottleneck, averaging 14.24 approval days, roughly 1.8 times the university average.
- Delayed approvals should be reviewed by approval level and finance reviewer to separate policy-driven delays from workload or routing issues.
- Competitive bid workload is substantial, with 103 requests flagged as competitive bid.
- Vendor and category concentration views can identify opportunities for preferred supplier agreements or improved intake templates.

## Page 4: Facilities & Workforce

### Business Purpose

Connect facilities service risk with workforce capacity indicators so Finance, Facilities, and HR leadership can evaluate whether backlog, staffing, vacancies, and salary trends require intervention.

### KPIs

| KPI | Definition | Required Fields | Current Dataset Value |
|---|---|---|---:|
| Open Work Orders | Count where status is not completed. | `status`, `work_order_number` | 11 |
| Critical Over 48h | Count of critical unresolved requests older than 48 hours. | `is_critical_over_48h` | 4 |
| Avg Days to Resolve | Average resolution or open aging days. | `days_to_resolve` | 17.46 |
| Estimated Maintenance Cost | Sum of estimated maintenance cost. | `estimated_cost` | $1.07M |
| Current Headcount | Latest-month total headcount. | `month_start_date`, `total_headcount` | 680 |
| Current FTE | Latest-month total FTE. | `month_start_date`, `total_fte` | 598.74 |
| Open Vacancies | Latest-month vacancies. | `month_start_date`, `vacancies` | 25 |
| Monthly Salary Expense | Latest-month salary expense. | `month_start_date`, `total_salary_expense` | $4.55M |

### Charts

| Chart | Exact Power BI Visual Type | Required Fields | Configuration |
|---|---|---|---|
| Work Orders by Priority and Status | Stacked bar chart | `priority`, `status`, `work_order_number` | Count work orders; sort by Critical, High, Medium, Low. |
| Critical Overdue Work Order List | Table | `work_order_number`, `building_name`, `request_type`, `priority`, `status`, `assigned_team`, `days_to_resolve`, `estimated_cost`, `is_critical_over_48h` | Filter to critical overdue; red conditional formatting. |
| Avg Days to Resolve by Request Type | Clustered bar chart | `request_type`, `days_to_resolve` | Average resolution days by request type. |
| Maintenance Cost by Building | Clustered column chart | `building_name`, `estimated_cost`, `actual_cost` | Compare estimated and actual cost where actual is available. |
| Headcount and Vacancies by Department | Line and clustered column chart | `department_name`, latest `total_headcount`, latest `vacancies` | Headcount as columns; vacancies as line. |
| Salary Expense Trend | Line chart | `month_start_date`, `total_salary_expense`, `department_name` | Monthly salary trend; department slicer enabled. |

### Required Fields

- `maintenance_dashboard`: `work_order_number`, `department_id`, `department_name`, `request_date`, `completed_date`, `building_name`, `request_type`, `priority`, `status`, `estimated_cost`, `actual_cost`, `assigned_team`, `days_to_resolve`, `is_critical_over_48h`
- `hr_workforce_dashboard`: `department_id`, `department_name`, `fiscal_year`, `fiscal_period`, `month_start_date`, `total_headcount`, `total_fte`, `total_salary_expense`, `overtime_expense`, `vacancies`, `turnover_count`, `avg_salary_per_headcount`, `headcount_change`
- `dim_department`: `department_id`, `division`, `department_type`, `vp_owner`, `is_academic`
- `dim_date`: `date_key`, `calendar_date`, `fiscal_year`, `fiscal_month`

### Filters

- Department
- Division
- Building
- Priority
- Maintenance Status
- Request Type
- Assigned Team
- Fiscal Year
- Fiscal Period

### Layout Wireframe

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ FACILITIES & WORKFORCE        Dept | Building | Priority | Status | Period  │
├────────────┬────────────┬────────────┬────────────┬────────────┬────────────┤
│ Open WO    │ Critical   │ Avg Resolve│ Est Cost   │ Headcount  │ Vacancies  │
│ 11         │ 4          │ 17.46 Days │ $1.07M     │ 680        │ 25         │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ Work Orders by Priority/Status│ Critical Overdue Work Order List             │
│ Stacked bar chart             │ Table                                        │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ Avg Resolve by Request Type   │ Headcount and Vacancies by Department        │
│ Clustered bar chart           │ Line and clustered column chart              │
├───────────────────────────────┴──────────────────────────────────────────────┤
│ Salary Expense Trend and Maintenance Cost by Building                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Expected Insights

- Four critical work orders are unresolved beyond 48 hours and should be reviewed as operational risk.
- Open work order backlog should be evaluated by priority, building, request type, and assigned team.
- Facilities Management has 111 latest-month headcount and 4 vacancies, which can be reviewed alongside backlog volume.
- University-wide latest-month workforce totals show 680 headcount, 598.74 FTE, 25 vacancies, and $4.55M in salary expense.
- Combining workforce and facilities metrics supports resource planning discussions rather than treating backlog as an isolated operational metric.

## Power BI Model Notes

Recommended relationships:

- `dim_department.department_id` one-to-many to every dashboard fact table.
- `dim_date.date_key` one-to-many to budget and HR date keys.
- Procurement and maintenance lifecycle dates should be modeled as role-playing date relationships if the semantic model is expanded.

Recommended measures:

```DAX
Total Budget = SUM(budget_summary[total_budget])
Actual Spend = SUM(budget_summary[total_actual_spend])
Budget Variance = SUM(budget_summary[budget_variance])
Budget Utilization % = DIVIDE([Actual Spend], [Total Budget])
Over Budget Departments = COUNTROWS(FILTER(budget_summary, budget_summary[is_over_budget] = TRUE()))
Watchlist Departments = COUNTROWS(FILTER(budget_summary, budget_summary[budget_utilization_pct] >= 95))
Average Days to Approve = AVERAGE(procurement_dashboard[days_to_approve])
Delayed Approvals = COUNTROWS(FILTER(procurement_dashboard, procurement_dashboard[is_approval_delayed] = TRUE()))
Critical Over 48h = COUNTROWS(FILTER(maintenance_dashboard, maintenance_dashboard[is_critical_over_48h] = TRUE()))
Open Work Orders = COUNTROWS(FILTER(maintenance_dashboard, maintenance_dashboard[status] <> "Completed"))
```

Security guidance:

- Department managers should be filtered to their department.
- Finance leadership can access cross-department financial reporting.
- HR salary expense detail should be restricted to HR, Finance leadership, and approved executive users.
