candidatos = {
    "Alice": {"Candidato 01": {"e": 5, "t": 10, "p": 8, "s": 8}},
    "Laura": {"Candidato 02": {"e": 10, "t": 7, "p": 7, "s": 8}},
    "Maria Alice": {"Candidato 03": {"e": 8, "t": 5, "p": 4, "s": 9}},
    "Sophia": {"Candidato 04": {"e": 2, "t": 2, "p": 2, "s": 1}},
    "Carolina": {"Candidato 05": {"e": 10, "t": 10, "p": 8, "s": 9}},
}

def pesquisar_candidato(nome_candidato):
    if nome_candidato in candidatos:
        avaliacoes = candidatos[nome_candidato]
        resultado = nome_candidato + ": "
        for candidato, notas in avaliacoes.items():
            resultado += candidato + " - "
            for avaliacao, nota in notas.items():
                resultado += avaliacao + str(nota) + " _ "
        return resultado[:-2]
    else:
        return "Candidato não encontrado"
    
def inserir_novo_candidato():
    nome = input("Digite o nome do novo candidato: ")
    chave = input("Digite a chave do novo candidato/Identificação(candidato xx): ")
    notas = {}
    avaliacoes = ["e", "t", "p", "s"]
    for avaliacao in avaliacoes:
        nota = int(input(f"Digite a nota de {avaliacao.upper()}: "))
        notas[avaliacao] = nota
    candidatos[nome] = {chave: notas}
    print("Novo candidato adicionado com sucesso!")

def buscar_candidatos_compatíveis(notas_minimas):
    candidatos_compativeis = []
    for nome, candidato in candidatos.items():
        notas_candidato = candidato[list(candidato.keys())[0]]
        if all(notas_candidato[avaliacao] >= nota_minima for avaliacao, nota_minima in zip(notas_candidato.keys(), notas_minimas)):
            candidatos_compativeis.append(nome)
    return candidatos_compativeis

print("Digite o nome do candidato para pesquisa, 'n' para inserir um novo candidato, 'c' para buscar candidatos compatíveis, ou 'q' para sair:")
while True:
    opcao = input("=> ").strip()
    if opcao == "q":
        print("Obrigado, volte sempre!")
        break
    elif opcao == "n":
        inserir_novo_candidato()
    elif opcao == "c":
        notas_minimas = [int(input(f"Digite a nota mínima para {avaliacao.upper()}: ")) for avaliacao in ["e", "t", "p", "s"]]
        candidatos_compativeis = buscar_candidatos_compatíveis(notas_minimas)
        if candidatos_compativeis:
            print("Os candidatos compatíveis são:")
            for candidato in candidatos_compativeis:
                print(candidato)
        else:
            print("Não há candidatos compatíveis com os critérios fornecidos.")
    else:
        print(pesquisar_candidato(opcao))