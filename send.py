import pika 




class RabbitMq():
    def __init__(self,queue,host="localhost"):
        self.connection = connection =  pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queue=queue
        self.channel.queue_declare(queue=self.queue)
    
    def publish(self,message):
        self.channel.basic_publish(exchange='',
            routing_key=self.queue,
            body=str(message))
        print("Sample Message Sent to rabbitmq")
        self.connection.close()
        print("Connection closed")
    
if __name__=="__main__":
    server = RabbitMq(queue="sample-queue")
    server.publish("This is from the sender message")