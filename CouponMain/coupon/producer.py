import pika , json

def publish(body):
    parameters = pika.ConnectionParameters('localhost', 5672)
    # parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.exchange_declare(exchange='coupon_main_exchange', exchange_type='fanout')
    channel.queue_declare(queue='backup_coupon',durable=True)
    channel.queue_declare(queue='redeem_coupon', durable=True)   
    channel.queue_declare(queue='saved_coupon', durable=True) 
    channel.queue_bind(exchange='coupon_main_exchange', queue='backup_coupon',routing_key='backup')
    channel.queue_bind(exchange='coupon_main_exchange', queue='redeem_coupon', routing_key='redeem')
    channel.queue_bind(exchange='coupon_main_exchange', queue='saved_coupon', routing_key='saved')
  
    print(json.dumps(body))
    channel.basic_publish(exchange='coupon_main_exchange',routing_key="backup" , body=json.dumps(body))
    connection.close()
