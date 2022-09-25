
from django.urls import path, include

from profiles.views import CommunityView, LeadView, EventView, CityView

urlpatterns = [
    path('community/<int:pk>', CommunityView.as_view(), name="view_community"),
    path('community/<int:pk>/edit', CommunityView.as_view(), name="edit_community"),
    path('community/<int:pk>/create', CommunityView.as_view(), name="create_community"),
    path('community/<int:pk>/delete', CommunityView.as_view(), name="delete_community"),

    path('lead/<int:pk>', LeadView.as_view(), name="view_lead"),
    path('lead/<int:pk>/edit', LeadView.as_view(), name="edit_lead"),
    path('lead/<int:pk>/create', LeadView.as_view(), name="create_lead"),
    path('lead/<int:pk>/delete', LeadView.as_view(), name="delete_lead"),

    path('event/<int:pk>', EventView.as_view(), name="view_event"),
    path('event/<int:pk>/edit', EventView.as_view(), name="edit_event"),
    path('event/<int:pk>/create', EventView.as_view(), name="create_event"),
    path('event/<int:pk>/delete', EventView.as_view(), name="delete_event"),

    path('city/<int:pk>', CityView.as_view(), name="view_city"),
    path('city/<int:pk>/edit', CityView.as_view(), name="edit_city"),
    path('city/<int:pk>/create', CityView.as_view(), name="create_city"),
    path('city/<int:pk>/delete', CityView.as_view(), name="delete_city"),

]