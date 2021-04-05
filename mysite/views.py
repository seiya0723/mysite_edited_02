from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TopView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.user.id)

        return render(request, 'mysite/top.html')


top = TopView.as_view()
