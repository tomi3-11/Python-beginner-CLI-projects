import os
import subprocess
import shlex

def run_shell():
    """It runs the shell."""
    while True:
        cwd = os.getcwd()
        command = input(f"{cwd}$ ")

        if not command.strip():
            continue

        # Tokenize input
        args = shlex.split(command)

        if args[0] == "exit":
            break
        elif args[0] == "cd":
            if len(args) > 1:
                try:
                    os.chdir(args[1])
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {args[1]}")
            else:
                print("cd: expected argument")
        elif args[0] == "pwd":
            print(os.getcwd())
        else:
            try:
                # Run external command
                subprocess.run(args)
            except FileNotFoundError:
                print(f"{args[0]}: command not found")

print("Welcome to Python Mini Shell! Type 'exit' to quit.")
run_shell()
