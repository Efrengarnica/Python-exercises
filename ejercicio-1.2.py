frase= input("Dime algo y te digo cuanto tiempo tardarías en decirlo: ")
palabras_separadas=frase.split(" ")
cantidad_palabras= len(palabras_separadas)
print(f'Dijiste {cantidad_palabras} y tardarías {cantidad_palabras/2} segundos en decirlo')

print(f'Dalto lo diría en {cantidad_palabras*100//2*1.3/100} segundos')

if cantidad_palabras>10:
    print("No me digas tanto bro")
