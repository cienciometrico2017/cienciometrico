from django.conf.urls import url
from app.principal1.views import inicio,produccion,similares,sesiones
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',login_required(inicio), name="inicios"),
    url(r'^cientifica$',login_required(produccion), name="produccions"),
    url(r'^similares$',login_required(similares), name="similars"),
    url(r'^sesion$',login_required(sesiones), name="sesion"),
]