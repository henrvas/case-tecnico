# Importa a biblioteca json para poder ler arquivos .json
import json


# Função responsável por ler o arquivo JSON
def ler_logs(nome_arquivo):

    # Abre o arquivo no modo leitura
    # encoding utf-8 garante que caracteres especiais funcionem corretamente
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Converte o JSON em um objeto Python (dicionário/lista)
        dados = json.load(arquivo)

    # Retorna apenas a lista de logs dentro do JSON
    return dados["logs"]


# Função que conta quantas vezes cada ação aparece (login, logout etc.)
def contar_acoes(logs):

    # Dicionário que vai armazenar a contagem das ações
    contagem = {}

    # Percorre todos os logs
    for log in logs:

        # Pega a ação do log (ex: login ou logout)
        acao = log["action"]

        # Se a ação já existe no dicionário, soma +1
        if acao in contagem:
            contagem[acao] += 1

        # Se não existir ainda, cria a chave com valor 1
        else:
            contagem[acao] = 1

    # Retorna o resultado final da contagem
    return contagem


# Função que conta quantos logins falharam
def contar_login_falha(logs):

    # Contador inicial
    total_falhas = 0

    # Percorre todos os logs
    for log in logs:

        # Verifica se é login e se o status é falha
        if log["action"] == "login" and log["status"] == "fail":

            # Soma +1 no contador
            total_falhas += 1

    return total_falhas


# Função que descobre qual usuário fez mais login
def usuario_com_mais_login(logs):

    # Dicionário para armazenar logins por usuário
    logins_por_usuario = {}

    for log in logs:

        # Considera apenas eventos de login
        if log["action"] == "login":

            usuario = log["user"]

            if usuario in logins_por_usuario:
                logins_por_usuario[usuario] += 1
            else:
                logins_por_usuario[usuario] = 1

    # Encontra o usuário com maior número de logins
    usuario_top = max(logins_por_usuario, key=logins_por_usuario.get)

    return usuario_top


# Função principal que executa o programa
def main():

    # Lê os logs do arquivo JSON
    logs = ler_logs("system_logs.json")

    # Executa as análises
    contagem = contar_acoes(logs)
    falhas_login = contar_login_falha(logs)
    usuario_top = usuario_com_mais_login(logs)

    # Mostra os resultados
    print("Contagem de ações:", contagem)
    print("Logins com falha:", falhas_login)
    print("Usuário com mais login:", usuario_top)


# Executa o programa
main()
