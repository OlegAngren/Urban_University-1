grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список
students_list = sorted(students)

# Создаем пустой словарь для хранения имен и средних баллов
average_grades = {}

# Проходимся по каждому студенту и его оценкам
for i in range(len(students_list)):
    student = students_list[i]
    grades_list = grades[i]
    # Вычисляем средний балл
    average_grade = sum(grades_list) / len(grades_list)
    # Добавляем данные в словарь
    average_grades[student] = average_grade

# Выводим результат
print(average_grades)