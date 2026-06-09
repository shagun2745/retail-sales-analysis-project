import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

plt.figure(figsize=(8,5))

plt.scatter(df["Discount"], df["Profit"])

plt.title("Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("profit_vs_discount.png")

plt.show()