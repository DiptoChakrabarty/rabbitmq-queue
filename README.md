# rabbitmq-queue

![RabbitmQ](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOnSKwpjbIsBsO_5dZkDWHwNWfPtX-iqb9dg&usqp=CAU)

## About the Repository Code 

```sh

- The Repository contains two examples of using RabbitMq

- RabbitMQ is the most widely deployed open source message broker

- It is lightweight and easy to run 
```

## Instructions to run

```sh
 - Clone the repository
  git clone https://github.com/DiptoChakrabarty/rabbitmq-queue.git
  
 - Activate virtualenv or do without it your choice
   virtualenv venv --python=python3 

 - Install dependencies
   pip3 install -r requirements.txt
   
 - Run a rabbitmq server using docker using following command
   sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ** If you want your raabitmq container to not terminate after usage remove --rm
 
 - Go to locahost:15672 to view your rabbitmq server , default login are guest and guest
```

## Codes to Run

### Send and Receive Messages
![Producer&Consumer](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_DeffYvm_NJFW0K1gzTjp-F1Fc60xgDThuA&usqp=CAU)
```sh
 - After Starting your rabbitmq server we are going to send messages and receive messages from the queue
 - Messages sent will be stored in the queue hence releasing the current program or process
 - Messages will be received by the receiver code and displayed 
 
 Run python3 send.py  to send messages to the queue
 - A new queue will be formed 
 - Message will be present in the queue
 Run python3 receive.py to receive messages from queue
 - It will retreive the message from the queue
 
 You can run receive.py before also , queue will be formed in both cases

```

### Remote Procedure Calls (RPC)
![RPC](https://www.rabbitmq.com/img/tutorials/python-six.png)
```sh
- In this we make use of two queues 
- Client creates an anonymous  callback queue
- Client provides required details in the queue
- Server picks up the required data from the client queue and does its processing (in this case tf idf of a document)
- The processed result is retured in another queue from where it is retured to client

Run python3 server.py

Run client.py 
```









