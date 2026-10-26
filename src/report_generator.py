from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from datetime import datetime


def generate_pdf_report(summary, output_path):
    document = SimpleDocTemplate(
        output_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(
        Paragraph("Sales Summary Report", styles["Title"])
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    table_data = [
        ["Metric", "Value"],
        ["Total Records", str(summary["total_records"])],
        ["Total Products Sold", str(summary["total_products_sold"])],
        ["Total Sales", f"Rs. {summary['total_sales']:,.2f}"],
        ["Average Sale", f"Rs. {summary['average_sale']:,.2f}"],
        ["Highest Sale", f"Rs. {summary['highest_sale']:,.2f}"],
        ["Lowest Sale", f"Rs. {summary['lowest_sale']:,.2f}"]
    ]

    table = Table(table_data, colWidths=[220, 220])

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("PADDING", (0, 0), (-1, -1), 8)
        ])
    )

    content.append(table)

    document.build(content)

    print(f"PDF report generated successfully: {output_path}")