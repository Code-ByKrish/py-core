import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "ExpenseTracker/Expenses.csv"
CHART_DIR = "ExpenseTracker/charts"

df = pd.read_csv(DATA_PATH)

print("First 5 rows:")
print(df.head())
print("\nColumn types and non-null counts:")
df.info()
print("\nSummary statistics:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())


df = df.drop_duplicates()
df["category"] = df["category"].fillna("Unknown")
df["category"] = df["category"].str.strip()
df["description"] = df["description"].str.strip()
df["category"] = df["category"].str.title()
print("\nAfter Cleaning:")
print(df.isnull().sum())
print("\nCategories:")
print(sorted(df["category"].unique()))


df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month_name()
df["weekday"] = df["date"].dt.day_name()


total_spending = df["amount"].sum()
print(f"\nTotal Spending: Rs {total_spending:,.0f}")
category_spending = (
    df.groupby("category")["amount"]
      .sum()
      .sort_values(ascending=False)
)
print("\nSpending by Category:")
print(category_spending)
print("\nTop Category:")
print(category_spending.idxmax())
monthly = df.groupby("month")["amount"].sum()
print("\nMonthly Spending:")
print(monthly)
print("\nTop 5 Expenses:")
print(
    df.nlargest(5, "amount")
      [["date", "description", "category", "amount"]]
)
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
weekday_avg = (
    df.groupby("weekday")["amount"]
      .mean()
      .reindex(day_order)
)
print("\nAverage Spend by Weekday:")
print(weekday_avg.round(2))


plt.figure(figsize=(8, 5))
category_spending.plot(kind="bar")
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (Rs)")
plt.xticks(rotation=45)

plt.savefig(
    f"{CHART_DIR}/category_spending.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(8, 4))
monthly.plot(
    kind="line",
    marker="o"
)
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount (Rs)")
plt.grid(True)
plt.savefig(
    f"{CHART_DIR}/monthly_spending.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


plt.figure(figsize=(8, 4))
weekday_avg.plot(kind="bar")
plt.title("Average Spend by Weekday")
plt.xlabel("Day")
plt.ylabel("Average Amount (Rs)")
plt.xticks(rotation=45)
plt.savefig(
    f"{CHART_DIR}/weekday_spending.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()