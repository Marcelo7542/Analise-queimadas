# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vCvOIufemWcBEE5jFp0b1hvM05_Kzcm4
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

BaseDados = pd.read_csv('Dados_queimadas.csv', encoding='latin-1')

queimadas = BaseDados.groupby(by=['year', 'month']).sum().reset_index()

plt.figure(figsize=(14,5))
sns.boxplot(data=queimadas, x='month', y='number',
            order=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
plt.title("Gráfico de queimadas no Brasil por mês")
plt.xlabel("Quantidade de queimadas")
plt.ylabel("Período")

plt.show()