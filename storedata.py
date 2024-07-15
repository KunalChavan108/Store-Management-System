import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Oneeyedeagle@21",
    database="store"
)

# Fetch the data
query = "SELECT nameofunit, profit FROM store"
df = pd.read_sql(query, conn)
conn.close()

# Print first few rows to verify data
print(df.head())


# Plotting a line chart of profits by unit name
plt.figure(figsize=(12, 8))
sns.lineplot(x='nameofunit', y='profit', data=df, marker='o')
plt.title('Profit by Unit Name')
plt.xlabel('Unit Name')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.show()
