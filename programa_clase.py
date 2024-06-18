import csv
def obtener_fichero_calificaciones():
    lista = []
    with open(r"C:\Users\cetecom\Documents\calificaciones.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
               for i in range(2,len(linea)):
                    if linea[i] == '':
                        linea[i] = '0,0'

               Apellidos = linea[0]
               nombre    = linea[1]
               Asistencia = float(linea[2].replace('%',''))
               Parcial1 = float(linea[3].replace(',','.'))
               Parcial2 = float(linea[4].replace(',','.'))
               Ordinario1 = float(linea[5].replace(',','.'))
               Ordinario2 = float(linea[6].replace(',','.'))
               Practicas = float(linea[7].replace(',','.'))
               OrdinarioPracticas = float(linea[8].replace(',','.'))
               lista.append({
                   'Apellidos':Apellidos,
                   'nombre':nombre,
                   'Asistencia': Asistencia,
                   'Parcial1': Parcial1,
                   'Parcial2': Parcial2,
                   'Ordinario1': Ordinario1,
                   'Ordinario2': Ordinario2,
                   'Practicas': Practicas,
                   'OrdinarioPracticas': OrdinarioPracticas,
                })    
            else:
                pos = 1    
    return lista


def añadir_nota_final(calificaciones):
        if alumno['Ordinario1']: #Si el alumno se ha presentado al examen de repesca del primer parcial tomamos esa nota como la nota del primer parcial
            parcial1 = nota(alumno['Ordinario1'])
        elif alumno['Parcial1']:
            parcial1 = nota(alumno['Parcial1'])
        else: # No se ha presentado al primer parcial ni a la repesca en el ordinario
            parcial1 = 0
        if alumno['Ordinario2']: #Si el alumno se ha presentado al examen de repesca del segundo parcial tomamos esa nota como la nota del segundo parcial
            parcial2 = nota(alumno['Ordinario2'])
        elif alumno['Parcial2']:
            parcial2 = nota(alumno['Parcial2'])
        else: # No se ha presentado al segundo parcial ni a la repesca en el ordinario
            parcial2 = 0 
        if alumno['OrdinarioPracticas']: #Si el alumno se ha presentado al examen de repesca de prácticas tomamos esa nota como la nota de prácticas
            practicas = nota(alumno['OrdinarioPracticas'])
        elif alumno['Practicas']:
            practicas = nota(alumno['Practicas'])
        else:
            practicas = 0
        alumno['Final1'] = parcial1
        alumno['Final2'] = parcial2
        alumno['FinalPracticas'] = practicas
        alumno['NotaFinal'] = parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4
        return alumno



calificacion = obtener_fichero_calificaciones()
añadir_nota_final(calificacion)