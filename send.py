import pika 


class RabbitConfigure():
    def __init__(self,queue="sample-queue",host="localhost",routing_key="sample-queue"):
        self.queue=queue
        self.host=host
        self.routing_key=routing_key

class RabbitMq():
    def __init__(self,config):
        self.config=config
        self.connection  =  pika.BlockingConnection(pika.ConnectionParameters(host=self.config.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)
    
    def publish(self,message):
        self.channel.basic_publish(exchange='',
            routing_key=self.config.routing_key,
            body=str(message))
        print("Sample Message Sent to rabbitmq , routing key {}".format(self.config.routing_key))
        self.connection.close()
        print("Connection closed")
    
if __name__=="__main__":
    config = RabbitConfigure(queue="sample",routing_key="sample")
    server =  RabbitMq(config)
    server.publish("This is from the sender message")