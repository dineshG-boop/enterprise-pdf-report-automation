# Automated PDF Sales Report Generator

## Project Overview

The Automated PDF Sales Report Generator is a Python-based automation project that reads sales data from a CSV file, validates the data, calculates sales statistics, and generates a formatted PDF report.

The project includes command-line arguments, logging, error handling, and automated testing using Pytest.

## Features

* Read sales data from CSV files.
* Validate required columns and input data.
* Calculate total sales, average sales, highest sale, and lowest sale.
* Generate formatted PDF reports.
* Accept input and output paths through command-line arguments.
* Record application events and errors in a log file.
* Run automated tests using Pytest.

## Technologies Used

* Python
* Pandas
* ReportLab
* Pytest
* Argparse
* Logging
* Git and GitHub

## Project Structure

```text
enterprise-pdf-report-automation/
├── data/
│   └── sales_data.csv
├── src/
│   ├── data_processor.py
│   └── report_generator.py
├── tests/
│   ├── test_data_processor.py
│   └── test_report_generator.py
├── reports/
├── generate_report.py
├── requirements.txt
├── automation.log
└── README.md
```

## Installation

Clone the repository and navigate to the project directory.

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Generate a PDF report by running:

```bash
python generate_report.py --input data/sales_data.csv --output reports/sales_report.pdf
```

The generated PDF report will be saved in the `reports` directory.

## Run Automated Tests

Execute the test suite:

```bash
python -m pytest -v
```

The tests validate CSV processing, sales calculations, input validation, and PDF generation.

## Sample Sales Summary

Using the included sample dataset:

* Total records: 8
* Total products sold: 33
* Total sales: ₹226,800
* Average sale per record: ₹28,350
* Highest sale: ₹90,000
* Lowest sale: ₹5,000

## Error Handling and Logging

The application records execution details and errors in `automation.log` to help troubleshoot problems.

## Future Improvements

* Add support for Excel input files.
* Generate charts and graphs in PDF reports.
* Add category-wise sales analysis.
* Support date-range filtering.
* Integrate continuous testing with GitHub Actions.

## Author

Dinesh Govindaraj
