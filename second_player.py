#!/usr/bin/env python
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def user_interface():
    number = 0
    while (number != 1 and number != 2):
        print("Enter number 1 or 2:")
        value = input()
        number = int(value)
        print ("You entered: ", number)
        if number == 1:
            print ("send odd: 1")
            os.system('http -a admin:password123 --json POST http://127.0.0.1:8000/player2actions/ actionid=1 iname=0')
        elif number == 2:
            print ("send even: 2")
            os.system('http -a admin:password123 --json POST http://127.0.0.1:8000/player2actions/ actionid=2 iname=0')
        else: 
            print ("Wrong Input. Please try again. Enter number 1 or 2" )

def view_result():
    print ("Here are results:")
    os.system('http -a admin:password123 http://127.0.0.1:8000/gameresultsdisplays/')


def on_request(ch, method, props, body):
    message = str(body)
    print('Got message: ', message)

    user_interface()
    view_result()
    response = 'done'

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body = str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

if __name__ == '__main__': 
    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()
