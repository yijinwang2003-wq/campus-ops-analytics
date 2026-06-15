# Higher Education Enterprise Analytics & Decision Support Platform

A portfolio project simulating a university Finance & Business Information Services analytics initiative. The project integrates siloed Finance, Procurement, Facilities, and HR data into a shared analytics model with Python ETL, PostgreSQL-compatible SQL, dashboard-ready CSV outputs, data quality tests, business requirements, process analysis, UAT documentation, and an executive report.

## Project Status

**Complete portfolio build:** SQL data model, Python data pipeline, validation tests, Power BI-ready CSV outputs, business requirements, process flow documentation, UAT package, executive report, and polished README.

Latest validation:

```text
All data validations passed.
6 passed
```

## Business Problem

University department managers and finance leaders often rely on separate reports from finance systems, procurement workflows, HR systems, and facilities work order tools. This creates fragmented visibility into budget utilization, procurement delays, maintenance backlog, and workforce trends.

This project demonstrates how a Business Analyst / Data Analyst can define requirements, model data, build a repeatable transformation pipeline, validate data quality, and prepare executive-ready insights for a higher education administrative environment.

## Key Findings From the Synthetic Dataset

| Finding | Evidence |
|---|---|
| IT exceeded FY2025 budget | Information Technology reached 107.00% utilization, about $504,000 over budget. |
| Student Affairs was near budget limit | Student Affairs reached 98.00% utilization, leaving about $108,000 remaining. |
| IT procurement was delayed | IT approval cycle averaged 14.24 days versus an 8.09-day university average. |
| Critical facilities backlog existed | Four critical unresolved maintenance requests were open more than 48 hours. |
| Workforce reporting supports context | HR dataset includes monthly headcount, FTE, salary expense, overtime, vacancies, and turnover by department. |

## Deliverables

| Deliverable | Location | Purpose |
|---|---|---|
| PostgreSQL schema | `sql/01_schema.sql` | Defines star-schema warehouse tables for departments, dates, budget, procurement, maintenance, and HR. |
| Indexes | `sql/02_indexes.sql` | Adds common query indexes for dashboard and analyst workloads. |
| Sample SQL queries | `sql/03_sample_queries.sql` | Provides example budget, procurement, and maintenance analysis queries. |
| Data generator | `src/generate_data.py` | Creates realistic FY2024-FY2025 synthetic source data. |
| Data transformation | `src/transform_data.py` | Produces Power BI-ready CSV datasets with calculated fields. |
| Data validation | `src/validate_data.py` | Validates data quality and business story conditions. |
| Pytest suite | `tests/test_data_quality.py` | Automates regression checks for data quality and metrics. |
| Data architecture | `docs/data_architecture.md` | Mermaid ER diagram, relationship summary, table grain, and Draw.io-compatible diagram description. |
| System architecture | `docs/system_architecture.md` | Enterprise-style data flow from source systems through Python ETL, warehouse, Power BI, and executive reporting. |
| Power BI dashboard design | `docs/powerbi_dashboard_design.md` | Four-page dashboard specification with KPIs, charts, filters, insights, and layout sketches. |
| Business requirements | `docs/business_requirements.md` | Professional BRD with requirements and acceptance criteria. |
| Process flows | `docs/process_flow_current_state.md`, `docs/process_flow_future_state.md` | Swimlane-style procurement process descriptions for Draw.io recreation. |
| BPMN swimlane diagram | `docs/procurement_swimlane_bpmn.md`, `docs/procurement_swimlane_bpmn.drawio` | Professional procurement swimlane diagram with Mermaid, Draw.io XML, and PNG export specification. |
| UAT package | `docs/uat_test_plan.md` | 20+ UAT cases, including realistic v1.0 defects fixed in v1.1. |
| Executive report | `docs/executive_summary_report.md` | 5-7 page style leadership report summarizing findings and recommendations. |

## Documentation Package

- [Data Architecture](docs/data_architecture.md)
- [System Architecture](docs/system_architecture.md)
- [Power BI Dashboard Design](docs/powerbi_dashboard_design.md)
- [Business Requirements Document](docs/business_requirements.md)
- [Procurement Swimlane BPMN Diagram](docs/procurement_swimlane_bpmn.md)
- [Current-State Procurement Process Flow](docs/process_flow_current_state.md)
- [Future-State Procurement Process Flow](docs/process_flow_future_state.md)
- [UAT Test Plan](docs/uat_test_plan.md)
- [Executive Summary Report](docs/executive_summary_report.md)

## Repository Structure

```text
higher-ed-analytics-platform/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── powerbi/
├── sql/
│   ├── 01_schema.sql
│   ├── 02_indexes.sql
│   └── 03_sample_queries.sql
├── src/
│   ├── generate_data.py
│   ├── transform_data.py
│   └── validate_data.py
├── docs/
│   ├── business_requirements.md
│   ├── data_architecture.md
│   ├── powerbi_dashboard_design.md
│   ├── procurement_swimlane_bpmn.drawio
│   ├── procurement_swimlane_bpmn.md
│   ├── system_architecture.md
│   ├── process_flow_current_state.md
│   ├── process_flow_future_state.md
│   ├── uat_test_plan.md
│   └── executive_summary_report.md
├── screenshots/
└── tests/
    └── test_data_quality.py
```

