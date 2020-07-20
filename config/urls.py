# Django
from django.contrib import admin
from django.urls import path, include

# Owner
from accounts.api.v1.urls import account_v1_urls
from courses.api.v1.urls import courses_v1_urls


urlpatterns = [
    path('dacodes/', admin.site.urls),
    path('api/', include(account_v1_urls)),
    path('api/', include(courses_v1_urls)),
]
