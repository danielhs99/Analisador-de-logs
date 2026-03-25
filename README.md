# Analisador-de-logs

Oi, esse é o meu primeiro projeto no Git! Para começar, escolhi um analisador de logs básico usando Python no formato Apache/Nginx Combined Log Format.


## Funcionalidades

- Top 5 IPs mais frequentes
- Status HTTP mais comuns (2xx, 4xx, 5xx)
- Listagem de erros com IP e rota afetada
- Validação de IPs e linhas malformadas
- Tratamento de erros de leitura e permissão

##  Tecnologias

- Python 3.10+
- `re`, `collections`, `ipaddress`, `pathlib`

##  Como usar

```bash
python analisador.py
```

Digite o caminho do arquivo de log quando solicitado:

```
Digite o caminho do arquivo de log: C:\logs\acesso.log
```

## Formato suportado

Logs no padrão Combined Log Format:

```
192.168.1.1 - - [10/Mar/2024:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

## Requisitos

- Python 3.10 ou superior
- Nenhuma dependência externa
