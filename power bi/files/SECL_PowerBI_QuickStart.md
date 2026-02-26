# SECL Attendance & Productivity Dashboard - Quick Start Guide

## 📋 Project Understanding Summary

### What This Project Is About
You have a comprehensive dataset from SECL (South Eastern Coalfields Limited) tracking the relationship between employee attendance and coal production. The goal is to create a Power BI dashboard that visualizes this correlation to help management make data-driven manpower budgeting decisions.

### Your Dataset Summary
- **13,140 records** covering the entire year 2025
- **3 mining areas**: Korba, Kusmunda, Dipka
- **3 shifts per day**: Morning, Evening, Night
- **29 columns** including attendance, production, financial, and efficiency metrics

### Key Findings From Your Data
1. **Strong Correlation**: 87% correlation between attendance and production
2. **Average Attendance**: 91.1% across all shifts and areas
3. **Production Achievement**: 232% of targets on average (targets may need revision)
4. **Total Production**: 67.8 Million tonnes of coal in 2025
5. **Total Profit**: ₹126.5 Billion
6. **Critical Workers**: Each critical worker produces ~13 tonnes per shift
7. **Optimal Critical Staff Ratio**: 72%+ for maximum productivity

---

## 🚀 Quick Start - Creating Your Dashboard

### Step 1: Open Power BI Desktop (5 minutes)
1. Launch Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Browse to `phase3_feature_engineered_dataset.csv`
4. Click **Load** (don't transform yet)

### Step 2: Create Date Table (10 minutes)
1. Go to **Modeling** tab → **New Table**
2. Paste this DAX formula:
```DAX
DateTable = 
ADDCOLUMNS(
    CALENDAR(DATE(2025,1,1), DATE(2025,12,31)),
    "Year", YEAR([Date]),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "WeekNum", WEEKNUM([Date]),
    "DayName", FORMAT([Date], "DDDD")
)
```

### Step 3: Create Relationships (2 minutes)
1. Go to **Model View** (left sidebar)
2. Drag from `Data[date]` to `DateTable[Date]`
3. Ensure relationship is **Many-to-One**

### Step 4: Create Key Measures (15 minutes)
Go to **Modeling** → **New Measure** and create these essential measures:

```DAX
Total_Production = SUM('Data'[coal_production_tonnes])
Avg_Attendance_Pct = AVERAGE('Data'[attendance_pct])
Total_Profit = SUM('Data'[net_profit_inr])
Production_Achievement = AVERAGE('Data'[production_achievement_pct])
```

### Step 5: Build Your First Page - Executive Summary (30 minutes)

#### A. Add 4 KPI Cards (Top Row)
1. **Insert** → **Visualizations** → **Card**
2. Drag these measures to create 4 cards:
   - `Total_Production` → Format as "0.0M Tonnes"
   - `Avg_Attendance_Pct` → Format as "0.0%"
   - `Production_Achievement` → Format as "0%"
   - `Total_Profit` → Format as "₹0.0B"

#### B. Add Production Trend Chart
1. Insert → **Line Chart**
2. X-axis: `DateTable[Date]`
3. Y-axis: `Total_Production`
4. Format: Add title "Coal Production Trend"

#### C. Add Area Performance Chart
1. Insert → **Clustered Column Chart**
2. X-axis: `Data[area]`
3. Y-axis: `Total_Production`
4. Format: Add data labels

### Step 6: Add Slicers (10 minutes)
1. Insert → **Slicer**
2. Field: `Data[area]` → Style: Dropdown
3. Insert another Slicer
4. Field: `DateTable[Date]` → Style: Between

---

## 📊 Dashboard Pages Overview

### Page 1: Executive Summary
**Target Audience**: Senior Management  
**Key Question**: "How is the overall operation performing?"

**What to Show**:
- Total production, attendance, profit (KPI cards)
- Production trend over time (Line chart)
- Area comparison (Column chart)
- Attendance vs production correlation (Scatter plot)

### Page 2: Operational Dashboard
**Target Audience**: Mine Managers  
**Key Question**: "What's happening today/this week?"

**What to Show**:
- Daily staffing levels (Cards)
- Shift-wise production (Stacked bar)
- Attendance breakdown (Donut chart)
- Performance table by area and shift (Matrix)

### Page 3: Attendance Impact
**Target Audience**: HR & Operations  
**Key Question**: "How does attendance affect production?"

**What to Show**:
- Production by attendance levels (Column chart)
- Critical vs total attendance impact (Line chart)
- Correlation analysis (Scatter with trend line)
- Key insights text box

### Page 4: Financial Performance
**Target Audience**: Finance & Senior Management  
**Key Question**: "What's the profitability and efficiency?"

**What to Show**:
- Profit margin, cost per tonne (KPI cards)
- Profit trend (Area chart)
- Efficiency metrics (Gauge charts)
- Area profitability heatmap (Matrix)

### Page 5: Manpower Planning
**Target Audience**: HR & Workforce Planning  
**Key Question**: "How should we optimize staffing?"

**What to Show**:
- Staffing requirements vs actual (Stacked bar)
- Critical role impact (Scatter plot)
- Overtime analysis (Line chart)
- Recommendations text box

### Page 6: Trends & Forecasting
**Target Audience**: Strategic Planning  
**Key Question**: "What patterns exist and what's coming?"

**What to Show**:
- Production forecast (Line with analytics)
- Monthly comparison (Column chart)
- Seasonal patterns (Heatmap)

---

## 🎨 Design Guidelines

### Color Scheme to Use
Use these exact color codes for consistency:

**Main Colors**:
- Primary (Navy): `#1E2761` - Use for headers, main elements
- Secondary (Terracotta): `#B85042` - Use for highlights
- Success (Green): `#2C5F2D` - Use for positive metrics
- Warning (Gold): `#F9E795` - Use for medium performance
- Danger (Red): `#990011` - Use for alerts

**Chart Colors**:
- Production: `#065A82` (Deep Blue)
- Attendance: `#028090` (Teal)
- Profit: `#2C5F2D` (Forest Green)
- Cost: `#B85042` (Terracotta)

### Formatting Standards
- **Page Background**: Light gray (#F5F5F5)
- **Card Background**: White
- **Font**: Segoe UI
- **Title Size**: 20pt
- **KPI Value Size**: 32pt
- **Spacing**: 20px between elements

---

## 📝 Essential DAX Measures (Copy-Paste Ready)

### Production Metrics
```DAX
Total_Production = SUM('Data'[coal_production_tonnes])

Avg_Production = AVERAGE('Data'[coal_production_tonnes])

Target_Production = SUM('Data'[target_production])

Production_Variance = [Total_Production] - [Target_Production]

Production_Variance_Pct = DIVIDE([Production_Variance], [Target_Production], 0)
```

### Attendance Metrics
```DAX
Avg_Attendance_Pct = AVERAGE('Data'[attendance_pct])

Avg_Critical_Attendance = AVERAGE('Data'[critical_attendance_pct])

Total_Present = SUM('Data'[total_present])

Total_Absent = SUM('Data'[total_absent])

Attendance_Status = 
SWITCH(
    TRUE(),
    [Avg_Attendance_Pct] >= 0.92, "High",
    [Avg_Attendance_Pct] >= 0.85, "Medium",
    "Low"
)
```

### Financial Metrics
```DAX
Total_Revenue = SUM('Data'[revenue_inr])

Total_Cost = SUM('Data'[total_cost_inr])

Total_Profit = SUM('Data'[net_profit_inr])

Avg_Profit_Margin = AVERAGE('Data'[profit_margin_pct])

Profit_Per_Tonne = DIVIDE([Total_Profit], [Total_Production], 0)
```

### Efficiency Metrics
```DAX
Avg_Tonnes_Per_Worker = AVERAGE('Data'[tonnes_per_worker])

Avg_Tonnes_Per_Critical = AVERAGE('Data'[tonnes_per_critical_worker])

Total_Overtime_Hours = SUM('Data'[total_overtime_hours])
```

### Correlation Analysis
```DAX
Correlation_Attendance_Production = 
VAR SampleTable = 
    ADDCOLUMNS(
        SUMMARIZE('Data', 'Data'[date]),
        "Attendance", CALCULATE(AVERAGE('Data'[attendance_pct])),
        "Production", CALCULATE(AVERAGE('Data'[coal_production_tonnes]))
    )
VAR MeanAttendance = AVERAGEX(SampleTable, [Attendance])
VAR MeanProduction = AVERAGEX(SampleTable, [Production])
VAR Numerator = 
    SUMX(SampleTable, ([Attendance] - MeanAttendance) * ([Production] - MeanProduction))
VAR DenomAttendance = 
    SUMX(SampleTable, POWER([Attendance] - MeanAttendance, 2))
VAR DenomProduction = 
    SUMX(SampleTable, POWER([Production] - MeanProduction, 2))
RETURN
    DIVIDE(Numerator, SQRT(DenomAttendance * DenomProduction), 0)
```

---

## 🎯 Key Insights to Highlight in Dashboard

### Text Boxes to Add

**On Executive Summary Page**:
```
KEY FINDINGS:
• 87% correlation between attendance and production
• Each 1% attendance increase = ~50 tonnes more production
• Critical staff ratio of 72%+ is optimal
• Current target achievement: 232% (targets may need revision)
```

**On Attendance Impact Page**:
```
ATTENDANCE IMPACT:
• High attendance (>92%): Average 5,400 tonnes/shift
• Medium attendance (85-92%): Average 5,100 tonnes/shift
• Low attendance (<85%): Average 4,600 tonnes/shift
• Each critical worker contributes ~13 tonnes per shift
```

**On Manpower Planning Page**:
```
RECOMMENDATIONS:
• Maintain critical staff attendance above 72%
• Each absent critical worker costs ~₹40,000 in lost profit
• Focus on reducing absenteeism in critical roles
• Plan for 600 assigned, expect 552 present (92% attendance)
```

---

## ⚡ Common Power BI Tips

### Formatting Numbers
- **Millions**: Custom format `0.0,,"M"`
- **Billions**: Custom format `0.0,,,"B"`
- **Percentage**: Format as Percentage, 1 decimal
- **Currency**: Format as Currency → Choose ₹ (Rupee)
- **Thousands**: Custom format `#,##0`

### Conditional Formatting
1. Select your visual (card, table, matrix)
2. Format pane → Conditional formatting
3. Choose field → Background color or Font color
4. Rules based on values:
   - Green: >92% attendance, >100% achievement
   - Yellow: 85-92% attendance, 90-100% achievement
   - Red: <85% attendance, <90% achievement

### Adding Analytics Lines
1. Select a line or column chart
2. Analytics pane (magnifying glass icon)
3. Add:
   - Average line (shows mean)
   - Median line
   - Trend line (shows correlation)
   - Forecast (predicts future values)

---

## 🐛 Troubleshooting

### Problem: Measures showing blank
**Solution**: Check if you have relationships set up correctly between Data and DateTable

### Problem: Charts not updating with slicers
**Solution**: Edit interactions - Format → Edit interactions → Ensure charts are set to "Filter"

### Problem: Dates not showing correctly
**Solution**: In Power Query, ensure date column is type "Date" not "Text"

### Problem: Numbers showing as decimals when they should be whole
**Solution**: Format → Category → Whole number

### Problem: Colors not consistent across charts
**Solution**: Use Data colors in Format pane → Set explicit colors for each series

---

## 📚 Learning Resources

### Power BI Essentials
- Official documentation: https://docs.microsoft.com/power-bi/
- DAX reference: https://dax.guide/
- YouTube: "Guy in a Cube" channel (excellent tutorials)
- YouTube: "SQLBI" channel (advanced DAX)

### Design Resources
- Color palette tool: https://coolors.co/
- Icon library: https://www.flaticon.com/
- Power BI community: https://community.powerbi.com/

---

## ✅ Pre-Presentation Checklist

Before showing to stakeholders:

- [ ] All slicers are working
- [ ] All charts have clear titles
- [ ] KPI cards have proper formatting (M, B, %, ₹)
- [ ] Colors are consistent across pages
- [ ] Date slicer shows correct range (2025)
- [ ] Test with different filter combinations
- [ ] Check mobile layout if users will use phones
- [ ] Save a copy before the presentation
- [ ] Test refresh if data will update
- [ ] Prepare 2-3 key insights to highlight

---

## 🎤 Presentation Talking Points

### Opening Statement
"This dashboard visualizes SECL's attendance and production data for 2025, covering 13,140 shift observations across three mining areas. It demonstrates a strong 87% correlation between employee attendance and coal production, with specific focus on critical roles like shovel and dumper operators."

### Key Messages
1. **Data-Driven**: "Using regression analysis, we've quantified that each critical worker contributes approximately 13 tonnes per shift."

2. **Business Impact**: "With 232% average target achievement, our actual production significantly exceeds targets, suggesting an opportunity to revise planning."

3. **Actionable Insights**: "Maintaining critical staff attendance above 72% is optimal. Each percentage point drop in attendance costs approximately 500 tonnes in production."

4. **Financial Correlation**: "The dashboard links attendance directly to profitability, showing that each absent critical worker represents roughly ₹40,000 in lost profit per shift."

### Closing
"This dashboard enables data-driven manpower budgeting and helps identify which shifts and areas need attention for optimal productivity."

---

## 📞 Next Steps

1. **Build the dashboard** following the Quick Start section
2. **Test with sample filters** to ensure everything works
3. **Get feedback** from a colleague or manager
4. **Iterate** based on feedback
5. **Present** to stakeholders
6. **Maintain** - set up scheduled refresh if data updates

---

**Document Version**: 1.0  
**Created**: January 31, 2026  
**Dataset**: phase3_feature_engineered_dataset.csv (13,140 records)  

---

## 💡 Pro Tips

1. **Start Simple**: Build Page 1 (Executive Summary) first, then expand
2. **Copy Formatting**: Use Format Painter to copy visual styles
3. **Save Often**: Save your .pbix file frequently
4. **Version Control**: Save dated copies (e.g., Dashboard_v1.pbix, Dashboard_v2.pbix)
5. **Performance**: Keep visuals per page under 12 for best performance
6. **Mobile First**: Design with mobile users in mind if applicable
7. **Test Filters**: Always test slicer combinations to catch errors
8. **Documentation**: Add text boxes with data sources and update dates
9. **Accessibility**: Use high-contrast colors for readability
10. **Backup**: Keep a backup of your CSV file

Good luck with your dashboard! 🚀
