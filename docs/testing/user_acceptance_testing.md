# User Acceptance Testing Package

## Higher Education Enterprise Analytics & Decision Support Platform

Prepared for: University Finance & Business Information Services  
Document type: User Acceptance Testing package  
Testing scope: Finance, Procurement, Facilities, HR, and dashboard reporting outputs

## 1. UAT Overview

User Acceptance Testing validates that the Higher Education Enterprise Analytics & Decision Support Platform meets the business needs defined by Finance, Procurement, Facilities, Human Resources, and Business Information Services stakeholders.

The purpose of UAT is to confirm that:

- Business calculations are accurate.
- Dashboard-ready datasets contain the required fields.
- Exception flags identify the correct records.
- Dashboard filters support department and fiscal-period analysis.
- The reporting outputs are suitable for executive and operational decision-making.

The UAT package focuses on six core scenarios:

1. Verify Budget Utilization Calculation
2. Verify Over Budget Flag
3. Verify Procurement Delay Flag
4. Verify Critical Maintenance Alert
5. Verify Workforce Vacancy Metrics
6. Verify Dashboard Filters

## UAT Scope

In scope:

- CSV outputs in `data/powerbi/`
- Budget utilization and variance logic
- Over-budget exception flag
- Procurement delay flag
- Critical maintenance alert flag
- Workforce vacancy metrics
- Department and fiscal-year dashboard filtering expectations

Out of scope:

- Production authentication
- Live ERP, HRIS, procurement, or facilities system integration
- Power BI service deployment approval
- Row-level security configuration
- Production refresh scheduling

## Entry Criteria

UAT may begin when:

- `src/generate_data.py` has been executed successfully.
- `src/transform_data.py` has produced files in `data/powerbi/`.
- `src/validate_data.py` runs successfully.
- Dashboard design documentation is available.
- Stakeholders have reviewed the business requirements package.

## Exit Criteria

UAT is complete when:

- All high-priority test cases pass.
- Any failed tests have documented resolution or accepted remediation.
- Stakeholders confirm that the reporting outputs meet business expectations.
- Business Information Services confirms the datasets are suitable for Power BI dashboard development.

## 2. Test Scenarios

### Scenario 1: Verify Budget Utilization Calculation

Objective: confirm that budget utilization is calculated as actual spend divided by approved budget.

Business importance: Finance users must trust budget utilization before using dashboards for fiscal review or executive reporting.

Datasets:

- `budget_summary.csv`
- `budget_monthly_dashboard.csv`

### Scenario 2: Verify Over Budget Flag

Objective: confirm that departments exceeding approved budget are correctly flagged.

Business importance: over-budget departments require Finance review, variance explanation, and possible executive escalation.

Datasets:

- `budget_summary.csv`
- `budget_monthly_dashboard.csv`

### Scenario 3: Verify Procurement Delay Flag

Objective: confirm that procurement requests exceeding the approval delay threshold are correctly flagged.

Business importance: delayed approvals should be visible to Procurement and Finance leadership for bottleneck review.

Dataset:

- `procurement_dashboard.csv`

### Scenario 4: Verify Critical Maintenance Alert

Objective: confirm that critical unresolved maintenance requests older than 48 hours are flagged.

Business importance: critical maintenance backlog may represent safety, continuity, service, or compliance risk.

Dataset:

- `maintenance_dashboard.csv`

### Scenario 5: Verify Workforce Vacancy Metrics

Objective: confirm that workforce vacancy metrics are available and aggregated correctly by department and fiscal period.

Business importance: vacancy data provides staffing context for budget pressure, service delays, and operational capacity.

Dataset:

- `hr_workforce_dashboard.csv`

### Scenario 6: Verify Dashboard Filters

Objective: confirm that dashboard outputs support filtering by fiscal year, fiscal period, department, and division.

Business importance: executives, Finance analysts, and department managers require consistent filters across reporting pages.

Datasets:

- `dim_department.csv`
- `dim_date.csv`
- All fact outputs in `data/powerbi/`

## 3. Test Case Table

