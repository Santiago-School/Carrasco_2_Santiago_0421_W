# capturar el nombre y el apellido 
app = (input("ingresa el apellido paterno"))
apm = (input("ingresa el apellido materno"))
n = (input("  ingresa tu nombre"))
print("-------------------------------------")
#desplegar las variables guardadas
print("apellido paterno: "+app)
print("apellido materno: "+apm)
print("nombre: "+n)
print("-------------------------------------")
# desplegar el nombre completo y con mayusculas
nc = n +" " + " "+app+" "+" "+apm
print("tu nombre completo es: "+ nc)
print("-------------------------------------")
#desplegar nombre completo en mayusculas
ncm = nc.upper()
print("tu nombre completo en mayusculas es: "+ncm)
print("-------------------------------------")
