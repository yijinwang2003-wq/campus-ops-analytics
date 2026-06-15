# Business Requirements Document

## Project

**Higher Education Enterprise Analytics & Decision Support Platform**

## Executive Summary

The university currently relies on separate operational reporting across Finance, Procurement, Human Resources, and Facilities. Department managers can see portions of their activity, but finance leadership does not have a single, trusted view of budget utilization, procurement cycle time, maintenance backlog, or workforce trends. This creates delayed variance detection, manual reconciliation, inconsistent definitions, and limited visibility into operational risk.

This project defines the requirements for a unified analytics platform that consolidates core enterprise data into a PostgreSQL-compatible star schema and produces dashboard-ready CSV datasets for Power BI. The platform supports department-level budget monitoring, procurement bottleneck analysis, facilities backlog review, and HR workforce trend reporting. The synthetic dataset models realistic findings, including Information Technology exceeding FY2025 budget by 7%, Student Affairs reaching 98% utilization, IT procurement approval cycles averaging 14.24 days versus an 8.09-day university average, and four critical facilities requests unresolved for more than 48 hours.

## Business Objectives

- Establish a shared reporting layer across Finance, Procurement, Facilities, and HR.
- Reduce manual spreadsheet reconciliation for department managers and finance analysts.
- Identify budget pressure earlier in the fiscal year.
- Monitor procurement approval delays and finance review bottlenecks.
- Surface critical maintenance backlog and service risk.
- Provide workforce trend visibility by department, fiscal period, and employee group.
- Support executive decision-making through consistent metrics and repeatable data validation.

## Stakeholders

| Stakeholder | Role | Primary Needs |
|---|---|---|
| Vice President for Finance | Executive sponsor | Budget utilization, enterprise risk, variance explanations |
| Finance & Business Information Services | Product owner / analytics team | Integrated data model, metric definitions, data quality controls |
| Budget Office | Finance subject matter expert | Budget-to-actual variance, commitments, department drilldown |
| Procurement Services | Process owner | Approval cycle time, delayed requests, workload visibility |
| Facilities Management | Operational owner | Critical backlog, work order aging, cost and completion trends |
| Human Resources | Data steward | Headcount, FTE, salary expense, vacancies, turnover trends |
| Department Managers | Business users | Department-specific dashboards and actionable exceptions |
| Internal Audit / Compliance | Oversight | Data lineage, access controls, consistent reporting definitions |
| IT Data Services | Technical partner | Database design, scheduled ETL, secure data delivery |

## In Scope

- Department, date, budget, procurement, maintenance, and HR datasets.
- PostgreSQL-compatible warehouse schema.
- Python-based synthetic data generation, transformation, and validation.
- Power BI-ready CSV exports.
- Business requirements, process analysis, UAT package, executive summary, and README documentation.
- Role-aware reporting requirements for department users, finance leadership, and executives.

## Business Requirements

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

## Non-Functional Requirements

| Category | Requirement |
|---|---|
| Data Refresh | Source data transformations should be executable on demand and schedulable for a daily refresh in a production environment. |
| Auditability | Metric definitions and transformation logic must be traceable to Python scripts and SQL schema. |
| Performance | Dashboard datasets should be pre-aggregated where appropriate to support responsive Power BI interactions. |
| Maintainability | Data generation, transformation, and validation scripts must be separated by responsibility. |
| Portability | SQL must remain PostgreSQL-compatible and CSV outputs must be usable without proprietary database dependencies. |
| Data Quality | Validation checks must fail clearly when required fields, dates, calculations, or modeled business conditions are invalid. |
| Usability | Dashboard fields should use business-readable names suitable for analysts and department managers. |
| Security | Role-based reporting design must prevent unauthorized access to cross-department financial details and sensitive HR compensation information. |

## Out of Scope

- Real university data ingestion.
- Live API integrations with ERP, procurement, HRIS, or work order systems.
- Power BI `.pbix` file development.
- Authentication implementation.
- Production deployment automation.
- Real-time streaming analytics.
- Predictive forecasting beyond descriptive and diagnostic analytics.
- Replacement of source systems of record.

## Assumptions

- Fiscal year runs from July 1 through June 30.
- Department IDs are treated as stable conformed identifiers.
- The reporting snapshot date for unresolved work order aging is June 30, 2025.
- CSV exports are the target handoff format for dashboard development.
- The synthetic data intentionally models realistic enterprise patterns and should not be interpreted as actual institutional performance.
