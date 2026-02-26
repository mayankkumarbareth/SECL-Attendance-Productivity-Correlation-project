import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ---------------- CONFIGURATION ----------------
start_date = datetime(2025, 1, 1)
num_days = 365
areas = ['Dipka', 'Kusmunda', 'Korba']
shifts = ['Morning', 'Evening', 'Night']

critical_roles = [
    'Dumper Operator', 'Shovel Operator',
    'Excavator Operator', 'Drill Operator', 'Blaster'
]

non_critical_roles = [
    'Helper', 'Clerk', 'HR Executive', 'Security Guard'
]

# ---------------- 1️⃣ EMPLOYEE MASTER ----------------
employees = []

for area in areas:
    for i in range(150):
        role = random.choice(critical_roles) if random.random() < 0.7 else random.choice(non_critical_roles)
        employees.append({
            'employee_id': f"SECL_{area[:3].upper()}_{i+1000}",
            'designation': role,
            'role_category': 'Critical' if role in critical_roles else 'Non-Critical',
            'employment_type': random.choice(['Permanent', 'Contractual']),
            'area': area,
            'experience_years': random.randint(1, 25)
        })

df_master = pd.DataFrame(employees)

# ---------------- 2️⃣ ATTENDANCE + 3️⃣ PRODUCTION ----------------
attendance_data = []
summary_data = []

for d in range(num_days):
    curr_date = start_date + timedelta(days=d)

    for area in areas:

        # ---- Area-based Financial Parameters ----
        if area == 'Dipka':
            price_per_ton = 2800
            diesel_per_ton = 400
            base_target = 6000
        elif area == 'Kusmunda':
            price_per_ton = 2200
            diesel_per_ton = 550
            base_target = 7500
        else:  # Korba
            price_per_ton = 1900
            diesel_per_ton = 350
            base_target = 4000

        for shift in shifts:
            area_pool = df_master[df_master['area'] == area]
            shift_pool = area_pool.sample(frac=0.33)

            critical_present = 0
            wage_cost = 0

            for _, emp in shift_pool.iterrows():
                status = np.random.choice(['Present', 'Absent'], p=[0.91, 0.09])
                overtime = round(random.uniform(0, 4), 1) if status == 'Present' and random.random() < 0.15 else 0

                attendance_data.append({
                    'date': curr_date.date(),
                    'employee_id': emp['employee_id'],
                    'shift': shift,
                    'attendance_status': status,
                    'work_hours': 8 if status == 'Present' else 0,
                    'overtime_hours': overtime
                })

                if status == 'Present':
                    wage = 1600 if emp['employment_type'] == 'Permanent' else 850
                    wage_cost += wage

                    if emp['role_category'] == 'Critical':
                        critical_present += 1

            # ---------------- PRODUCTION LOGIC ----------------
            actual_coal = (critical_present * 165) + np.random.normal(0, 100)
            actual_coal = max(0, round(actual_coal, 2))

            revenue = round(actual_coal * price_per_ton, 2)
            total_cost = round((actual_coal * diesel_per_ton) + wage_cost, 2)
            net_profit = round(revenue - total_cost, 2)

            summary_data.append({
                'date': curr_date.date(),
                'area': area,
                'shift': shift,
                'coal_production_tonnes': actual_coal,
                'target_production': base_target // 3,
                'critical_roles_present': critical_present,
                'total_wage_cost': wage_cost,          # ✅ ADDED
                'Total_Cost_INR': total_cost,
                'Revenue_INR': revenue,
                'Net_Profit_INR': net_profit
            })

# ---------------- SAVE FILES ----------------
df_master.to_csv('1_employee_master.csv', index=False)
pd.DataFrame(attendance_data).to_csv('2_biometric_attendance.csv', index=False)
pd.DataFrame(summary_data).to_csv('3_production_financial_summary.csv', index=False)

print("✅ All datasets created successfully with total_wage_cost included!")


    