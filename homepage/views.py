from .models import Job, Member
from django.views.generic import CreateView, ListView, DetailView
import requests
from config import ADMIN, TOKEN
from django.utils.translation import gettext_lazy as _


class JobListView(ListView):
    model = Job
    template_name = 'all_jobs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobListView, self).get_context_data(*args, **kwargs)
        context['myjobs'] = _(Job.objects.all())
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = "job_details.html"


class CreateMemberView(CreateView):
    model = Member
    template_name = 'member_djangoform.html'
    fields = ["name", "phone_number", "email"]

    def get_context_data(self, *args, **kwargs):
        context = super(CreateMemberView, self).get_context_data(*args, **kwargs)
        context['myjobs'] = Job.objects.order_by('created_at')[:3]
        print(context['myjobs'])
        return context

    def get_success_url(self):
        text = f'Зарегистрирован новый клиент!\n/admin'
        for chat_id in ADMIN:
            base_tg_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
            requests.get(url=base_tg_url)
        return self.request.path