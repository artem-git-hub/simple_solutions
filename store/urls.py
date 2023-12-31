# urls.py

from django.urls import path
from .views import get_session_id, item_detail

urlpatterns = [
    path('buy/<int:item_id>/', get_session_id, name='get_session_id'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    # Другие маршруты
]
