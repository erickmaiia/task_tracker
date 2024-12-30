import shlex
from task_cli import TaskCLI

def main():
    cli = TaskCLI()

    while True:
        # Lê o comando completo do usuário
        user_input = input(">>> ").strip()
        if user_input.lower() == "exit":
            print("Exiting Task Manager. Goodbye!")
            exit()

        # Divide o comando em partes, mantendo argumentos entre aspas intactos
        
        try:
            args = shlex.split(user_input)
        except ValueError:
            print("Invalid input format. Please check your quotes and try again.")
            continue

        if not args:
            print("Invalid command. Please try again.")
            continue

        # Processa o comando
        command = args[0].lower()

        try:
            if command == "add" and len(args) >= 2:
                description = " ".join(args[1:])
                cli.add_task(description)
            elif command == "update" and len(args) >= 3:
                task_id = int(args[1])
                description = " ".join(args[2:])
                cli.update_task(task_id, description)
            elif command == "delete" and len(args) == 2:
                task_id = int(args[1])
                cli.delete_task(task_id)
            elif command == "mark-in-progress" and len(args) == 2:
                task_id = int(args[1])
                cli.mark_in_progress(task_id)
            elif command == "mark-done" and len(args) == 2:
                task_id = int(args[1])
                cli.mark_done(task_id)
            elif command == "list":
                status = args[1] if len(args) == 2 else None
                cli.list_tasks(status)
            else:
                print("Invalid command or arguments. Please try again.")
        except ValueError:
            print("Invalid task ID. Please enter a numeric ID.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
