A terminal-based Python program built in VS Code to compute linear (straight-line) and dégressif (declining balance) depreciation schedules, adhering to Moroccan accounting logic.

File Structure & Logic
main.py: The main terminal entry point to run the program.

linear/: Module containing specific logic and formulas for straight-line calculations.

degressif/: Module containing specific logic and formulas for declining balance calculations.

common/: Shared helper functions called across both calculation modes to keep code DRY (Don't Repeat Yourself).

How to Run
Open your terminal in VS Code inside the project directory.

Install the required dependencies:

Bash
pip install pandas openpyxl
Execute the program:

Bash
python main.py
