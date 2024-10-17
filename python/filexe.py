import openpyxl 
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
import apartments
import sys
intro_url="https://www.apartments.com/apartments/min-1-bedrooms/?sk=cc5fd2fd21f4c785795254c92a2c32ae&bb=4z_pp9wt-I-k2-nwH"

wb = Workbook()
ws = wb.active

alph=['A','B','C','D','E','F']
# writing to the cell of an excel sheet 
ws['A1'] = "Name"
ws['A1'].font = Font(bold=True)

ws['B1'] = "Address"
ws['B1'].font = Font(bold=True)

ws['C1'] = "Cost"
ws['C1'].font = Font(bold=True)

ws['D1'] = "Room"
ws['D1'].font = Font(bold=True)

ws['E1'] = "Phone Number"
ws['E1'].font = Font(bold=True)

ws['F1'] = "info"
ws['F1'].font = Font(bold=True)

for cell in alph:
    ws.column_dimensions[cell].width = len(ws[f'{cell}1'].value)+5

wb.save(f"_{sys.argv[2]}/apartment_list.xlsx")

data=apartments.aparment_info
if len(data)<20:
    print("stop")
    sys.exit()
elif len(data)>=20:
    apple="apple"
    for row in data:
        ws.append(row)
    # save the file 
    wb.save(f"_{sys.argv[2]}/apartment_list.xlsx")

    workbook = openpyxl.load_workbook(f"_{sys.argv[2]}/apartment_list.xlsx") 
    
    # Get the first sheet 
    sheet = workbook.worksheets[0] 
    
    # Create a list to store the values 
    length=[]
    column_count = sheet.max_column
    row_count = sheet.max_row
    # Iterate over the rows in the sheet 
    for i in range(0,column_count):
        names = [] 
        for row in sheet: 
            # Get the value of the first cell 
            # in the row (the "Name" cell)
            name = row[i].value 
            # Add the value to the list '
            names.append(len(name))
        names.sort(reverse = True)
        for cell in alph:
            ws.column_dimensions[cell].width = names[0]

    wb.save(f"_{sys.argv[2]}/apartment_list.xlsx")