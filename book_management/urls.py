from django.urls import path
from books.views import BookListCreateView, BookDetailView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book Management API",
        default_version='v1',
        description="Book Management App",
        contact=openapi.Contact(email="bipin94179@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('book/', BookListCreateView.as_view(), name='book-list-create'),
    path('book/<str:isbn>/', BookDetailView.as_view(), name='book-detail'),
]

