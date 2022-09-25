
from django.urls import path, include

from panel.views import NotFoundView, IndexView, ChartsView

urlpatterns = [
    path('404', NotFoundView.as_view(), name="not_found"),
    path('charts', ChartsView.as_view(), name="charts_view"),
    path('', IndexView.as_view(), name="panel_index"),

]