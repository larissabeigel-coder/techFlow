#Etapa1 - Criação da empresa e os projetos 
startups = {
    "nome": "Flare Solution",
    "etapa": "Aceleração",
    "inicio": "Abril de 2026"
}
projetos_ativos =["App Mobile","Signal Found"]

print("STARTUP:",startups["nome"],"Fase:",startups["etapa"])
print("Projeto em Andamento:",projetos_ativos[0],"inicio",startups["inicio"])

#Etapa2 - Mapeamento de Salas 
#Sala Ocupada = 1 e Sala Livre =0
salas = [
    [1,0],
    [0,1]
]
print("Status da sala A1", salas[0][0])
print("Status da Sala A2", salas[0][1])
print("Status da Sala B1", salas[1][0])
print("Status da Sala B2",salas[1][1])
print("Classificação de Status: 1= Ocupado e 0 = Livre")

#Etapa3 - Leitura de dados operacionais
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print("Cabeçalho:", cabecalho)
print("Linha 1:", linha1)
print("Linha 2:", linha2)
print("Linha 3:", linha3)
print("Linha 4:", linha4)

