

import openpyxl


path = 'C:\\Users\khanb\PycharmProjects\selenium\write_excel.xlsx'

workbook = openpyxl.load_workbook(path)

sheet = workbook.active

for i in range(1,6):
    for j in range(1,3):
        sheet.cell(row=i,column=j).value="welcome"

#this will save the data
workbook.save(path)