from django.conf.urls import url
from apps.ponencias.views import registro, eventos, libros, revistas
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^registrar$',registro, name="registroponencias"),
    url(r'^eventos$',eventos, name="registroeventos"),
    url(r'^libros$',libros, name="registrolibros"),
    url(r'^revistas$',revistas, name="registrorevista"),

]