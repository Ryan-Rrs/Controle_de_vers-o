from replit import db 

def adiciona_contato(nome, telefone):
    if nome in db:
        print("Nome existente!")
    else:
        db[nome] = telefone

def ler_contato(nome):
    telefone = db.get(nome)
    return telefone

def pesquisa_contatos(pesquisa):
    resultados = db.prefix(pesquisa)
    return {k: db[k] for k in resultados}

def atualiza_telefone(nome_anterior, novo_telefone):
    db[nome_anterior] = novo_telefone

def atualiza_contato(nome_anterior, novo_nome, novo_telefone):
    db[novo_nome] = novo_telefone
    del db[nome_anterior]

def apaga_contato(nome):
del db[nome]