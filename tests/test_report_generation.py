from src.report_generator import generate_pdf_report


def test_generate_pdf_report(tmp_path):
    summary = {
        "total_records": 8,
        "total_products_sold": 33,
        "total_sales": 226800.0,
        "average_sale": 28350.0,
        "highest_sale": 90000.0,
        "lowest_sale": 5000.0
    }

    output_file = tmp_path / "test_report.pdf"

    generate_pdf_report(summary, str(output_file))

    assert output_file.exists()
    assert output_file.stat().st_size > 0