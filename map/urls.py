
from django.urls import path, include

from map.views import IndexView, LeadApiView, CommunityMapView, LeadMapView, EventMapView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('map/leads', LeadMapView.as_view(), name="map_leads"),
    path('map/communities', CommunityMapView.as_view(), name="map_communities"),
    path('map/events', EventMapView.as_view(), name="map_events"),
    path('api/lead/<int:pk>', LeadApiView.as_view(), name="api_lead")


]