# Log Parser

O Log Parser foi escrito em Python 2.7.15, e desenvolvido no SO Ubuntu 18.04.

Ele lê um arquivo de log de envios de webhook, nomeado log.txt que contém informações no formato:

level=info response_body="" request_to" url " response_headers= response_status=" code "

onde url é a url para onde foi enviado o webhook e code é o status code retornado pelo servidor do cliente.
O programa então analiza a informação e retorna:
  - as 3 urls mais chamadas em quantidade;
  - uma tabela mostrando a quantidade de webhooks por status.
  
Para executar, basta dar o comando:

python readLog.py

no Terminal, desde que os arquivos readLog.py e log.txt estejam no mesmo diretório.

A documentação de como o programa funciona internamente se encontra em comentários no código-fonte.