## Data Model

The project uses a star-schema style data warehouse:

- `dim_department`
- `dim_date`
- `fact_budget`
- `fact_procurement`
- `fact_maintenance`
- `fact_hr`

The Power BI exports flatten and aggregate the raw data into analyst-friendly files:

- `budget_summary.csv`
- `budget_monthly_dashboard.csv`
- `procurement_dashboard.csv`
- `maintenance_dashboard.csv`
- `hr_workforce_dashboard.csv`
- `dim_department.csv`
- `dim_date.csv`

Generated source files are stored in `data/raw/`. Dashboard-ready outputs are stored in `data/powerbi/`.

## Data Architecture

The platform uses an enterprise analytics star schema with shared department and date dimensions connected to four business process fact tables: budget, procurement, maintenance, and HR. This supports consistent fiscal reporting, department-level security design, and cross-functional dashboard analysis.

See [docs/data_architecture.md](docs/data_architecture.md) for the full Mermaid ER diagram, primary and foreign keys, relationship summary, table grain, and Draw.io-compatible recreation instructions.

## System Architecture

The solution follows a layered enterprise analytics flow: source systems for Finance, Procurement, HR, and Facilities feed a Python ETL layer, which produces a governed star-schema data warehouse and Power BI-ready dashboard datasets. Executive reporting then converts dashboard outputs into budget risk, procurement bottleneck, facilities backlog, and workforce trend insights.

See [docs/system_architecture.md](docs/system_architecture.md) for the full Mermaid architecture diagram, Draw.io-compatible build instructions, layer definitions, and data control points.

## Dashboard Page Concepts

The recommended Power BI dashboard contains four pages:

- **Executive Overview:** enterprise summary of budget exceptions, procurement delays, critical facilities backlog, and workforce indicators.
- **Budget Analytics:** budget-to-actual analysis by department, fiscal year, fiscal period, and category.
- **Procurement Operations:** approval cycle-time monitoring by department, vendor, procurement category, approval level, and request status.
- **Facilities & Workforce:** integrated view of maintenance backlog, critical work orders, headcount, vacancies, and salary trends.

See [docs/powerbi_dashboard_design.md](docs/powerbi_dashboard_design.md) for KPI cards, charts, filters, business insights, and layout sketches for each page.

## Tech Stack

- Python
- Pandas
- NumPy
- Pytest
- PostgreSQL-compatible SQL
- CSV outputs for Power BI
- Markdown documentation

## How to Run

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Generate raw synthetic data:

```bash
python src/generate_data.py
```

Create Power BI-ready datasets:

```bash
python src/transform_data.py
```

Run validation checks:

```bash
python src/validate_data.py
```

Run tests:

```bash
pytest -q
```

Expected validation result:

```text
All data validations passed.
6 passed
```

To inspect the main synthetic business findings after running the pipeline, open:

- `data/powerbi/budget_summary.csv`
- `data/powerbi/procurement_dashboard.csv`
- `data/powerbi/maintenance_dashboard.csv`
- `data/powerbi/hr_workforce_dashboard.csv`

## Calculated Fields

| Field | Definition |
|---|---|
| `budget_utilization_pct` | Actual spend divided by approved budget. |
| `budget_variance` | Approved budget minus actual spend. |
| `budget_variance_pct` | Budget variance divided by approved budget. |
| `days_to_approve` | Approval date minus request date. |
| `days_to_complete` | Invoice date minus request date. |
| `days_to_resolve` | Completed date or snapshot date minus maintenance request date. |
| `is_over_budget` | True when actual spend exceeds approved budget. |
| `is_approval_delayed` | True when procurement approval exceeds 10 days. |
| `is_critical_over_48h` | True when a critical unresolved maintenance request is open more than two days. |

## Business Analyst Framing

This project is designed to demonstrate end-to-end analyst work, not just technical scripting:

- Translated a university administrative problem into business requirements and acceptance criteria.
- Modeled cross-functional reporting needs across Finance, Procurement, Facilities, and HR.
- Designed current-state and future-state procurement workflows using swimlane-ready process documentation.
- Built repeatable ETL scripts and dashboard-ready outputs.
- Created validation checks to prove key metrics and protect against regression.
- Developed UAT test cases with realistic defects and v1.1 remediation.
- Produced an executive report with findings, implications, and recommendations.

## Completed Scope

- Repository structure
- SQL schema and sample queries
- Synthetic data generation
- Power BI-ready transformations
- Data validation and tests
- Business requirements
- Procurement process flows
- UAT test package
- Executive summary report
- Polished portfolio README
