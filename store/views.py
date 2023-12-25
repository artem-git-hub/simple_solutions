from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from simple_solutions.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY

from store.models import Item

stripe.api_key = STRIPE_SECRET_KEY

@csrf_exempt
def get_session_id(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 10000),
        currency=item.currency,
    )

    return JsonResponse({'session_id': intent.client_secret})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_price_in_cents = int(item.price * 100)
    return render(request, 'item_detail.html', {'item': item, "item_price_in_cents": item_price_in_cents, "STRIPE_PUBLIC_KEY": STRIPE_PUBLIC_KEY})
