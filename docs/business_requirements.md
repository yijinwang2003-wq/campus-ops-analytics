# Business Requirements Final

## Higher Education Enterprise Analytics & Decision Support Platform

Prepared for: University Finance & Business Information Services  
Document type: Final Business Requirements Package  
Intended audience: University Business Analyst, Business Systems Analyst, Reporting Analyst, Institutional Analytics, Finance leadership, and administrative operations stakeholders

## 1. Executive Summary

The Higher Education Enterprise Analytics & Decision Support Platform is a university administrative analytics initiative designed to unify reporting across Finance, Procurement, Facilities, and Human Resources. The project addresses a common institutional challenge: business units operate in separate systems, while leadership needs a single view of budget utilization, procurement bottlenecks, facilities backlog, and workforce trends.

The current reporting environment relies on siloed operational reports, manual spreadsheet reconciliation, email-based procurement status tracking, and separately prepared executive summaries. These reporting gaps limit the university's ability to identify financial risk, operational delays, and staffing constraints early enough for timely intervention.

The proposed solution establishes a governed reporting layer using a star-schema data model, Python-based data preparation, data validation checks, and Power BI-ready datasets. The platform supports executive monitoring, department-level drilldown, and analyst-led investigation of budget, procurement, facilities, and HR trends.

The synthetic dataset used for the prototype model includes realistic business findings:

- Information Technology exceeds FY2025 budget at approximately 107% utilization.
- Student Affairs reaches approximately 98% utilization and should be monitored as a near-limit department.
- IT procurement approvals average 14.24 days versus an 8.09-day university average.
- Four critical facilities requests remain unresolved for more than 48 hours.
- HR data provides headcount, FTE, salary expense, vacancies, turnover, and headcount trend context by department.

## 2. Business Problem

University administrative reporting is fragmented across multiple business functions. Finance, Procurement, Facilities, and HR each maintain their own operational data, reporting cadence, terminology, and ownership model. While these systems support day-to-day processing, they do not provide a consolidated executive view of institutional performance.

### Core Problems

| Problem Area | Description | Business Impact |
|---|---|---|
| Data silos | Finance, Procurement, Facilities, and HR data are maintained in separate systems and reports. | Leaders cannot easily connect budget pressure, procurement delays, facilities backlog, and workforce capacity. |
| Limited executive visibility | Executive reporting depends on manually prepared summaries and disconnected source reports. | Budget risk and operational bottlenecks may be identified late. |
| Manual reporting processes | Analysts and department managers rely on spreadsheets, email updates, and local reconciliations. | Reporting is time-consuming, difficult to audit, and vulnerable to inconsistent definitions. |
| Inconsistent metric definitions | Budget utilization, delayed approvals, critical backlog, and workforce measures are not governed through a shared reporting layer. | Stakeholders may interpret performance differently. |
| Limited exception monitoring | Operational exceptions are not consistently surfaced in a shared dashboard. | Leadership intervention is reactive rather than proactive. |

## 3. Project Objectives

The project objectives are to:

1. Establish an integrated reporting model across Finance, Procurement, Facilities, and HR.
2. Provide a shared department and fiscal calendar structure for cross-functional analysis.
3. Produce Power BI-ready datasets for executive and operational dashboards.
4. Define consistent KPIs for budget utilization, variance, approval cycle time, maintenance backlog, and workforce trends.
5. Reduce manual spreadsheet-based reporting and reconciliation.
6. Improve early identification of over-budget departments and near-threshold departments.
7. Improve visibility into procurement approval delays and finance review bottlenecks.
8. Surface critical facilities backlog as an executive operational risk.
9. Connect workforce metrics to operational and financial analysis.
10. Provide validation checks that confirm data completeness, calculation accuracy, and expected business conditions.

## 4. Stakeholder Analysis

