 from datatime import datetime, date 

def get_days_from_today(date):
  try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
    
    today = date.today()
    delta = today - target_date
    return delta.days

def get_numbers_ticket(min_num, max_num, quantity):

 if not (1 <= min_num <= max_num <= 1000):
        return []
    if not (min_num <= quantity <= max_num - min_num + 1):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        num = random.randint(min_num, max_num)
        numbers.add(num)
    
    return sorted(numbers)

def normalize_phone(phone_number):
    """
    Нормалізує номер телефону, залишаючи лише цифри та '+' на початку.
    Якщо відсутній міжнародний код, додає код '+38'.
    """
    # Видаляємо все, крім цифр і плюса
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    
    if phone_number.startswith("+"):
        
        if not phone_number.startswith("+380"):
           
            pass
        return phone_number
    
    
    if phone_number.startswith("380"):
        return "+" + phone_number
    
    
    return "+38" + phone_number


if name == "main":
    
    print("Кількість днів від 2021-10-09 до сьогодні:", get_days_from_today("2021-10-09"))
    
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
 
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)