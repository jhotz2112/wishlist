from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishes_index, name='wishes_index'),
    path('wishes/create/', views.WishesCreate.as_view(), name='wishes_create'),
    path('wishes/<int:pk>/delete/', views.WishesDelete.as_view(), name='wishes_delete')
]