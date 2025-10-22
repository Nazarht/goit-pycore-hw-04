from pathlib import Path
import sys
import colorama

colors_iter = [colorama.Fore.GREEN, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.RED, colorama.Fore.MAGENTA, colorama.Fore.CYAN]

def get_color(level: int) -> str:
    return colors_iter[level % len(colors_iter)]

def list_structure(path: str, level: int = 1) -> None:
    path_obj = Path(path)
    files = list(path_obj.iterdir())
    file_separator = ' ' * (level * 2 + 1)
    folder_separator = '-' * (level * 2 + 1)
    
    if level == 1:
        print(f"{get_color(level)}{'-' * (level * 2)}{path_obj}/{colorama.Fore.RESET}")
    
    for entry in files:
        if entry.is_file():
            print(f"{get_color(level)}{file_separator}{entry.name}{colorama.Fore.RESET}")
        else:
            print(f"{get_color(level)}{folder_separator}{entry.name}/{colorama.Fore.RESET}")
            list_structure(entry, level + 1)

if __name__ == "__main__":
    path = sys.argv[1]
    list_structure(path)