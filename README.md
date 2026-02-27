📊  SECL Analytics Project
Attendance & Productivity Correlation Analysis
Using Biometric Attendance Data  ·  Coal Production Logs  ·  Power BI Dashboard

🏭  Korba  |  Kusmunda  |  Dipka      🗓  Full Year 2025      📁  13,140 Records

📌  What Is This Project?
This project was built for South Eastern Coalfields Limited (SECL), a coal-producing company under the Ministry of Coal, Government of India. It answers a simple but powerful business question:

"How much does one absent critical worker (Shovel/Dumper Operator) actually cost SECL in lost coal production and profit per shift?"

To answer this, we:
•	Combined HR biometric attendance records with daily coal production logs
•	Cleaned, validated, and engineered 29 analytical features across 13,140 shift records
•	Ran statistical correlation (r = 0.87) and regression analysis to quantify the impact
•	Built a 6-page interactive Power BI dashboard for SECL management

🔢  Key Numbers at a Glance
📋  Total Shift Records
13,140	🏭  Mining Areas Analyzed
3 Areas
⛏️  Total Coal Production
67.8 Million T	📈  Attendance-Production Corr.
87%  (r = 0.87)
👷  Average Attendance Rate
91.1%	🎯  Avg. Production Achievement
232% of Target
💸  Cost / Absent Critical Worker
₹40,000 / Shift	💰  Total Net Profit (2025)
₹126.5 Billion

🛠️  Tech Stack
Category	Tool / Library	Purpose
Language	Python 3.10	Data cleaning, EDA, regression modeling
Data Processing	Pandas, NumPy	Data manipulation and feature engineering
Visualization	Matplotlib, Seaborn	EDA charts and statistical plots
Statistics	Scikit-learn, StatsModels	Linear regression, OLS, correlation
Database	SQL (MySQL / PostgreSQL)	Data integration and aggregation via JOINs
BI Dashboard	Microsoft Power BI Desktop	6-page interactive management dashboard
IDE	VS Code + Jupyter Notebooks	Development environment
Environment	Anaconda / conda (secl_env)	Dependency & environment management

 
📁  Project Folder Structure
Set up your project exactly like this before writing any code:

SECL_Project/
│
├── data/
│   ├── 1_employee_master.csv
│   ├── 2_biometric_attendance.csv
│   └── 3_production_financial_summary.csv
│
├── notebooks/
│   ├── 01_data_quality_check.ipynb
│   ├── 02_data_integration.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_eda_analysis.ipynb
│   └── 05_regression_model.ipynb
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── regression_model.py
│
├── dashboard/
│   └── SECL_Dashboard.pbix
│
├── outputs/
│   └── phase3_feature_engineered_dataset.csv
│
|── reports/
│   └── SECL_Project_Report.docx
│
├── requirements.txt
└── README.md

⚙️  Installation & Setup
Step 1 — Clone the Repository
git clone https://github.com/your-username/SECL-Analytics.git
cd SECL-Analytics

Step 2 — Create Conda Environment  (Recommended for Windows + Anaconda)
Why conda and not venv?
If you have Anaconda installed, using conda avoids a common Windows error where venv fails to copy launcher files when your folder path contains spaces.

# Open Anaconda Prompt (NOT regular CMD)

# Navigate to project folder
cd "D:\SECL_Project"

# Create the environment
conda create -n secl_env python=3.10 -y

# Activate it
conda activate secl_env

# You should now see (secl_env) in your terminal

Step 3 — Install Required Libraries
pip install pandas numpy matplotlib seaborn jupyter
pip install scikit-learn statsmodels openpyxl

# Save your environment for others
pip freeze > requirements.txt

Step 4 — Connect to VS Code
1.	Open VS Code and open your project folder: File → Open Folder
2.	Press Ctrl + Shift + P
3.	Type: Python: Select Interpreter
4.	Choose: Python 3.10 (secl_env) — your conda environment

Step 5 — Verify Your Setup
# Create a file called test_env.py and run it
import pandas as pd
import numpy as np
print("Environment working ✔")
print(pd.__version__)
If it prints a version number without errors — you're ready to go!

 
🗄️  Data Architecture — The 3 Core Tables
The entire project is built on three tables. Everything else is derived from them.

