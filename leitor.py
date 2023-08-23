# ...
from datetime import datetime
import requests
# Mapeamento de nomes de meses em português para inglês
meses = {
    'jan': 'Jan', 'fev': 'Feb', 'mar': 'Mar',
    'abr': 'Apr', 'mai': 'May', 'jun': 'Jun',
    'jul': 'Jul', 'ago': 'Aug', 'set': 'Sep',
    'out': 'Oct', 'nov': 'Nov', 'dez': 'Dec'
}

# Abra o arquivo de texto para leitura com codificação 'utf-8'
caminho_arquivo = r'C:\Users\Prosperidade\Desktop\pagamento\fatura.txt'

# Inicialize uma lista vazia para armazenar os dados
dados = []

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    # Use um loop for para ler cada linha do arquivo
    for linha in arquivo:
        # Verifique se a linha contém 'R$'
        if 'R$' in linha:
            # Divida a linha em palavras
            palavras = linha.split()
            
            # Encontre a posição de 'R$'
            pos_r = palavras.index('R$')
            
            # Extraia os elementos relevantes da linha
            data_str = f"{palavras[0]} {meses[palavras[1].lower()]} {palavras[2]}"  # Mapeie o mês para o inglês
            movimentacao = ' '.join(palavras[3:pos_r])  # Pega todas as palavras entre a data e 'R$'
            valor_str = palavras[pos_r + 1]  # Pega a palavra após 'R$'

            # Formate a data como 'dd/mm/yyyy'
            data = datetime.strptime(data_str, '%d %b %Y').strftime('%d/%m/%Y')

            # Crie um dicionário com os elementos extraídos
            registro = {
                'DATA': data,
                'MOVIMENTACAO': movimentacao,
                'VALOR': valor_str
            }
            
            # Adicione o dicionário à lista de dados
            dados.append(registro)

# Exiba os dados
for registro in dados:
    url = 'http://localhost:8000/api/registros/'
    
    # Converter a data para o formato correto (YYYY-MM-DD)
    data_formatada = datetime.strptime(registro['DATA'], '%d/%m/%Y').strftime('%Y-%m-%d')
    
    # Certifique-se de que o campo "VALOR" seja uma string válida representando um número decimal
    valor_str = registro['VALOR'].replace(',', '.')  # Substitua ',' por '.' se necessário
    
    # Usar os dados formatados para criar os dados a serem enviados na solicitação POST
    data = {
        'DATA': data_formatada,
        'MOVIMENTACAO': registro['MOVIMENTACAO'],
        'VALOR': valor_str
    }
    
    # Faça a solicitação POST
    response = requests.post(url, data=data)
    
    # Verifique a resposta da solicitação
    if response.status_code == 201:
        print("Registro criado com sucesso!")
        print(response.json())  # Se desejar, você pode imprimir a resposta da API
    else:
        print("Erro ao criar registro.")


