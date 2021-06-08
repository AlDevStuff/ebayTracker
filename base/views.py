from django.shortcuts import render
from .forms import MainForm
from .models import Item
from django.conf import settings
from django.core.mail import EmailMessage


# Create your views here.


def home(request):
    form = MainForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            product_url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('receiver_email')
            targetPRICE = form.cleaned_data.get('target_price')

            body = f'This email confirms that you will be notified when {product_url} is at or below ${targetPRICE}. Thank you for using Ebay Price Alerter!'
            email = EmailMessage('Ebay Price Alerter Confirmation', body, settings.EMAIL_HOST_USER, to=[email], )
            email.fail_silently = False
            email.send()
            print(f'Confirmation email has been sent to {email}')

    form = MainForm()

    queryset = Item.objects.all()

    context = {'queryset': queryset, 'form': form}
    return render(request, 'base/index.html', context)
