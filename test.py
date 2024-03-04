import numpy as np

# Предположим, что у нас есть следующая выборка значений
values = [0.007, 0.008, 0.009, 0.015, 0.007, 0.009, 0.007, 0.007]


# Среднее значение (mean) выборки
mean_sample = np.mean(values)

# Стандартное отклонение (std_dev) выборки
std_dev_sample = np.std(values, ddof=1)

# Размер выборки (n)
size_sample = len(values)

# Предполагаемое среднее значение генеральной совокупности (mu)
mu_population = 0.007  # Здесь должно быть ваше реальное предполагаемое значение

# Вычисляем t-статистику (t_score)
t_score = (mean_sample - mu_population) / (std_dev_sample / np.sqrt(size_sample))

# Выводим полученное значение t-статистики
print('t = ' +str(t_score))


e = 72*(10**9) # коэффициент юнга из госта по оптоволокну
s = 3.14159265358979 *(125*10**-6)**2 # площадь сечения оптоволокна

l = 0.1 # длина оптоволокна

k = s*e/l
print('k = ' +str(k))
ld = 0.007 # удлинение оптоволокна
f = k*ld
print('f = ' +str(f))
f = e*s*ld/l
print('f = ' +str(f))
p = f/s
print('p = ' +str(p))
