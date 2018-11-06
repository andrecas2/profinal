from django.conf.urls import url
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
#urls de las vistas y manteminento de la tabla comic
    url(r'^$', views.listado_comics, name ='listado_comics'),
    url(r'^comic/nueva/$', views.comic_nueva, name='comic_nueva'),
    url(r'^comic/(?P<pk>[0-9]+)/detalle/$', views.detalle_comic, name='detalle_comic'),
    url(r'^comic/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_comic, name='eliminar_comic'),
    url(r'^comic/(?P<pk>[0-9]+)/editar/$', views.editar_comic, name='editar_comic'),
    ]
