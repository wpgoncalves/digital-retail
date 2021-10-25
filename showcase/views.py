from django.shortcuts import render, redirect
from showcase.models import Products, Newsletter


# Create your views here.
def showcase(request):
    # noinspection PyUnresolvedReferences
    products = Products.objects.filter(discontinued=False).order_by('name')
    status = request.GET.get('status')

    return render(request, 'showcase.html', {'status': status, 'products': products})


def valida_newsletter(request):
    email = str(request.POST.get('email'))

    # noinspection PyUnresolvedReferences
    registred = Newsletter.objects.filter(email=email)

    if len(email.strip()) > 0:
        if len(registred) > 0:
            return redirect('/showcase/?status=2')
        else:
            # noinspection PyBroadException
            try:
                newsletter = Newsletter(email=email)
                newsletter.save()
                return redirect('/showcase/?status=3')
            except Exception:
                return redirect('/showcase/?status=4')
    else:
        return redirect('/showcase/?status=1')
