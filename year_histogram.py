import json
import matplotlib.pyplot as plt


# Create a histogram of publication years from a bibliography file in 'CLS JSON' format.

with open("bib.json") as f:
    bib = json.load(f)

years = []
for ref in bib:
    if 'issued' in ref:
        issued = ref['issued']
        if 'date-parts' in issued:
            years.append(int(issued['date-parts'][0][0]))

min_year = max(1940, min(years))
max_year = max(years)

fig, ax = plt.subplots()
ax.hist(years, bins=max_year - min_year + 1, range=(min_year, max_year + 1), align='left')
ax.set_xlabel("Year")
ax.set_ylabel("Count")
plt.show()
