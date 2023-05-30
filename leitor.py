import zmq
import sys

def main():

    # Cria o contexto, o socket, connecta o socket na porta 5563 e diz para qual "chave" está inscrito
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5556")

    jrnl_length = len(sys.argv)
    if (jrnl_length <= 1):
        subscriber.setsockopt(zmq.SUBSCRIBE, b"A")

    else:
        for i in range(1,jrnl_length):
            filter = bytes(sys.argv[i], "utf-8")
            subscriber.setsockopt(zmq.SUBSCRIBE, filter)
    

    while True:
        # Le as multiplas partes da mensagem, separando-as
        [address, contents] = subscriber.recv_multipart()
        address = address.decode("utf-8")
        contents = contents.decode("utf-8")
        print(f"[{address}] {contents}")

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()


if __name__ == "__main__":
    main()