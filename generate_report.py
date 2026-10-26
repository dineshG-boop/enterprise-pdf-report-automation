import argparse
import logging
import os

from src.data_processor import load_sales_data, calculate_summary
from src.report_generator import generate_pdf_report


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("automation.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Automated PDF Sales Report Generator"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input sales CSV file"
    )

    parser.add_argument(
        "--output",
        default="sales_report.pdf",
        help="Path for the output PDF report"
    )

    args = parser.parse_args()

    try:
        logger.info("Starting sales report generation")

        logger.info("Loading CSV file: %s", args.input)
        data = load_sales_data(args.input)

        logger.info("Calculating sales summary")
        summary = calculate_summary(data)

        output_directory = os.path.dirname(args.output)

        if output_directory:
            os.makedirs(output_directory, exist_ok=True)

        logger.info("Generating PDF report: %s", args.output)
        generate_pdf_report(summary, args.output)

        logger.info("Sales report generated successfully")

    except Exception:
        logger.exception("Report generation failed")
        raise SystemExit(1)


if __name__ == "__main__":
    main()