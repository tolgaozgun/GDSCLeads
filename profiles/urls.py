
from django.urls import path, include

from profiles.views import CommunityView, LeadView, EventView, CityView, VenueView

urlpatterns = [
    path('community/<int:pk>', CommunityView.as_view(), name="view_community"),
    path('community/<int:pk>/edit', CommunityView.as_view(), name="edit_community"),
    path('community/<int:pk>/create', CommunityView.as_view(), name="create_community"),
    path('community/<int:pk>/delete', CommunityView.as_view(), name="delete_community"),

    path('member/<int:pk>', LeadView.as_view(), name="view_member"),
    path('member/<int:pk>/edit', LeadView.as_view(), name="edit_member"),
    path('member/<int:pk>/create', LeadView.as_view(), name="create_member"),
    path('member/<int:pk>/delete', LeadView.as_view(), name="delete_member"),

    path('event/<int:pk>', EventView.as_view(), name="view_event"),
    path('event/<int:pk>/edit', EventView.as_view(), name="edit_event"),
    path('event/<int:pk>/create', EventView.as_view(), name="create_event"),
    path('event/<int:pk>/delete', EventView.as_view(), name="delete_event"),

    path('city/<int:pk>', CityView.as_view(), name="view_city"),
    path('city/<int:pk>/edit', CityView.as_view(), name="edit_city"),
    path('city/<int:pk>/create', CityView.as_view(), name="create_city"),
    path('city/<int:pk>/delete', CityView.as_view(), name="delete_city"),

    path('venue/<int:pk>', VenueView.as_view(), name="view_venue"),
    path('venue/<int:pk>/edit', VenueView.as_view(), name="edit_venue"),
    path('venue/<int:pk>/create', VenueView.as_view(), name="create_venue"),
    path('venue/<int:pk>/delete', VenueView.as_view(), name="delete_venue"),

]