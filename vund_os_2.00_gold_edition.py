import os
import time
import sys
import shutil

class VundKernel2:
    def __init__(self):
        self.version = "2.00 GOLD"
        self.user = "Coding God"  # Твій незмінний статус [cite: 2026-02-07]
        self.is_running = True
        self.root = os.path.abspath("VUND_SYSTEM_ROOT")
        self.apps_dir = os.path.join(self.root, "apps")
        
        # Автоматичне створення структури при старті
        try:
            for p in [self.root, self.apps_dir]:
                if not os.path.exists(p):
                    os.makedirs(p, exist_ok=True)
        except Exception as e:
            print(f"CRITICAL ERROR: Could not initialize filesystem: {e}")

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
        print("\n")
        for line in logo:
            print(line.center(w))
        print("\n")

    def boot_animation(self):
        w = 80
        for i in range(17):
            os.system('cls' if os.name == 'nt' else 'clear')
            bg = "-" * 40
            print("\n" * 2 + bg.center(w))
            self.print_logo()
            bar = "█" * i + "░" * (16 - i)
            percent = int((i / 16) * 100)
            sys.stdout.write(f"\r{'[' + bar + '] ' + str(percent) + '%' : ^80}")
            sys.stdout.flush()
            time.sleep(0.08)
        print("\n\n" + "[ SYSTEM READY ]".center(w))
        time.sleep(0.5)

    def cmd_ls(self):
        print("\n--- Directory Content ---")
        try:
            items = os.listdir(self.root)
            if not items:
                print("[ Empty ]")
            for item in items:
                path = os.path.join(self.root, item)
                tag = "📂" if os.path.isdir(path) else "📄"
                print(f" {tag} {item}")
        except Exception as e:
            print(f"[ ERR ]: {e}")

    def cmd_delete(self):
        target = input("Name of file/folder to delete: ").strip()
        path = os.path.join(self.root, target)
        if os.path.exists(path):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"[ OK ]: Directory '{target}' removed.")
                else:
                    os.remove(path)
                    print(f"[ OK ]: File '{target}' removed.")
            except Exception as e:
                print(f"[ ERR ]: Cannot delete: {e}")
        else:
            print("[ ERR ]: Object not found.")

    def cmd_system_info(self):
        print("\n" + "═"*35)
        print(f" VUND-OS VERSION : {self.version}")
        print(f" OPERATOR        : {self.user}")
        print(f" ROOT DIRECTORY  : {self.root}")
        print(f" KEYBOARD MODE   : MECHANICAL [cite: 2026-02-08]")
        print(f" NEXT GOAL       : NT KERNEL GUI [cite: 2026-02-08]")
        print("═"*35)

    def cmd_tree(self):
        print(f"\nSTRUCTURE OF {self.root}:")
        for root, dirs, files in os.walk(self.root):
            level = root.replace(self.root, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}📂 {os.path.basename(root) or 'ROOT'}/")
            for f in files:
                print(f"{indent}    📄 {f}")

    def cmd_createimage(self):
        name = input("Image name (e.g. house.img): ").strip()
        print("Draw your ASCII (type 'END' on a new line to save):")
        buffer = []
        while True:
            line = input()
            if line.strip().upper() == 'END': break
            buffer.append(line)
        try:
            with open(os.path.join(self.root, name), "w", encoding="utf-8") as f:
                f.write("\n".join(buffer))
            print(f"[ OK ]: Image '{name}' saved to disk.")
        except Exception as e:
            print(f"[ ERR ]: {e}")

    def cmd_install(self):
        app = input("App name to install: ").strip()
        print(f"Downloading {app}...")
        time.sleep(1.0)
        path = os.path.join(self.apps_dir, f"{app}.vapp")
        try:
            with open(path, "w") as f:
                f.write(f"# VundApp: {app}\n# Status: Installed\n# Created for: {self.user}")
            print(f"[ OK ]: {app} installed in /apps.")
        except Exception as e:
            print(f"[ ERR ]: {e}")

    def run(self):
        self.boot_animation()
        while self.is_running:
            try:
                # Введення команди оптимізовано під механічну клавіатуру [cite: 2026-02-08]
                cmd_input = input(f"\n{self.user}@vund-gold > ").lower().strip()
                
                if not cmd_input:
                    continue
                
                if cmd_input == "exit":
                    print("Shutting down Vund OS...")
                    self.is_running = False
                elif cmd_input == "help":
                    print("\n[ COMMAND LIST ]")
                    print("Basic: ls, delete, createfolder, exit")
                    print("Gold: tree, system_info, logo, install, createimage")
                elif cmd_input == "ls": self.cmd_ls()
                elif cmd_input == "delete": self.cmd_delete()
                elif cmd_input == "tree": self.cmd_tree()
                elif cmd_input == "system_info": self.cmd_system_info()
                elif cmd_input == "logo": self.print_logo()
                elif cmd_input == "createimage": self.cmd_createimage()
                elif cmd_input == "install": self.cmd_install()
                elif cmd_input == "createfolder":
                    folder = input("Folder name: ").strip()
                    os.makedirs(os.path.join(self.root, folder), exist_ok=True)
                    print(f"[ OK ]: Folder '{folder}' created.")
                else:
                    print(f"[ Unknown ]: {cmd_input}. Type 'help' for info.")
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")
            except Exception as e:
                print(f"\n[ KERNEL PANIC ]: {e}")

if __name__ == "__main__":
    VundKernel2().run()