Table 1 — employee_master
The HR baseline. Tells us who works where, in what role, and how experienced they are.
Column	Type	Description
employee_id	INT (PK)	Unique employee number
designation	TEXT	Dumper Operator, Shovel Operator, etc.
role_category	TEXT	Critical / Non-Critical — used for regression filtering
department	TEXT	Mining / Transport
area	TEXT	Korba / Kusmunda / Dipka
employment_type	TEXT	Permanent / Contract
experience_years	INT	Skill maturity of the employee

Table 2 — biometric_attendance
Core HR input. Every punch-in and punch-out. Used to calculate attendance % and effective manpower.
Column	Type	Description
attendance_id	INT (PK)	Primary key
date	DATE	Attendance date (ISO format: YYYY-MM-DD)
employee_id	INT (FK)	Links to employee_master
shift	TEXT	Morning / Evening / Night
check_in_time	TIME	Punch-in time
check_out_time	TIME	Punch-out time
attendance_status	TEXT	Present / Absent
work_hours	DECIMAL	Actual hours worked
late_entry_flag	BOOLEAN	Yes / No
early_exit_flag	BOOLEAN	Yes / No

Table 3 — production_financial_summary  (daily_production)
Operations output. This is the dependent variable (Y) in the regression. Tells us how much was produced and what it was worth.
Column	Type	Description
date	DATE	Shift date
area	TEXT	Korba / Kusmunda / Dipka
shift	TEXT	Morning / Evening / Night
coal_production_tonnes	DECIMAL	Main output — the Y variable in regression
target_production	DECIMAL	Planned output (daily target ÷ 3 shifts)
production_achievement_pct	DECIMAL	(Actual / Target) × 100 — efficiency measure
critical_roles_present	INT	Count of Shovel/Dumper Operators present
total_wage_cost	DECIMAL	HR cost for the shift
revenue_inr	DECIMAL	Revenue from coal produced
net_profit_inr	DECIMAL	Revenue minus costs for the shift

Data Flow:
employee_master  →  biometric_attendance  →  production_financial_summary  →  Regression Analysis  →  Power BI

▶️  How to Run the Project
Correct Order: Python First, then SQL, then Python Again
Step	Action	Tool	Output
1	Data quality & validation	Python (Pandas)	Confirmed clean dataset
2	Data integration & aggregation	SQL (JOINs on date+area+shift)	Unified shift-level table
3	Feature engineering	Python (Pandas)	29-column analytical CSV
4	Exploratory data analysis (EDA)	Python (Matplotlib, Seaborn)	Pattern charts & insights
5	Regression model	Python (Scikit-learn, StatsModels)	r = 0.87, coefficients
6	Power BI dashboard (6 pages)	Power BI Desktop	SECL_Dashboard.pbix
7	Documentation & report	MS Word / GitHub README	Final submission

Run the Notebooks in Order
# Step 1 — Data Quality Check
jupyter notebook notebooks/01_data_quality_check.ipynb

# Step 2 — Feature Engineering
jupyter notebook notebooks/03_feature_engineering.ipynb

# Step 3 — Regression Model
jupyter notebook notebooks/05_regression_model.ipynb

 
📊  Key Findings
1.  Strong Attendance-Production Correlation
Pearson r = 0.87
For every 1% drop in shift attendance → production falls by approximately 50 tonnes per shift.

Attendance Level	Avg. Production / Shift	Status
High  (> 92%)	~5,400 tonnes	✅ Target Zone
Medium (85–92%)	~5,100 tonnes	🟡 Acceptable Zone
Low  (< 85%)	~4,600 tonnes	🔴 Alert Zone

2.  Critical Role Impact
•	Each absent critical worker (Shovel/Dumper Operator) = -13 tonnes production per shift
•	If critical staff attendance drops below 60%, production collapses regardless of overall attendance
•	Optimal critical staff ratio: 72%+ of total present staff
•	Financial cost: 1 absent critical worker = ₹40,000 in lost net profit per shift

3.  Area-Level Performance
Area	Avg. Attendance	Avg. Production / Shift	Avg. Profit Margin
Korba	91.3%	~4,750 tonnes	~81%
Kusmunda	90.8%	~5,400 tonnes	~75%
Dipka	91.4%	~5,970 tonnes	~85%

