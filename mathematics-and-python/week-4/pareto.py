import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt

from IPython.display import display, Markdown
from scipy.stats import pareto

display(Markdown('# Распределение Парето'))
b = 3.14
pareto_rv = sts.pareto(b)
display(Markdown(f"## Коэффицент распеределения b={b}"))
_, ax = plt.subplots(1, 1)

# Генерирует числа для графика
x = np.linspace(pareto_rv.ppf(0.01),
                pareto_rv.ppf(0.99), 100)

# Рисуем функцию плотности для нашего распределения
ax.plot(x, pareto_rv.pdf(x), 'r-', lw=3, alpha=0.6, label='Pareto pdf')

# Делаем выборку 1000 значений по нашей фукнции
r = pareto_rv.rvs(1000)

# Рисуем гистограмму
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

def build_vars(n, size):
  return [calculate_E(pareto_rv.rvs(n)) for _ in range(size)]

def calculate_E(vars):
  return np.sum(vars) / np.size(vars)

def plot_gist(n, size, plt):
  _, ax = plt.subplots(1, 1)
  ax.hist(build_vars(n, size), normed=True, histtype='stepfilled', alpha=0.2, label=f"n={n}")
  ax.legend(loc='best', frameon=False)

for n in [5, 10, 50]:
  plot_gist(n, 1000, plt)
plt.show()
