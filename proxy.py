import zmq

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.XSUB)
    subscriber.bind("tcp://*:5557")


    publisher = context.socket(zmq.XPUB)
    publisher.bind("tcp://*:5556")

    zmq.proxy(publisher, subscriber)

    subscriber.close()
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()


    