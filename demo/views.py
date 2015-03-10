from django.views.generic import ListView
from .models import Notification


class Notifications(ListView):
    model = Notification
    template_name = 'home.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pk')[:5]

    def get_context_data(self,**kwargs):
        context = super(Notifications, self).get_context_data(**kwargs)
        print(self.request.user)
        print(self.request.session)
        return context
