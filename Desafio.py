#Objetivo
# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro 
# Se XP for entre 1.001 e 2.000 = Bronze 
# Se XP for entre 2.001 e 5.000 = Prata 
# Se XP for entre 5.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina 
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000 = Imortal
# Se XP for maior ou igual a 10.001 = Radiante

heroi = input("Nome do Heroí: ")
exp = int(input("Experiência recebida: "))

def classificar():
    if exp <= 1000:
        nivel = "Ferro"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 1000 and exp <= 2000:
        nivel = "Bronze"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 2000 and exp <= 5000:
        nivel = "Prata"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 5000 and exp <= 7000:
        nivel = "Ouro"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 7000 and exp <= 8000:
        nivel = "Platina"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 8000 and exp <= 9000:
        nivel = "Ascendente"
        print(f"O Herói {heroi} está no nível {nivel}")

    elif exp > 9000 and exp <= 10000:
        nivel = "Imortal"
        print(f"O Herói {heroi} está no nível {nivel}")

    else:
        nivel = "Radiante"
        print(f"O Herói {heroi} está no nível máximo {nivel}")

classificar()

while(exp < 10002):
    adicionar = input("Heroí realizou outra missão? v ou f: ")
    if adicionar == "v":
        exp2 = int(input("Experiência recebida: "))
        exp = exp + exp2
        print(f"Total de exp: {exp}")
        classificar()

    else:
        classificar()