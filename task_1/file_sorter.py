import shutil
from pathlib import Path
import argparse
import os

def sort_files_by_extension(src_path, dest_path):
    """Рекурсивно копіює файли з вихідної директорії до нової та сортує за розширенням."""
    for item in src_path.iterdir():
        if item.is_dir():
            # Рекурсивний виклик для директорій
            sort_files_by_extension(item, dest_path)
        elif item.is_file():
            # Отримання розширення файлу без крапки
            ext = item.suffix[1:] if item.suffix else "no_extension"
            dest_folder = dest_path / ext
            dest_folder.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(item, dest_folder / item.name)
                print(f"Файл {item} скопійовано в {dest_folder / item.name}")
            except Exception as e:
                print(f"Помилка при копіюванні файлу {item}: {e}")

def main(source_dir, dest_dir):
    """Основна функція для налаштування шляхів і виклику функції сортування файлів."""
    src_path = Path(source_dir)
    dest_path = Path(dest_dir)
    
    if not src_path.exists():
        print(f"Вихідна директорія {source_dir} не існує.")
        return
    
    if not dest_path.exists():
        try:
            dest_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Помилка при створенні директорії {dest_dir}: {e}")
            return
    
    try:
        sort_files_by_extension(src_path, dest_path)
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіює та сортує файли за розширенням.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    args = parser.parse_args()
    
    main(args.source, args.destination)
