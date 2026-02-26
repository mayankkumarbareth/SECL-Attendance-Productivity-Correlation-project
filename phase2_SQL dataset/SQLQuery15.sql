-- ============================================================
-- PHASE 3: Shift Manpower Summary
-- ============================================================
-- This view aggregates attendance and work hours by date, area, and shift


CREATE OR ALTER VIEW shift_manpower_summary AS
SELECT
    a.date,
    e.area,
    a.shift,

    COUNT(*) AS total_assigned,

    SUM(CASE WHEN a.attendance_status = 'Present' THEN 1 ELSE 0 END) AS total_present,

    SUM(CASE WHEN a.attendance_status = 'Absent' THEN 1 ELSE 0 END) AS total_absent,

    SUM(CASE 
        WHEN a.attendance_status = 'Present' 
         AND e.role_category = 'Critical'
        THEN 1 ELSE 0 
    END) AS critical_present,

    SUM(TRY_CAST(a.work_hours AS FLOAT)) AS total_work_hours,

    SUM(TRY_CAST(a.overtime_hours AS FLOAT)) AS total_overtime_hours
   

FROM biometric_attendance a
JOIN employee_master e
    ON a.employee_id = e.employee_id
GROUP BY
    a.date,
    e.area,
    a.shift;
GO

PRINT 'shift_manpower_summary view created successfully';
GO

-- ============================================================
-- PHASE 4: Final Productivity Dataset
-- ============================================================
-- This view combines production data with manpower metrics


CREATE OR ALTER VIEW final_productivity_dataset AS
SELECT
    p.date,
    p.area,
    p.shift,

    -- Manpower metrics from shift_manpower_summary
    m.total_assigned,
    m.total_present,
    m.total_absent,
    m.critical_present,
    m.total_work_hours,
    m.total_overtime_hours, 

    -- Production metrics from production_financial_summary
    p.coal_production_tonnes,
    p.target_production,
    p.total_cost_inr,
    p.revenue_inr,

    -- Calculated field
    (p.revenue_inr - p.total_cost_inr) AS net_profit_inr

FROM production_financial_summary p
LEFT JOIN shift_manpower_summary m
    ON p.date = m.date
   AND p.area = m.area
   AND p.shift = m.shift;
GO

PRINT 'final_productivity_dataset view created successfully';
GO

;
SELECT * FROM shift_manpower_summary



SELECT * FROM final_productivity_dataset



PRINT 'Views Created and Validated Successfully!';
