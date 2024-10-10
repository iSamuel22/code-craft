tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"\ntarefa '{tarefa}' adicionada.")

def listar_tarefas():
    print("\nlista de tarefas:")
    for idx, tarefa in enumerate(tarefas, start = 1):
        print(f"{idx}. {tarefa}")

def remover_tarefa(indice):
    if 0 < indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        print(f"tarefa '{tarefa_removida}' removida.")
    else:
        print("\níndice inválido.")

while True:
    acao = input("\nescolha uma ação (adicionar, listar, remover, sair): ").lower()

    if acao == 'adicionar' or acao == 'add' or acao == 'a':
        tarefa = input("digite a tarefa: ")
        adicionar_tarefa(tarefa)
        print("\n")
    elif acao == 'listar' or acao == 'list' or acao == 'l':
        listar_tarefas()
        print("\n")
    elif acao == 'remover' or acao == 'del' or acao == 'r':
        indice = int(input("digite o índice da tarefa a ser removida: "))
        remover_tarefa(indice)
        print("\n")
    elif acao == 'sair' or acao == 'exit' or acao == 's':
        print("saindo do sistema...\n")
        break
    else:
        print("ação inválida.\n")
