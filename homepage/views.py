from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Job, Member
from .forms import NameForm
from django.views.generic import CreateView, ListView, DetailView


def members(request):
    myjobs = Job.objects.all().values()
    template = loader.get_template('index.html')
    context = {
      'myjobs': myjobs,
    }
    return HttpResponse(template.render(context, request))


def get_name(request):
    submitted = False
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            template = loader.get_template('form_success.html')
            context = {
                'form': form,
            }
            return HttpResponseRedirect('/data?=submittedTrue')
    else:
        form = NameForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True

        return render(request, 'form_success.html', {'form': form, 'submitted': submitted})


class JobListView(ListView):
    model = Job
    template_name = 'all_jobs.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobListView, self).get_context_data(*args, **kwargs)
        context['myjobs'] = Job.objects.all()
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
        return context

    def get_success_url(self):
        return self.request.path
