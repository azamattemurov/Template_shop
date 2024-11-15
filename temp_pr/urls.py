from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "Online Market"
admin.site.index_title = "Hush kelibsiz !..."

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('', include('resume.urls', namespace='resume')),
    path('home', include('pages.urls', namespace='pages')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('bot/', include('telegram_bot.urls', namespace='bot')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
