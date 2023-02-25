"""
Додайте до попередньої програми код, будь-якого алгоритму сортування.
Додайте функцію, яка б обраховувала середній час роботи алгоритму сортування.
Функція повинна приймати список і кількість ітерацій циклів сортування, а повертати
середній час роботи алгоритму сортування.
"""
import time

def bubble_sort_run_time(my_list):
    cur_time = time.time()
    for run in range(len(my_list)-1):
        for i in range(len(my_list)-1-run):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i +1] = my_list[i + 1], my_list[i]
    print(my_list)
    print(f"Duration time: {time.time() - cur_time}")









