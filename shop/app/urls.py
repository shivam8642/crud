from django.urls import path
from app import views
from .views import ShowStudent,Student_form_data,Student_create,UpdateView
urlpatterns = [
path('',views.create,name="create"),
path('delete/<int:id>',views.delete,name="delete"),
path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
path('edit_data/<int:id>',views.edit_data,name="edit_data"),
path('update_item/<int:id>',views.update_item,name="update_item"),
path('search',views.search,name="search"),
path('ShowStudent',ShowStudent.as_view(),name="ShowStudent"),
path('Student_form_data',Student_form_data.as_view(),name="Student_form_data"),
path('Student_create',Student_create.as_view(),name="Student_create"),
path('UpdateView/<int:pk>',UpdateView.as_view(),name="UpdateView"),
path('Student_Delete/<int:pk>',views.Student_Delete.as_view(),name="Student_Delete")
]