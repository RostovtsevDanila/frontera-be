from django.urls import path

from .views import LanguageView, CategoryView

urlpatterns = [
    path('frontera/languages/', LanguageView.as_view({
        'get': 'list',
    })),
    path('frontera/categories/', CategoryView.as_view({
        'get': 'list',
    })),
]
