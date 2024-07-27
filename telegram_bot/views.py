from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Telegram webhook request handling logic here
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})
