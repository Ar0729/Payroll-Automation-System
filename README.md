# Payroll Automation System

A Python-based payroll automation system designed to process employee leave, resignation, and allowance data, detect important leave patterns, apply validation rules, and generate structured Excel payroll reports.

This project demonstrates how **Python, Pandas, and OpenPyXL** can be used to automate repetitive Excel-based payroll data processing tasks.

> **Current Version:** v1.0.0  
> **Release Date:** 15 October 2026  
> **Project Type:** Portfolio / Demo Project

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Objectives](#-project-objectives)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Input Data](#-input-data)
- [Usage](#-usage)
- [Processing Workflow](#-processing-workflow)
- [Processors](#-processors)
- [Data Processing Logic](#-data-processing-logic)
- [Output Report](#-output-report)
- [Sample Data](#-sample-data)
- [Example Output](#-example-output)
- [Troubleshooting](#-troubleshooting)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Version History](#-version-history)
- [License](#-license)
- [Author](#-author)

---

## 📌 Overview

The **Payroll Automation System** automates common payroll-related data processing and validation tasks.

The system reads employee leave, resignation, and allowance data from Excel files, applies predefined business rules, identifies relevant patterns, and generates a formatted Excel report.

Instead of manually reviewing large Excel datasets, the system separates the processing into independent modules called **processors**. Each processor performs a specific payroll-related analysis.

### Main processing areas

- Loss of Pay (LOP) analysis
- Previous-month LOP tracking
- Repeated sick leave detection
- Maternity leave processing
- Friday-Monday leave pattern detection
- Sandwich leave detection
- Resignation tracking
- Allowance validation
- Employee name handling
- Excel report generation

---

## 🎯 Project Objectives

The main objectives of this project are:

- Automate repetitive payroll-data processing tasks
- Reduce manual Excel-based analysis
- Detect predefined leave patterns automatically
- Validate leave-related business rules
- Process resignation information
- Validate employee allowance data
- Generate structured Excel reports
- Create a modular and maintainable Python project
- Demonstrate practical Data Science/Data Analytics automation skills

---

## ✨ Features

### 🏖️ Leave Processing

#### Loss of Pay (LOP) Analysis

- Detects current-month LOP records
- Detects previous-month LOP records
- Handles leave periods crossing month boundaries
- Generates remarks for detected LOP records

#### Maternity Leave Tracking

- Identifies maternity leave records
- Calculates leave duration
- Generates maternity leave information

#### Repeated Sick Leave Detection

- Detects sick leave exceeding 5 consecutive days
- Calculates total leave duration
- Flags records that require review

#### Sandwich Leave Detection

- Detects Friday-Monday leave combinations
- Supports predefined leave combinations
- Validates Casual Leave (CL) weekday rules
- Identifies weekend days between leave records
- Supports cross-month leave periods

#### Friday-Monday Pattern Detection

- Detects employees taking leave on Friday and Monday
- Identifies recurring patterns
- Generates pattern-based remarks

---

### 👤 Resignation Management

The resignation processor handles:

- Employee ID
- Employee Name
- Date of Resignation
- Last Working Day
- Notice Period
- Relieving Date
- Process/Hold status
- Reason for resignation
- Asset clearance
- HR clearance
- Finance clearance
- Remarks

---

### 💰 Allowance Processing

The allowance processor:

- Processes employee allowance records
- Validates allowance amounts
- Detects invalid amounts
- Flags negative allowance values
- Generates allowance details

---

### 🧹 Data Processing

The system provides:

- Date conversion
- Date validation
- Employee ID handling
- Employee name mapping
- Missing-data handling
- Column validation
- Month-based processing
- Cross-month date handling

---

### 📊 Excel Report Generation

The generated Excel report includes:

- Multiple worksheets
- Formatted headers
- Automatic column-width adjustment
- Freeze panes
- Auto filters
- Structured remarks
- Separate output for each processor
- Empty-result handling

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data processing and analysis |
| OpenPyXL | Excel reading, writing and formatting |
| NumPy | Numerical operations |
| Excel | Input and output data |
| Git | Version control |
| GitHub | Source-code management |

---

## 📁 Project Structure

```text
Payroll-Automation-System/
│
├── config/
│   └── setting.py
│
├── input/
│   └── payroll_sample_data.xlsx
│
├── output/
│   └── payroll_output.xlsx
│
├── processors/
│   ├── allowance.py
│   ├── fri_mon_processor.py
│   ├── lop_current.py
│   ├── lop_previous.py
│   ├── maternity_leave.py
│   ├── repeated_sick.py
│   ├── resignees.py
│   └── sandwich_leave.py
│
├── utils/
│   ├── dataframe_tools.py
│   ├── date_utils.py
│   ├── employee_name_mapper.py
│   ├── excel_writer.py
│   └── file_loader.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📂 Folder Description

### `config/`

Contains project configuration such as:

- Input paths
- Output paths
- Date format
- Leave thresholds
- Validation rules

### `input/`

Contains sample input data used for testing and demonstration.

### `output/`

Contains generated Excel reports.

Generated output files are excluded from Git tracking using `.gitignore`.

### `processors/`

Contains independent modules responsible for different payroll-processing tasks.

### `utils/`

Contains reusable helper functions for:

- Excel loading
- Date processing
- DataFrame operations
- Employee name mapping
- Excel report generation

### `main.py`

Acts as the main entry point and coordinates all processors.

---

## 🚀 Installation

### Prerequisites

Make sure you have:

- Python 3.8 or higher
- pip
- Git
- Excel or another `.xlsx` compatible application

---

### 1. Clone the Repository

```bash
git clone https://github.com/Ar0729/Payroll-Automation-System.git
```

---

### 2. Navigate to the Project

```bash
cd Payroll-Automation-System
```

---

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 4. Activate the Virtual Environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

---

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Project configuration is maintained in:

```text
config/setting.py
```

The configuration includes:

```python
DATE_FORMAT = "%d-%m-%Y"

SICK_LEAVE_THRESHOLD = 5

VALID_CL_WEEKDAYS = {1, 2, 3}
```

### CL Weekday Mapping

```text
1 = Tuesday
2 = Wednesday
3 = Thursday
```

Therefore, Casual Leave is considered valid on:

- Tuesday
- Wednesday
- Thursday

---

## 📥 Input Data

The system uses Excel-based input data.

### 1. Absence Data

The absence data contains employee leave information.

Required columns:

```text
Employee ID
Employee Name
Leave Type
From Date
To Date
Leave Applied Date
Status
No. of Days
Unit Structure
Comments
```

### Example

| Employee ID | Employee Name | Leave Type | From Date | To Date | No. of Days |
|-------------|---------------|------------|-----------|---------|-------------|
| EMP001 | Rahul Sharma | SL | 05-10-2026 | 11-10-2026 | 7 |
| EMP002 | Priya Patil | ML | 01-10-2026 | 15-11-2026 | 46 |
| EMP003 | Amit Verma | CL | 07-10-2026 | 07-10-2026 | 1 |
| EMP004 | Sneha Joshi | LOP | 12-10-2026 | 14-10-2026 | 3 |

---

### 2. Resignation Data

Required columns:

```text
Emp ID
Employee Name
Date of Resignation
Last Working Day
Notice Period Days
Relieving Date
Process/Hold
Reason for Resignation
Asset Clearance Completed
HR Clearance Completed
Finance Clearance Completed
Remark
```

---

### 3. Allowance Data

Required columns:

```text
Employee ID
Employee Name
Allowance Type
Amount
```

The allowance processor validates the amount and assigns an appropriate status.

---

## 🚀 Usage

After installing the dependencies and placing the required input data inside the `input/` folder, run:

```bash
python main.py
```

The program will:

```text
1. Load absence data
2. Detect the processing month
3. Process current-month LOP
4. Process previous-month LOP
5. Detect repeated sick leave
6. Process maternity leave
7. Detect Friday-Monday patterns
8. Detect sandwich leave
9. Process resignation data
10. Process allowance data
11. Generate the Excel report
```

The final report is generated in:

```text
output/payroll_output.xlsx
```

---

## 🔄 Processing Workflow

```text
                 ┌─────────────────────┐
                 │    Input Excel Data │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Load & Validate  │
                 │        Data         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Detect Processing    │
                 │       Month         │
                 └──────────┬──────────┘
                            │
            ┌───────────────┼────────────────┐
            │               │                │
            ▼               ▼                ▼
       LOP Analysis    Leave Pattern    Resignation
                         Analysis       Processing
            │               │                │
            └───────────────┼────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Allowance Validation│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Generate Excel      │
                 │      Report         │
                 └──────────┬──────────┘
                            │
                            ▼
                 payroll_output.xlsx
```

---

# 🔧 Processors

## 1. Current LOP Processor

File:

```text
processors/lop_current.py
```

### Purpose

Detects Loss of Pay records that overlap with the current processing month.

### Processing

The processor:

- Converts dates to datetime
- Determines current month boundaries
- Identifies LOP records
- Handles missing `To Date`
- Generates remarks

---

## 2. Previous LOP Processor

File:

```text
processors/lop_previous.py
```

### Purpose

Identifies LOP records from the previous month that may be relevant to the current payroll cycle.

### Processing

- Determines previous month
- Checks leave-period overlap
- Identifies LOP records
- Generates carry-forward remarks

---

## 3. Repeated Sick Leave Processor

File:

```text
processors/repeated_sick.py
```

### Purpose

Detects sick leave exceeding the configured threshold.

Default threshold:

```text
More than 5 consecutive days
```

Example:

```text
05-10-2026 → 11-10-2026

Total = 7 days
```

Result:

```text
Repeated sick leave detected
```

---

## 4. Maternity Leave Processor

File:

```text
processors/maternity_leave.py
```

### Purpose

Identifies maternity leave records and calculates the duration.

Supported leave types include:

```text
ML
MATERNITY
MATERNITY LEAVE
```

---

## 5. Friday-Monday Processor

File:

```text
processors/fri_mon_processor.py
```

### Purpose

Detects leave patterns where an employee has leave on Friday and Monday.

Pattern:

```text
Friday
  ↓
Saturday
  ↓
Sunday
  ↓
Monday
```

The processor identifies the Friday and Monday records and generates a remark.

---

## 6. Sandwich Leave Processor

File:

```text
processors/sandwich_leave.py
```

### Purpose

Detects predefined Friday-Monday sandwich leave patterns.

Supported combinations:

```text
SL + CL
CL + SL
EL + CL
CL + EL
```

### Validation

The system validates whether CL is applied on a valid weekday.

Valid:

```text
Tuesday
Wednesday
Thursday
```

Invalid:

```text
Monday
Friday
Saturday
Sunday
```

If the CL date is invalid, the generated remark includes a warning.

---

## 7. Resignation Processor

File:

```text
processors/resignees.py
```

### Purpose

Processes employee resignation information.

It extracts:

- Employee ID
- Employee Name
- Resignation Date
- Last Working Day
- Notice Period
- Relieving Date
- Process/Hold status
- Reason
- Asset Clearance
- HR Clearance
- Finance Clearance
- Remarks

---

## 8. Allowance Processor

File:

```text
processors/allowance.py
```

### Purpose

Processes and validates employee allowance records.

The processor checks:

- Missing amount
- Invalid amount
- Negative amount
- Valid allowance amount

Example:

```text
Amount = 5000
Status = Valid
```

Invalid example:

```text
Amount = ABC
Status = Invalid
```

Negative example:

```text
Amount = -1000
Status = Invalid
```

---

# 📊 Data Processing Logic

## Leave Type Normalization

The system recognizes common leave abbreviations:

```text
CL → Casual Leave
SL → Sick Leave
EL → Emergency Leave
PL → Personal Leave
LOP → Loss of Pay
ML → Maternity Leave
```

---

## Date Handling

The system:

- Converts input dates to Pandas datetime
- Handles invalid dates
- Uses `DD-MM-YYYY` formatting
- Handles missing `To Date`
- Supports month boundaries
- Processes cross-month leave periods

---

## Month Filtering

The system checks whether a leave period overlaps with the processing month.

For example:

```text
Leave Period:
28-09-2026 → 03-10-2026
```

This record can be relevant to both:

```text
September 2026
October 2026
```

because the leave period crosses the month boundary.

---

## CL Validation

```text
Valid CL Days:
Tuesday
Wednesday
Thursday

Invalid CL Days:
Monday
Friday
Saturday
Sunday
```

---

## Sandwich Leave Detection

General pattern:

```text
Friday Leave
      +
Monday Leave
      =
Potential Sandwich Pattern
```

Supported combinations:

```text
SL (Friday) + CL (Monday)

CL (Friday) + SL (Monday)

EL (Friday) + CL (Monday)

CL (Friday) + EL (Monday)
```

The system generates a warning when CL is applied on a weekday that violates the configured CL rule.

---

# 📤 Output Report

The generated report is:

```text
output/payroll_output.xlsx
```

### Output Sheets

| Sheet | Purpose |
|-------|---------|
| Current_month | Current-month LOP records |
| Previous_month | Previous-month LOP records |
| Repeated Sick Leave | Sick leave exceeding 5 days |
| Mon-Fri | Friday-Monday patterns |
| Maternity Leave | Maternity leave records |
| Sandwich Leave | Sandwich leave patterns |
| Resignees | Employee resignation records |
| Allowance | Allowance validation |

---

## 📊 Output Format

The generated worksheets contain relevant information such as:

- Employee ID
- Employee Name
- Leave dates
- Number of days
- Leave type
- Allowance information
- Resignation information
- Processing status
- Remarks

The Excel writer also provides:

- Formatted headers
- Column-width adjustment
- Freeze panes
- Auto filters
- Empty-result handling

---

# 🧪 Sample Data

The repository includes synthetic sample data for demonstration and testing.

Example employees include:

```text
EMP001 - Rahul Sharma
EMP002 - Priya Patil
EMP003 - Amit Verma
EMP004 - Sneha Joshi
EMP005 - Vikas Gupta
EMP006 - Neha Kulkarni
EMP007 - Rohit Mehta
EMP008 - Anjali Singh
EMP009 - Karan Deshmukh
EMP010 - Pooja Nair
```

The sample data demonstrates:

- Sick leave
- Maternity leave
- Casual leave
- Loss of Pay
- Emergency leave
- Personal leave
- Resignation records
- Allowance validation
- Pending leave records
- Cross-month leave periods

> **Note:** All sample employee and payroll data included in this repository is synthetic and is used only for demonstration and testing.

---

# 🖥️ Example Output

When the program runs successfully, the terminal displays processing information similar to:

```text
============================================================
PAYROLL AUTOMATION SYSTEM
============================================================

Loading absence data...

Processing month: 10-2026

Running processors...

1. Current LOP
2. Previous LOP
3. Repeated Sick Leave
4. Maternity Leave
5. Friday-Monday
6. Sandwich Leave
7. Resignees
8. Allowance

Generating report...

============================================================
DONE!
============================================================
```

The generated file will be:

```text
output/payroll_output.xlsx
```

---

# 🧩 Utility Modules

## `file_loader.py`

Responsible for:

- Reading Excel files
- Checking whether files exist
- Checking empty datasets
- Normalizing columns

---

## `date_utils.py`

Provides:

- Date conversion
- Date formatting
- Month-range calculation
- Month-name generation
- Weekday validation
- CL-date validation

---

## `dataframe_tools.py`

Provides reusable DataFrame utilities for:

- Finding columns
- Validating required columns
- Removing empty rows
- Adding serial numbers

---

## `employee_name_mapper.py`

Handles mapping between:

```text
Employee ID → Employee Name
```

This allows employee names to be added to processed results.

---

## `excel_writer.py`

Responsible for:

- Creating Excel workbooks
- Writing processor results to worksheets
- Formatting headers
- Adjusting column widths
- Adding filters
- Freezing header rows

---

# 🐛 Troubleshooting

## "Input file not found"

Check that the input Excel file exists in:

```text
input/
```

Also verify the filename configured in:

```text
config/setting.py
```

---

## "No valid dates found"

Check that the input file contains valid values in:

```text
From Date
To Date
```

---

## Missing required columns

Make sure the Excel file contains the required column names.

For example:

```text
Employee ID
Employee Name
Leave Type
From Date
To Date
```

---

## No output file generated

Check:

1. Python is installed correctly.
2. The virtual environment is activated.
3. Dependencies are installed.
4. Input files exist.
5. Input columns are correct.
6. No Python error is displayed in the terminal.

---

# ⚠️ Limitations

This project is a **portfolio/demo implementation** designed to demonstrate payroll-data automation concepts.

It is not intended to be used as a production payroll system without additional:

- Security controls
- Authentication and authorization
- Data privacy controls
- Database integration
- Comprehensive business-rule validation
- Audit logging
- Unit and integration testing
- Production deployment
- Payroll compliance validation

The sample employee and payroll information included in this repository is synthetic.

---

# 🔮 Future Enhancements

Potential future improvements include:

### 📊 Analytics

- Payroll analytics dashboard
- Power BI integration
- Employee leave trend analysis
- Monthly payroll summaries
- KPI tracking

### 🌐 Application

- Streamlit web interface
- Upload Excel files through UI
- Download generated reports
- Interactive filtering

### 🗄️ Database

- MySQL/PostgreSQL integration
- Centralized employee data
- Historical payroll records
- Automated data retrieval

### 🤖 AI

- AI-assisted payroll remarks
- Anomaly detection
- Pattern analysis
- Natural-language payroll summaries

### ⚙️ Automation

- Scheduled report generation
- Automated email delivery
- Cloud deployment
- Automated data pipelines

### 🧪 Testing

- Unit tests for every processor
- Integration testing
- Automated test pipeline
- GitHub Actions CI/CD

---

# 🔄 Version History

## v1.0.0 — 15 October 2026

### Initial Public Release

The first public GitHub release of the Payroll Automation System.

### Included Features

- Current-month LOP processing
- Previous-month LOP processing
- Repeated sick leave detection
- Maternity leave processing
- Friday-Monday pattern detection
- Sandwich leave detection
- Resignation processing
- Allowance processing
- Employee name mapping
- Date processing and validation
- Cross-month leave handling
- Excel report generation
- Excel formatting
- Synthetic sample data
- Modular processor-based architecture
- Utility modules for reusable processing
- Git/GitHub project configuration
- Documentation and setup instructions

---

# 📅 Project Information

| Information | Details |
|-------------|---------|
| Project Name | Payroll Automation System |
| Version | v1.0.0 |
| Release Date | 15 October 2026 |
| Last Updated | 15 October 2026 |
| Project Type | Portfolio / Demo |
| Programming Language | Python |
| Data Processing | Pandas |
| Excel Automation | OpenPyXL |
| Version Control | Git |
| Repository | GitHub |

---

# 👨‍💻 About the Project

This project was developed as a practical demonstration of **Python-based data processing and Excel automation**.

The project focuses on converting repetitive payroll-data review tasks into a modular automated workflow.

It demonstrates practical skills in:

- Python programming
- Data manipulation
- Pandas
- Excel automation
- Data validation
- Business-rule implementation
- Modular programming
- File handling
- Report generation
- Git and GitHub

The project is designed as a **portfolio/demo implementation** and uses synthetic data rather than real employee or company payroll data.

---

# 🎓 Skills Demonstrated

```text
Python
Pandas
OpenPyXL
Excel Automation
Data Cleaning
Data Validation
Data Processing
Business Logic
Report Automation
Git
GitHub
Modular Programming
Problem Solving
```

---

# 📄 License

This project is intended for educational, learning, and portfolio purposes.

The sample data included in this repository is synthetic and does not contain real employee payroll information.

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📌 Author

**Aryan Gunjewar**

B.Tech — Data Science

Data Science | Data Analytics | Python | SQL | Power BI

---

**Current Version:** v1.0.0  
**Release Date:** 15 October 2026  
**Last Updated:** 15 October 2026