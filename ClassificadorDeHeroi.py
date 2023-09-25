# # 1️⃣ Desafio Classificador de nível de Herói

# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões

# ## Objetivo

# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 6.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"
nomeHeroi = "spartacus"
xpHeroi = 3250
nivel = ""

if xpHeroi <= 1000:
    nivel = "Ferro"
elif xpHeroi >= 1001 and xpHeroi <=2000:
    nivel = "Bronze"
elif xpHeroi >= 2001 and xpHeroi <=5000:
    nivel = "Prata"
elif xpHeroi >= 5001 and xpHeroi <=7000:
    nivel = "Ouro"
elif xpHeroi >= 7001 and xpHeroi <=8000:
    nivel = "Platina"
elif xpHeroi >= 8001 and xpHeroi <=9000:
    nivel = "Ascendente"
elif xpHeroi >= 9001 and xpHeroi <=10000:
    nivel = "Imortal"
else:
    nivel ="Radiante"

print("O Herói de nome **{}** está no nível de **{}**".format(nomeHeroi,nivel))