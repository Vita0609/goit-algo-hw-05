import sys
from collections import defaultdict

# Парсинг рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    log_data = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3] if len(parts) > 3 else ""
    }
    return log_data

# Завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    return logs

# Фільтрація логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]

# Підрахунок кількості логів за рівнями
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts

# Виведення статистики про логи
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level:<15} | {count}")

# Головна функція
def main():
    if len(sys.argv) < 2:
        print("Error: You must provide the log file path.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    
    display_log_counts(counts)
    
    # Якщо зазначено фільтр за рівнем
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nНемає записів для рівня '{level_filter.upper()}'.")
    
if __name__ == "__main__":
    main()
