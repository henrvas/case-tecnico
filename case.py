"""
Log Analyzer - JSON Version

Este script lê um arquivo JSON contendo logs de sistema e realiza algumas análises:

1. Conta quantas vezes cada ação aparece (login, logout, etc.)
2. Conta quantos logins falharam
3. Descobre qual usuário fez mais login

Formato esperado do JSON:

{
  "logs": [
    {"user": "henry", "action": "login", "status": "success"},
    {"user": "maria", "action": "login", "status": "fail"}
  ]
}
"""

# Importa a biblioteca json para leitura de arquivos JSON
import json


# Função responsável por ler o arquivo JSON e retornar os logs
def ler_logs(nome_arquivo):

    # Abre o arquivo no modo leitura
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Converte o JSON em um objeto Python (dicionário/lista)
        dados = json.load(arquivo)

    # Retorna apenas a lista de logs
    return dados["logs"]


# Conta quantas vezes cada ação aparece (login, logout, etc.)
def contar_acoes(logs):

    # Dicionário que armazenará a contagem das ações
    contagem = {}

    # Percorre todos os logs
    for log in logs:

        # Obtém a ação do log
        acao = log["action"]

        # Atualiza a contagem
        if acao in contagem:
            contagem[acao] += 1
        else:
            contagem[acao] = 1

    return contagem


# Conta quantos logins falharam
def contar_login_falha(logs):

    total_falhas = 0

    # Percorre todos os logs
    for log in logs:

        # Verifica se é login e se o status é fail
        if log["action"] == "login" and log["status"] == "fail":
            total_falhas += 1

    return total_falhas


# Descobre qual usuário fez mais login
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

    # Exibe os resultados
    print("Contagem de ações:", contagem)
    print("Logins com falha:", falhas_login)
    print("Usuário com mais login:", usuario_top)


# Executa o programa
main()
