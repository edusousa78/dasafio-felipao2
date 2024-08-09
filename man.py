# definindo a função para calcular os niveis e saldos
def calcular_nivel(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldoVitorias, nivel

# Declaramos as variaveis
vitorias = 70
derrotas = 45

saldoVitorias, nivel = calcular_nivel(vitorias, derrotas)

print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}")
