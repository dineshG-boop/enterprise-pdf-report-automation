import pytest
import pandas as pd

from src.data_processor import load_sales_data, calculate_summary


def test_load_sales_data():
    data = load_sales_data("data/sales_data.csv")

    assert len(data) == 8
    assert "Sales" in data.columns


def test_calculate_summary():
    data = load_sales_data("data/sales_data.csv")

    summary = calculate_summary(data)

    assert summary["total_records"] == 8
    assert summary["total_products_sold"] == 33
    assert summary["total_sales"] == 226800.0


def test_empty_csv(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text(
        "Date,Product,Category,Quantity,Unit_Price\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="CSV file is empty"):
        load_sales_data(file_path)


def test_missing_column(tmp_path):
    file_path = tmp_path / "invalid.csv"

    file_path.write_text(
        "Date,Product,Quantity,Unit_Price\n"
        "2026-10-01,Laptop,2,45000\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="Missing column: Category"):
        load_sales_data(file_path)


def test_negative_quantity(tmp_path):
    file_path = tmp_path / "negative.csv"

    file_path.write_text(
        "Date,Product,Category,Quantity,Unit_Price\n"
        "2026-10-01,Laptop,Electronics,-2,45000\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="Quantity must be positive"):
        load_sales_data(file_path)
