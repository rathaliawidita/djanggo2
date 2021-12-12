from django.urls import path

from .views import index, add, cth_html, IndexCoba

urlpatterns = [
    path('hello_index', index, name='hello_index'),
    path('add/<int:no1>/<int:no2>', add, name='add'),
    path('coba_template', cth_html, name='contoh'),
    path('template_view_sample', IndexCoba.as_view(), name='template_view_sample'),
]