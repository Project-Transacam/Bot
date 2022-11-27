from django.urls import path
from . views import *


app_name="telegrambot"

urlpatterns =[
    path('send/',Bot.as_view(),name='send_money'),
    # path('balance/',Bot.as_view(),name='check_balance'),
    # path('withdraw/',Bot.as_view(),name='withdraw_money'),
    # path('deposite/',Bot.as_view(),name='deposite_money'),
    # path('history/',Bot.as_view(),name='check_history'),
    # path('help/',Bot.as_view(),name='help'),
    # path('faq/',Bot.as_view(),name='faq'),
    # path('get_user_info/<str:pk>/',Bot.as_view(),name='receiver_info'),
]