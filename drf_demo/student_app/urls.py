from django.urls import path
from .views import create_student, update_student, delete_student, view_students, view_by_id

urlpatterns = [

    path('create/', create_student),

    path('update/<int:id>/', update_student),

    path('delete/<int:id>/', delete_student),

    path('view/', view_students),

    path('view/<int:id>/', view_by_id),

]
