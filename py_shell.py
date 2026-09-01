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
    print("  pwd - показать текущую директорию")
    return 0

def execute_pwd(args):
    print(os.getcwd())  # current working directory
    return 0

COMMANDS = {
    "echo": execute_echo,
    "help": execute_help,
    "pwd": execute_pwd
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