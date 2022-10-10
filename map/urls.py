
from django.urls import path, include

from map.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('forgot_password', ForgotPasswordView.as_view(), name="forgot_password"),
    path('map/leads', LeadMapView.as_view(), name="map_leads"),
    path('map/communities', CommunityMapView.as_view(), name="map_communities"),
    path('map/events', EventMapView.as_view(), name="map_events"),
    path('api/lead/<int:pk>', LeadApiView.as_view(), name="api_lead"),
    path('api/event/<int:pk>', EventApiView.as_view(), name="api_event"),
    path('api/community/<int:pk>', CommunityApiView.as_view(), name="api_community"),


]