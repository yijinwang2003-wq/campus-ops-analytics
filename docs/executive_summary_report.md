# Executive Summary Report

## Higher Education Enterprise Analytics & Decision Support Platform

Prepared for: University Finance & Business Information Services  
Reporting Period: FY2024-FY2025 synthetic portfolio dataset  
Reporting Snapshot: June 30, 2025

## Executive Summary

University finance and operations leaders need a consolidated view of budget performance, procurement efficiency, facilities service risk, and workforce trends. In the current environment, these domains are reported through separate operational systems and manual spreadsheets, which limits the ability to identify cross-functional issues early.

This analytics platform demonstrates how a Finance & Business Information Services team can consolidate siloed data into a shared reporting layer. The project uses a PostgreSQL-compatible star schema, Python data generation and transformation scripts, automated validation checks, and Power BI-ready CSV outputs. The resulting datasets support executive dashboards, department manager reporting, and analyst-led process improvement.

The FY2025 synthetic dataset highlights four priority findings:

- Information Technology exceeded its FY2025 budget by approximately 7%, with 107.00% utilization and a negative variance of about $504,000.
- Student Affairs approached its budget limit at 98.00% utilization, leaving approximately $108,000 available.
- Information Technology procurement approvals averaged 14.24 days, materially higher than the 8.09-day university average.
- Facilities had four critical unresolved maintenance requests open for more than 48 hours as of the June 30, 2025 reporting snapshot.

These findings indicate that the university would benefit from earlier budget exception monitoring, procurement cycle-time alerts, clearer finance review visibility, and executive review of critical facilities backlog.

## Budget Performance Analysis

The FY2025 budget dataset shows a meaningful range of utilization across departments. Most departments remained within budget, but several were close enough to require active monitoring during the final quarter.

| Department | FY2025 Utilization | Variance |
|---|---:|---:|
| Information Technology | 107.00% | -$504,000 |
| Student Affairs | 98.00% | $108,000 |
| College of Engineering | 97.00% | $396,000 |
| Facilities Management | 96.00% | $344,000 |
| College of Liberal Arts | 95.00% | $575,000 |
| Finance & Accounting | 94.00% | $288,000 |
| Human Resources | 93.00% | $273,000 |
| Research Administration | 92.00% | $368,000 |

Information Technology is the only department exceeding budget in the FY2025 synthetic data. The overrun is concentrated in technology-related categories such as software, hardware, and cloud services. This pattern is realistic for higher education environments where infrastructure modernization, cybersecurity requirements, cloud migration, and software licensing renewals can accelerate faster than annual budget planning cycles.

Student Affairs did not exceed budget, but 98% utilization represents limited year-end flexibility. This department should be included in a watchlist because student programming, counseling services, and student support activities can experience seasonal demand late in the academic year.

### Budget Implications

- IT requires immediate variance explanation and a decision on whether recurring software and cloud costs should be rebased in the next budget cycle.
- Student Affairs should monitor commitments and discretionary spend closely in the final fiscal periods.
- Departments between 95% and 98% utilization should receive early-warning dashboard indicators to support proactive management.
- Finance leadership should review whether committed amounts are visible early enough to prevent late-cycle surprises.

## Procurement Efficiency Analysis

Procurement cycle time is a major operational theme in the dataset. Information Technology requests averaged 14.24 days to approval, compared with a university average of 8.09 days. This indicates that IT approvals take roughly 1.8 times the overall average.

| Department | Average Days to Approve |
|---|---:|
| Information Technology | 14.24 |
| College of Engineering | 6.82 |
| Finance & Accounting | 6.77 |
| College of Liberal Arts | 6.73 |
| Facilities Management | 6.73 |
| Student Affairs | 6.73 |
| Research Administration | 6.41 |
| Human Resources | 5.86 |

The IT cycle-time pattern is consistent with complex procurement categories: software, hardware, cloud services, cybersecurity tools, and professional services. These requests often require higher approval levels, contract review, competitive bid review, or additional finance scrutiny. However, without transparent status tracking, department leaders may not know whether delays are caused by missing documentation, procurement workload, finance review, or approval routing.

### Procurement Implications

- IT procurement should be monitored through a dedicated cycle-time exception view.
- Requests exceeding 10 approval days should trigger automated reminders or escalation.
- The workflow should distinguish manager approval, procurement review, finance review, and PO issuance status.
- Finance review turnaround time should be measured separately from procurement review time.
- Vendor, category, and approval-level analysis should be used to identify repeat bottlenecks.

## Facilities Operations Review