| Stakeholder | Role in Initiative | Key Interests | Decisions Supported |
|---|---|---|---|
| CFO | Executive sponsor | Fiscal stewardship, budget risk, enterprise performance visibility | Budget intervention, funding prioritization, executive escalation |
| Vice President for Finance | Executive owner | Budget utilization, variance explanation, financial controls | Finance operating review, departmental accountability |
| Finance Department | Primary business owner | Budget-to-actual reporting, commitments, variance analysis, department drilldown | Monthly close review, budget reallocation, department follow-up |
| Budget Office | Finance subject matter expert | Budget categories, fiscal periods, commitments, funding source reporting | Budget monitoring, forecast assumptions, threshold management |
| Procurement Office | Process owner | Approval cycle time, delayed requests, vendor/category analysis, finance review bottlenecks | Workflow improvement, policy review, sourcing strategy |
| Facilities Management | Operational owner | Work order backlog, critical maintenance, building risk, cost and completion trends | Service prioritization, resource planning, risk escalation |
| Human Resources | Data steward | Headcount, FTE, salary expense, vacancies, turnover, workforce planning | Staffing review, vacancy analysis, workforce cost monitoring |
| Business Information Services | Analytics delivery team | Data model, ETL logic, dashboard datasets, validation, documentation | Reporting architecture, data governance, dashboard delivery |
| Department Managers | Business users | Department-specific budget status, procurement status, workforce and service context | Department operations, spend control, request follow-up |
| Internal Audit / Compliance | Oversight stakeholder | Data lineage, consistent definitions, access controls, auditability | Control review, reporting governance, risk assessment |
| IT Data Services | Technical partner | Database design, scheduled ETL, secure data delivery, platform support | Technical implementation and production readiness |
| Executive Leadership | Report consumers | Exception monitoring, decision support, trend visibility | Institutional priorities, escalation, resource allocation |

## 5. Current State Analysis

The current state is characterized by siloed reporting, manual consolidation, and limited cross-domain analysis.

### Finance

Finance reporting focuses on budget, actual spend, commitments, and variance. Reports are typically reviewed monthly or at fiscal checkpoints. Department managers may not have timely visibility into committed spend or the operational drivers behind budget pressure.

Current challenges:

- Budget risk is often identified after expenses have posted.
- Commitments and actuals may be reviewed separately.
- Department reporting depends on spreadsheet exports.
- Leadership lacks a single exception dashboard for over-budget and near-threshold departments.

### Procurement

Procurement requests move through department approval, finance review, sourcing review, purchase order creation, and invoice completion. Status visibility often depends on email follow-up or direct access to procurement tools.

Current challenges:

- Requesters lack transparent status tracking.
- Approval delays are not consistently escalated.
- Finance review bottlenecks are difficult to isolate.
- Vendor, category, and approval-level trends require manual analysis.
- Invoice and completion status are not consistently connected to the original request lifecycle.

### Facilities

Facilities teams manage work orders by building, request type, priority, assigned team, and status. Critical backlog may be visible operationally but is not consistently integrated with executive reporting.

Current challenges:

- Critical unresolved requests are not always elevated in leadership summaries.
- Work order aging is not consistently tied to staffing or resource planning.
- Facilities cost and completion trends are not integrated with financial dashboards.

### Human Resources

HR maintains workforce data including headcount, FTE, salary expense, overtime, vacancies, turnover, and headcount changes. These metrics are often reviewed separately from financial and operational reporting.

Current challenges:

- Workforce trends are not consistently linked to budget pressure or service delivery.
- Salary expense data requires role-based access controls.
- Vacancy context may be missing when reviewing operational backlog or delayed services.

## 6. Future State Solution

The future state solution is an integrated analytics platform that consolidates administrative reporting into a governed, dashboard-ready model. The platform does not replace source systems; it provides a shared reporting and decision-support layer.

### Future-State Capabilities

- Shared `dim_department` dimension across Finance, Procurement, Facilities, and HR.
- Shared fiscal and calendar reporting through `dim_date`.
- Star-schema reporting model with fact datasets for budget, procurement, maintenance, and workforce reporting.
- Power BI-ready CSV outputs for dashboard development.
- Executive Overview dashboard for cross-functional exception monitoring.
- Domain dashboards for Budget Analytics, Procurement Operations, and Facilities & Workforce.
- Automated data validation for keys, dates, calculations, and expected business conditions.
- Role-aware reporting design for executive, Finance, HR, and department manager audiences.

