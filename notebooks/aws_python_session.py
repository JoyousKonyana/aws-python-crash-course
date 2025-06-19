# 📦 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')


# 📥 Load the dataset
df = pd.read_csv("../data/ESK2033.csv")

print(df.head())

# ⏱️ Parse dates if needed (optional depending on your format)
df['Date'] = pd.to_datetime(df['Date Time Hour Beginnin'], errors='coerce')

# -------------------------
# 1. Dataset shape
print("1. Dataset shape (rows, columns):", df.shape)

# 2. Column names
print("\n2. Column names:")
print(df.columns.tolist())

# 3. Missing values
print("\n3. Missing values per column:")
print(df.isnull().sum())

# 4. Data types
print("\n4. Data types:")
print(df.dtypes)

# 5. Date range
print("\n5. Date range:")
print(df['Date'].min(), "to", df['Date'].max())

# 6. Average residual demand
print("\n6. Average Residual Demand:", df['Residual Demand'].mean())

# 7. Max & Min residual demand
print("\n7. Max:", df['Residual Demand'].max(), "| Min:", df['Residual Demand'].min())

# 8. Residual demand over time
plt.figure(figsize=(12, 5))
sns.lineplot(data=df, x='Date', y='Residual Demand')
plt.title('Residual Demand Over Time')
plt.xlabel('Date')
plt.ylabel('Residual Demand')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Average international exports and imports
print("\n9. Avg International Export:", df['International Exports'].mean())
print("Avg International Import:", df['International Imports'].mean())

# 10. Total electricity generation
df['Total Generation'] = df[['Thermal Generation', 'Nuclear Generation',
                             'Hydro Generation', 'Gas Generation']].sum(axis=1)
print("\n10. Total Generation sample:")
print(df['Total Generation'].head())

# 11. Thermal vs Nuclear generation over time
plt.figure(figsize=(12, 5))
sns.lineplot(data=df[['Date', 'Thermal Generation', 'Nuclear Generation']].dropna(), x='Date', y='Thermal Generation', label='Thermal')
sns.lineplot(data=df[['Date', 'Thermal Generation', 'Nuclear Generation']].dropna(), x='Date', y='Nuclear Generation', label='Nuclear')
plt.title('Thermal vs Nuclear Generation')
plt.legend()
plt.tight_layout()
plt.show()

# 12. Correlation: Residual Demand vs Dispatchable Generation
correlation = df['Residual Demand'].corr(df['Dispatchable Generation'])
print("\n12. Correlation (Residual Demand vs Dispatchable Gen):", correlation)

# 13. Hour with highest avg residual demand (if Time or Hour exists)
if 'Hour Beginning' in df.columns:
    print("\n13. Avg Residual Demand by Hour:")
    hourly_avg = df.groupby('Hour Beginning')['Residual Demand'].mean()
    print(hourly_avg.sort_values(ascending=False).head())

# 14. Renewable capacity trend
plt.figure(figsize=(10, 4))
sns.lineplot(data=df, x='Date', y='Total RE Installed Capacity')
plt.title('Total Renewable Installed Capacity Over Time')
plt.tight_layout()
plt.show()

# 15. Load shedding over months/years — Assuming Total UCLF as proxy
df['Year'] = df['Date'].dt.year
monthly_avg = df.groupby(df['Date'].dt.to_period('M'))['Total UCLF'].mean()
monthly_avg.plot(kind='bar', figsize=(14, 5), title='Avg UCLF by Month')
plt.ylabel('UCLF')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 16. Pattern in UCLF
plt.figure(figsize=(12, 4))
sns.lineplot(data=df, x='Date', y='Total UCLF')
plt.title('Unplanned Capacity Loss Factor Over Time')
plt.tight_layout()
plt.show()

# 17. Avg non-commercial sent-out
print("\n17. Avg Non-Commercial Sent-Out:", df['Non Comm Sentout'].mean())

# 18. Drakensberg variation
print("\n18. Drakensberg Gen Hours - Summary:")
print(df['Drakensberg Gen Unit Hours'].describe())

# 19. Compare Palmiet and Ingula generation hours
plt.figure(figsize=(12, 5))
sns.lineplot(data=df, x='Date', y='Palmiet Gen Unit Hours', label='Palmiet')
sns.lineplot(data=df, x='Date', y='Ingula Gen Unit Hours', label='Ingula')
plt.title('Palmiet vs Ingula Gen Unit Hours Over Time')
plt.legend()
plt.tight_layout()
plt.show()

# 20. Correlation heatmap
plt.figure(figsize=(16, 10))
sns.heatmap(df.corr(numeric_only=True), annot=False, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
