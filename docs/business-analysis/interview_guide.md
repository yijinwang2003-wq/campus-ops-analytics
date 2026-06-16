# Interview Guide

## Higher Education Enterprise Analytics & Decision Support Platform

Target role: University Business Analyst, Business Systems Analyst, Reporting Analyst, Institutional Analytics  
Note: This file is intended for local interview preparation and should not be pushed to GitHub.

## 1. 30-Second Project Summary

I built a higher education enterprise analytics platform that simulates a university Finance & Business Information Services initiative. The project starts with a realistic business problem: Finance, Procurement, Facilities, and HR reporting are siloed, so leadership lacks a single view of budget risk, procurement delays, critical maintenance backlog, and workforce trends.

I created synthetic data, designed a star-schema data model, built a Python ETL and validation pipeline, generated Power BI-ready datasets, produced dashboard mockups, and documented the project with a BRD, current/future state analysis, UAT package, data model, and solution architecture.

## 2. 2-Minute Project Walkthrough

The project represents a university administrative analytics initiative for Finance & Business Information Services.

The business problem is that university leaders often receive separate reports from Finance, Procurement, Facilities, and HR. Finance can see budget-to-actual performance, Procurement can see request approvals, Facilities can see work order backlog, and HR can see staffing trends, but there is no integrated decision-support view.

To solve this, I designed a reporting architecture with four layers:

1. Source systems for Finance, Procurement, Facilities, and HR.
2. A Python ETL pipeline to generate, transform, and validate data.
3. An analytics data layer with conformed department and date dimensions.
4. A Power BI dashboard suite for executive and operational reporting.

The data model uses a star schema with `dim_department` and `dim_date` connected to fact tables for budget, procurement, maintenance, and workforce reporting. This lets users filter across different business areas by the same department and fiscal period.

The dashboard suite includes Executive Overview, Budget Analytics, Procurement Operations, and Facilities & Workforce pages. The generated findings include IT exceeding FY2025 budget at 107% utilization, Student Affairs near budget limit at 98%, IT procurement approvals averaging 14.24 days compared with an 8.09-day university average, and four critical maintenance requests unresolved for more than 48 hours.

The project demonstrates Business Analyst skills because it includes business requirements, stakeholder analysis, process documentation, data modeling, dashboard specifications, UAT, and executive reporting.

## 3. Business Problem Explanation

The core business problem is fragmented administrative reporting.

Finance, Procurement, Facilities, and HR each have their own systems, data definitions, and reporting processes. This makes it difficult for executives and department managers to answer cross-functional questions such as:

- Which departments are close to or over budget?
- Are procurement delays contributing to budget or operational issues?
- Are critical facilities requests being resolved quickly enough?
- Are vacancies or staffing constraints affecting service delivery?

Without an integrated analytics layer, leadership decisions are delayed, manual reporting effort increases, and performance issues are reviewed in isolation.

## 4. Why Universities Have Data Silos

Universities often have data silos because each administrative function uses specialized systems.

Finance teams use ERP and budgeting tools. Procurement teams manage requests, vendors, approvals, purchase orders, and invoices. Facilities teams use work order systems organized around buildings, priorities, and service teams. HR teams manage sensitive workforce and compensation data in HRIS systems.

These systems are optimized for operational transactions, not enterprise analytics. They also have separate data owners, security requirements, business definitions, and reporting calendars. The result is that a university may have plenty of data but limited integrated insight.

## 5. Why Star Schema Was Selected

I selected a star schema because it is well suited for enterprise reporting and Power BI dashboard development.

The project has clear dimensions and facts:

- `dim_department` provides organizational context.
- `dim_date` provides calendar and fiscal reporting context.
- Fact tables store measurable events and periodic snapshots for budget, procurement, maintenance, and HR.

The star schema allows each business process to keep its own grain while sharing common filters. For example, budget data is monthly or annual, procurement data is request-level, maintenance data is work-order-level, and HR data is monthly by department. A star schema lets these different facts coexist without forcing direct fact-to-fact joins.

This design also improves dashboard performance, makes relationships easier to explain, and supports consistent slicers by department and fiscal period.

## 6. Why Power BI Was Selected

Power BI was selected because it is commonly used for enterprise reporting, especially in Finance and administrative analytics teams.

It fits the project for several reasons:

- It supports dashboard-ready CSV files.
- It works well with star-schema semantic models.
- It provides slicers, KPI cards, matrix visuals, line charts, bar charts, and conditional formatting.
- It is familiar to Finance, Budget Office, Procurement, Facilities, HR, and executive users.
- Power BI Service can be used from a Mac, which makes it practical for a portfolio workflow.

For this project, I created Power BI-ready datasets and high-fidelity static dashboard mockups to show how the report would look and function.

## 7. Why Synthetic Data Was Used

Synthetic data was used because real university Finance, Procurement, Facilities, and HR data is sensitive and not appropriate for a public portfolio project.

The goal was to create realistic data without exposing confidential information. The synthetic data was intentionally designed to include business stories that an analyst could investigate:

