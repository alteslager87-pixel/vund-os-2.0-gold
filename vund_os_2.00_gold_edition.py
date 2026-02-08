import os
import time
import sys

class VundKernel2:
    def __init__(self):
        self.version = "2.00 GOLD"
        self.user = "Coding God"
        self.is_running = True
        self.root = os.path.join(os.getcwd(), "VUND_SYSTEM_ROOT")
        self.apps_dir = os.path.join(self.root, "apps")
        
        # Ініціалізація структури
        for p in [self.root, self.apps_dir]:
            os.makedirs(p, exist_ok=True)

    def print_logo(self):
        w = 80
        logo = [
            "__      __ _    _  _   _  _____  ",
            "\\ \\    / /| |  | || \\ | ||  __ \\ ",
            " \\ \\  / / | |  | ||  \\| || |  | |",
            "  \\ \\/ /  | |  | || . ` || |  | |",
            "   \\  /   | |__| || |\\  || |__| |",
            "    \\/     \____/ |_| \_||_____/ ",
            "         SYSTEM v2.00 GOLD       "
        ]
        print("\n")
        for line in logo:
            print(line.center(w))
        print("\n")

    def boot_animation(self):
        w = 80
        for i in range(16):
            os.system('cls' if os.name == 'nt' else 'clear')
            bg = " " * (i % 10) + "----------------------------------------"
            print("\n" * 2 + bg.center(w))
            self.print_logo()
            bar = "█" * i + "░" * (15 - i)
            sys.stdout.write(f"\r{'[' + bar + '] ' + str(int(i*6.6)) + '%' : ^80}")
            sys.stdout.flush()
            time.sleep(0.05)
        print("\n\n" + "[ SYSTEM READY ]".center(w))
        time.sleep(0.5)

    # --- ПОКРАЩЕНІ КОМАНДИ 1.XX ---
    
    def cmd_ls(self):
        print(f"\n--- Directory Content ---")
        items = os.listdir(self.root)
        if not items:
            print("[ Empty ]")
        for item in items:
            path = os.path.join(self.root, item)
            tag = "📂" if os.path.isdir(path) else "📄"
            print(f" {tag} {item}")

    def cmd_delete(self):
        target = input("Name of file/folder to delete: ")
        path = os.path.join(self.root, target)
        if os.path.exists(path):
            if os.path.isdir(path):
                import shutil
                shutil.rmtree(path)
                print(f"[ OK ]: Directory '{target}' and its content removed.")
            else:
                os.remove(path)
                print(f"[ OK ]: File '{target}' removed.")
        else:
            print("[ ERR ]: Object not found.")

    # --- НОВІ КОМАНДИ 2.00 GOLD ---

    def cmd_system_info(self):
        print(f"\n" + "═"*30)
        print(f" VUND-OS VERSION: {self.version}")
        print(f" OPERATOR: {self.user}")
        print(f" ROOT: {self.root}")
        print(f" FILESYSTEM: Hierarchical ANSI")
        print("═"*30)

    def cmd_tree(self):
        print(f"\nSTRUCTURE OF {self.root}:")
        for root, dirs, files in os.walk(self.root):
            level = root.replace(self.root, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}📂 {os.path.basename(root) or 'ROOT'}/")
            for f in files:
                print(f"{indent}    📄 {f}")

    def cmd_createimage(self):
        name = input("Image name (e.g. car.img): ")
        print("Draw your ASCII (type 'END' to save):")
        buffer = []
        while True:
            line = input()
            if line.upper() == 'END': break
            buffer.append(line)
        with open(os.path.join(self.root, name), "w", encoding="utf-8") as f:
            f.write("\n".join(buffer))
        print(f"[ OK ]: Image '{name}' saved to disk.")

    def cmd_install(self):
        app = input("App name to install: ")
        print(f"Downloading {app}...")
        time.sleep(1.5)
        path = os.path.join(self.apps_dir, f"{app}.vapp")
        with open(path, "w") as f:
            f.write(f"# VundApp: {app}\n# Status: Installed")
        print(f"[ OK ]: {app} is now in /apps and ready to use.")

    def run(self):
        self.boot_animation()
        
        while self.is_running:
            cmd = input(f"\n{self.user}@vund-gold > ").lower().strip()
            
            if cmd == "exit": self.is_running = False
            elif cmd == "help":
                print("\n1.xx Enhanced: ls, delete, create (use createfolder)")
                print("2.xx Gold: tree, system_info, logo, install, createimage, createfolder, exit")
            elif cmd == "ls": self.cmd_ls()
            elif cmd == "delete": self.cmd_delete()
            elif cmd == "tree": self.cmd_tree()
            elif cmd == "system_info": self.cmd_system_info()
            elif cmd == "logo": self.print_logo()
            elif cmd == "createimage": self.cmd_createimage()
            elif cmd == "install": self.cmd_install()
            elif cmd == "createfolder":
                folder = input("Folder path: ")
                os.makedirs(os.path.join(self.root, folder), exist_ok=True)
                print("[ OK ]: Created.")
            elif cmd == "": continue
            else: print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    VundKernel2().run()