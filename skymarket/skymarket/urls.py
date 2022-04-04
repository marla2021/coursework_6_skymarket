from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# TODO здесь необходимо подклюючит нужные нам urls к проекту
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("redoc-tasks/", include("redoc.urls")),
    path("", include("users.urls")),
    path("", include("ads.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)