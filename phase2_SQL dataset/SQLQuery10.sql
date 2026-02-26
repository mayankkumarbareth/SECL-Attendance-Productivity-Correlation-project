--==================================================================
-- PHASE 2: Join Employee Master + Attendance (FOUNDATION JOIN)
--.=================================================================

CREATE VIEW attendance_with_employee AS
SELECT
    a.date,
    a.shift,
    a.employee_id,
    e.area,
    e.designation,
    e.role_category, 
    e.employment_type,
    a.attendance_status,
    a.work_hours,
    a.overtime_hours
FROM biometric_attendance a
JOIN employee_master e
ON a.employee_id = e.employee_id;
GO

SELECT*FROM attendance_with_employee