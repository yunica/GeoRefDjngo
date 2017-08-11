from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    url(r'^mapa1/', include('mapa1.urls'), name='mapa1'),
}
