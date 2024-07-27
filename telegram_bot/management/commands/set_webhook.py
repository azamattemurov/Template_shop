from django.core.management.base import BaseCommand
import requests
from django.conf import settings

class Command(BaseCommand):
    help = 'Set webhook for the Telegram bot'

    def handle(self, *args, **options):
        TELEGRAM_API_URL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/setWebhook"
        payload = {
            "url": settings.TELEGRAM_WEBHOOK_URL
        }
        response = requests.post(TELEGRAM_API_URL, data=payload)
        self.stdout.write(self.style.SUCCESS(f'Set webhook: {response.json()}'))
