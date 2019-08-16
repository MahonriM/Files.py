from io import *
def escritura(datoa, datob, datoc):
    prueba=open ("archivo.txt","w")
    prueba.write(datoa)
    prueba.write(datob)
    prueba.write(datoc)
    print("/n escritura/n")
    prueba.close()
escritura('hola'
              ,'mundo','bonito')
def lectura():
    prueba = open ("archivo.txt","r")
    print(prueba.read())
    prueba.close()
lectura()

