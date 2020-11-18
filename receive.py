import pika 


class RabbitReceiverConfig():
    def __init__(self,queue="sample-queue",host="localhost",routing="sample-queue"):
        self.queue = queue
        self.host = host
        self.routing = routing



class RabbitMqRecv():
    def __init__(self,config):
        self.config = config
        self.connection =  pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)

    def consume(self):
        self.channel.basic_consume(queue=self.config.routing,
        on_message_callback=RabbitMqRecv.callback,auto_ack=True)
        print("Waiting for the messages\n")
        self.channel.start_consuming()

    @staticmethod
    def callback(ch,method,properties,body):
        print("Received message",body)




if __name__=='__main__':
    try:
        config = RabbitReceiverConfig(queue="sample",routing="sample")
        server = RabbitMqRecv(config)
        server.consume()
    except KeyboardInterrupt:
        print("keyboard interrupt")