### Future-State Operating Model

| Capability | Future-State Description |
|---|---|
| Data integration | Finance, Procurement, Facilities, and HR data are aligned through shared department and date dimensions. |
| Reporting governance | KPI definitions and transformation logic are documented and repeatable. |
| Executive monitoring | Leaders can review budget, procurement, facilities, and workforce exceptions in one view. |
| Department accountability | Managers can review department-level budget utilization, procurement status, and workforce context. |
| Data quality | Validation scripts confirm referential integrity, calculation accuracy, and business story conditions. |

## 7. Scope

### In Scope

- Department and date dimensions.
- Budget summary and monthly budget reporting.
- Procurement request lifecycle reporting.
- Facilities maintenance work order reporting.
- HR workforce trend reporting.
- Power BI-ready CSV outputs.
- Business requirements, dashboard requirements, data model documentation, and validation.
- Role-aware reporting requirements.

### Out of Scope

- Real university data ingestion.
- Live API integrations with ERP, procurement, HRIS, or work order systems.
- Production deployment automation.
- Power BI `.pbix` delivery.
- Authentication implementation.
- Predictive forecasting beyond descriptive and diagnostic analytics.
- Replacement of source systems of record.

## 8. Business Requirements

| ID | Domain | Requirement | Acceptance Criteria |
|---|---|---|---|
| BR-001 | Finance & Budget | The platform shall provide department-level FY2024 and FY2025 budget-to-actual reporting. | Users can filter budget metrics by fiscal year and department; total budget, actual spend, variance, and utilization percentage are available in the dashboard dataset. |
| BR-002 | Finance & Budget | The platform shall calculate budget utilization percentage using actual spend divided by approved budget. | `budget_utilization_pct` matches recalculated values within rounding tolerance in validation tests. |
| BR-003 | Finance & Budget | The platform shall identify departments that exceed approved annual budget. | `is_over_budget` is true when actual spend is greater than total budget; IT FY2025 is flagged as over budget at approximately 107% utilization. |
| BR-004 | Finance & Budget | The platform shall identify departments nearing budget limits. | Student Affairs FY2025 appears near threshold with approximately 98% utilization and remaining budget variance of about $108,000. |
| BR-005 | Finance & Budget | The platform shall support monthly budget trend analysis by category. | Power BI export includes fiscal year, fiscal period, budget category, monthly budget, actual spend, committed amount, and variance fields. |
| BR-006 | Procurement | The platform shall calculate procurement approval cycle time. | `days_to_approve` is calculated as approval date minus request date for each procurement request. |
| BR-007 | Procurement | The platform shall flag delayed procurement approvals. | `is_approval_delayed` is true for requests taking more than 10 days to approve. |
| BR-008 | Procurement | The platform shall compare department procurement cycle time to the university average. | IT average approval time is greater than the university average; generated data shows IT at 14.24 days versus 8.09 days overall. |
| BR-009 | Procurement | The platform shall support procurement analysis by vendor, category, status, approval level, and department. | Export includes vendor name, procurement category, request status, approval level, competitive bid flag, and finance reviewer. |
| BR-010 | Facilities | The platform shall calculate maintenance resolution time. | `days_to_resolve` is calculated using completion date when available and reporting snapshot date for unresolved requests. |
| BR-011 | Facilities | The platform shall flag critical open requests older than 48 hours. | `is_critical_over_48h` is true for critical, unresolved maintenance requests open more than two days; generated data contains at least four records. |
| BR-012 | Facilities | The platform shall support backlog monitoring by priority, building, request type, assigned team, and department. | Maintenance dashboard export includes all listed fields and status. |
| BR-013 | HR & Workforce | The platform shall provide monthly headcount, FTE, salary expense, vacancy, and turnover measures. | HR dashboard export includes department, fiscal year, fiscal period, total headcount, total FTE, salary expense, vacancies, and turnover count. |
| BR-014 | HR & Workforce | The platform shall show workforce trends over time by department. | HR output includes month start date and prior-month headcount comparison fields. |
| BR-015 | Dashboard / Reporting | The platform shall provide dashboard-ready exports for Power BI. | CSV files are created in `data/powerbi/` for budget, procurement, maintenance, HR, department dimension, and date dimension. |
| BR-016 | Dashboard / Reporting | The platform shall use consistent department identifiers across all subject areas. | Validation confirms no missing or invalid department IDs in dashboard datasets. |
| BR-017 | Dashboard / Reporting | The platform shall provide a shared fiscal calendar. | Date dimension supports calendar date, fiscal year, fiscal quarter, fiscal month, month start, and month end. |
| BR-018 | Data Quality | The platform shall include automated validation checks for key calculations and business story conditions. | `validate_data.py` and pytest tests pass for department integrity, date validity, budget calculations, IT over-budget condition, IT procurement delays, and critical overdue maintenance. |
| BR-019 | Security / Role-Based Access | The reporting solution shall support role-based access by user group. | Security design supports executive enterprise view, finance cross-department view, and department manager restricted view. |
| BR-020 | Security / Role-Based Access | Sensitive HR salary data shall be restricted to approved roles. | HR compensation measures are only available to HR, Finance leadership, and approved executive users in the target dashboard design. |

