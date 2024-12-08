print(f'[CONVERSOR DE UNIDADES]')
metro = float(input('Digite a quantidade de metros: '))
centimetro = metro * 100
milimetro = centimetro * 10

if metro > 1:
    metros = 'metros'
else:
    metros = 'metro'

print(f'{metro} {metros} tem [{centimetro} centímetros] e [{milimetro} milímetros]')