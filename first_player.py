#!/usr/bin/env python
import os
import pika
import uuid

def user_interface():
    number = 0
    while (number != 1 and number != 2):
        print("Enter number 1 or 2:")
        value = input()
        number = int(value)
        print ("You entered: ", number)        
        if number == 1:
            print ("send odd: 1")
            os.system('http -a admin:password123 --json POST http://127.0.0.1:8000/player1actions/ actionid=1 iname=0')
        elif number == 2:
            print ("send even: 2")
            os.system('http -a admin:password123 --json POST http://127.0.0.1:8000/player1actions/ actionid=2 iname=0')
        else: 
            print ("Wrong Input. Please try again. Enter number 1 or 2" )


def view_result():
    print ("Here are results:")
    os.system('http -a admin:password123 http://127.0.0.1:8000/gameresultsdisplays/')

class GameRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)


if __name__ == '__main__':
    while 1:
        user_interface()
        game_rpc = GameRpcClient()

        print(" [x] Requesting Second Player Step")
        response = game_rpc.call('yourTurn')
        print(" [.] Got %s" % response)
        view_result()