## 9. Reporting Requirements

| ID | Reporting Requirement |
|---|---|
| RR-001 | Reports must support executive summary views and department-level drilldown. |
| RR-002 | Reports must distinguish over-budget departments from near-threshold departments. |
| RR-003 | Reports must compare procurement approval cycle time by department and identify departments above the university average. |
| RR-004 | Reports must identify delayed procurement approvals using a defined delay threshold. |
| RR-005 | Reports must show facilities backlog by priority, status, building, request type, and assigned team. |
| RR-006 | Reports must identify critical maintenance requests unresolved for more than 48 hours. |
| RR-007 | Reports must show workforce capacity indicators such as headcount, FTE, salary expense, vacancies, and turnover. |
| RR-008 | Reports must support fiscal-year and fiscal-period filtering. |
| RR-009 | Reports must use consistent department naming and identifiers across all domains. |
| RR-010 | Reports must use business-friendly field names, clear KPI labels, and consistent threshold colors. |

## 10. Dashboard Requirements

The Power BI dashboard package shall include four primary pages.

| Page | Audience | Required Content | Decision Supported |
|---|---|---|---|
| Executive Overview | CFO, VP Finance, executive leadership | Budget utilization, over-budget count, procurement cycle time, critical backlog count, workforce indicator, exception matrix | Executive escalation and enterprise risk monitoring |
| Budget Analytics | Finance Department, Budget Office, department managers | Budget vs actual, variance by department, category spend, monthly utilization trends, watchlist indicators | Budget review and department follow-up |
| Procurement Operations | Procurement Office, Finance reviewers, department managers | Approval days by department, delayed approvals, category/status mix, vendor and approval-level analysis | Bottleneck identification and process improvement |
| Facilities & Workforce | Facilities Management, HR, Finance leadership | Work orders by priority/status, critical overdue list, resolution time, headcount, vacancies, salary context | Service risk review and resource planning |

## 11. KPI Definitions

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

## 12. Data Sources

| Data Source | Dataset | Description |
|---|---|---|
| Finance | `budget_summary.csv` | Annual budget-to-actual summary by department and fiscal year. |
| Finance | `budget_monthly_dashboard.csv` | Monthly budget, actual spend, commitments, variance, category, and funding source. |
| Procurement | `procurement_dashboard.csv` | Procurement requests, vendors, approval dates, PO dates, invoices, status, category, approval level, reviewer, and cycle-time fields. |
| Facilities | `maintenance_dashboard.csv` | Work orders, buildings, priority, request type, status, assigned team, costs, and resolution aging. |
| Human Resources | `hr_workforce_dashboard.csv` | Monthly headcount, FTE, salary expense, overtime, vacancies, turnover, and headcount change. |
| Enterprise Reference Data | `dim_department.csv` | Department, division, department type, VP owner, and academic flag. |
| Enterprise Reference Data | `dim_date.csv` | Calendar and fiscal date dimension. |

## 13. Non-Functional Requirements

