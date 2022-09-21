
from django.urls import path, include

from map.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index")

]