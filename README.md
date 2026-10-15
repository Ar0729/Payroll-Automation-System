# Payroll Automation System

A comprehensive Python-based payroll automation system designed to process employee leave data, detect various leave patterns, and generate detailed payroll reports with advanced analysis.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Input Files](#input-files)
- [Output Files](#output-files)
- [Processors](#processors)
- [Data Processing Logic](#data-processing-logic)

---

## ✨ Features

### Leave Processing
- **Loss of Pay (LOP) Analysis** - Detects LOP for current and previous months
- **Maternity Leave Tracking** - Identifies and processes maternity leave records
- **Repeated Sick Leave Detection** - Flags employees with >5 consecutive sick days
- **Sandwich Leave Detection** - Identifies Friday-Monday leave patterns with CL validation
- **Friday-Monday Patterns** - Tracks recurring weekend leave patterns

### Resignation Management
- **Multi-Month Resignation Tracking** - Groups resignees by previous, current, and next month
- **Process Status Monitoring** - Tracks Processing vs Hold status
- **Asset & Clearance Tracking** - Records HR/Finance/Asset clearance status
- **Formatted Reporting** - Month-grouped output with visual highlighting

### Data Enrichment
- **Employee Name Mapping** - Automatically links employee IDs to names
- **AI-Powered Insights** - Optional AIGuard integration for enhanced remarks
  - Context-aware analysis of each record
  - Automated summary generation
  - Fraud/anomaly detection suggestions
  - Graceful degradation if AI unavailable
- **Date Formatting** - Automatic conversion to standard DD-MM-YYYY format
- **Validation Rules** - CL (Casual Leave) applied only on Tuesday-Thursday

### Output Generation
- **Excel Reports** - Professional formatted Excel output with multiple sheets
- **Month-Based Organization** - Data grouped logically by month and leave type
- **Color Highlighting** - Visual distinction for month headers and important records
- **Rich Text Remarks** - Enhanced remarks with AI insights and leave application dates
- **Comprehensive Coverage** - 8 different leave analysis processors with integrated output

---

## 📁 Project Structure

```
payroll_automation/
├── main.py                          # Main entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── config/
│   └── settings.py                  # Configuration settings
├── input/
│   ├── Absence Details Report_*.xlsx     # Employee leave data
│   └── Resignation_Input_*.xlsx          # Resignation data
├── output/
│   └── payroll_output.xlsx          # Generated report
├── template/
│   └── Template.xlsx                # Excel template
├── processors/
│   ├── lop_current.py               # Current month LOP processor
│   ├── lop_previous.py              # Previous month LOP processor
│   ├── maternity_leave.py           # Maternity leave processor
│   ├── repeated_sick.py             # Repeated sick leave processor
│   ├── sandwich_leave.py            # Sandwich leave processor
│   ├── fri_mon_processor.py         # Friday-Monday pattern processor
│   ├── resignees.py                 # Resignation processor
│   └── sick_leave.py                # Sick leave utilities
└── utils/
    ├── file_loader.py               # Excel file loader
    ├── excel_writer.py              # Excel report writer
    ├── date_utils.py                # Date utilities
    ├── employee_name_mapper.py       # Employee name mapping
    ├── dataframe_tools.py            # DataFrame utilities
    ├── aiguard_client.py             # AIGuard API client
    └── aiguard_output_enhancer.py    # AI-powered enhancements
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd payroll_automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure file paths** (if different from defaults)
   Edit `main.py` and update the file paths:
   ```python
   INPUT_FILE = r"path/to/Absence Details Report.xlsx"
   RESIGNATION_INPUT_FILE = r"path/to/Resignation_Input.xlsx"
   TEMPLATE_FILE = r"path/to/Template.xlsx"
   OUTPUT_FILE = r"path/to/payroll_output.xlsx"
   ```

---

## ⚙️ Configuration

### Environment Variables
Set AIGuard credentials (optional, for AI enhancements):
```bash
set AIGUARD_CLIENT_ID=your_client_id
set AIGUARD_CLIENT_SECRET=your_client_secret
```

### Month Detection
The system automatically detects the current month from:
1. System date (if data available)
2. Latest available month in input data (fallback)

Months are calculated as:
- **Current Month**: Latest month in data
- **Previous Month**: Month before current
- **Next Month**: Month after current

---

## 🤖 AIGuard Integration (Optional)

### What is AIGuard?
AIGuard is an optional AI-powered module that enhances payroll output with intelligent insights and remarks. It analyzes each record contextually and generates actionable summaries.

### Setup

1. **Ensure environment variables are set**:
   ```python
   os.environ["AIGUARD_CLIENT_ID"] = "your_client_id"
   os.environ["AIGUARD_CLIENT_SECRET"] = "your_client_secret"
   ```

2. **AIGuard is automatically loaded** if credentials are available
   - If not available, system continues without AI enhancements
   - Graceful fallback ensures data processing is never blocked

### Features

- **AI-Enhanced Remarks**: Each leave record gets an AI-generated summary
- **Context-Aware Analysis**: Different analysis for each leave type
- **Lazy Loading**: Credentials loaded only when AI features are actually used
- **Error Resilience**: Errors in AI calls don't stop payroll processing
- **Configurable Model**: Uses GPT-4o-mini by default (configurable)

### Supported Leave Types for AI Enhancement

- **Current LOP**: Analyzes loss of pay patterns and flags anomalies
- **Previous LOP**: Tracks carryforward status and transitions
- **Friday-Monday Patterns**: Detects potential time-off abuse patterns
- **Repeated Sick Leave**: Flags suspicious patterns and suggests medical review
- **Maternity Leave**: Validates dates and flags compliance issues
- **Sandwich Leave**: Analyzes leave combination patterns and CL usage

### Example AI-Enhanced Remark
```
Original Remark: Sick Leave: 25-05-2026 to 28-05-2026
AI Enhancement: [AI]: Potential legitimate sick leave - 4 consecutive days midweek. 
                Consider checking medical documentation.
```

---

## 📖 Usage

### Basic Execution

```bash
python main.py
```

### Workflow

1. **Load Data** - Reads employee leave and resignation data from Excel files
2. **Detect Months** - Identifies current, previous, and next month
3. **Filter Data** - Separates data by month
4. **Run Processors** - Executes all leave analysis processors
5. **Enrich Names** - Maps employee IDs to employee names
6. **Enhance Data** - Optional AI-powered remarks (AIGuard)
7. **Generate Report** - Writes professional Excel report
8. **Save Output** - Saves to specified output location

### Example Output
```
✅ Loading BPHR data...
✅ Detecting months...
✅ Running CURRENT LOP processor...
✅ Running PREVIOUS LOP processor...
✅ Running REPEATED SICK LEAVE...
✅ Running MATERNITY LEAVE...
✅ Running Sandwich Leave...
✅ Running RESIGNEES processor...
✅ Adding employee names...
✅ Excel saved: output/payroll_output.xlsx
[DONE] Payroll report generated successfully!
```

---

## 📥 Input Files

### 1. Absence Details Report (Required)
**Format**: Excel (.xlsx)  
**Required Columns**:
- Employee ID
- Employee Name
- Leave Type (SL, CL, EL, PL, etc.)
- From Date
- To Date
- Leave Applied Date
- Status (Approved, Pending, etc.)
- No. of Days
- Unit Structure
- Comments

**File Location**: `input/Absence Details Report_DD.MM.YYYY.xlsx`

### 2. Resignation Input (Optional but recommended)
**Format**: Excel (.xlsx)  
**Required Columns**:
- Emp ID
- Employee Name
- Date of Resignation
- Last Working Day (LWD)
- Notice Period Days
- Relieving Date
- Process/Hold (Process or Hold)
- Reason for Resignation
- Asset Clearance Completed
- HR Clearance Completed
- Finance Clearance Completed
- Remark

**File Location**: `input/Resignation_Input_*.xlsx`

### 3. Excel Template (Required)
**Format**: Excel (.xlsx)  
**Content**: Pre-formatted template with sheets:
- Current_month
- Previous_month
- Repeated Sick Leave
- Mon-Fri
- Maternity Leave
- Sandwich Leave
- Resignees

**File Location**: `template/Template.xlsx`

---

## 📤 Output Files

### Payroll Output Report
**Location**: `output/payroll_output.xlsx`

**Contains Sheets**:

| Sheet Name | Purpose | Data |
|-----------|---------|------|
| **Current_month** | Current month LOP | Employees with zero productivity days |
| **Previous_month** | Previous month LOP | LOP from previous month carried forward |
| **Repeated Sick Leave** | Sick leave >5 days | Employee ID, Days, Remarks |
| **Mon-Fri** | Friday-Monday patterns | Recurring weekend leave instances |
| **Maternity Leave** | Maternity leaves | Maternity leave records |
| **Sandwich Leave** | Sandwich patterns | Friday-Monday leave combinations |
| **Resignees** | Resignation tracking | Grouped by month with process status |

**Column Format**:
- S. No
- Employee ID
- Employee Name (when available)
- Relevant metrics (days, count, dates, etc.)
- Remarks (with leave applied date)

---

## 🔧 Processors

### 1. LOP Current (`lop_current.py`)
Detects Loss of Pay in the current month
- Identifies employees with zero attendance
- Flags half-day absences
- Generates remarks for each LOP case

### 2. LOP Previous (`lop_previous.py`)
Processes previous month LOP carried forward
- Identifies ongoing LOP from previous month
- Tracks continuation into current month
- Updates status in current payroll

### 3. Maternity Leave (`maternity_leave.py`)
Processes maternity leave records
- Identifies maternity leave applicants
- Validates dates
- Generates maternity leave report

### 4. Repeated Sick Leave (`repeated_sick.py`)
Detects excessive sick leave
- Flags >5 consecutive sick days
- Calculates total days
- Marks for HR review

### 5. Sandwich Leave (`sandwich_leave.py`)
Detects Friday-Monday leave patterns
- Identifies valid combinations: SL-CL, CL-SL, EL-CL, CL-EL
- Validates CL applied only on Tue/Wed/Thu
- Counts weekend days as leave
- Spans across month boundaries

**Validation Rules**:
- Friday + Monday leave = Sandwich pattern
- CL (Casual Leave) only valid on Tuesday, Wednesday, Thursday
- Invalid CL days flagged with warning

### 6. Friday-Monday Processor (`fri_mon_processor.py`)
Tracks simple Friday-Monday patterns
- Detects employees taking Friday off and Monday off
- Counts occurrences
- Generates detailed remarks

### 7. Resignees (`resignees.py`)
Processes resignation data
- Groups by month (previous, current, next)
- Month headers highlighted in grey
- Tracks process/hold status
- Formats dates as DD-MM-YYYY

### 8. Allowance (`allowance.py`)
Processes allowance records
- Identifies and processes employee allowances
- Generates allowance details report
- Tracks allowance status and amount
- Integrated in payroll output

---

## 📊 Data Processing Logic

### Leave Type Normalization
```
CL → Casual Leave
SL → Sick Leave
EL → Emergency Leave
PL → Personal Leave
```

### Date Handling
- All dates converted to `DD-MM-YYYY` format
- Time component removed (00:00 format excluded)
- Month boundaries respected
- Cross-month leaves properly handled

### Month Filtering
- Leaves included if they fall in target month
- Spans across month boundaries supported
- Both "From Date" and "To Date" checked
- Partial overlaps properly counted

### CL Validation
```
Valid days for CL: Tuesday, Wednesday, Thursday
Invalid days: Monday, Friday, Saturday, Sunday
```

### Sandwich Leave Detection
```
Pattern: Leave on Friday + Leave on Monday
Validated Combinations:
  - SL (Friday) + CL (Monday)
  - CL (Friday) + SL (Monday)
  - EL (Friday) + CL (Monday)
  - CL (Friday) + EL (Monday)
```

---

## 🎯 Key Features by Processor

| Processor | Detects | Validation | Output |
|-----------|---------|-----------|--------|
| **LOP Current** | Zero productivity | Attendance records | LOP days |
| **LOP Previous** | Carried forward LOP | Month transition | LOP status |
| **Maternity** | Maternity leaves | Date ranges | Leave duration |
| **Repeated Sick** | >5 consecutive days | Leave duration | Total days |
| **Sandwich** | Fri-Mon patterns | Leave combinations, CL rules | Weekend count |
| **Fri-Mon** | Recurring patterns | Date proximity | Occurrence count |
| **Resignees** | Resignation records | Relieving dates | Process status |
| **Allowance** | Allowance records | Amount validation | Allowance details |

---

## 🔄 Month Calculation

The system uses this logic to determine months:

```python
# Get current system month
current_month, current_year = get_current_month()

# If no data for current month, use latest available
if no_data_for_month:
    use_latest_month()

# Calculate previous and next months
previous = current_month - 1
next = current_month + 1
```

**Example** (April 2026):
- Previous: March 2026
- Current: April 2026
- Next: May 2026

---

## 📝 Remarks and Comments

Each record includes:
- **Automatically generated remarks** from processor logic
- **Leave applied date** in bold at end of remarks
- **Validation warnings** for rule violations
- **Context-specific information** (e.g., weekend dates for sandwich leave)

Example:
```
Sandwich Leave Detected: SL on 29-03-2026 (Friday) + CL on 01-04-2026 (Monday).
Weekend days (30-03-2026, 31-03-2026) must be counted as leave.
Leave Applied: 15-03-2026
```

---

## 🐛 Troubleshooting

### Common Issues

**"Input data has no valid dates"**
- Ensure "From Date" or "Date" column exists and has valid dates
- Check date format in Excel

**"Employee names feature DISABLED"**
- Verify "Employee Name" column exists in input
- Check column spelling (case-insensitive)

**"No data for current system month"**
- System uses latest available month in data
- Check input file has recent dates

**"CL applied on invalid day(s)"**
- CL (Casual Leave) only valid on Tuesday-Thursday
- Check leave dates and update if needed

---

## 📞 Support

For issues or questions:
1. Check the output/logs for detailed error messages
2. Verify input file formats and required columns
3. Ensure all required files exist in correct locations
4. Check Python version (3.8+)

---

## 📄 License

This project is proprietary. All rights reserved.

---

## � Recent Updates

### Latest Enhancements (May 2026)

#### ✅ AI-Powered Output Enrichment
- **AIGuard Integration**: Added optional AI-powered insights to enhance payroll remarks
- **Smart Remark Generation**: AI analyzes each record and generates contextual summaries
- **Lazy Loading**: AIGuard module loads only when needed to avoid credential prompts
- **Error Handling**: Graceful fallback if AI enhancement fails - data processing continues
- **Enhanced Remarks**: Each record gets AI-generated insights combined with existing remarks

#### ✅ Enhanced Data Enrichment
- **Employee Name Mapping**: Automatically maps employee IDs to names across all output sheets
- **Comprehensive Integration**: Names enriched for all leave types and resignation records
- **Data Validation**: Ensures name mapping accuracy before output generation
- **Flexible Output**: Supports both ID-only and ID+Name formats

#### ✅ Allowance Processing
- **New Allowance Processor**: Added `allowance.py` module for allowance data processing
- **Allowance Tracking**: Identifies and processes employee allowances
- **Integration with Payroll**: Allowance data seamlessly integrated into Excel output
- **Amount Validation**: Validates allowance amounts and flags anomalies

#### ✅ Improved Excel Output
- **Multiple Processors**: Output now includes data from 8 processors
- **Better Organization**: Data grouped by leave type and resignation status
- **Rich Remarks**: All remarks include AI enhancements and leave applied dates
- **Professional Formatting**: Color-coded headers and proper column alignment

#### ✅ System Improvements
- **Robust Configuration**: Hardcoded month/year support with fallback to current system month
- **Path Flexibility**: Easy configuration of input/output paths
- **Error Logging**: Detailed console output for monitoring processing status
- **Batch Processing**: Handles large datasets efficiently with progress indicators

---

## 🔄 Version History

**v1.1.0** (May 2026)
- AIGuard integration for AI-powered remarks enhancement
- Allowance processor module
- Employee name mapping across all sheets
- Enhanced error handling and logging
- Improved data enrichment pipeline

**v1.0.0** (April 2026)
- Initial release with 7 processors
- Resignation module with month grouping
- Grey highlighted month headers
- Date formatting without time component
- Employee name mapping
- AIGuard integration (optional)

---

## 📅 Last Updated

May 23, 2026

---

**Generated for**: Payroll Automation System  
**Project Location**: `payroll_automation 1 (4)/payroll_automation`
