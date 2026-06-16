# Business Requirements Document

## Higher Education Enterprise Analytics Platform

Prepared for: University Finance & Business Information Services  
Project type: Enterprise analytics and decision support initiative  
Primary users: Finance leadership, department managers, Procurement, Facilities, HR, and executive administration

## 1. Executive Summary

The Higher Education Enterprise Analytics Platform is designed to provide a unified reporting and decision support layer for university administrative operations. The platform integrates Finance, Procurement, Facilities, and Human Resources reporting into a shared analytics model that supports executive visibility, department-level accountability, and operational performance monitoring.

The current reporting environment is fragmented across multiple functional areas. Finance teams monitor budget performance separately from procurement cycle time, facilities backlog, and workforce trends. Department leaders often rely on static spreadsheets, manually prepared reports, and email-based status updates. As a result, leadership has limited ability to identify budget risk, procurement bottlenecks, critical maintenance issues, or staffing pressure in a timely and consistent way.

This initiative establishes a structured analytics foundation using synthetic but realistic university data, a star-schema data model, Python-based data preparation, Power BI-ready datasets, and professional documentation. The platform demonstrates how a Finance & Business Information Services team can move from siloed operational reporting toward integrated enterprise analytics.

## 2. Business Problem

### Data Silos Across Finance, Procurement, Facilities, and HR

University administrative data is typically distributed across separate systems of record:

- Finance systems track budgets, actual spend, commitments, and fiscal periods.
- Procurement systems track purchase requests, approvals, vendors, purchase orders, and invoices.
- Facilities systems track work orders, priorities, buildings, assigned teams, costs, and completion status.
- HR systems track headcount, FTE, salary expense, vacancies, overtime, and turnover.

These systems serve different operational purposes and use different reporting structures. Without a shared analytics layer, leaders cannot easily compare financial risk, procurement delays, facilities service levels, and workforce capacity across departments.

### Limited Executive Visibility

Executive leaders need concise, reliable indicators of institutional performance. In the current state, enterprise-level insight is limited because:

- Budget exceptions are reviewed separately from procurement and staffing drivers.
- Procurement delays are not consistently visible to Finance leadership.
- Critical facilities backlog is not integrated with executive financial reporting.
- Workforce trends are not consistently connected to operational performance.
- Department-level comparisons require manual consolidation.

### Manual Reporting Processes

Many reporting activities depend on manual steps:

- Analysts export data from separate systems.
- Department managers maintain local spreadsheets.
- Procurement status is communicated through email.
- Finance reviews are performed outside a shared reporting workflow.
- Executive updates are prepared as static summaries.

Manual reporting increases the risk of inconsistent definitions, outdated data, delayed escalation, and limited auditability.

## 3. Project Objectives

The objectives of the Higher Education Enterprise Analytics Platform are to:

1. Create an integrated analytics model across Finance, Procurement, Facilities, and HR.
2. Provide a shared department and fiscal-period reporting structure.
3. Improve executive visibility into budget utilization, procurement cycle time, facilities backlog, and workforce trends.
4. Reduce reliance on manual spreadsheet consolidation.
5. Support department-level budget accountability and operational review.
6. Establish dashboard-ready datasets for Power BI.
7. Define clear KPI calculations and reporting requirements.
8. Provide a repeatable framework for data validation and quality checks.
9. Demonstrate Business Analyst deliverables including requirements, current-state analysis, future-state design, dashboard specifications, and acceptance criteria.

## 4. Stakeholders

| Stakeholder | Role in Initiative | Key Interests |
|---|---|---|
| CFO | Executive sponsor | Budget risk, fiscal stewardship, enterprise performance visibility |
| Finance Department | Primary business owner | Budget-to-actual reporting, variance analysis, commitments, department accountability |
| Procurement Office | Process owner | Approval cycle time, delayed requests, vendor/category analysis, finance review bottlenecks |
| Facilities Management | Operational owner | Work order backlog, critical maintenance requests, building/service risk, cost visibility |
| Human Resources | Data steward | Headcount, FTE, salary expense, vacancies, turnover, workforce planning |
| Business Information Services | Analytics delivery team | Data model, ETL process, dashboard datasets, validation, documentation, stakeholder reporting |
| Department Managers | Business users | Department-level performance, budget status, procurement status, workforce and service context |
| Executive Leadership | Report consumers | Exception monitoring, decision support, trend visibility |

