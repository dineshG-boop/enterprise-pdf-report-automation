import pandas as pd


def load_sales_data(file_path):
    df = pd.read_csv(file_path)

    required_columns = [
        "Date",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    if df.empty:
        raise ValueError("CSV file is empty")

    if df[required_columns].isnull().any().any():
        raise ValueError("CSV contains missing values")

    if (df["Quantity"] <= 0).any():
        raise ValueError("Quantity must be positive")

    if (df["Unit_Price"] < 0).any():
        raise ValueError("Price cannot be negative")

    df["Date"] = pd.to_datetime(df["Date"], errors="raise")

    df["Sales"] = df["Quantity"] * df["Unit_Price"]

    return df


def calculate_summary(df):
    summary = {
        "total_records": len(df),
        "total_products_sold": int(df["Quantity"].sum()),
        "total_sales": float(df["Sales"].sum()),
        "average_sale": float(df["Sales"].mean()),
        "highest_sale": float(df["Sales"].max()),
        "lowest_sale": float(df["Sales"].min())
    }

    return summary