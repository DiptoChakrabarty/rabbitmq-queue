import pika 
from tfdf import compute

class Config():
    def __init__(self,host="localhost",queue="rpc",routing_key="rpc"):
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
        filename = str(body.decode("UTF-8"))
        #filename = filename.replace('b',"")
        response = compute(filename)
        ch.basic_publish(exchange="",
        routing_key = props.reply_to,
        properties = pika.BasicProperties(correlation_id = props.correlation_id),
        body =  str(response))

        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    def publish(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.config.queue,on_message_callback=RabbitMq.request)
        self.channel.start_consuming()


serverobj = Config()
server = RabbitMq(serverobj)
server.publish()