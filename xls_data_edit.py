import xlwt

def editar_celda(nombre_archivo, numero_hoja, fila, columna, valor):
    # Abrir el archivo de Excel
    libro = xlwt.Workbook(nombre_archivo)

    # Crear la hoja si no existe
    try:
        hoja = libro.get_sheet(numero_hoja)
    except IndexError:
        hoja = libro.add_sheet(numero_hoja)

    # Escribir el valor en la celda especificada
    hoja.write(fila, columna, valor)

    # Guardar el archivo
    libro.save(nombre_archivo)

editar_celda('pagina.xls','sheet1', 2, 2, 'TRUEE')