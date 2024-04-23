import contatos
from os import system

mensagem_principal = """AGENDA DE CONTATOS
----------------------------------
ESCOLHA:
1 - ADICIONAR CONTATO
2 - PESQUISAR CONTATO
3 - ALTERAR CONTATO
4 - APAGAR CONTATO
----------------------------------
"""


def prompt_adiciona_contato():
  nome = input("NOME: ")
  telefone = input("TELEFONE: ")

  print(f"Adicionando {nome} e {telefone}")
  contatos.adiciona_contato(nome, telefone)


def prompt_ler_contato():
  nome = input("Digite o nome para pesquisar: ")

  telefone = contatos.ler_contato(nome)
  if telefone:
    print(f"{nome}: {telefone}")
  else:
    resultados = contatos.pesquisa_contatos(nome)
    if resultados:
      for k in resultados:
        print(f"{k}: {resultados[k]}")
    else:
      print(f"Parece que {nome} não existe")


def prompt_atualiza_contato():
  nome_anterior = input("Informe o nome do contato para alterar: ")
  telefone_anterior = contatos.ler_contato(nome_anterior)
  if telefone_anterior:
    novo_nome = input(
        f"Digite o novo nome (Deixe em branco para manter {nome_anterior}): "
    ).strip()
    novo_telefone = input(
        f"Digite o novo telefone para o contato (Deixe em branco para manter {telefone_anterior}): "
    ).strip()

    if not novo_telefone:
      novo_telefone = telefone_anterior

    if not novo_nome:
      contatos.atualiza_telefone(nome_anterior, novo_telefone)
    else:
      contatos.atualiza_contato(nome_anterior, novo_nome, novo_telefone)
  else:
    print(f"Parece que {nome_anterior} não existe")


def prompt_apaga_contato():
  nome = input("Digite o nome do contato para apagar: ")
  contato = contatos.ler_contato(nome)
  if contato:
    print(f"Apagando {nome}")
    contatos.apaga_contato(nome)
  else:
    print(f"Parece que {nome} não existe")


def main():
  print(mensagem_principal)
  escolha = input("ESCOLHA UMA OPÇÃO: ").strip()
  if escolha == "1":
    prompt_adiciona_contato()
  elif escolha == "2":
    prompt_ler_contato()
  elif escolha == "3":
    prompt_atualiza_contato()
  elif escolha == "4":
    prompt_apaga_contato()
  else:
    print("Escolha inválida, escolha novamente.")


while True:
  system('clear')
  main()
  input("Pressione ENTER para continuar: ")
