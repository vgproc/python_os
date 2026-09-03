import os
import sys

def parse_command(command):
    # Разбивает строку команды на аргументы
    parts = command.split()
    if not parts:
        return "", []
    cmd = parts[0]
    args = parts[1:]
    return cmd, args

def execute_echo(args):
    print(" ".join(args))
    return 0  # код успеха

def execute_help(args):
    print("Доступные команды:")
    print("  echo [текст] - вывести текст")
    print("  help - показать справку")
    print("  exit - выйти из shell")
    print("  pwd - показать текущую папку")
    print("  ls - список содержимого папки")
    print("  cd - сменить текущую папку")
    print("  mkdir - создать папку")
    print("  rmdir - удалить папку")
    return 0

def execute_pwd(args):
    print(os.getcwd())  # current working directory
    return 0

def execute_ls(args):
    path = args[0] if args else "."
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
        return 0
    except FileNotFoundError:
        print(f"Папка не найдена: {path}")
        return 1

def execute_cd(args):
    if not args:
        path = os.path.expanduser("~")  # домашняя папка
    else:
        path = args[0]
    try:
        os.chdir(path)
        return 0
    except FileNotFoundError:
        print(f"Папка не найдена: {path}")
        return 1

def execute_mkdir(args):
    if not args:
        print("Ошибка: укажите имя папки")
        return 1
    try:
        os.mkdir(args[0])
        return 0
    except FileExistsError:
        print(f"Папка уже существует: {args[0]}")
        return 1

def execute_rmdir(args):
    if not args:
        print("Ошибка: укажите имя папки")
        return 1
    try:
        os.rmdir(args[0])
        return 0
    except FileNotFoundError:
        print(f"Папка не существует: {args[0]}")
        return 1

COMMANDS = {
    "echo": execute_echo,
    "help": execute_help,
    "pwd": execute_pwd,
    "ls": execute_ls,
    "cd": execute_cd,
    "mkdir": execute_mkdir,
    "rmdir": execute_rmdir
}

def main():
    print("Wellcome to MyShell!")
    print("Enter 'exit' for quit")
    while True:
        command = input("my-shell> ").strip()
        if not command:
            continue
            
        cmd, args = parse_command(command)
        
        if cmd == "exit":
            print("By!")
            break
        elif cmd in COMMANDS:
            COMMANDS[cmd](args)
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()