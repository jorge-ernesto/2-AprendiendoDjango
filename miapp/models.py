from django.db import models

# Create your models here.

class Article(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    title      = models.CharField(max_length=150, verbose_name="Titulo")
    content    = models.TextField(verbose_name="Contenido")
    image      = models.ImageField(default='null', verbose_name="Miniatura", upload_to="articles")
    public     = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        # db_table          = "articulo"  # Especificar el nombre de la tabla que se creara en la migración
        verbose_name        = "Artículo"  # Manipular nombre en el panel
        verbose_name_plural = "Artículos"  # Manipular nombre en el panel
        # ordering          = ['-id']
        ordering            = ['-created_at']

    # Metodos magicos en Python
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # Metodo para devolver una representacion de cadena de su objeto (clase definida por el usuario)
    def __str__(self):
        if self.public == True:
            public = "Publicado"
        else:
            public = "Privado"
        
        # Formatear fecha
        # https://docs.python.org/es/dev/library/locale.html
        # https://ourcodeworld.co/articulos/leer/555/como-formatear-objetos-de-fecha-y-hora-en-la-vista-y-la-plantilla-en-django
        import locale
        locale.setlocale(locale.LC_ALL, 'es-ES')
        date = self.created_at.strftime('%d %B %Y - %H:%M')

        return f"{self.id}. {self.title} | {public} | {date}"

class Category(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    name        = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at  = models.DateField()

    class Meta:
        verbose_name        = "Categoria"
        verbose_name_plural = "Categorias"
