from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from .models import Post,Cotegory

@receiver(pre_save, sender=Post)
def update_post_price(sender, instance, **kwargs):
    price = instance.price
    if 1000 < price <2000:
        discount=price * 5 /100
        price-=discount
    if 2000 < price <5000:
            discount=price * 15 /100
            price-=discount
    if price >5000:
            discount=price * 5 /100
            price-=discount
