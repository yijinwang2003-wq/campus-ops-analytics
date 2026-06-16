# Project Story

## Higher Education Enterprise Analytics & Decision Support Platform

This document explains the project background, scope, stakeholder context, solution design, and analytical findings for the Higher Education Enterprise Analytics & Decision Support Platform.

## 1. Business Problem

The project addresses a common administrative challenge in higher education: university leaders need integrated visibility across Finance, Procurement, Facilities, and Human Resources, but those functions often report through separate systems and manual processes.

In the simulated university environment, department managers and finance leadership lacked a single source of truth for:

- Budget utilization and budget-to-actual variance.
- Procurement approval cycle time and delayed requests.
- Critical maintenance backlog and work order aging.
- Workforce capacity, salary expense, vacancies, and headcount trends.

Without integrated reporting, leaders may identify budget risk too late, miss procurement bottlenecks, or review facilities service issues without understanding staffing context. The goal of this project was to simulate that business problem and build a practical analytics solution that supports better decision-making.

## 2. Why Universities Have Data Silos

Universities often develop data silos because each administrative function has its own system, workflow, ownership model, and reporting cadence.

Finance teams usually work in ERP or budgeting systems. Procurement teams manage request, approval, vendor, purchase order, and invoice workflows. Facilities teams operate work order systems organized around buildings, priorities, and maintenance teams. HR teams manage sensitive workforce and compensation data in HRIS systems.

These systems are optimized for operational processing, not enterprise analytics. As a result:

- Departments use different definitions for similar reporting concepts.
- Finance reports may not include procurement cycle time or facilities backlog.
- Procurement status may be visible only inside procurement tools or email threads.
- HR salary and staffing data requires access controls.
- Executives often receive manually prepared summaries instead of live exception reporting.

This project treats those silos as the core business analysis problem and demonstrates how a shared analytics layer can connect the data without replacing the source systems.

## 3. Solution Architecture

The solution follows a simple enterprise analytics architecture:

```text
Source Systems
Finance / Procurement / HR / Facilities
        ↓
Python ETL
        ↓
Star Schema Data Warehouse
        ↓
Power BI Dashboard Outputs
        ↓
Executive Reporting
```

The architecture separates operational systems from reporting. Synthetic source data is generated to represent the separate systems, transformed into dashboard-ready outputs, and documented as an enterprise reporting model.

Key design decisions:

- Use `dim_department` as a conformed dimension across all subject areas.
- Use `dim_date` as the fiscal and calendar reporting dimension.
- Keep fact tables aligned to business processes: budget, procurement, maintenance, and HR.
- Produce CSV outputs that can be used in Power BI Service for dashboard development and review.
- Add validation checks so the project demonstrates data quality discipline, not just visualization.

## 4. Data Engineering Pipeline

The data pipeline is built in Python with Pandas and includes three main scripts:

| Script | Purpose |
|---|---|
| `src/generate_data.py` | Generates realistic synthetic FY2024 and FY2025 data for departments, dates, budget, procurement, maintenance, and HR. |
| `src/transform_data.py` | Cleans and transforms raw data into Power BI-ready CSV files with calculated fields. |
| `src/validate_data.py` | Validates data quality, calculations, and expected business story conditions. |

The generated raw data is stored in `data/raw/`. Dashboard-ready outputs are stored in `data/powerbi/`.

The pipeline creates important calculated fields such as:

- `budget_utilization_pct`
- `budget_variance`
- `budget_variance_pct`
- `days_to_approve`
- `days_to_complete`
- `days_to_resolve`
- `is_over_budget`
- `is_approval_delayed`
- `is_critical_over_48h`

Automated tests validate that department IDs are complete, dates are valid, budget calculations are correct, IT is over budget in FY2025, IT procurement approval time exceeds the university average, and critical overdue maintenance requests exist.

## 5. Dashboard Design Process

The dashboard design was built around business questions rather than visuals first.

The four dashboard pages are:

1. **Executive Overview**
   - Designed for senior leaders who need quick exception monitoring.
   - Combines budget risk, procurement delays, facilities backlog, and workforce indicators.

2. **Budget Analytics**
   - Designed for Finance and budget analysts.
   - Focuses on budget-to-actual performance, variance, utilization, and category-level spend.

