import openpyxl

# name_woorkbook = '/home/Piztecho/mysite/'
name_woorkbook = 'pagina.xls'
woorkbook = openpyxl.load_workbook(name_woorkbook)

def edit_cell( index_sheet, rowx, columny, data):
    sheet = woorkbook[index_sheet]
    cell_select = sheet.cell(row=rowx, column=columny)
    cell_select.value = data
    woorkbook.save(name_woorkbook)

edit_cell('Hoja1',2, 2, 'TRUEE' )