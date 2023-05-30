# Trabalho básico para entendimento de Middleware Orientado a Mensagens

Este é um trabalho simples feito durante a cadeira de Computação Distribuída
no curso de Ciência da Computação da Universidade Federal de Santa Catarina.

# Modo de utilizar

1. Ter instalado o python3

2. Ter instalado o pyzmq, pode-se instalá-lo via terminal com o seguinte comando, utilizando o pip
    pip install pyzmq

3. Executar proxy.py normalmente

4. Executar 'n' jornais.py e 'm' leitor.py, todos em diferentes processos.
    Exemplo de execução de cada um no cmd do Windows 10:
        py jornais.py JornalA "Jornal B" C
        py leitor.py "Jornal B" C

        Dessa forma, este processo jornais.py adicionará as mensagens dos jornais A, B e C na fila. Ainda, o processo leitor.py
        irá consumir as mensagens dos jornais B e C, apenas.