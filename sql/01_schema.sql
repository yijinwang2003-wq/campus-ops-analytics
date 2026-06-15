/*
Higher Education Enterprise Analytics & Decision Support Platform
PostgreSQL-compatible star schema for integrated Finance, Procurement,
Facilities, and HR analytics.
*/

CREATE SCHEMA IF NOT EXISTS higher_ed_analytics;

SET search_path TO higher_ed_analytics;

CREATE TABLE dim_department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    division VARCHAR(100) NOT NULL,
    department_type VARCHAR(50) NOT NULL,
    vp_owner VARCHAR(100) NOT NULL,
    is_academic BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE dim_department IS 'Conformed department dimension used across Finance, Procurement, Facilities, and HR facts.';
COMMENT ON COLUMN dim_department.department_id IS 'Stable department surrogate key used by all fact tables.';
COMMENT ON COLUMN dim_department.division IS 'Executive division or cabinet-level reporting group.';

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    calendar_date DATE NOT NULL UNIQUE,
    calendar_year INTEGER NOT NULL,
    calendar_quarter INTEGER NOT NULL CHECK (calendar_quarter BETWEEN 1 AND 4),
    calendar_month INTEGER NOT NULL CHECK (calendar_month BETWEEN 1 AND 12),
    month_name VARCHAR(20) NOT NULL,
    fiscal_year INTEGER NOT NULL,
    fiscal_quarter INTEGER NOT NULL CHECK (fiscal_quarter BETWEEN 1 AND 4),
    fiscal_month INTEGER NOT NULL CHECK (fiscal_month BETWEEN 1 AND 12),
    month_start_date DATE NOT NULL,
    month_end_date DATE NOT NULL,
    is_month_end BOOLEAN NOT NULL DEFAULT FALSE
);

COMMENT ON TABLE dim_date IS 'Date dimension covering fiscal years used for dashboard filtering and trend analysis.';
COMMENT ON COLUMN dim_date.date_key IS 'Integer date key in YYYYMMDD format.';
COMMENT ON COLUMN dim_date.fiscal_year IS 'University fiscal year ending June 30.';

CREATE TABLE fact_budget (
    budget_fact_id BIGSERIAL PRIMARY KEY,
    department_id INTEGER NOT NULL REFERENCES dim_department(department_id),
    date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
    fiscal_year INTEGER NOT NULL,
    fiscal_period INTEGER NOT NULL CHECK (fiscal_period BETWEEN 1 AND 12),
    budget_category VARCHAR(75) NOT NULL,
    monthly_budget NUMERIC(14, 2) NOT NULL CHECK (monthly_budget >= 0),
    actual_spend NUMERIC(14, 2) NOT NULL CHECK (actual_spend >= 0),
    committed_amount NUMERIC(14, 2) NOT NULL DEFAULT 0 CHECK (committed_amount >= 0),
    funding_source VARCHAR(75) NOT NULL,
    last_updated_date DATE NOT NULL,
    CONSTRAINT uq_fact_budget_dept_period_category UNIQUE (department_id, fiscal_year, fiscal_period, budget_category)
);

COMMENT ON TABLE fact_budget IS 'Monthly department budget, actual spend, and commitments by category.';
COMMENT ON COLUMN fact_budget.monthly_budget IS 'Approved monthly budget for the department/category/period.';
COMMENT ON COLUMN fact_budget.actual_spend IS 'Recognized actual expense for the department/category/period.';

CREATE TABLE fact_procurement (
    procurement_id BIGSERIAL PRIMARY KEY,
    request_number VARCHAR(30) NOT NULL UNIQUE,
    department_id INTEGER NOT NULL REFERENCES dim_department(department_id),
    request_date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
    approval_date_key INTEGER REFERENCES dim_date(date_key),
    po_date_key INTEGER REFERENCES dim_date(date_key),
    invoice_date_key INTEGER REFERENCES dim_date(date_key),
    vendor_name VARCHAR(150) NOT NULL,
    procurement_category VARCHAR(75) NOT NULL,
    request_amount NUMERIC(14, 2) NOT NULL CHECK (request_amount > 0),
    approved_amount NUMERIC(14, 2) CHECK (approved_amount >= 0),
    request_status VARCHAR(40) NOT NULL,
    approval_level VARCHAR(50) NOT NULL,
    finance_reviewer VARCHAR(100),
    is_competitive_bid BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE fact_procurement IS 'Procurement request lifecycle from requisition through approval and invoice.';
COMMENT ON COLUMN fact_procurement.request_status IS 'Lifecycle status such as Approved, In Review, Rejected, or Closed.';
COMMENT ON COLUMN fact_procurement.approval_level IS 'Approval routing level determined by request amount and policy.';

CREATE TABLE fact_maintenance (
    maintenance_id BIGSERIAL PRIMARY KEY,
    work_order_number VARCHAR(30) NOT NULL UNIQUE,
    department_id INTEGER NOT NULL REFERENCES dim_department(department_id),
    request_date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
    completed_date_key INTEGER REFERENCES dim_date(date_key),
    building_name VARCHAR(100) NOT NULL,
    request_type VARCHAR(75) NOT NULL,
    priority VARCHAR(25) NOT NULL CHECK (priority IN ('Low', 'Medium', 'High', 'Critical')),
    status VARCHAR(40) NOT NULL,
    estimated_cost NUMERIC(12, 2) NOT NULL CHECK (estimated_cost >= 0),
    actual_cost NUMERIC(12, 2) CHECK (actual_cost >= 0),
    assigned_team VARCHAR(75) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE fact_maintenance IS 'Facilities work order fact table for maintenance backlog, cost, and response analysis.';
COMMENT ON COLUMN fact_maintenance.priority IS 'Operational priority assigned during triage.';
COMMENT ON COLUMN fact_maintenance.completed_date_key IS 'Null when request is unresolved or still active.';

CREATE TABLE fact_hr (
    hr_fact_id BIGSERIAL PRIMARY KEY,
    department_id INTEGER NOT NULL REFERENCES dim_department(department_id),
    date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
    fiscal_year INTEGER NOT NULL,
    fiscal_period INTEGER NOT NULL CHECK (fiscal_period BETWEEN 1 AND 12),
    employee_group VARCHAR(50) NOT NULL,
    headcount INTEGER NOT NULL CHECK (headcount >= 0),
    fte NUMERIC(8, 2) NOT NULL CHECK (fte >= 0),
    total_salary_expense NUMERIC(14, 2) NOT NULL CHECK (total_salary_expense >= 0),
    overtime_expense NUMERIC(12, 2) NOT NULL DEFAULT 0 CHECK (overtime_expense >= 0),
    vacancies INTEGER NOT NULL DEFAULT 0 CHECK (vacancies >= 0),
    turnover_count INTEGER NOT NULL DEFAULT 0 CHECK (turnover_count >= 0),
    CONSTRAINT uq_fact_hr_dept_period_group UNIQUE (department_id, fiscal_year, fiscal_period, employee_group)
);

COMMENT ON TABLE fact_hr IS 'Monthly workforce measures by department and employee group.';
COMMENT ON COLUMN fact_hr.fte IS 'Full-time equivalent staffing level for the month.';
COMMENT ON COLUMN fact_hr.total_salary_expense IS 'Monthly salary expense for the employee group.';
