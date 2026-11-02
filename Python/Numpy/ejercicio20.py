import numpy as np

# Tienes un conjunto de datos que contiene información demográfica de varias personas, 
# incluyendo edad, ingresos anuales, y nivel de educación. El objetivo es realizar un análisis y encontrar patrones significativos entre estas variables.

np.random.seed(3)
ages = np.random.randint(18, 70, size=200)
income = np.random.normal(50000, 15000, size=200)
education_years = np.random.randint(0, 20, size=200)

correlacion = np.corrcoef(education_years, income)
print("Correlacion:", correlacion[0, 1])

grupo1 = income[(ages >= 18) & (ages <= 30)]
grupo2 = income[(ages >= 31) & (ages <= 45)]
grupo3 = income[(ages >= 46) & (ages <= 60)]
grupo4 = income[ages >= 61]
print("18-30:", grupo1.mean())
print("31-45:", grupo2.mean())
print("46-60:", grupo3.mean())
print("61+:", grupo4.mean())

p90 = np.percentile(income, 90)
print("Percentil 90:", p90)
print("Personas por encima:", len(income[income > p90]))

for anyos in np.unique(education_years):
    print(anyos, "años:", income[education_years == anyos].mean())
