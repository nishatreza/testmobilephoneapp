from django.shortcuts import render, redirect
from .forms import MobileForm
from .models import Mobile


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
            form.save()
        return redirect('/list')


def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobile_list.html', {'mobiles': mobiles})


def mobile_delete(request, id):
    mobile = Mobile.objects.get(pk=id)
    mobile.delete()
    return redirect('/list')

