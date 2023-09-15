import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(f'wb = {wb}')