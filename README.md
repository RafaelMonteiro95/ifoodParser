# ifoodParser
Script feito em Python 3.5 para extrair o cardápio de um restaurante do iFood para um formato fácil de inserir numa planilha do Google Spreadsheets

# Uso
```python ifood_parser [arquivo]```
onde [arquivo] é um arquivo .html da página do restaurante a ser parseado.

# Saída
é gerado um arquivo [arquivo].out com os dados parseados e formatados. A formatação é [item do cardápio][tab][preço], onde preço está no formato R$X,XX

# Dependências
Python 3

# Nota
Esse script foi feito em python 3.5.2. Caso sua versão padrão seja python2, ele não irá funcionar.
