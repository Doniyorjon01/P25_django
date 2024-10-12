from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.models import Product


# def index_view(request):
#     return JsonResponse({
#         "Firstname": "Abduraximov",
#         "Lastname": "Doniyorjon",
#         "Phone_number": "88 708 22 27",
#         "Age": "19"
#     })
#
# def calculator(request):
#     global result
#     n1 = int(request.GET.get('num1'))
#     n2 = int(request.GET.get("num2"))
#     amal = request.GET.get("amal")
#     if amal == "add":
#         result = n1+n2
#     elif amal == "-":
#         result = n1-n2
#     elif amal == "*":
#         result = n1*n2
#     elif amal == "/":
#         result = n1/n2
#
#     return JsonResponse({"calculator":result})



def products_list_view(request):
    context = {
        "products" : Product.objects.all()
    }
    return render(request, 'apps/products_list.html', context=context)

class BaseTemplateView(TemplateView):
    template_name = 'apps/test.html'