NOTICE: This ONLY supports Windows right now; it will support macOS in the future.

Move CP-XP to the root of your C: drive, and open "boot.py" to start. For more information, open "boot.py".

(Recommended: Use the Nouveau IBM font in Python properties.)

Help Index:

    How do you load files?
    What is included with CP-XP?
    Where do I store files to load them?
    What are some helpful commands?

Starting with 1, "How do you load files?" You use loadf(filename) to load a file in the drv folder, which is located in the CP-XP folder. Alternatively, you can use load(filepath) to load a file from its full path on your PC.

Number 2, "What is included with CP-XP?" Currently, only the drv folder. It includes a Notepad program called "notepad.py," "pydown.py," which downloads a Python file from the internet, allowing you to load it afterward, and a Tic-Tac-Toe game called "tictactoe.py"—it’s literally just Tic-Tac-Toe.

Number 3, "Where do I store files to load them?" Simply put your Python file(s) in the drv folder, which is in the CP-XP folder, then follow the instructions in Index #1.

Number 4, "What are some helpful commands?" Here’s a quick rundown:

    beep(frequency, duration) — Makes a beep sound. Be careful with the frequency, as an incorrect value may cause errors.
    color(0-8) — 0 applies default colors, and 1 through 8 apply custom colors.
    ver() — Displays version information.