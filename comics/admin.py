from django.contrib import admin
from comics.models import Autor, Comic, Editorial

#Registramos nuestras clases principales.
admin.site.register(Autor)
admin.site.register(Comic)
admin.site.register(Editorial)




# Register your models here.
