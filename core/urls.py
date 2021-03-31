from django.urls import path

from .views import *

from django.conf.urls import handler404, handler500
from core import views


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact),
    path('produto/<int:product_id>', product),
]

handler404 = views.error404
handler500 = views.error500
