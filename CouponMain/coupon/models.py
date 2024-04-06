from django.db import models
import uuid , json
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .producer import publish



class Product(models.Model):
    couponcode=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coupontitle = models.CharField(max_length=200)
    redeemed=models.BooleanField(default=False)
    saved=models.BooleanField(default=False)

# @receiver(post_save, sender=Product)
# def product_saved(sender, instance, created, **kwargs):
#     if created:
#         print(f"New product created with coupon code: {instance}")

#         serialized_data = json.dumps({
#             'couponcode': str(instance.couponcode),
#             'coupontitle': instance.coupontitle,
#             'redeemed': instance.redeemed,
#             'saved': instance.saved,
#         })

#         publish(body=serialized_data)
        
#     else:
#         serialized_data = json.dumps({
#             'couponcode': str(instance.couponcode),
#             'coupontitle': instance.coupontitle,
#             'redeemed': instance.redeemed,
#             'saved': instance.saved,
#         })

#         publish(body=serialized_data)
