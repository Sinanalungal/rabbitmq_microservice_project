import pika
import json
import time
from django.core.exceptions import ObjectDoesNotExist

def callback(ch, method, properties, body):
    from .serializer import ProductSerializer
    from .models import Product

    print('Message received')
    message = body.decode('utf-8')
    message_dict = json.loads(message)
    
    coupon_code = message_dict['couponcode']
    
    try:
        product_instance = Product.objects.get(couponcode=coupon_code)
        print('Updating existing product')
    except ObjectDoesNotExist:
        product_instance = None

    if product_instance:
        serializer = ProductSerializer(instance=product_instance, data=message_dict)
    else:
        product_instance = Product(couponcode=coupon_code)
        serializer = ProductSerializer(instance=product_instance, data=message_dict)

    if serializer.is_valid():
        product_instance = serializer.save()  
        print(f" [x] Product saved: {product_instance}")
    else:
        print(" [x] Invalid message format:", serializer.errors)

def consumerfunction():
    params = pika.ConnectionParameters('localhost', 5672)
    
    while True:
        try:
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            channel.exchange_declare(exchange='coupon_main_exchange', exchange_type='fallout')
            channel.queue_declare(queue='saved_coupon', durable=True)
            channel.queue_bind(exchange='coupon_main_exchange', queue='saved_coupon', routing_key='saved')
            channel.basic_consume(queue='saved_coupon', on_message_callback=callback, auto_ack=True)
            time.sleep(2)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except:
            print('main is not available')
            try:
                
                params = pika.ConnectionParameters('localhost', 5672)
                connection = pika.BlockingConnection(params)
                channel = connection.channel()
                channel.exchange_declare(exchange='coupon_main_exchange', exchange_type='fanout')
                channel.queue_declare(queue='saved_coupon', durable=True)
                channel.queue_bind(exchange='coupon_main_exchange', queue='saved_coupon', routing_key='saved')
                channel.basic_consume(queue='saved_coupon', on_message_callback=callback, auto_ack=True)
                print(' [*] Waiting for messages. To exit press CTRL+C')
                time.sleep(2)
                channel.start_consuming()
            except:
                print('backup is not available')
                time.sleep(10)
                


