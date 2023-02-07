import datetime as timepo


ador,Titulo = "","reloj"

print(f"{ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{ador.center(50,'*')}")

#Bloque desecuencia del reloj
def reloj():
    while True:
        x = timepo.datetime.now()
        hora = f"{x.hour}:{x.minute}:{x.second} {x.strftime('%p')}"
        print(hora, end="\r")
reloj()

#Con Ctl+c para el programa