from src.data_processor import load_sales_data, calculate_summary


df = load_sales_data("data/sales_data.csv")

summary = calculate_summary(df)

print("Sales Data:")
print(df)

print("\nSales Summary:")

for key, value in summary.items():
    print(f"{key}: {value}")