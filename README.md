Neste projeto será implementada uma DSL(Domain Specific Language). Esta linguagem irá permitir a simulação de bibliotecas e outros tipos de acervos que mantêm livros para empréstimo.

Estes locais são organizados em corredores que possuem um espaço limitado para manter esses livros. Os funcionários dedicados a tarefa de garantir a organização desses espaços são contratados com base no número de livros armazenados e do fluxo de empréstimos.

Nesta avaliação devera ser entregue um compilador implementado em Python3 usando a ferramenta ANTLR (submeter os arquivos Python3, o arquivo de gramática do ANTLR, e os arquivos de Test). Esse compilador receberá um arquivo de entrada que representa uma biblioteca ou acervo, e retornara um programa em Python3 que permitira executar uma simulação desse local.

O compilador deve validar se a representação de biblioteca ou acervo respeita as regras de número mínimo de funcionários, e de espaço mínimo para armazenamento.

Arquivo Exemplo:
´´´json
{
  tipo -> biblioteca ou acervo
  funcionarios -> 10
  corredores -> 3
  livros -> {
    artes -> 20
    esportes -> 10
    coputacao -> 31
    ciencias -> 25
  }
}
´´´
## Regras de validação:

    Em uma biblioteca para cada 12 livros é necessário um corredor;
    Em uma biblioteca para cada 2 corredores é necessário um funcionário;
    Toda biblioteca deve ter um atendente para registrar os empréstimos e as devoluções;
    Em um acervo cada livro deve ter um número par de cópias sendo no mínimo 4 cópias;
    Em um acervo para cada 20 livros é necessário um corredor;
    Em um acervo para cada 4 corredores é necessário um funcionário.

O compilador deverá validar essas regras, e caso alguma não seja respeitada um erro deve ser mostrado e a compilação interrompida (cada regra retorna um erro, uma mesma compilação pode retornar vários erros).

O programa final deverá simular empréstimos de livros, devoluções de livros, e informar a situação dos livros armazenados. Esse programa depois de iniciado fica esperando três comandos: empresta artes (empresta um livro de artes dos disponíveis), devolve artes (devolve um livro de artes), livros (mostra uma relação entre os livros disponíveis e o total de livros). Os comandos empresta e devolve recebem um tipo de livro como parâmetro.
