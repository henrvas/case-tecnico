# Log Analyzer (Python)

Este projeto lê um arquivo JSON de logs de sistema e realiza algumas análises básicas.

## Funcionalidades

- Ler arquivos JSON contendo logs
- Contar quantas vezes cada ação aparece (login, logout)
- Identificar quantos logins falharam
- Descobrir qual usuário realizou mais logins

## Estrutura do código

- `ler_logs()` → lê o arquivo JSON
- `contar_acoes()` → conta ações do sistema
- `contar_login_falha()` → conta falhas de login
- `usuario_com_mais_login()` → encontra o usuário com mais logins

## Tecnologias

- Python 3
- Biblioteca padrão `json`

## Como executar

```bash
python log_analyzer.py