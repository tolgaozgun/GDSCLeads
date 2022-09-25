from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoggedInView(View, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect'


class IndexView(LoggedInView):
    def get(self, request):
        return render(request, "panel/index.html")


class NotFoundView(LoggedInView):
    def get(self, request):
        return render(request, "panel/404.html")


class ChartsView(LoggedInView):
    def get(self, request):
        return render(request, "panel/layout-static.html")