import pika 

def main():

    connection =  pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="sample")

    def callback(ch,method,properties,body):
        print("Received message",body)

    channel.basic_consume(queue="sample",
    on_message_callback=callback,auto_ack=True)

    print("Waiting for the messages\n")
    channel.start_consuming()




if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("keyboard interrupt")