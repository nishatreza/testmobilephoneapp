from django.shortcuts import render, redirect
from .forms import MobileForm
from .models import Mobile
import json
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.


def mobile_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = MobileForm()
        else:
            mobile = Mobile.objects.get(pk=id)
            form = MobileForm(instance=mobile)

        return render(request, 'mobile_form.html', {'form': form})
    else:
        if id == 0:

            form = MobileForm(request.POST)
        else:
            mobile = Mobile.objects.get(pk=id)
            form = MobileForm(request.POST, instance=mobile)

        if form.is_valid():
            brand_name = form.cleaned_data['brand_name']
            model = form.cleaned_data['model']
            color = form.cleaned_data['color']
            jan_code = form.cleaned_data['jan_code']
            if Mobile.objects.filter(brand_name=brand_name).exists():
                messages.info(request, 'Brand name taken!')
                return redirect('/')
            elif Mobile.objects.filter(model=model).exists():
                messages.info(request, 'Model No. taken!')
                return redirect('/')
            elif Mobile.objects.filter(color=color).exists():
                messages.info(request, 'Color taken!')
                return redirect('/')
            elif Mobile.objects.filter(jan_code=jan_code).exists():
                messages.info(request, 'Jan Code taken!')
                return redirect('/')
            else:
                form.save()
            return redirect('/list')


def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobile_list.html', {'mobiles': mobiles})


def mobile_delete(request, id):
    mobile = Mobile.objects.get(pk=id)
    mobile.delete()
    return redirect('/list')


def search_mobile(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        mobiles = Mobile.objects.filter(model__startswith=search_str) | Mobile.objects.filter(jan_code__startswith=search_str)

        data = mobiles.values()

        return JsonResponse(list(data), safe=False)



