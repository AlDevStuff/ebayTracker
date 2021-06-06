from django.db import models
from .utils import linkParser
from django.conf import settings
from django.core.mail import EmailMessage


# Create your models here.
class Item(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200, blank=True)
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0, blank=True)
    target_price = models.FloatField(default=100000, blank=False)
    receiver_email = models.EmailField(max_length=100, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-updated']

    def save(self, *args, **kwargs):
        title, price = linkParser(self.url)
        old_price = self.current_price

        if self.current_price:
            if price != old_price:
                self.old_price = old_price
        else:
            self.old_price = 0

        # sends email if target price = old price
        body = f'''The Ebay product {self.url} has reached your target price of ${self.target_price}. Thus, we will stop notifying you. Thank you for using Ebay Price Alerter!\n\n\n
            Ebay Price Alerter :)
            '''
<<<<<<< HEAD
            
        # if self.old_price <= self.target_price and self.old_price != 0:
        if self.current_price <= self.target_price:
=======
#         if self.old_price <= self.target_price and self.old_price != 0:
          if self.current_price <= self.target_price:
>>>>>>> 5b5bea1c0e81d536339586bcf2b5544dfc3710d3
            email = EmailMessage('Ebay Price Alerter: Target Price Reached', body, settings.EMAIL_HOST_USER,
                                 to=[self.receiver_email], )
            email.fail_silently = False
            email.send()
            print(f'Price alert email has been sent to {self.receiver_email}')

            self.email_sent = True
            


        self.title = title
        self.current_price = price
        super().save(*args, **kwargs)
