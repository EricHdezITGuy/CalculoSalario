horas=int(input("Cantidad de horas laboradas "))
precioHora=int(input("Precio de la hora laboral "))
if horas<=40:
    salario = horas * precioHora
else:
    horaExtra = horas - 40
    salario =(horaExtra*1.5*precioHora) + (40*precioHora)
print ("El total es: ", salario)