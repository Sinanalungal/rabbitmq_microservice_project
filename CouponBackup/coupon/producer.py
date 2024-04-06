import pika
import json

def publish(body):
    try:
        parameters = pika.ConnectionParameters('localhost', 5672)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.exchange_declare(exchange='coupon_main_exchange', exchange_type='fanout')
        channel.queue_declare(queue='main_coupon', durable=True)
        channel.queue_declare(queue='redeem_coupon', durable=True)
        channel.queue_declare(queue='saved_coupon', durable=True)
        channel.queue_bind(exchange='coupon_main_exchange', queue='main_coupon', routing_key='main')
        channel.queue_bind(exchange='coupon_main_exchange', queue='redeem_coupon', routing_key='redeem')
        channel.queue_bind(exchange='coupon_main_exchange', queue='saved_coupon', routing_key='saved')
        print(json.dumps(body))
        channel.basic_publish(exchange='coupon_main_exchange', routing_key='main', body=json.dumps(body))
    except :
        print('some error happened')
    finally:
        connection.close()
