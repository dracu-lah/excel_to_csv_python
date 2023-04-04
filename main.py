import pandas as pd
# Replace "input.xlsx" with the name of your Excel file
excel_file = pd.read_excel("CTS3_result analysis.xlsx")

# Convert the Excel file to a CSV file and store it in a variable
csv_data = excel_file.to_csv(index=None, header=None)

# Replace the first row of the CSV data with a new row
new_header=['Register No','Student Name', 'Branch', 'Semester', 'Course', 'Exam Type', 'Attendance', 'Withheld', 'IMark', 'Grade', 'Result']
csv_data = "\n".join([",".join(new_header)] + csv_data.split("\n")[1:])

# Write the modified CSV data to a new CSV file
with open("CTS3_result analysis_fixed.csv", "w") as f:
    f.write(csv_data)

