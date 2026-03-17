# Função responsável por ler o arquivo TXT
def ler_logs_txt(nome_arquivo):

    # Lista que irá armazenar os logs convertidos
    logs = []

    # Abre o arquivo no modo leitura
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Percorre cada linha do arquivo
        for linha in arquivo:

            # Remove espaços e quebra de linha
            linha = linha.strip()

            # Ignora linhas vazias
            if linha == "":
                continue

            # Ignora comentários
            if linha.startswith("#"):
                continue

            # Divide a linha em partes
            partes = linha.split()

            # Cria um dicionário semelhante ao formato JSON
            log = {
                "action": partes[0],
                "user": partes[1],
                "status": partes[2]
            }

            # Adiciona o log na lista
            logs.append(log)

    # Retorna todos os logs
    return logs


# Função que conta quantas vezes cada ação aparece
def contar_acoes(logs):

    # Dicionário que armazenará a contagem
    contagem = {}

    for log in logs:

        acao = log["action"]

        if acao in contagem:
            contagem[acao] += 1
        else:
            contagem[acao] = 1

    return contagem


# Função que conta quantos logins falharam
def contar_login_falha(logs):

    total_falhas = 0

    for log in logs:

        if log["action"] == "login" and log["status"] == "fail":
            total_falhas += 1

    return total_falhas


# Função que descobre qual usuário fez mais login
def usuario_com_mais_login(logs):

    logins_por_usuario = {}

    for log in logs:

        if log["action"] == "login":

            usuario = log["user"]

            if usuario in logins_por_usuario:
                logins_por_usuario[usuario] += 1
            else:
                logins_por_usuario[usuario] = 1

    usuario_top = max(logins_por_usuario, key=logins_por_usuario.get)

    return usuario_top


# Função principal que executa o programa
def main():

    # Lê os logs do arquivo TXT
    logs = ler_logs_txt("logs.txt")

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