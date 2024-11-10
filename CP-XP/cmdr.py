import code
import os
import winsound
import sys

def loadf(file):
    file_path = os.path.join("C:\\CP-XP\\drv", file)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                content = f.read()
                print("")
                exec(content, globals())
            print("")
            print("Ready.")
        except SyntaxError as e:
            print("?Syntax  Error")
        except Exception as e:
            print("?Syntax  Error")
    else:
        print("File not found.")

def load(file):
    file_path = os.path.join("", file)
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                content = f.read()
                print("")
                exec(content, globals())
            print("")
            print("Ready.")
        except SyntaxError as e:
            print("?Syntax  Error")
        except Exception as e:
            print("?Syntax  Error")
    else:
        print("File not found.")

def beep(freq, dur):
    winsound.Beep(int(freq), int(dur))
    print("")
    print("Ready.")

def color(num):
    if num == "1":
        os.system("color 01")
    elif num == "2":
        os.system("color 02")
    elif num == "3":
        os.system("color 03")
    elif num == "4":
        os.system("color 04")
    elif num == "5":
        os.system("color 05")
    elif num == "6":
        os.system("color 06")
    elif num == "7":
        os.system("color 07")
    elif num == "8":
        os.system("color 08")
    elif num == "cmdinp\\[/?\\]":
        os.system("color /?")
    elif num == "":
        os.system("color 07")
    else:
        print("?Syntax  Error")
    print("")
    print("Ready.")

def ver(inp):
    if inp == "":
        print(" C O M M O D O R E   P  Y T H O  N  | Python")
        print("███   ███ ████████  ███████████████ | Commodore")
        print(" ███ ███  ██     ██ █████████████   | Emulator")
        print("   ███    ██ █████  ███████████     | version")
        print(" ███ ███  ██        █████████       | 2.03 OSR 2")
    elif inp == "OSR":
        print("OSR 2")
    elif inp == "XPV":
        print("2.03")
    else:
        print("?Syntax Error")
    print("")
    print("Ready.")

custom_commands = {
    "loadf": loadf,
    "load": load,
    "beep": lambda args: beep(*args.split(',')),
    "color": color,
    "ver": ver,
}

def execute_custom_command(command):
    if "(" in command and ")" in command:
        command_name, args = command.split("(", 1)
        args = args.rstrip(")").strip().strip('"')
        if command_name in custom_commands:
            custom_commands[command_name](args)
            return True
    return False

def main():
    print("Ready.")

    while True:
        try:
            command = input("").strip()
            
            if command in ("exit()", "quit()"):
                quit()
            if command in ("res()", "restart()"):
                os.system("\"C:\\CP-XP\\boot.py\"")

            custom_command_executed = execute_custom_command(command)

            if not custom_command_executed:
                exec(command)

            if not custom_command_executed:
                if command == "":
                    os.system("")
                else:
                    print("")
                    print("Ready.")

        except (SyntaxError, NameError):
            print("?Syntax  Error")
            print("")
            print("Ready.")
        except (KeyboardInterrupt, EOFError):
            print("?Syntax  Error")
            break

if __name__ == "__main__":
    main()
