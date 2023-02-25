"""
Створіть три списки: int_list, float_list і str_list. Користуючись пакетами
рандомізації, заповніть словник int_list випадковими цілочисельними значеннями,
у кількості 5000 елементів, в діапазоні від 0 до 1000. Заповніть словник float_list
випадковими значеннями, у кількості 5000 елементів, в діапазоні від 0.1 до 100.0.
Також заповніть словник str_list випадковими словами, теж у кількості 5000 елементів.
"""
import random
from random_words import RandomWords
from Task2 import bubble_sort_run_time

int_list = []
float_list = []
str_list = []
w = RandomWords()

# Заповнюємо int_list випадковими цілочисельними значеннями
for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
print(int_list)

# Заповнюємо float_list випадковими цілочисельними значеннями
for i in range(0, 5000):
    float_list.append(random.uniform(0.1, 100.0))
print(float_list)

# Заповнюємо словник str_list випадковими словами
for i in range(0, 5000):
    str_list.append(w.random_word())
print(str_list)
print()


bubble_sort_run_time(str_list)
bubble_sort_run_time(float_list)
bubble_sort_run_time(int_list)

