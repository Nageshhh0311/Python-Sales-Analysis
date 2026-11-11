import pandas as pd
import matplotlib.pyplot as plt

print("Sales Analysis Project")

df = pd.read_excel("raw data.xlsx")

print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Column Names:")
print(df.columns.tolist())


df = df[df["Row Labels"] != "Grand Total"].copy()

df["Gap"] = df["Sum of Target"] - df["Sum of Achieved"]

df["Achievement_Percentage"] = (
    df["Sum of Achieved"] / df["Sum of Target"]
) * 100

print("Department Performance:")
print(df)


plt.figure(figsize=(8, 5))

plt.bar(df["Row Labels"], df["Achievement_Percentage"])

plt.title("Department Achievement Percentage")
plt.xlabel("Department")
plt.ylabel("Achievement (%)")

# plt.show()


plt.figure(figsize=(8, 5))

plt.bar(df["Row Labels"], df["Sum of Target"], label="Target")
plt.bar(df["Row Labels"], df["Sum of Achieved"], label="Achieved")

plt.title("Department Target vs Achieved")
plt.xlabel("Department")
plt.ylabel("Amount")
plt.legend()
plt.savefig("department_target_vs_achieved.png")
# plt.show()


print("\nFinal Department Summary:")
print(df[["Row Labels", "Sum of Target", "Sum of Achieved", "Gap", "Achievement_Percentage"]])