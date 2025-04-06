def leer_archivo(archivo):
    with open(archivo, 'r') as f:
        return leer_archivo_recursivamente(f,"")

def leer_archivo_recursivamente(archivo,texto):
    linea_actual = archivo.readline().strip()
    if linea_actual == '':
        return texto
    else:
        print(linea_actual)
        pos_actual = archivo.tell()
        archivo.seek(pos_actual)
        if texto !='':
            return leer_archivo_recursivamente(archivo,texto+"\n"+linea_actual)
        else:
            return leer_archivo_recursivamente(archivo,linea_actual)

def reEscribirArchivo(archivo,nuevoValor):
    with open(archivo, 'r+') as f:
         reEscribirArchivoRecursivamente(f,nuevoValor,"")

def reEscribirArchivoRecursivamente(archivo, nuevoValor, texto):
    lineaActual = archivo.readline().strip()
    if lineaActual == '':
        archivo.truncate()
        archivo.seek(0)
        archivo.write(texto+"\n"+nuevoValor)
        return 
    elif int(lineaActual.split(" ")[1]) < int(nuevoValor.split(" ")[1]):
        pos_actual = archivo.tell()
        archivo.seek(pos_actual)
        if(texto==""):
            reEscribirArchivoRecursivamente(archivo, lineaActual, nuevoValor)
        else:
            reEscribirArchivoRecursivamente(archivo, lineaActual, texto+"\n"+nuevoValor)
    else:
        pos_actual = archivo.tell()
        archivo.seek(pos_actual)
        if texto !='':
            reEscribirArchivoRecursivamente(archivo,nuevoValor,texto+"\n"+lineaActual)
        else:
            reEscribirArchivoRecursivamente(archivo,nuevoValor,lineaActual)
        

#leer_archivo('archivo.txt')
#reEscribirArchivo('archivo.txt',"Jeff 700")