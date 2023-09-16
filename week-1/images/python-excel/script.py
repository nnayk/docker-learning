import openpyxl,os

print(os.listdir())

wb = openpyxl.load_workbook('example.xlsx')
ws = wb.active
print(ws['A1'].value)

print(f'wb = {wb}')