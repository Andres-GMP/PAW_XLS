import xlrd
# import xlwt
from xlutils.copy import copy 

workbook = 'pagina.xls'
file_excel  = xlrd.open_workbook(workbook, formatting_info=True)

def edit_cell(num_sheet, rowx, coly, new_value):    
    book_editable = copy(file_excel)
    sheet = book_editable.get_sheet(num_sheet)
    sheet.write(rowx,coly, new_value)
    book_editable.save(workbook)

edit_cell(0, 0,0,'Aqui algo')
