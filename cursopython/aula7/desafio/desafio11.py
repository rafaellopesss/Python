parede_height = float(input("Digite a altura da parede:"))
parede_width = float(input("Digite a largura da parede:"))

tinta = 2

area = parede_height * parede_width
litros = area / 2

print(f'Para pintar uma parede com a área de {area} é necessário {litros} litros')