- IT budget overrun.
- Student Affairs near budget limit.
- IT procurement approval delays.
- Critical maintenance backlog.
- Workforce headcount and vacancy trends.

This approach shows that I understand the business context while maintaining privacy and ethical data handling.

## 8. Most Important Business Findings

| Finding | Business Interpretation |
|---|---|
| IT reached 107% FY2025 budget utilization | IT requires Finance review, variance explanation, and possible budget rebasing. |
| Student Affairs reached 98% utilization | Student Affairs should be monitored as a near-limit department. |
| IT procurement approvals averaged 14.24 days | IT procurement is a bottleneck compared with the 8.09-day university average. |
| 43 procurement approvals were delayed | Procurement and Finance should review workflow routing, approval levels, and documentation quality. |
| Four critical maintenance requests were unresolved for more than 48 hours | Facilities backlog should be escalated as an operational risk. |
| Latest workforce data shows 680 headcount and 25 vacancies | Workforce metrics provide context for service capacity and operating pressure. |

## 9. Expected Business Analyst Interview Questions

1. What business problem were you solving?
2. Who were the stakeholders?
3. How did you gather or define requirements?
4. Why did you use a star schema?
5. How did you decide which dashboards to build?
6. What KPIs did you define?
7. How did you validate the data?
8. What would you do differently in a real implementation?
9. How does this project demonstrate Business Analyst skills?
10. How would you handle stakeholder disagreement about metric definitions?
11. How would you manage sensitive HR salary data?
12. How would you prioritize future enhancements?

## 10. Sample Answers

### Question: What business problem were you solving?

I was solving the problem of siloed administrative reporting in a university environment. Finance, Procurement, Facilities, and HR each had separate data views, but leadership needed an integrated view of budget utilization, procurement cycle time, critical maintenance backlog, and workforce trends. The project creates a unified analytics layer to support executive decision-making and department-level accountability.

### Question: Who were the stakeholders?

The main stakeholders were the CFO and Finance leadership, the Budget Office, Procurement Office, Facilities Management, Human Resources, Business Information Services, department managers, and executive leadership. Each group had different needs: Finance wanted budget and variance reporting, Procurement wanted cycle-time visibility, Facilities wanted backlog monitoring, HR wanted workforce trends, and executives wanted exception-based reporting.

### Question: How did you define requirements?

I started with the business problem and stakeholder needs, then translated them into functional requirements, reporting requirements, dashboard requirements, KPI definitions, and acceptance criteria. I documented these in a final BRD and connected them to specific datasets, calculations, and UAT scenarios.

### Question: Why did you use a star schema?

I used a star schema because the reporting domains share department and date context but have different grains. Budget data can be annual or monthly, procurement data is request-level, maintenance data is work-order-level, and HR data is monthly workforce data. A star schema lets each fact table keep its correct grain while using shared department and date dimensions for filtering.

### Question: How did you validate the data?

I created a validation script and pytest tests. The checks confirm no missing department IDs, valid dates, correct budget utilization calculations, IT over-budget behavior, IT procurement approval delays above the university average, and critical overdue maintenance records. This shows that the dashboard data is not just generated but tested against business expectations.

### Question: What would you do differently in a real implementation?

In a real implementation, I would connect to actual ERP, procurement, HRIS, and facilities systems; define data owners and refresh schedules; implement row-level security; create a formal Power BI semantic model; add role-playing date dimensions; and set up automated data quality alerts. I would also run stakeholder workshops to confirm KPI definitions and dashboard layouts.

### Question: How does this project demonstrate Business Analyst skills?

It demonstrates the full BA lifecycle: identifying a business problem, documenting stakeholders, defining requirements, analyzing current and future state processes, creating data and dashboard specifications, validating outputs through UAT, and presenting executive findings and recommendations. It also shows that I can work across business and technical teams.

### Question: How would you handle disagreement about KPI definitions?

I would facilitate a working session with the relevant stakeholders, document each proposed definition, identify the decision owner, and agree on a standard definition for enterprise reporting. If different definitions are needed for different contexts, I would label them clearly and document when each should be used.

### Question: How would you manage sensitive HR salary data?

I would treat salary data as restricted. In Power BI, I would use role-based access and row-level security where appropriate. I would also separate summary workforce metrics from sensitive compensation details and make sure access is approved by HR and Finance leadership.

## 11. Resume Talking Points

- Built a higher education enterprise analytics platform simulating Finance, Procurement, Facilities, and HR reporting for a university Finance & Business Information Services team.
- Created a consulting-style Business Analyst documentation package including BRD, current-state and future-state process analysis, UAT package, solution architecture, data model design, dashboard specifications, and executive report.
- Designed a star-schema reporting model with conformed department and date dimensions supporting budget, procurement, facilities, and workforce analytics.
- Developed a Python ETL pipeline using Pandas to generate realistic synthetic data, transform it into Power BI-ready outputs, and validate business rules and KPI calculations.
- Produced dashboard mockups showing executive budget risk, IT procurement bottlenecks, critical facilities backlog, and workforce vacancy trends.
- Demonstrated ability to connect business requirements, data modeling, analytics engineering, dashboard design, testing, and executive communication in one end-to-end project.
