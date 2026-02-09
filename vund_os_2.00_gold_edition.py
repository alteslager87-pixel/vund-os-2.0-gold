import os
import time
import sys
import shutil

class VundKernel2:
    def __init__(self):
        self.version = "2.00 GOLD"
        self.user = "Coding God"
        self.is_running = True
        self.root = os.path.abspath("VUND_SYSTEM_ROOT")
        self.apps_dir = os.path.join(self.root, "apps")
        
        # Створюємо корінь системи
        for p in [self.root, self.apps_dir]:
            os.makedirs(p, exist_ok=True)

    def clear_screen(self):
        # Очищуємо консоль повністю
        os.system('cls' if os.name == 'nt' else 'clear')
        # Для онлайн-компіляторів та терміналів
        print("\033[H\033[J", end="")

    def print_logo(self):
        w = 80
        logo = [
            "__      __ _    _  _   _  _____  ",
            "\\ \\    / /| |  | || \\ | ||  __ \\ ",
            " \\ \\  / / | |  | ||  \\| || |  | |",
            "  \\ \\/ /  | |  | || . ` || |  | |",
            "   \\  /   | |__| || |\\  || |__| |",
            "    \\/     \\____/ |_| \\_||_____/ ",
            "         SYSTEM v2.00 GOLD       "
        ]
        for line in logo:
            print(line.center(w))

    def boot_animation(self):
        w = 80
        for i in range(17):
            self.clear_screen()
            print("\n" * 2 + ("-" * 40).center(w))
            self.print_logo()
            bar = "█" * i + "░" * (16 - i)
            percent = int((i / 16) * 100)
            sys.stdout.write(f"\r{'[' + bar + '] ' + str(percent) + '%' : ^80}")
            sys.stdout.flush()
            time.sleep(0.07)
        print("\n\n" + "[ SYSTEM READY ]".center(w))
        time.sleep(0.7) # Даємо 0.7 сек насолодитися успіхом

    def run(self):
        self.boot_animation()
        
        # ОСЬ ВОНО: Очищення «ПО СТАРИНЦІ» ;)
        self.clear_screen() 
        
        self.print_logo()
        print(f"\nWelcome back, {self.user}. System is stable.")
        print("Type 'help' to explore the Gold Edition.\n")

        while self.is_running:
            try:
                cmd = input(f"{self.user}@vund-gold > ").lower().strip()
                if not cmd: continue

                if cmd == "exit":
                    print("Shutdown initiated...")
                    self.is_running = False
                elif cmd == "clear":
                    self.clear_screen()
                elif cmd == "help":
                    print("\nCommands: ls, tree, delete, createfolder, createimage, install, system_info, logo, clear, exit")
                elif cmd == "system_info":
                    print(f"\nVUND-OS {self.version} | Operator: {self.user}")
                    print(f"Filesystem: {self.root}")
                elif cmd == "ls":
                    for item in os.listdir(self.root):
                        tag = "📂" if os.path.isdir(os.path.join(self.root, item)) else "📄"
                        print(f" {tag} {item}")
                elif cmd == "createfolder":
                    f_name = input("Folder name: ").strip()
                    os.makedirs(os.path.join(self.root, f_name), exist_ok=True)
                    print(f"[ OK ]: Folder '{f_name}' created.")
                elif cmd == "logo":
                    self.print_logo()
                else:
                    print(f"Unknown command: {cmd}")
            except Exception as e:
                print(f"Kernel Error: {e}")

if __name__ == "__main__":
    VundKernel2().run()
