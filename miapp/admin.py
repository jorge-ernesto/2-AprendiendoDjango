'''
Estas líneas de código son parte de un archivo de configuración en Django
que se utiliza para administrar el panel de administración del sitio web.
A continuación, te explico lo que hace cada línea:

from django.contrib import admin              : esta línea importa el módulo de Django admin, que proporciona la funcionalidad para administrar el sitio web a través de un panel de administración.
from .models import Article, Category         : esta línea importa los modelos Article y Category desde el archivo models.py del directorio actual.

class ArticleAdmin(admin.ModelAdmin)          : esta línea define una clase llamada ArticleAdmin, que se utiliza para personalizar el formulario de administración de los artículos.
readonly_fields = ('created_at', 'updated_at'): esta línea define los campos created_at y updated_at como solo lectura en el formulario de administración.

admin.site.register(Article, ArticleAdmin)    : esta línea registra el modelo Article en el panel de administración y utiliza la clase ArticleAdmin para personalizar su formulario.
admin.site.register(Category)                 : esta línea registra el modelo Category en el panel de administración.

title = "Master en Python"                    : esta línea define la variable title con el valor "Master en Python".
subtitle = "Panel de gestión"                 : esta línea define la variable subtitle con el valor "Panel de gestión".
admin.site.site_header = title                : esta línea establece el título de la página de administración como title.
admin.site.site_title = title                 : esta línea establece el título de la pestaña del navegador como title.
admin.site.index_title = subtitle             : esta línea establece el título de la página de inicio del panel de administración como subtitle.
'''

'''
La forma en que importas los modelos en tu código depende
de la ubicación de los archivos y carpetas en tu proyecto Django.

Si la carpeta models está en la raíz de tu proyecto Django, entonces la importación correcta sería:
from models import Article, Category

Por otro lado, si la carpeta models está dentro de una aplicación de Django, entonces la importación correcta sería:
from miapp.models import Article, Category

Finalmente, si estás importando los modelos desde un archivo que se encuentra en la misma carpeta que la carpeta models, la importación correcta sería:
from .models import Article, Category
'''

from django.contrib import admin
from .models import Article, Category

# Register your models here.

# Configuracion extra en el panel
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configuracion del panel
title = "Master en Python"
subtitle = "Panel de gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