Facilities Management faces a different operational risk: critical work orders that remain unresolved beyond expected service thresholds. The synthetic dataset includes four critical unresolved requests open for more than 48 hours as of June 30, 2025.

Critical unresolved facilities work can affect safety, continuity of instruction, student experience, and regulatory compliance. Examples in the dataset include HVAC, life safety, electrical, and plumbing work orders across campus buildings. These are not simply maintenance metrics; they represent operational exposure that should be visible to both Facilities leadership and executive administration.

### Facilities Implications

- Critical open work orders should be reviewed daily.
- Requests older than 48 hours should appear in an executive exception list.
- Dashboard views should support filtering by building, assigned team, priority, status, and request type.
- Facilities should monitor whether unresolved critical requests are caused by staffing constraints, parts delays, vendor scheduling, or triage gaps.
- Long-term reporting should compare estimated cost, actual cost, completion time, and recurring building issues.

## HR / Workforce Trends

The HR dataset provides monthly headcount, FTE, salary expense, overtime, vacancy, and turnover measures by department. June 2025 headcount is highest in the academic units and Facilities Management:

| Department | June 2025 Headcount | June 2025 Salary Expense | Vacancies |
|---|---:|---:|---:|
| College of Liberal Arts | 167 | $1,194,710.70 | 1 |
| College of Engineering | 152 | $1,203,932.52 | 5 |
| Facilities Management | 111 | $647,033.26 | 4 |
| Information Technology | 76 | $499,622.94 | 3 |
| Student Affairs | 64 | $358,053.52 | 2 |
| Finance & Accounting | 38 | $225,511.87 | 3 |
| Research Administration | 38 | $226,025.15 | 4 |
| Human Resources | 34 | $198,170.51 | 3 |

Workforce data is important because budget pressure is often tied to staffing, vacancies, overtime, and compensation trends. For example, IT over-budget performance should be reviewed alongside staffing mix and salary trends to determine whether the pressure is driven by personnel, contracts, software, or infrastructure spending. Facilities backlog should also be interpreted with workforce capacity and overtime data.

### HR Implications

- Workforce reporting should be connected to financial and operational metrics.
- Vacancy reporting can help explain service delays or overtime pressure.
- HR salary data requires role-based access because of sensitivity.
- Department managers should see headcount and vacancy trends, while detailed salary data should be restricted to approved HR and Finance leadership roles.

## Recommendations & Next Steps

### 1. Implement Executive Exception Monitoring

Create a dashboard landing page focused on the most important exceptions:

- Departments over budget.
- Departments above budget watch thresholds.
- Procurement approvals older than 10 days.
- Critical maintenance requests open longer than 48 hours.
- Departments with rising vacancies or headcount changes.

### 2. Add Procurement Cycle-Time Alerts

The current IT approval cycle time of 14.24 days should trigger operational review. Add alerts for requests pending approval more than 10 days, and separate approval status into manager review, procurement review, finance review, and PO issuance.

### 3. Strengthen Budget Forecasting and Commitment Visibility

Budget dashboards should include actual spend and commitments. This helps Finance and department managers detect risk before expenses post. IT cloud and software spend should receive separate recurring-cost analysis before the next budget cycle.

### 4. Establish Facilities Critical Backlog Governance

Critical work orders older than 48 hours should be reviewed in a recurring operational meeting. Facilities should document reason codes for delay, such as parts availability, vendor scheduling, access constraints, or staffing capacity.

### 5. Define Role-Based Dashboard Access

The platform should support at least three reporting roles:

- Executive users: enterprise-wide summary and exception reporting.
- Finance users: cross-department financial detail and variance analysis.
- Department managers: department-specific budget, procurement, maintenance, and workforce views.

HR salary detail should be restricted to HR, Finance leadership, and approved executives.

### 6. Move from Static Reporting to Managed Analytics

The prototype demonstrates the value of a managed analytics layer. The next maturity step would be scheduling ETL jobs, loading data into PostgreSQL, connecting Power BI directly to curated tables or views, and adding production monitoring for refresh status and data quality checks.

## Conclusion

The Higher Education Enterprise Analytics & Decision Support Platform provides a realistic model for moving from siloed operational reporting to integrated decision support. The project demonstrates core Business Analyst and Data Analyst capabilities: requirements gathering, process analysis, data modeling, ETL development, data quality testing, dashboard dataset preparation, UAT planning, and executive communication.

The synthetic findings are realistic enough to support interview discussion and portfolio review. They show how integrated analytics can help a university identify over-budget departments, procurement bottlenecks, critical maintenance risk, and workforce trends in a single reporting environment.
