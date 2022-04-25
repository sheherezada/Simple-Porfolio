from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib import messages
from PROJECT.web.forms import CreateQuoteForm, ContactFormForm
from PROJECT.accounts.models import Profile, ProjectUser
from PROJECT.web.models import Projects, Portfolio, CV, ContactModel


def nav(request):
    return render(request, 'nav.html')


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_project():
    projects = Projects.objects.all()
    return projects


class IndexView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = ProjectUser
    template_name = 'dashboard.html'

    context_object_name = 'username'


def about_me(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,

    }
    return render(request, 'about-me.html', context)


def download(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        upload1 = request.FILES['upload']
        object = CV.objects.create(title=filename, upload=upload1)
        object.save()
    context = CV.objects.all()

    return render(request, 'download.html', {'context': context})


def success(request):
    details = ContactModel.objects.all()
    context = {
        'details': details
    }

    return render(request, 'success.html', context)


class CreateQuoteView(views.CreateView):
    template_name = 'quotes.html'
    form_class = CreateQuoteForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    success_url = reverse_lazy('success')


#

def tutorials(request):
    return render(request, 'tutorials.html')


#


def contact(request):
    if request.method == 'POST':

        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            messages.error(request, 'Please correct the error below.')
    form = ContactFormForm()
    context = {'form': form}

    return render(request, 'contact-form.html', context)


class PortfolioView(views.ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    queryset = Portfolio.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Portfolio.objects.all()

        return context


def portfolio_item(request):
    return render(request, 'portfolio-item.html')


def price(request):
    return render(request, 'price.html')


def careers(request):
    return render(request, 'careers.html')


def price_list(request):
    return render(request, 'price.html')
