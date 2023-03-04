
from django.contrib import admin
from django.urls import include, path

from hr import urls

urlpatterns = [
    # admin link
    path('admin/', admin.site.urls),
    # hr defualt links
    path('', include('hr.urls')),
    # path for login logout
    path('login/',include('django.contrib.auth.urls'))
]