## 5. Current State Analysis

The current state is characterized by functional reporting silos and limited cross-domain visibility.

### Finance Current State

Finance reporting focuses on budget, actual spend, and variance. Reports are typically reviewed monthly or at fiscal checkpoints. Department managers may not have real-time visibility into committed spend or operational drivers behind budget pressure.

Current challenges:

- Budget risk is often identified after spend has posted.
- Commitments and actuals may be reviewed separately.
- Department-level reporting depends on spreadsheet extracts.
- Leadership lacks a unified exception dashboard.

### Procurement Current State

Procurement requests move through approval, finance review, sourcing review, purchase order creation, and invoice matching. Status visibility is often dependent on email updates or system-specific access.

Current challenges:

- Requesters lack transparent status tracking.
- Approval delays are not consistently escalated.
- Finance review bottlenecks are difficult to isolate.
- Vendor and category trends require manual analysis.

### Facilities Current State

Facilities teams manage work orders by building, priority, request type, assigned team, and status. Critical backlog may be visible operationally but not consistently elevated to executive reporting.

Current challenges:

- Critical unresolved requests are not always included in executive summaries.
- Work order aging is not consistently tied to resource planning.
- Facilities costs are not integrated with financial dashboards.

### HR Current State

HR maintains workforce data including headcount, FTE, vacancies, salary expense, overtime, and turnover. These metrics are often reviewed separately from financial and operational reporting.

Current challenges:

- Staffing trends are not consistently linked to budget or service delivery.
- Salary expense detail requires controlled access.
- Vacancy context is not always available when reviewing operational backlog.

## 6. Future State Solution

The future state solution is an integrated analytics platform that consolidates administrative reporting into a governed, dashboard-ready model.

Key future-state capabilities:

- Shared department dimension across all subject areas.
- Shared fiscal calendar for consistent time-period reporting.
- Star-schema reporting model with fact tables for budget, procurement, maintenance, and HR.
- Power BI-ready CSV outputs for dashboard development.
- KPI definitions for budget utilization, variance, approval cycle time, critical backlog, headcount, and vacancies.
- Executive Overview dashboard for cross-functional exception monitoring.
- Domain dashboards for Budget Analytics, Procurement Operations, and Facilities & Workforce.
- Data quality validation to confirm keys, dates, calculations, and expected business conditions.

The future state enables leadership to move from static reporting to exception-based management.

## 7. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | The platform shall provide department-level budget-to-actual reporting by fiscal year. | High |
| FR-002 | The platform shall provide monthly budget reporting by fiscal period and budget category. | High |
| FR-003 | The platform shall calculate budget utilization percentage, budget variance, and budget variance percentage. | High |
| FR-004 | The platform shall identify departments that exceed budget. | High |
| FR-005 | The platform shall identify departments at or above budget watch thresholds. | High |
| FR-006 | The platform shall provide procurement request-level reporting by department, vendor, category, status, approval level, and reviewer. | High |
| FR-007 | The platform shall calculate procurement approval cycle time. | High |
| FR-008 | The platform shall flag delayed procurement approvals. | High |
| FR-009 | The platform shall provide maintenance work order reporting by department, building, request type, priority, status, and assigned team. | High |
| FR-010 | The platform shall calculate days to resolve maintenance requests. | High |
| FR-011 | The platform shall flag critical unresolved maintenance requests older than 48 hours. | High |
| FR-012 | The platform shall provide HR workforce reporting by department and fiscal period. | High |
| FR-013 | The platform shall report headcount, FTE, salary expense, overtime, vacancies, turnover, and headcount change. | Medium |
| FR-014 | The platform shall support filtering by department, division, department type, fiscal year, and fiscal period. | High |
| FR-015 | The platform shall produce dashboard-ready CSV outputs for Power BI. | High |
| FR-016 | The platform shall include automated validation checks for data quality and KPI logic. | High |

