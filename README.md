# Sistema de Gerenciamento de Estoque

Sistema em Python, executado no terminal, para gerenciar o estoque de uma loja: cadastro de produtos e clientes, registro de pedidos com baixa no estoque e salvamento dos dados em arquivo.

## Funcionalidades

**Produtos**
- Cadastrar produto (nome, código, preço, categoria e quantidade)
- Listar e buscar produtos
- Repor estoque
- Mostrar o produto mais vendido

**Clientes**
- Cadastrar, listar e buscar clientes

**Pedidos**
- Realizar pedido, verificando se há estoque suficiente
- Dar baixa no estoque e registrar a venda automaticamente
- Listar pedidos e calcular o valor total

**Arquivos**
- Salvar o estoque em `arquivo.txt`
- Recarregar o estoque salvo

## Tecnologias

- Python 3 (sem bibliotecas externas)

## Conceitos aplicados

- Funções
- Dicionários e estruturas de repetição
- Estruturas condicionais
- Leitura e escrita de arquivos com `with open`

## Como executar

```bash
git clone https://github.com/decoprodat/sistema-gerenciamento-estoque.git
cd sistema-gerenciamento-estoque
python sistema.py
```

## Menu

```
1 - Cadastrar Produto        6 - Cadastrar Cliente     9  - Realizar Pedido
2 - Listar Produtos          7 - Listar Clientes       10 - Listar Pedidos
3 - Buscar Produto           8 - Buscar Cliente        11 - Calcular valor total dos pedidos
4 - Repor estoque                                      12 - Salvar Estoque
5 - Produto mais vendido                               13 - Recarregar Estoque
                                                       14 - Encerrar Programa
```

## Próximos passos

- Salvar também clientes e pedidos em arquivo
- Validar as entradas do usuário para evitar erros de digitação
- Migrar o armazenamento para um banco de dados SQLite

## Autor

André Luiz Pinheiro Lopes — [LinkedIn](https://www.linkedin.com/in/andre-luiz-pinheiro-lopes/) · [GitHub](https://github.com/decoprodat)
