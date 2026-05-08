import csv
import matplotlib.pyplot as plt

with open("salaries.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

traditional_years = []
traditional_salaries = []
ai_years = []
ai_salaries = []

for row in rows:
    year = int(row["year"])
    salary = int(row["monthly_salary_eur"])
    if row["researcher_type"] == "traditional":
        traditional_years.append(year)
        traditional_salaries.append(salary)
    else:
        ai_years.append(year)
        ai_salaries.append(salary)

plt.figure(figsize=(10, 6))
plt.plot(traditional_years, traditional_salaries, marker="o", label="Traditional")
plt.plot(ai_years, ai_salaries, marker="s", label="AI-Skilled")

plt.title("Neuroscience Researcher Salaries: Traditional vs AI-Skilled")
plt.xlabel("Year")
plt.ylabel("Monthly Salary (EUR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("salaries_chart.png", dpi=150)
print("Chart saved to salaries_chart.png")
plt.show()
