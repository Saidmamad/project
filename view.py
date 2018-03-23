from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tours.forms import CreateTourForm, SearchTourForm
from tours.models import Tour, Destination#, TourOperator
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings


def search_tours(request):
    if request.method == 'GET':
        form = SearchTourForm(request.GET)
        if form.is_valid():
            Country = form.cleaned_data['Country']
            Type = form.cleaned_data['Type']
            Destination = form.cleaned_data['Destination']
            StartDate = form.cleaned_data['StartDate']

            tours = Tour.objects.filter(Q(Country__icontains = Country)|
                                Q(Type__exact = int(Type))|
                                Q(Destination__exact = int(Destination))|
                                Q(StartDate__gte = int(StartDate)))

            return render(request, 'tours/search_tours.html', {
                'tours': tours,
                'media_url': settings.MEDIA_URL,
                'form':form,
            })

    else:
        form = SearchTourForm()

    tours = Tour.objects.filter(Available = True)


    return render(request, 'tours/search_tours.html', {
        'tours': tours,
        # 'media_url': settings.MEDIA_URL,
        'form':form,
    })
