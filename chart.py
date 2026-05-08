import csv
import numpy as np
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

projected_years = list(range(2030, 2041))

trad_coeffs = np.polyfit(traditional_years, traditional_salaries, 3)
ai_coeffs = np.polyfit(ai_years, ai_salaries, 3)

trad_projected = np.polyval(trad_coeffs, projected_years)
ai_projected = np.polyval(ai_coeffs, projected_years)

plt.figure(figsize=(12, 6))

trad_line, = plt.plot(traditional_years, traditional_salaries, marker="o", label="Traditional (actual)")
ai_line, = plt.plot(ai_years, ai_salaries, marker="s", label="AI-Skilled (actual)")

plt.plot(projected_years, trad_projected, linestyle="--", color=trad_line.get_color(),
         marker="o", markersize=4, alpha=0.7, label="Traditional (projected)")
plt.plot(projected_years, ai_projected, linestyle="--", color=ai_line.get_color(),
         marker="s", markersize=4, alpha=0.7, label="AI-Skilled (projected)")

plt.axvline(x=2030, color="gray", linestyle=":", alpha=0.7, label="Projection starts")

plt.title("Neuroscience Researcher Salaries: Traditional vs AI-Skilled (Projected to 2040)")
plt.xlabel("Year")
plt.ylabel("Monthly Salary (EUR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("salaries_chart.png", dpi=150)
print("Chart saved to salaries_chart.png")
plt.show()
