import csv
from rich.console import Console
from rich.table import Table

with open("salaries.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

table = Table(title="Neuroscience Researcher Salaries")
table.add_column("Year", justify="center")
table.add_column("Researcher Type", justify="left")
table.add_column("Monthly Salary (EUR)", justify="right")

for row in rows:
    salary = f"{int(row['monthly_salary_eur']):,}"
    table.add_row(row["year"], row["researcher_type"], salary)

Console().print(table)

# A change!