import pika 
from tfdf import compute

class Config():
    def __init__(self,host,queue,routing_key):
        self.host = host
        self.queue =  queue
        self.routing_key = routing_key

class RabbitMq():
    def __init__(self,config):
        self.config = config
        self.connection =  pika.BlockingConnection(pika.ConnectionParameters(host=self.config.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config.queue)
    

    @staticmethod
    def request(ch,method,props,body):
        filename = str(body)
        response = compute(filename)

        ch.basic_publish(excahnge="",
        routing_key = self.config.routing_key,
        properties = pika.BasicProperties(correlation_id = props.correlation_id),
        body =  str(response))

        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def publish(self):
        self.channel.basic_Qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue,on_message_callback=RabbitMq.request)
        self.channel.start_consuming()