SET search_path TO higher_ed_analytics;

CREATE INDEX IF NOT EXISTS idx_fact_budget_department_fy ON fact_budget (department_id, fiscal_year);
CREATE INDEX IF NOT EXISTS idx_fact_budget_date_key ON fact_budget (date_key);
CREATE INDEX IF NOT EXISTS idx_fact_procurement_department ON fact_procurement (department_id);
CREATE INDEX IF NOT EXISTS idx_fact_procurement_request_date ON fact_procurement (request_date_key);
CREATE INDEX IF NOT EXISTS idx_fact_procurement_status ON fact_procurement (request_status);
CREATE INDEX IF NOT EXISTS idx_fact_maintenance_department ON fact_maintenance (department_id);
CREATE INDEX IF NOT EXISTS idx_fact_maintenance_priority_status ON fact_maintenance (priority, status);
CREATE INDEX IF NOT EXISTS idx_fact_hr_department_fy ON fact_hr (department_id, fiscal_year);
CREATE INDEX IF NOT EXISTS idx_dim_date_fiscal ON dim_date (fiscal_year, fiscal_month);
