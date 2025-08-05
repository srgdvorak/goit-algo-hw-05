def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # перевірка, що рядок не порожній
                    try:
                        name, salary_str = line.split(',')
                        salary = float(salary_str)
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Пропущено рядок з помилкою формату: {line}")
        
        if count == 0:
            return (0, 0)
        average = total / count
        return (total, average)
    
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)