from django.contrib import admin
from django.urls import path, include

from apps.views import products_list_view, BaseTemplateView

# from apps.views import index_view, calculator

urlpatterns = [
    # path('Myme', index_view),

    # path('calculator', calculator)

    path('admin', admin.site.urls),

    path('', products_list_view),
    path('temp', BaseTemplateView.as_view())
]