| Category | Requirement |
|---|---|
| Data Refresh | Source data transformations should be executable on demand and schedulable for recurring refresh in a production environment. |
| Auditability | Metric definitions and transformation logic must be traceable to source scripts, SQL schema, and documentation. |
| Performance | Dashboard datasets should be curated and pre-aggregated where appropriate for responsive Power BI interaction. |
| Maintainability | Data generation, transformation, validation, and reporting documentation should remain separated by responsibility. |
| Portability | SQL should remain PostgreSQL-compatible and CSV outputs should remain usable without proprietary database dependencies. |
| Data Quality | Validation checks must fail clearly when required fields, dates, calculations, or modeled business conditions are invalid. |
| Usability | Dashboard fields should use business-readable names and support executive, analyst, and department manager interpretation. |
| Security | Role-based reporting design must prevent unauthorized access to cross-department financial details and sensitive HR compensation information. |

## 14. Assumptions and Constraints

### Assumptions

- Fiscal year runs from July 1 through June 30.
- Department is the primary shared organizational dimension.
- Department IDs are stable across reporting domains.
- Power BI is the target dashboard platform.
- CSV exports are acceptable for dashboard demonstration and prototyping.
- The reporting snapshot date for unresolved maintenance aging is June 30, 2025.
- Synthetic data is representative of realistic university administrative scenarios but is not actual institutional data.

### Constraints

- The project does not connect to live university systems.
- The project does not include production authentication or authorization.
- The project does not include a deployed production database.
- Power BI `.pbix` delivery is outside scope.
- HR salary data must be treated as sensitive in any production implementation.
- Procurement and maintenance lifecycle date reporting may require role-playing date dimensions in a mature semantic model.

## 15. Expected Business Benefits

| Benefit | Description |
|---|---|
| Improved executive visibility | Leadership can review budget, procurement, facilities, and workforce exceptions in one reporting environment. |
| Earlier budget risk detection | Finance can identify over-budget and near-threshold departments earlier in the fiscal cycle. |
| Reduced manual reporting | Standardized dashboard datasets reduce spreadsheet consolidation and ad hoc reporting effort. |
| Procurement transparency | Approval cycle-time reporting identifies bottlenecks by department, category, approval level, and reviewer. |
| Stronger facilities risk monitoring | Critical overdue maintenance requests are visible as operational exceptions. |
| Workforce-informed decisions | Headcount, vacancies, and salary expense provide context for financial and operational performance. |
| Shared metric definitions | KPI definitions improve stakeholder alignment and trust in reporting. |
| Stronger analyst delivery model | The project demonstrates requirements gathering, process analysis, data modeling, ETL, validation, dashboard design, UAT, and executive reporting. |

## 16. Acceptance Criteria

| ID | Acceptance Criteria |
|---|---|
| AC-001 | The solution identifies Finance, Procurement, Facilities, HR, Department, and Date datasets. |
| AC-002 | Dashboard-ready CSV outputs are produced in `data/powerbi/`. |
| AC-003 | Budget utilization percentage is calculated as actual spend divided by budget. |
| AC-004 | Budget variance is calculated as budget minus actual spend. |
| AC-005 | FY2025 IT budget utilization is greater than 100% and appears as an over-budget exception. |
| AC-006 | FY2025 Student Affairs budget utilization appears near budget limit at approximately 98%. |
| AC-007 | Procurement approval cycle time is calculated in days. |
| AC-008 | IT procurement approval time is greater than the university average and appears as a bottleneck. |
| AC-009 | Critical maintenance requests unresolved for more than 48 hours are flagged. |
| AC-010 | HR workforce reporting includes headcount, FTE, salary expense, vacancies, and turnover. |
| AC-011 | Dashboard requirements include Executive Overview, Budget Analytics, Procurement Operations, and Facilities & Workforce pages. |
| AC-012 | The data model uses department and date dimensions to support cross-functional filtering. |
| AC-013 | The reporting package includes KPI definitions, data source documentation, and role-aware security expectations. |
| AC-014 | Data validation scripts pass without errors. |
| AC-015 | Documentation is written in a professional consulting style suitable for University Business Analyst, Business Systems Analyst, Reporting Analyst, and Institutional Analytics roles. |
