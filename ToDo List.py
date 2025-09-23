

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
        elif choice == "2":
            task = input("New Task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "3":
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            num = int(input("Remove which number? "))
            if 1 <= num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
