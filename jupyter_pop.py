import matplotlib.pyplot as plt
godine = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029"]
populacija = 1420062022
pdg = []
pdg.append(populacija)
for  i in range(10):
    populacija += populacija/100*0.35
    pdg.append(populacija)
plt.plot(godine, pdg)
plt.ylabel("populacija u milijardama")
plt.xlabel("godine")

plt.title("Populacija U kini")
plt.show()
