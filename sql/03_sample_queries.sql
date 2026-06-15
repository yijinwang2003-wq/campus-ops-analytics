SET search_path TO higher_ed_analytics;

-- Budget utilization by department and fiscal year
SELECT
    d.department_name,
    b.fiscal_year,
    SUM(b.monthly_budget) AS total_budget,
    SUM(b.actual_spend) AS total_actual_spend,
    ROUND(SUM(b.actual_spend) / NULLIF(SUM(b.monthly_budget), 0) * 100, 2) AS budget_utilization_pct
FROM fact_budget b
JOIN dim_department d ON d.department_id = b.department_id
GROUP BY d.department_name, b.fiscal_year
ORDER BY b.fiscal_year, budget_utilization_pct DESC;

-- Procurement cycle time by department
SELECT
    d.department_name,
    COUNT(*) AS request_count,
    AVG(approval.calendar_date - request.calendar_date) AS avg_days_to_approve
FROM fact_procurement p
JOIN dim_department d ON d.department_id = p.department_id
JOIN dim_date request ON request.date_key = p.request_date_key
LEFT JOIN dim_date approval ON approval.date_key = p.approval_date_key
WHERE p.approval_date_key IS NOT NULL
GROUP BY d.department_name
ORDER BY avg_days_to_approve DESC;

-- Critical unresolved maintenance backlog
SELECT
    d.department_name,
    m.work_order_number,
    m.building_name,
    m.request_type,
    m.priority,
    request.calendar_date AS request_date,
    CURRENT_DATE - request.calendar_date AS days_open
FROM fact_maintenance m
JOIN dim_department d ON d.department_id = m.department_id
JOIN dim_date request ON request.date_key = m.request_date_key
WHERE m.priority = 'Critical'
  AND m.completed_date_key IS NULL
ORDER BY days_open DESC;
