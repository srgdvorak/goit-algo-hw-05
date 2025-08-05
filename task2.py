def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # перевірка, що рядок не порожній
                    try:
                        cat_id, name, age = line.split(',')
                        cats.append({
                            "id": cat_id,
                            "name": name,
                            "age": age
                        })
                    except ValueError:
                        print(f"Пропущено рядок з помилкою формату: {line}")
        return cats

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []