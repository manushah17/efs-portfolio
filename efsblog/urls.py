from django.conf.urls import url, include
from django.contrib import admin
from portfolio.views import login_view, logout_view, register_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'', include('portfolio.urls', namespace='portfolio')),
   
]
