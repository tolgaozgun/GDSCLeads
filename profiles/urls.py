
from django.urls import path, include

from profiles.views import CommunityView, LeadView

urlpatterns = [
    path('community/<int:pk>', CommunityView.as_view(), name="view_community"),
    path('community/<int:pk>/edit', CommunityView.as_view(), name="edit_community"),
    path('community/<int:pk>/create', CommunityView.as_view(), name="create_community"),
    path('community/<int:pk>/delete', CommunityView.as_view(), name="delete_community"),

    path('lead/<int:pk>', LeadView.as_view(), name="view_lead"),
    path('lead/<int:pk>/edit', LeadView.as_view(), name="edit_lead"),
    path('lead/<int:pk>/create', LeadView.as_view(), name="create_lead"),
    path('lead/<int:pk>/delete', LeadView.as_view(), name="delete_lead"),

]