3. **Procurement Operations**
   - Designed for Procurement Services and Finance reviewers.
   - Focuses on approval cycle time, delayed requests, vendor/category analysis, and process bottlenecks.

4. **Facilities & Workforce**
   - Designed for Facilities, HR, Finance, and executive stakeholders.
   - Connects work order backlog and critical maintenance risk with staffing and vacancy context.

The design process included:

- Defining the audience for each page.
- Selecting KPIs tied to business decisions.
- Prioritizing exception-based reporting.
- Using department and fiscal year as common slicers.
- Creating high-fidelity static dashboard mockups for stakeholder review.

## 6. Key Insights Found

The synthetic dataset was intentionally designed to include realistic university business findings. These findings give the dashboard and documentation a clear analytical story.

### Budget Findings

Information Technology exceeded its FY2025 budget, reaching **107.00% utilization**. This represents an unfavorable variance of approximately **$504,000**.

Student Affairs was not over budget, but it reached **98.00% utilization**, leaving limited remaining budget flexibility.

Five departments reached at least 95% utilization, which indicates a need for watchlist reporting and proactive fiscal review.

### Procurement Findings

Information Technology procurement approvals averaged **14.24 days**, compared with a university average of **8.09 days**.

This suggests IT procurement is a process bottleneck, likely due to more complex purchases such as software, hardware, cloud services, cybersecurity tools, or professional services.

The generated data also includes **43 delayed approvals**, giving Procurement and Finance a clear population of requests to review.

### Facilities Findings

The Facilities dataset includes **four critical unresolved maintenance requests older than 48 hours**.

This is an operational risk because critical work orders can affect safety, continuity of instruction, student experience, and regulatory compliance.

### Workforce Findings

The latest generated HR data shows **680 total headcount** and **25 vacancies** across the university.

Facilities Management has **111 headcount** and **4 vacancies**, which provides useful context when reviewing facilities backlog and service response capacity.

## 7. Business Recommendations

Based on the analysis, the recommended actions are:

### 1. Create a Budget Exception Review Process

Finance should review over-budget and near-threshold departments on a recurring basis. IT should receive immediate variance review because it exceeded budget by approximately 7%. Student Affairs should remain on a watchlist due to 98% utilization.

### 2. Add Procurement Cycle-Time Monitoring

Procurement should monitor average days to approve by department, category, approval level, and finance reviewer. Requests exceeding the delay threshold should be escalated or reviewed for missing documentation, policy complexity, or workload issues.

### 3. Review IT Procurement Workflow

IT approval time is materially above the university average. The university should review whether IT requests require clearer intake templates, earlier finance review, pre-approved vendor agreements, or better routing for software and cloud purchases.

### 4. Establish Critical Facilities Backlog Governance

Critical work orders older than 48 hours should appear in an executive exception list. Facilities should document reason codes for delay, such as parts availability, staffing constraints, vendor scheduling, or building access issues.

### 5. Connect Workforce Metrics to Operational Reviews

Vacancies, headcount, and overtime should be reviewed alongside facilities backlog and service delays. This helps leadership determine whether performance issues are process-related, staffing-related, or budget-related.

### 6. Standardize KPI Definitions

Finance & Business Information Services should maintain shared definitions for budget utilization, variance, delayed approvals, critical backlog, and workforce metrics. This reduces confusion and improves trust in reporting.

## 8. Future Enhancements

The current project is a prototype, but it could be extended into a more mature enterprise analytics solution.

Potential enhancements include:

- Load the data into PostgreSQL and connect Power BI directly to database views.
- Add scheduled refresh and automated data quality alerts.
- Build a formal Power BI semantic model with role-playing date dimensions.
- Add row-level security for department managers.
- Create drill-through pages for department, vendor, building, and employee group analysis.
- Add forecasting for budget utilization and maintenance backlog.
- Add procurement process mining to identify bottlenecks by workflow stage.
- Add more detailed HR dimensions such as employee group, job family, and funding source.
- Create real Draw.io exports and dashboard screenshots for final stakeholder presentation.

## Project Summary

The project demonstrates business analysis, data modeling, process analysis, data quality validation, dashboard design, and executive communication in one end-to-end analytics initiative.
