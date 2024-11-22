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