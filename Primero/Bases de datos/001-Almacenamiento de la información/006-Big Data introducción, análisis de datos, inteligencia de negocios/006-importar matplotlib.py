import matplotlib.pyplot as plt

etiquetas = ['Category A', 'Category B', 'Category C']
datos = [30, 45, 25]

plt.pie(datos, labels=etiquetas)

plt.savefig('grafica.png')

plt.close()
