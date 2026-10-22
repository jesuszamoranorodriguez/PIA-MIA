# 2. Escribe compare_means(nums) que reciba una lista de números positivos y 
# devuelva un dict con: media aritmética (mean), media armónica (harmonic_mean), 
# media geométrica (geometric_mean), desviación poblacional (pstdev) 
# y coeficiente de variación (cv = pstdev/mean). 
import statistics

nums = (2,4,6,7,7,7,7,10,100)

def compare_means(nums): 

    return (statistics.mean(nums), statistics.harmonic_mean(nums), statistics.geometric_mean(nums), statistics.pstdev(nums), statistics.pstdev(nums))

print(compare_means(nums))
