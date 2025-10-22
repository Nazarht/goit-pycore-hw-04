def total_salary(path: str) -> tuple[int, float]:
    total = 0
    try:
        with open(path, 'r') as file:
            file_lines = file.readlines()
            lines_count = len(file_lines)
            
            for line in file_lines:
                try:
                    name, salary = line.strip().split(',')
                except Exception as e:
                    print(f"Invalid data in line: {line}: {e}")
                    continue
                
                total += int(salary)
                
        return total , round(total / lines_count, 2)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except ValueError:
        print(f"Invalid data in file: {path}")
        return 0, 0

def get_cats_info(path: str) -> list[dict[str, str | int]]:
    cats_info_list = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                lines_list = line.strip().split(',')
                try:
                    id, name, age = lines_list
                except Exception as e:
                    print(f"Invalid data in line: {line}: {e}")
                    continue
                
                cats_info_list.append({
                    'id': id,
                    'name': name,
                    'age': int(age)
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