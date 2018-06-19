import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='processing',
                         exchange_type='direct')

while True:
    routing_key, message = raw_input("Digite o comando que deseja executar: ").split(" ")
    channel.basic_publish(exchange='processing',
                          routing_key=routing_key,
                          body=message)
    print("[x] Enviado para o consumidor %r a tarefa %r" % (routing_key, message))
