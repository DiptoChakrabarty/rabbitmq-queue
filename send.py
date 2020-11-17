import pika 

connection =  pika.BlockingConnection(pika.connectionParameters("localhost")
channel = connection.channel())

channel.queue_declare(queue="sample-queue")
channel.basic_publish(exchange='',
            routing_key="sample",
            body="sample body")
print("Sample Message Sent to rabbitmq")
connection.close()
print("Connection closed")