import time
import zmq
import sys

def main():

    # Cria o contexto, o socket publisher e faz o bind na porta 5563
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.connect("tcp://localhost:5557")

    jrnl_length = len(sys.argv)
    jrnl_array = []

    if (jrnl_length <= 1):
        jrnl_array = ["A"]

    else:
        for i in range (1, jrnl_length):
            jrnl_array.append(sys.argv[i])

    while True:
        #   Escreve as mensagens
        #   Aqui, em multipart, para que a primeira parte da mensagem seja a "chave" que
        # deve correlacionar com a especificada pelo subscriber
        for jrnl in jrnl_array:
            publisher.send_multipart([bytes(jrnl, "utf-8"), bytes(f'Noticia de {jrnl}', "utf-8")])
            print(f"Publicada noticia de {str(jrnl)}")
        
        time.sleep(1)

    # Nunca chega aqui, mas só para lembrar como deve ser feita a saída de um socket e contexto (muito importante em C e algumas outras linguagens)
    publisher.close()
    context.term()


if __name__ == "__main__":
    main()