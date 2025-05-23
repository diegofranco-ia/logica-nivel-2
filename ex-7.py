#7) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

#Inputs

#Qual a quantidade de votos brancos?
#válidos?

totEleitores = int(input("Total de eleitores: "))
totVotosEmBranco = int(input("total em branco: "))
totNulos = int(input("total nulos: "))
totValidos = int(input("total validos: "))

porcbranco = (totVotosEmBranco / totEleitores) * 100
print("de votos em branco", porcbranco, "%")

#Output
#Total de porcentagens

#Total de votos válidos: x%
#Total de votos em branco: y%
#Total de votos nulos: t%
