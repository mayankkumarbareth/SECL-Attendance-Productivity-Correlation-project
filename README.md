# #📊  SECL Analytics Project
# Attendance & Productivity Correlation Analysis


# ⛏️ SECL Attendance & Productivity Intelligence (SAPI)End-to-End Analytics Pipeline:

Quantifying Workforce Impact on Coal ProductionOrganization: South Eastern Coalfields Limited (SECL), Ministry of Coal, Govt. of IndiaScope: 3 Major Mining Areas (Korba, Kusmunda, Dipka) | 13,140 Shift RecordsRole: Data Analytics Intern (Bilaspur, CG)

# 📈 Executive Impact Summary"How much does a single absent Shovel Operator cost SECL?" 


This project transitions mine management from 'gut-feel' to 'data-driven' by quantifying the direct correlation between HR Biometrics and Operational Output.Financial Leakage: Identified a ₹40,000 profit loss per absent critical worker per shift.Production Correlation: Established a high-fidelity 87% correlation ($r=0.87$) between attendance and tonnage.Operational Insight: Discovered that every 1% drop in attendance leads to a ~50 tonne production deficit.Target Optimization: Proven that current benchmarks (232% achievement) are undervalued; recommended a data-backed baseline revision.


# 🏗️ Data Architecture & Engineering


The project implements a professional Medallion Architecture (Bronze/Silver/Gold) to ensure data reliability.1. The Schema (3-Table Star Schema)employee_master (Dim): HR baseline (ID, Role, Category, Area).biometric_attendance (Fact): 13k+ daily punch logs (Check-in/out, Status, Work Hours).production_financial_summary (Fact): Operational output (Tonnage, Target, Profit, Cost).2. Feature Engineering (The "Secret Sauce")I derived 29 analytical features to translate raw logs into business intelligence:critical_staff_ratio: Identifying the 72% tipping point for peak productivity.tonnes_per_work_hour: Measuring true labor efficiency.attendance_volatility: Tracking area-wise manpower risk (Highest in Kusmunda).


# 🛠️ Technical StackLanguages: 


Python 3.10 (Pandas, NumPy, Scikit-learn, StatsModels)Statistics: OLS Regression, Pearson Correlation, Hypothesis Testing (P-values)BI & Visualization: Microsoft Power BI (6-Page Executive Dashboard), Seaborn, MatplotlibDatabase: SQL (Complex Joins & Aggregations across 6 logical tables)Environment: Anaconda/Conda for dependency management (secl_env)


# 📊 Statistical Key 

FindingsMetricValueBusiness ImplicationsPearson Correlation ($r$)0.87Attendance is a direct driver of output, not just a compliance metric.
Critical Staff Tipping Point72%Production collapses if the Critical/Total staff ratio falls below this.
Shift EfficiencyDipkaHighest profit margin (85%) and attendance stability.
Target Anomaly232%Targets are currently too conservative; need +50% adjustment.

📺 Power BI Dashboard HighlightsThe dashboard serves four distinct internal audiences:

Executive: High-level P&L and Tonnage trends.Operations: Real-time shift monitoring & "What-If" parameter sliders.HR: Absenteeism heatmaps and "Critical Role" impact tracking.Finance: Cost-per-tonne analysis and revenue leakage reports.

# 2. Install Dependencies
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels


# 3. Run Analysis
jupyter notebook notebooks/05_regression_model.ipynb
💡 Strategic RecommendationsDynamic Incentives: Implement "Attendance Bonuses" for Critical Roles; the ₹40k loss/shift justifies the expense.Staffing Optimization: Standardize a 72% Critical Staff Ratio across all shift schedules.Live Integration: Bridge Power BI directly to Biometric SQL Servers for real-time risk alerts.


Author: Mayank Kumar BarethProject
Date: 2025
Context: 1-Month Data Internship | SECL Bilaspur
