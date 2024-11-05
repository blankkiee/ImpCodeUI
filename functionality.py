# functionality.py
from PyQt5.QtWidgets import QTableWidgetItem

# Function to analyze the code
def analyze_code_function(code, result_table, console_edit):
    # Clear the previous results from the table
    result_table.setRowCount(0)

    # Split the code into lines
    lines = code.split('\n')

    # Iterate over each line to tokenize it
    for line_number, line in enumerate(lines, start=1):
        tokens = line.split()  # Split the line into tokens (words)
        for token in tokens:
            # Add a new row for each token
            row_position = result_table.rowCount()
            result_table.insertRow(row_position)

            # Populate the table with line number and tokens (lexeme)
            result_table.setItem(row_position, 0, QTableWidgetItem(str(line_number)))
            result_table.setItem(row_position, 1, QTableWidgetItem(token))

            # Add placeholders for token type and attributes
            result_table.setItem(row_position, 2, QTableWidgetItem("Identifier"))  # For demo purposes, labeling all tokens as 'Identifier'
            result_table.setItem(row_position, 3, QTableWidgetItem("None"))

    # Display message in the console
    console_edit.append("Code analyzed successfully!")


# Function to refresh the UI (clear code editor, result table, and console)
def refresh_ui(code_edit, result_table, console_edit):
    # Clear the code editor
    code_edit.clear()

    # Clear the result table
    result_table.setRowCount(0)

    # Clear the console
    console_edit.clear()

    # Add a message to the console after refresh
    console_edit.append("UI has been refreshed!")
