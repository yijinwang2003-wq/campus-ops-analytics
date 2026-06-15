# Future-State Procurement Process Flow

## Purpose

This document describes a target procurement process supported by a unified analytics and decision support platform. The future state adds automated status tracking, approval notifications, cycle-time alerts, dashboard monitoring, and consistent reporting definitions.

## Swimlanes

Use the following swimlanes from top to bottom:

1. Department Requester
2. Department Manager
3. Procurement Workflow System
4. Procurement Services
5. Finance / Budget Office
6. Vendor
7. Accounts Payable
8. Analytics Platform / Dashboard

## Future-State Flow

| Step | Swimlane | Activity | Automation / Control | Reporting Output |
|---|---|---|---|---|
| 1 | Department Requester | Submits standardized procurement request. | Required fields for vendor, category, amount, justification, quote, and department. | New request appears in procurement dashboard. |
| 2 | Procurement Workflow System | Assigns request number and status of Submitted. | Automated timestamp and department ID validation. | Request lifecycle starts. |
| 3 | Procurement Workflow System | Routes request to Department Manager based on department and amount. | Approval notification sent automatically. | Pending manager approval count updates. |
| 4 | Department Manager | Approves, rejects, or requests clarification. | Decision captured in workflow history. | Approval status visible to requester and leadership. |
| 5 | Procurement Workflow System | Evaluates policy thresholds. | Determines manager, director, or cabinet approval level; flags competitive bid requirement. | Approval level available for cycle-time analysis. |
| 6 | Procurement Services | Reviews sourcing and documentation requirements. | Missing documentation checklist and queue prioritization. | Procurement workload dashboard updates. |
| 7 | Finance / Budget Office | Performs budget availability review using current budget data. | Budget utilization and commitments visible during review. | Finance review cycle time is measured. |
| 8 | Procurement Workflow System | Sends reminder if approval age exceeds service threshold. | Cycle-time alert triggered after 10 days. | `is_approval_delayed` flag is available for dashboard monitoring. |
| 9 | Procurement Services | Issues purchase order when policy and funding checks are complete. | PO date captured automatically. | Request moves to Approved / PO Issued. |
| 10 | Vendor | Fulfills order or service. | Vendor and category retained for spend analysis. | Vendor trend analysis supported. |
| 11 | Accounts Payable | Receives invoice and performs system-supported match. | PO, invoice, and approval record linked by request number. | Invoice exceptions can be monitored. |
| 12 | Department Requester | Confirms receipt when required. | Automated task notification. | Receiving delays become visible. |
| 13 | Accounts Payable | Processes payment after match completion. | Final status updates to Closed. | Complete procurement cycle time available. |
| 14 | Analytics Platform / Dashboard | Refreshes procurement, budget, and department datasets. | Scheduled ETL and validation checks. | Dashboards show approval delays, cycle time, spend, and budget impact. |
| 15 | Department Leadership | Reviews dashboard exceptions. | Filters by department, vendor, category, fiscal period, and approval level. | Actionable exception list replaces manual follow-up. |

## Draw.io Shape Guidance

- Start / End: rounded rectangles.
- Activities: rectangles.
- Decisions: diamonds for manager approval, policy threshold, budget availability, and invoice match.
- Automated steps: rectangles with blue fill.
- Alerts: yellow callouts for cycle-time reminders and budget threshold warnings.
- Data stores: cylinders for workflow system, ERP, and analytics warehouse.
- Dashboard outputs: screen shapes in the Analytics Platform lane.

## Future-State Controls

- Standardized request intake.
- Automated approval routing.
- Time-stamped status history.
- Budget validation during finance review.
- Cycle-time alerts for requests exceeding 10 approval days.
- Dashboard exception reporting for delayed approvals.
- Linked PO, invoice, and receiving documentation.
- Data validation checks before dashboard publication.

## Expected Benefits

- Improved requester and manager visibility into request status.
- Reduced manual email follow-up.
- Earlier identification of finance review bottlenecks.
- More consistent documentation for audit and compliance.
- Faster detection of over-budget departments and near-limit departments.
- More reliable procurement cycle-time reporting.

## Target-State Dashboard Metrics

- Average days to approve by department.
- Delayed approval count by approval level.
- Requests by status and category.
- Requests requiring competitive bid.
- Budget utilization at request approval.
- Vendor spend and request volume.
- Requests pending finance review.
- Closed requests and average days to complete.
