"""
Log Analyzer - TXT Version

Este script lê um arquivo de logs em formato TXT e realiza algumas análises:

1. Conta quantas vezes cada ação aparece (login, logout, etc.)
2. Conta quantos logins falharam
3. Descobre qual usuário fez mais login

Formato esperado do arquivo logs.txt:

login henry success
login maria fail
logout henry success

Cada linha possui:
acao usuario status
"""


# Função responsável por ler o arquivo TXT e converter para uma estrutura Python
def ler_logs_txt(nome_arquivo):

    # Lista que armazenará todos os logs convertidos
    logs = []

    # Abre o arquivo no modo leitura
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Percorre cada linha do arquivo
        for linha in arquivo:

            # Remove espaços extras e quebra de linha
            linha = linha.strip()

            # Ignora linhas vazias
            if linha == "":
                continue

            # Ignora comentários (linhas que começam com #)
            if linha.startswith("#"):
                continue

            # Divide a linha em partes
            partes = linha.split()

            # Verifica se a linha possui o formato esperado
            if len(partes) < 3:
                continue

            # Cria um dicionário representando o log
            log = {
                "action": partes[0],
                "user": partes[1],
                "status": partes[2]
            }

            # Adiciona o log na lista
            logs.append(log)

    # Retorna todos os logs
    return logs


# Conta quantas vezes cada ação aparece
def contar_acoes(logs):

    contagem = {}

    for log in logs:

        acao = log["action"]

        if acao in contagem:
            contagem[acao] += 1
        else:
            contagem[acao] = 1

    return contagem


# Conta quantos logins falharam
def contar_login_falha(logs):

    total_falhas = 0

    for log in logs:

        if log["action"] == "login" and log["status"] == "fail":
            total_falhas += 1

    return total_falhas


# Descobre qual usuário fez mais login
def usuario_com_mais_login(logs):

    logins_por_usuario = {}

    for log in logs:

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

    # Lê os logs do arquivo
    logs = ler_logs_txt("logs.txt")

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