## 8. Reporting Requirements

| ID | Reporting Requirement |
|---|---|
| RR-001 | Reports must support executive summary views and department-level drilldown. |
| RR-002 | Reports must distinguish over-budget departments from near-threshold departments. |
| RR-003 | Reports must compare procurement approval cycle time by department. |
| RR-004 | Reports must identify delayed procurement approvals using a defined delay threshold. |
| RR-005 | Reports must show facilities backlog by priority and status. |
| RR-006 | Reports must identify critical maintenance requests unresolved for more than 48 hours. |
| RR-007 | Reports must show workforce capacity indicators such as headcount and vacancies. |
| RR-008 | Reports must support fiscal-year and fiscal-period filtering. |
| RR-009 | Reports must use consistent department naming and identifiers across all domains. |
| RR-010 | Reports must use business-friendly field names and clear KPI labels. |

## 9. Dashboard Requirements

The Power BI dashboard package shall include four pages.

### Page 1: Executive Overview

Purpose: provide executive leadership with a consolidated view of financial and operational risk.

Required content:

- Budget utilization summary.
- Budget exception count.
- Procurement approval cycle time.
- Critical facilities backlog count.
- Workforce capacity indicator.
- Department-level exception matrix.

### Page 2: Budget Analytics

Purpose: support Finance review of budget-to-actual performance and department variance.

Required content:

- Budget vs actual by department.
- Budget variance by department.
- Spend by budget category.
- Monthly utilization trends.
- Over-budget and watchlist indicators.

### Page 3: Procurement Operations

Purpose: support procurement cycle-time monitoring and bottleneck identification.

Required content:

- Average approval days by department.
- Delayed approval count.
- Requests by category and status.
- Vendor and approval-level analysis.
- IT procurement cycle-time exception visibility.

### Page 4: Facilities & Workforce

Purpose: connect facilities service risk with workforce capacity.

Required content:

- Work orders by priority and status.
- Critical overdue work order list.
- Average days to resolve by request type.
- Headcount and vacancies by department.
- Salary or workforce trend context.

## 10. KPI Definitions

| KPI | Definition | Business Use |
|---|---|---|
| Total Budget | Sum of approved budget. | Establishes fiscal capacity by department or enterprise. |
| Actual Spend | Sum of recognized spend. | Shows expense activity against budget. |
| Budget Variance | Budget minus actual spend. | Identifies remaining budget or overspend. |
| Budget Utilization % | Actual spend divided by budget. | Measures how much budget capacity has been used. |
| Over-Budget Department Count | Count of departments where actual spend exceeds budget. | Executive exception monitoring. |
| Watchlist Department Count | Count of departments at or above a defined utilization threshold, such as 95%. | Early warning for departments nearing budget limits. |
| Days to Approve | Approval date minus request date. | Measures procurement cycle time. |
| Delayed Approval Count | Count of procurement requests exceeding the approval delay threshold. | Identifies procurement bottlenecks. |
| Days to Complete | Invoice date minus request date. | Measures procurement lifecycle completion time. |
| Open Work Orders | Count of maintenance requests not completed. | Indicates facilities backlog. |
| Critical Over 48h | Count of critical unresolved maintenance requests open more than 48 hours. | Highlights operational and service risk. |
| Days to Resolve | Completed date or reporting snapshot date minus request date. | Measures maintenance resolution performance. |
| Headcount | Number of employees or workers in a department. | Workforce capacity indicator. |
| FTE | Full-time equivalent staffing. | Capacity and resource planning metric. |
| Vacancies | Open positions by department. | Staffing pressure indicator. |
| Salary Expense | Monthly salary expense. | Workforce cost monitoring. |

## 11. Data Sources