| Test ID | Requirement | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| UAT-001 | Verify Budget Utilization Calculation | Open `budget_summary.csv`; filter FY2025; calculate `total_actual_spend / total_budget * 100` for Information Technology. | Calculated utilization equals approximately 107.00%. | Information Technology FY2025 utilization is 107.00%. | Pass |
| UAT-002 | Verify Budget Utilization Calculation | Open `budget_summary.csv`; filter FY2025; calculate enterprise utilization as total actual spend divided by total budget. | Enterprise FY2025 utilization equals approximately 96.88%. | Enterprise FY2025 utilization is 96.88%. | Pass |
| UAT-003 | Verify Budget Utilization Calculation | Open `budget_monthly_dashboard.csv`; select sample rows; recalculate `actual_spend / monthly_budget * 100`. | Recalculated row-level utilization matches `budget_utilization_pct` within rounding tolerance. | Row-level utilization matched expected calculation. | Pass |
| UAT-004 | Verify Over Budget Flag | Open `budget_summary.csv`; filter FY2025 and `department_name = Information Technology`. | `is_over_budget` is true. | IT is flagged as over budget. | Pass |
| UAT-005 | Verify Over Budget Flag | Open `budget_summary.csv`; filter FY2025 and count rows where `is_over_budget = TRUE`. | Count equals 1 department. | One department is over budget. | Pass |
| UAT-006 | Verify Over Budget Flag | Open `budget_summary.csv`; filter FY2025 and `department_name = Student Affairs`. | Student Affairs is not over budget but utilization is approximately 98%. | Student Affairs shows 98.00% utilization and is not over budget. | Pass |
| UAT-007 | Verify Procurement Delay Flag | Open `procurement_dashboard.csv`; filter rows where `days_to_approve > 10`. | `is_approval_delayed` is true for delayed rows. | Delayed approval rows are flagged. | Pass |
| UAT-008 | Verify Procurement Delay Flag | Count rows in `procurement_dashboard.csv` where `is_approval_delayed = TRUE`. | Delayed approvals are available for dashboard reporting. | 43 delayed approvals are present. | Pass |
| UAT-009 | Verify Procurement Delay Flag | Calculate average `days_to_approve` for Information Technology and compare with university average. | IT average approval time is greater than university average. | IT average is 14.24 days; university average is 8.09 days. | Pass |
| UAT-010 | Verify Critical Maintenance Alert | Open `maintenance_dashboard.csv`; filter `priority = Critical`, `status != Completed`, and `days_to_resolve > 2`. | Matching rows have `is_critical_over_48h = TRUE`. | Critical overdue rows are flagged. | Pass |
| UAT-011 | Verify Critical Maintenance Alert | Count rows where `is_critical_over_48h = TRUE`. | At least one critical overdue maintenance request exists. | Four critical overdue maintenance requests exist. | Pass |
| UAT-012 | Verify Critical Maintenance Alert | Review fields for critical overdue records. | Work order number, building, request type, priority, status, assigned team, days to resolve, and estimated cost are available. | Required fields are available in `maintenance_dashboard.csv`. | Pass |
| UAT-013 | Verify Workforce Vacancy Metrics | Open `hr_workforce_dashboard.csv`; filter latest month `2025-06-01`; sum `vacancies`. | Latest-month vacancy total is available. | Latest-month vacancy total is 25. | Pass |
| UAT-014 | Verify Workforce Vacancy Metrics | Open `hr_workforce_dashboard.csv`; filter latest month `2025-06-01`; sum `total_headcount`. | Latest-month headcount total is available. | Latest-month headcount total is 680. | Pass |
| UAT-015 | Verify Workforce Vacancy Metrics | Filter latest month and `department_name = Facilities Management`. | Facilities Management vacancy and headcount values are available. | Facilities Management has 111 headcount and 4 vacancies. | Pass |
| UAT-016 | Verify Dashboard Filters | Open `dim_department.csv`; confirm department fields exist. | `department_id`, `department_name`, `division`, `department_type`, `vp_owner`, and `is_academic` are available for filtering. | Department filter fields are available. | Pass |
| UAT-017 | Verify Dashboard Filters | Open `dim_date.csv`; confirm fiscal fields exist. | `fiscal_year`, `fiscal_quarter`, and `fiscal_month` are available. | Fiscal filter fields are available. | Pass |
| UAT-018 | Verify Dashboard Filters | Confirm all fact files include `department_id`. | Every fact dataset can join or filter through `dim_department`. | All fact outputs include `department_id`. | Pass |
| UAT-019 | Verify Dashboard Filters | Confirm budget monthly data includes `date_key`. | Monthly budget data can connect to `dim_date`. | `budget_monthly_dashboard.csv` includes `date_key`. | Pass |
| UAT-020 | Verify Dashboard Filters | Confirm procurement and maintenance data include lifecycle date keys. | Procurement and maintenance support lifecycle date analysis. | Procurement and maintenance files include request, approval/completion, and other date keys as applicable. | Pass |

## 4. UAT Signoff Section

The following stakeholders confirm that the UAT results meet business expectations for the prototype version of the Higher Education Enterprise Analytics & Decision Support Platform.

| Stakeholder Group | Representative | Review Area | Signoff Decision | Date | Notes |
|---|---|---|---|---|---|
| Finance | Finance Lead / Budget Office | Budget utilization, variance, over-budget flag, dashboard filters | Approved | TBD | Confirms budget calculations and IT over-budget scenario. |
| Procurement | Procurement Office Lead | Approval cycle time, delayed approval flag, department comparison | Approved | TBD | Confirms procurement delay logic and IT bottleneck visibility. |
| Facilities | Facilities Management Lead | Critical maintenance alert, work order fields, backlog reporting | Approved | TBD | Confirms critical over-48-hour alert logic. |
| HR | HR Data Steward | Headcount, FTE, salary expense, vacancies, turnover metrics | Approved | TBD | Confirms workforce metrics are available for reporting. |
| Business Information Services | Analytics / BI Lead | Data model, CSV outputs, validation scripts, dashboard readiness | Approved | TBD | Confirms datasets are suitable for Power BI dashboard development. |

## UAT Summary

All UAT scenarios passed for the prototype implementation. The platform successfully validates the core business requirements:

- Budget utilization is calculated correctly.
- Over-budget departments are flagged.
- Procurement approval delays are identified.
- Critical maintenance alerts are available.
- Workforce vacancy metrics are present.
- Dashboard filters are supported through department and date reference data.

This UAT package demonstrates that the solution is ready for dashboard buildout and stakeholder walkthrough in a university Finance & Business Information Services context.
