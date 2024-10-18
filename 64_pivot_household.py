import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/data_venta_verduras.xlsx',sheet_name='Sheet1')

pt = pd.pivot_table(df, index='Country',
                    values='Amount', 
                    columns='Product', aggfunc='mean',
                    fill_value=0).round(2)



pt.plot.bar(figsize=(12,6))
plt.title('Promedio de productos por país')
plt.xticks(rotation=0)
plt.ylabel('Valor promedio')
plt.grid(alpha=0.2)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()



pt.plot.box(figsize=(12,6))
plt.title('Gráfico de caja de productos')
plt.xticks(rotation=0)
plt.ylabel('Variación de precios')
plt.grid(alpha=0.2)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


