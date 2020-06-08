# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys

from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe

# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in the Developer Dashboard

# Using Django
@require_POST
@csrf_exempt
def webhook(request):
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        print("I'm at webhook try")
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        print("I'm at webhook except1")
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print("I'm at webhook except2")
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        print("I'm at webhook except3")
        return HttpResponse(content=e, status=400)

    # Set up webhook handler

    handler = StripeWH_Handler(request)

    # Map webhook events to handler functions

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get webhook event type from Stripe
    event_type = event['type']

    # If handler exists, get it from map otherwise use default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call event handler with event
    response = event_handler(event)
    print("I'm returning response")
    print(response)
    return response
