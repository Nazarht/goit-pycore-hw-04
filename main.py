def total_salary(path: str) -> tuple[float, float]:
    total: float = 0.0
    try:
        with open(path, 'r') as file:
            file_lines = file.readlines()

        lines_count = len(file_lines)
        if lines_count == 0:
            return 0.0, 0.0

        for line in file_lines:
            try:
                name, salary = line.strip().split(',')
                total += float(salary)
            except Exception as e:
                print(f"Invalid data in line: {line}: {e}")
                continue

        return total, round(total / lines_count, 2) if lines_count else (0.0, 0.0)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0.0, 0.0
    except ValueError:
        print(f"Invalid data in file: {path}")
        return 0.0, 0.0

def get_cats_info(path: str) -> list[dict[str, str]]:
    cats_info_list: list[dict[str, str]] = []
    try:
        with open(path, 'r') as file:
            file_lines = file.readlines()

        for line in file_lines:
            lines_list = line.strip().split(',')
            try:
                id, name, age = lines_list
            except Exception as e:
                print(f"Invalid data in line: {line}: {e}")
                continue

            cats_info_list.append({
                'id': id,
                'name': name,
                'age': age
            })

        return cats_info_list
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except ValueError:
        print(f"Invalid data in file: {path}")
        return []

total, average = total_salary('data/salary.txt')
print(f"Total salary: {total}")
print(f"Average salary: {average}")

cats_info = get_cats_info('data/cats.txt')
print(cats_info)