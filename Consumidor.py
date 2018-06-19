import pika
import sys
import time
import progressbar
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='processing',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

routing_key = sys.argv[1]
channel.queue_bind(exchange='processing',
                   queue=queue_name,
                   routing_key=routing_key)

print('[*] Esperando tarefas para processamento.')

def callback(ch, method, properties, body):
    print "[x] Processando a tarefa: " + body
    for i in progressbar.progressbar(xrange(random.randint(150, 250))):
        time.sleep(0.1)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
