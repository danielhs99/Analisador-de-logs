from collections import Counter

def analisar_logs(arquivo):
    ips=[]
    status_codes = []
    erros = []

    try: 
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.split()

                if len(partes) < 9: 
                    continue 

                ip = partes [0]
                status = partes [-2]

                ips.append(ip)
                status_codes.append(status)

                if status.startswith('4') or status.startswith('5'):
                    erros.append((ip, status))
                    
        print('\n=== Análise de logs ===')

        print('\n Top 5 Ips:')
        for ip, count in Counter(ips).most_common(5):
            print(f'{ip} - {count} vezes')

        print('\nErros encontrados:')
        for ip, status in erros[:10]:
            print(f'{ip}->{status}')

    except FileNotFoundError:
            print('Arquivo não encontrado.')

def main(): 
    print('=== Analisador de Logs ===')
    arquivo = input ('Digite o caminho do arquivo de log:')
    analisar_logs(arquivo)

if __name__ == '__main__':
    main()

             