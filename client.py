import pika
import uuid

class ClientConfig():
    def __init__(self,host,queue):
        self.host = host
        self.queue =  queue

class TfIdfClient():
    def __init__(self):
        def __init__(self,config):
        self.config = config
        self.connection =  pika.BlockingConnection(pika.ConnectionParameters(host=self.config.host))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="",exclusive=True)

        self.callback_queue =  result.method.queue

        self.channel.basic_consume(
            queue = self.callback_queue,
            on_message_callback = self.on_response, auto_ack=True)
    
    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body
    
    def call(self,filename):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key = self.routing_key,
            properties = pika.BaiscProperties(
                reply_to = self.callback_queue,
                correlation_id =  self.corr_id,
            ),
            body = str(filename)
        )
        while self.response is None:
            self.connection.process_data_events()
        return self.response

