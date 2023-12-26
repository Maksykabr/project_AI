from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('', views.chat_view, name='chat_view'),
    # path('get_chat_response/', views.get_chat_response, name='get_chat_response'),
    path('', views.chatbot, name='chatbot'),
]