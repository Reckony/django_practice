from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.meeting_detail, name='meeting_detail'),
    path('rooms', views.show_rooms, name='rooms'),
    path('rooms/<int:id>', views.room_detail, name='room_details')
]