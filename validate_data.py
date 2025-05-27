import pandas as pd
from datetime import datetime

def is_valid_email(email):
    return isinstance(email, str) and "@" in email and "." in email.split("@")[1]

def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    return phone.startswith("+7") and len(phone) == 12 and phone[1:].isdigit()

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

# Путь к файлу
file_path = "exc.xlsx"

# Чтение файла
df = pd.read_excel(file_path)

errors = []

required_columns = ["Имя", "Email", "Телефон", "Дата рождения"]

# Проверка наличия столбцов
for col in required_columns:
    if col not in df.columns:
        errors.append(f"Отсутствует столбец: {col}")

# Проверка строк
for index, row in df.iterrows():
    name = row["Имя"]
    email = row["Email"]
    phone = row["Телефон"]
    birthdate = row["Дата рождения"]

    if pd.isna(name) or name == "":
        errors.append(f"Пустое значение 'Имя' в строке {index + 1}")
    if pd.isna(email) or email == "":
        errors.append(f"Пустое значение 'Email' в строке {index + 1}")
    elif not is_valid_email(email):
        errors.append(f"Неверный формат email '{email}' в строке {index + 1}")

    if pd.isna(phone) or phone == "":
        errors.append(f"Пустое значение 'Телефон' в строке {index + 1}")
    elif not is_valid_phone(str(phone)):
        errors.append(f"Неверный формат телефона '{phone}' в строке {index + 1}")

    if pd.isna(birthdate) or birthdate == "":
        errors.append(f"Пустое значение 'Дата рождения' в строке {index + 1}")
    elif not is_valid_date(str(birthdate)):
        errors.append(f"Неверный формат даты '{birthdate}' в строке {index + 1}")

# Вывод результатов
if errors:
    print("Найдены ошибки:")
    for error in errors:
        print(f"- {error}")
else:
    print("Все данные корректны!")
