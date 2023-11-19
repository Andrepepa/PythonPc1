edad=int(input('Introduzca cual es su edad:'))
if edad<4:
    precio_pagar=0
elif 4<=edad<18:
    precio_pagar=5
elif edad>=18:
    precio_pagar=10
print(f'El precio que usted debe de pagar es:{precio_pagar}$')