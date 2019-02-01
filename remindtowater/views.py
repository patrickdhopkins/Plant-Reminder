from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import get_user, get_user_model

from remindtowater.forms import AddPlantForm
from .models import Plant


def login_redirect(request):
    return HttpResponseRedirect(
        reverse('remindtowater:index',
                args=[request.user.username]))

class DetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'remindtowater/detail.html'
    model = Plant


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'remindtowater/index.html'
    context_object_name = 'plant_list'
    model = get_user_model()

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user).order_by('-pub_date')



class AddPlantView(LoginRequiredMixin, generic.FormView):
    template_name = 'remindtowater/add_plant.html'
    model = Plant
    form_class = AddPlantForm
    success_url = '/plant/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        plant = Plant()
        plant.name = form.cleaned_data['name']
        image = form.cleaned_data['image']
        plant.user = get_user(self.request)
        if image:
            plant.image = image
        plant.period = form.cleaned_data['period']
        plant.instructions = form.cleaned_data['instructions']
        print(plant.image)
        plant.save()
        return super(AddPlantView, self).form_valid(form)
