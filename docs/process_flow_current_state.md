# Current-State Procurement Process Flow

## Purpose

This document describes the current procurement process in a swimlane-style format that can be recreated in Draw.io. The current state reflects a fragmented university purchasing workflow with limited status visibility, manual email approvals, finance review bottlenecks, and manual invoice matching.

## Swimlanes

Use the following swimlanes from top to bottom:

1. Department Requester
2. Department Manager
3. Procurement Services
4. Finance / Budget Office
5. Vendor
6. Accounts Payable
7. Department Leadership

## Current-State Flow

| Step | Swimlane | Activity | System / Artifact | Pain Point |
|---|---|---|---|---|
| 1 | Department Requester | Identifies need for goods or services. | Email, spreadsheet, local notes | No standard intake form across departments. |
| 2 | Department Requester | Checks available budget using local spreadsheet or prior monthly report. | Department budget spreadsheet | Budget data may be stale and not reconciled to Finance. |
| 3 | Department Requester | Emails purchase request details to Department Manager. | Email | Request status is not visible after submission. |
| 4 | Department Manager | Reviews business justification and estimated cost. | Email thread | Approval history is embedded in email and difficult to audit. |
| 5 | Department Manager | Sends approval or clarification request by email. | Email | Rework loops are not tracked. |
| 6 | Department Requester | Forwards approved request to Procurement Services. | Email attachment | Attachments may omit quote, vendor, or funding details. |
| 7 | Procurement Services | Reviews request for completeness and purchasing policy. | Procurement queue, email | Queue prioritization is manual. |
| 8 | Procurement Services | Requests missing information from requester when required. | Email | Cycle time increases without automated reminders. |
| 9 | Procurement Services | Determines whether competitive bid or contract review is required. | Policy manual | Decision logic is not visible to requester. |
| 10 | Finance / Budget Office | Performs budget availability review. | ERP inquiry, spreadsheet | Finance review becomes a bottleneck during high-volume periods. |
| 11 | Finance / Budget Office | Confirms funding or asks department for alternate chart string. | Email | No centralized status field shows pending finance review. |
| 12 | Procurement Services | Issues purchase order when policy and funding checks are complete. | Procurement system | Department receives updates only if manually notified. |
| 13 | Vendor | Fulfills order or provides service. | Vendor invoice / delivery record | Delivery information is not consistently tied to original request. |
| 14 | Accounts Payable | Receives invoice. | AP inbox | Invoice may arrive before PO details are fully matched. |
| 15 | Accounts Payable | Manually matches invoice to PO and department approval. | ERP, email, attachments | Manual invoice matching creates delays and rework. |
| 16 | Department Requester | Confirms goods or services were received when asked. | Email | Receiving confirmation is reactive and inconsistently documented. |
| 17 | Accounts Payable | Processes payment after match is complete. | ERP | Payment status is not visible to department managers. |
| 18 | Department Leadership | Reviews monthly budget reports after spend posts. | Static report | Overspend risk is discovered late in the month or quarter. |

## Draw.io Shape Guidance

- Start / End: rounded rectangles.
- Activities: rectangles.
- Decisions: diamonds for completeness check, bid requirement, and budget availability.
- Documents: folded-corner document shapes for quote, PO, invoice, and budget spreadsheet.
- Data stores: cylinder shapes for ERP, procurement system, and local spreadsheets.
- Pain points: red callouts attached to steps 3, 10, 15, and 18.

## Current-State Pain Points

- **No status visibility:** Requesters and department managers rely on email follow-up to determine whether a request is pending manager approval, procurement review, finance review, PO creation, vendor fulfillment, or AP matching.
- **Manual email approval:** Approval evidence is distributed across email threads, creating audit and rework risk.
- **Finance review bottleneck:** Budget checks are performed outside a shared workflow queue, increasing cycle time for high-value or incomplete requests.
- **Manual invoice matching:** AP staff manually reconcile invoices, purchase orders, receiving confirmations, and email approvals.
- **Delayed variance detection:** Spend becomes visible to leadership after posting, limiting early intervention when departments approach budget thresholds.

## Metrics Impacted

- Average days to approve.
- Count of delayed approvals.
- Requests pending finance review.
- Invoice match exception count.
- Department budget utilization.
- Number of requests with missing documentation.
