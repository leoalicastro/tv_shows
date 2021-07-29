from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new_show', views.new_show),
    path('show/<int:show_id>', views.show),
    path('add_show', views.add_show),
    path('edit/<int:show_id>', views.edit_show),
    path('show/<int:show_id>/edit', views.edit),
    path('delete/<int:show_id>', views.delete)
]