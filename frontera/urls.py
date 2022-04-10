from django.urls import path

from .views import LanguageView

urlpatterns = [
    path('frontera/languages/', LanguageView.as_view({
        'get': 'list',
    }))
]
