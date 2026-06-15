# UAT Test Plan

## Overview

This User Acceptance Testing plan validates that the Higher Education Enterprise Analytics & Decision Support Platform meets the business needs of Finance & Business Information Services, department managers, Procurement Services, Facilities Management, and HR. The test cases focus on data integrity, dashboard-ready outputs, metric calculations, exception flags, and role-based reporting expectations.

## Test Scope

- Raw data generation for FY2024 and FY2025.
- Power BI-ready CSV transformation outputs.
- Budget utilization and variance metrics.
- Procurement cycle-time metrics.
- Facilities critical backlog flags.
- HR monthly workforce trends.
- Data quality checks and expected business stories.
- Documentation and dashboard readiness.

## Entry Criteria

- Python dependencies installed from `requirements.txt`.
- `src/generate_data.py` runs successfully.
- `src/transform_data.py` runs successfully.
- Dashboard CSVs exist in `data/powerbi/`.
- Business requirements are approved for testing.

## Exit Criteria

- All Priority 1 and Priority 2 UAT cases pass or have approved remediation.
- Failed v1.0 test cases are retested and documented as fixed in v1.1.
- Finance & Business Information Services confirms that outputs are suitable for Power BI dashboard development.

## UAT Test Cases

| TC-ID | Requirement ID | Test Scenario | Test Steps | Expected Result | Actual Result | Status | Tester | Date |
|---|---|---|---|---|---|---|---|---|
| TC-001 | BR-001 | Verify budget summary output exists. | Run data generation and transformation; open `budget_summary.csv`. | File exists and contains FY2024 and FY2025 rows for all eight departments. | 16 rows generated for 8 departments across 2 fiscal years. | Pass | Finance BA | 2025-07-08 |
| TC-002 | BR-002 | Validate budget utilization calculation. | Recalculate actual spend divided by budget for sample departments. | Calculated values match `budget_utilization_pct`. | Values matched within rounding tolerance. | Pass | Finance Analyst | 2025-07-08 |
| TC-003 | BR-003 | Confirm IT FY2025 over-budget flag. | Filter budget summary to Information Technology and FY2025. | IT is over budget and utilization is greater than 100%. | IT utilization was 107.00% and over-budget flag was true. | Pass | Budget Office | 2025-07-08 |
| TC-004 | BR-004 | Confirm Student Affairs near-limit utilization. | Filter budget summary to Student Affairs and FY2025. | Utilization is approximately 98%. | Student Affairs utilization was 98.00%. | Pass | Budget Office | 2025-07-08 |
| TC-005 | BR-005 | Verify monthly budget category detail. | Open `budget_monthly_dashboard.csv`; filter one department and fiscal year. | Monthly rows include budget category, budget, spend, commitments, and variance. | Required fields were present. | Pass | Finance BA | 2025-07-08 |
| TC-006 | BR-006 | Validate procurement approval days. | Select approved procurement records and recalculate approval date minus request date. | `days_to_approve` matches date difference. | Values matched for sampled records. | Pass | Procurement Analyst | 2025-07-09 |
| TC-007 | BR-007 | Verify delayed approval flag. | Filter procurement records where days to approve are greater than 10. | `is_approval_delayed` is true for delayed records. | Delayed records were flagged correctly. | Pass | Procurement Analyst | 2025-07-09 |
| TC-008 | BR-008 | Confirm IT procurement cycle exceeds average. | Compare IT average approval days to university average. | IT average is greater than university average. | IT averaged 14.24 days versus 8.09 days overall. | Pass | Procurement Services | 2025-07-09 |
| TC-009 | BR-009 | Verify procurement category and vendor fields. | Open procurement dashboard output and inspect fields. | Vendor, category, status, approval level, reviewer, and competitive bid flag are present. | Required fields were present. | Pass | Procurement Services | 2025-07-09 |
| TC-010 | BR-010 | Validate maintenance resolution days. | Recalculate completed date or snapshot date minus request date. | `days_to_resolve` matches expected date difference. | Values matched for sampled records. | Pass | Facilities Analyst | 2025-07-10 |
| TC-011 | BR-011 | Confirm critical overdue maintenance flags. | Filter critical open requests older than two days. | At least one critical overdue request exists and is flagged. | Four critical overdue requests existed. | Pass | Facilities Manager | 2025-07-10 |
| TC-012 | BR-012 | Verify maintenance backlog dimensions. | Inspect maintenance dashboard fields. | Priority, building, request type, assigned team, department, and status are available. | Required fields were present. | Pass | Facilities Analyst | 2025-07-10 |
| TC-013 | BR-013 | Verify HR workforce metrics. | Open HR dashboard output. | Headcount, FTE, salary expense, overtime, vacancies, and turnover are available. | Required fields were present. | Pass | HR Analyst | 2025-07-11 |
| TC-014 | BR-014 | Validate HR monthly trend fields. | Filter one department over several months. | Month start date, prior-month headcount, and headcount change are available. | Trend fields were present. | Pass | HR Analyst | 2025-07-11 |
| TC-015 | BR-015 | Verify all Power BI CSV outputs. | Check `data/powerbi/` folder after transformation. | Budget, procurement, maintenance, HR, department, and date CSVs exist. | All expected files were generated. | Pass | BI Developer | 2025-07-11 |
| TC-016 | BR-016 | Validate department ID integrity. | Compare department IDs across facts to department dimension. | No missing or invalid department IDs. | Automated validation passed. | Pass | Data Analyst | 2025-07-12 |
| TC-017 | BR-017 | Validate fiscal calendar fields. | Open date dimension and inspect fiscal fields. | Fiscal year, fiscal quarter, fiscal month, month start, and month end exist. | Fiscal fields were present. | Pass | Data Analyst | 2025-07-12 |
| TC-018 | BR-018 | Run automated validation script. | Execute `python src/validate_data.py`. | Script completes without assertion errors. | All data validations passed. | Pass | QA Analyst | 2025-07-12 |
| TC-019 | BR-019 | Verify role-based dashboard design notes. | Review requirements and README dashboard descriptions. | Executive, finance, and department manager access expectations are documented. | Role descriptions were documented. | Pass | Product Owner | 2025-07-13 |
| TC-020 | BR-020 | Verify HR salary sensitivity is documented. | Review security requirements. | Salary data restriction is documented for HR, Finance leadership, and approved executives. | Restriction was documented. | Pass | HR Data Steward | 2025-07-13 |
| TC-021 | BR-006 | v1.0 defect: Procurement approval date displayed as text in one dashboard prototype. | Load procurement CSV into Power BI prototype and inspect date type. | Approval date should be recognized as a date. | v1.0 imported field as text due to model setting. Fixed by explicitly setting Power BI data type in v1.1. | Fixed v1.1 | BI Developer | 2025-07-15 |
| TC-022 | BR-011 | v1.0 defect: Critical overdue count excluded open requests without completed date. | Compare manual filter to dashboard card. | Dashboard card should count critical open requests older than 48 hours. | v1.0 card counted only completed records. Fixed in v1.1 measure logic. | Fixed v1.1 | Facilities Manager | 2025-07-15 |
| TC-023 | BR-004 | v1.0 defect: Near-budget threshold label used 95% instead of approved 98% business rule. | Inspect budget exception tile for Student Affairs. | Student Affairs should display as near limit at 98% utilization. | v1.0 label threshold caused too many warning departments. Fixed in v1.1 by documenting warning and watch thresholds separately. | Fixed v1.1 | Budget Office | 2025-07-16 |
| TC-024 | BR-015 | Verify files can be regenerated consistently. | Delete dashboard CSVs, rerun generation and transformation scripts. | CSVs regenerate with stable business story metrics. | Files regenerated and validation passed. | Pass | QA Analyst | 2025-07-16 |

## Defect Summary

| Defect ID | Related TC | Severity | Description | Resolution |
|---|---|---|---|---|
| DEF-001 | TC-021 | Medium | Power BI prototype interpreted approval date as text. | Corrected dashboard model data type in v1.1. |
| DEF-002 | TC-022 | High | Critical overdue dashboard card excluded unresolved critical requests. | Updated measure logic in v1.1 to use snapshot aging for open work orders. |
| DEF-003 | TC-023 | Low | Near-budget threshold label was broader than approved business rule. | Clarified threshold definition and updated dashboard label in v1.1. |

## Sign-Off

| Role | Name | Decision | Date |
|---|---|---|---|
| Finance Product Owner | Finance & Business Information Services | Approved for portfolio release | 2025-07-17 |
| Procurement Representative | Procurement Services | Approved with v1.1 fixes | 2025-07-17 |
| Facilities Representative | Facilities Management | Approved with v1.1 fixes | 2025-07-17 |
| HR Representative | Human Resources | Approved | 2025-07-17 |
