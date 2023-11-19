consumo=float(input('Introduzca cuanto fue el consumo en dolares:'))
porcentaje_propina=float(input('Ponga el porcentaje que usted desea dejar como propina:'))
propina=consumo*(porcentaje_propina/100)
print(f'La propina que debe dejar es: {propina:.2f}')