Dipka leads in both production and profit. Kusmunda shows the most volatile relationship — priority area for manpower interventions.

4.  Target Achievement Anomaly
Average production achievement = 232% of set targets.
Current targets are too conservative and do not serve as meaningful benchmarks. They need an upward revision to enable realistic performance management.

📺  Power BI Dashboard — 6 Pages
Page	Title	What It Shows
1	Executive Summary	KPI cards, coal production trend, area comparison, correlation scatter plot
2	Operational Dashboard	Real-time shift-level monitoring, attendance breakdown, performance matrix
3	Attendance Impact	Production by attendance bracket (High/Medium/Low), critical vs total attendance
4	Financial Performance	Profit margin, cost per tonne, revenue per tonne, profitability heatmap
5	Manpower Planning	Staffing requirements vs actual, critical role impact scatter, overtime trends
6	Trends & Forecasting	Production forecast, monthly comparison, seasonal attendance heatmap

DAX Measures Used
-- Attendance
Avg_Attendance_Pct = AVERAGE('Data'[attendance_pct])
Avg_Critical_Attendance = AVERAGE('Data'[critical_attendance_pct])

-- Production
Total_Production = SUM('Data'[coal_production_tonnes])
Production_Achievement = AVERAGE('Data'[production_achievement_pct])

-- Financial
Total_Profit = SUM('Data'[net_profit_inr])
Profit_Per_Tonne = DIVIDE([Total_Profit],[Total_Production],0)

 
🧮  Feature Engineering — Key Derived Metrics
Feature Name	Formula / Meaning
attendance_pct	(total_present / total_assigned) × 100
critical_attendance_pct	(critical_present / (critical_present + critical_absent)) × 100
tonnes_per_worker	coal_production_tonnes / total_present
tonnes_per_critical_worker	coal_production_tonnes / critical_present  ← most impactful
critical_staff_ratio	critical_present / total_present  (target: 72%+)
profit_per_tonne	net_profit_inr / coal_production_tonnes
work_hours_per_tonne	total_work_hours / coal_production_tonnes
target_gap_tonnes	coal_production_tonnes − target_production
production_achievement_pct	(coal_production_tonnes / target_production) × 100
overtime_pct	(overtime_hours / regular_hours) × 100

💡  Recommendations
Immediate Actions (0–3 Months)
5.	Alert System — Set up Power BI attendance alerts for shifts where critical staff is projected below 72%
6.	Incentives — Introduce attendance incentives for Shovel/Dumper Operators — ₹40,000 loss per absence justifies the investment
7.	Targets — Revise production targets upward — 232% achievement means current benchmarks are meaningless

Medium-Term Actions (3–6 Months)
8.	Scheduling — Build a shift scheduling model maintaining 72%+ critical staff ratio as a minimum standard
9.	Root Cause — Conduct root cause analysis at Kusmunda — most volatile area, highest manpower risk
10.	Overtime Control — Cap night-shift overtime and cross-train general staff for semi-critical tasks

Strategic Actions (6–12 Months)
11.	Live Dashboard — Integrate Power BI with live biometric feeds for real-time monitoring
12.	Budgeting — Use regression findings to build a quarterly Manpower Budgeting Model
13.	Expand Analytics — Add equipment utilization data to separate human absence losses from mechanical downtime losses

✅  Conclusions
C1	Attendance is a core operational variable, not just a compliance metric. Every 1% drop in attendance = -50 tonnes coal.
C2	Critical roles (Shovel/Dumper Operators) have a disproportionate impact — their absence costs 13× more than general staff.
C3	Current production targets are too low (232% avg. achievement) and need upward revision.
C4	The Power BI dashboard shifts management from reactive reporting to proactive decision-making.
C5	High night-shift overtime is a chronic staffing symptom, not occasional peak demand — it inflates costs and drives fatigue.

👤  Author & Credits
Mayank Kumar Bareth
Data Analytics Intern  ·  Bilaspur, Chhattisgarh, India

Project:  SECL Attendance & Productivity Correlation Analysis  |  2025
Organization:  South Eastern Coalfields Limited (SECL), Ministry of Coal, Government of India

⭐  If this project helped you, please star the repository!

MIT License  ·  Data used with permission of SECL  ·  Built for educational and operational improvement purposes