| Data Source | Dataset | Description |
|---|---|---|
| Finance | `budget_summary.csv` | Annual budget-to-actual summary by department and fiscal year. |
| Finance | `budget_monthly_dashboard.csv` | Monthly budget, actual spend, commitments, variance, category, and funding source. |
| Procurement | `procurement_dashboard.csv` | Procurement requests, vendors, approval dates, PO dates, invoices, status, category, and cycle-time fields. |
| Facilities | `maintenance_dashboard.csv` | Work orders, buildings, priority, request type, status, assigned team, costs, and resolution aging. |
| Human Resources | `hr_workforce_dashboard.csv` | Monthly headcount, FTE, salary expense, overtime, vacancies, turnover, and headcount change. |
| Enterprise Reference Data | `dim_department.csv` | Department, division, department type, VP owner, and academic flag. |
| Enterprise Reference Data | `dim_date.csv` | Calendar and fiscal date dimension. |

## 12. Assumptions and Constraints

### Assumptions

- Fiscal year reporting is required for executive and Finance users.
- Department is the primary shared organizational dimension.
- Power BI is the target dashboard platform.
- CSV outputs are acceptable for a portfolio prototype and dashboard development.
- Synthetic data is representative of realistic university administrative reporting scenarios.
- The reporting snapshot date for unresolved maintenance aging is June 30, 2025.

### Constraints

- The project does not connect to real university source systems.
- The project does not include a deployed production database.
- The project does not include Power BI `.pbix` files because it is optimized for a Mac and Power BI Service workflow.
- HR salary data should be treated as sensitive and restricted in a production implementation.
- Some date relationships, such as procurement lifecycle dates, require role-playing date design in a mature semantic model.

## 13. Expected Business Benefits

| Benefit | Description |
|---|---|
| Improved executive visibility | Leadership can review budget, procurement, facilities, and workforce exceptions in one reporting environment. |
| Faster budget risk detection | Finance can identify over-budget and near-threshold departments earlier. |
| Reduced manual reporting | Standardized dashboard datasets reduce spreadsheet consolidation and ad hoc reporting effort. |
| Better procurement transparency | Approval cycle-time reporting identifies bottlenecks by department, category, approval level, and reviewer. |
| Stronger facilities risk monitoring | Critical overdue maintenance requests are visible as operational exceptions. |
| Workforce-informed decision-making | Headcount, vacancies, and salary expense provide context for financial and operational performance. |
| Shared metric definitions | KPI definitions improve consistency across stakeholders. |
| Portfolio-ready analyst artifact | The project demonstrates requirements gathering, process analysis, data modeling, ETL, validation, dashboard design, and executive reporting. |

## 14. Acceptance Criteria

| ID | Acceptance Criteria |
|---|---|
| AC-001 | The solution identifies Finance, Procurement, Facilities, HR, Department, and Date datasets. |
| AC-002 | The solution provides dashboard-ready CSV outputs in `data/powerbi/`. |
| AC-003 | Budget utilization percentage is calculated as actual spend divided by budget. |
| AC-004 | Budget variance is calculated as budget minus actual spend. |
| AC-005 | FY2025 IT budget utilization is greater than 100% and appears as an over-budget exception. |
| AC-006 | FY2025 Student Affairs budget utilization appears near budget limit at approximately 98%. |
| AC-007 | Procurement approval cycle time is calculated in days. |
| AC-008 | IT procurement approval time is greater than the university average and appears as a bottleneck. |
| AC-009 | Critical maintenance requests unresolved for more than 48 hours are flagged. |
| AC-010 | HR workforce reporting includes headcount, FTE, salary expense, vacancies, and turnover. |
| AC-011 | The dashboard design includes Executive Overview, Budget Analytics, Procurement Operations, and Facilities & Workforce pages. |
| AC-012 | The data model uses department and date dimensions to support cross-functional filtering. |
| AC-013 | Data validation scripts pass without errors. |
| AC-014 | Documentation is written in a professional consulting style suitable for a Business Analyst portfolio. |
