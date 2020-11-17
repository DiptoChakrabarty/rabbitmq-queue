import pika 

connection =  pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="sample")
channel.basic_publish(exchange='',
            routing_key="sample",
            body="sample body")
print("Sample Message Sent to rabbitmq")
connection.close()
print("Connection closed")