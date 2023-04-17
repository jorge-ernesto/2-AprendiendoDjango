from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio web con Django | Victor Robles</h1>
<hr>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>
<hr>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        </p>Años hasta el 2050:</p>
        <ul>
    ""

    year = 2022
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{year}</li>"
        year += 1
    html += "</ul>"
    """
    year = 2022
    hasta = range(year, 2051)

    nombre = 'Victor Robles 2'
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, "index.html", {
        'title': 'Inicio 2',
        'mi_variable': 'Soy un dato que en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, "hola_mundo.html")

def pagina(request, redirigir=0):
    if redirigir == 1:
        # return redirect("/inicio/")
        # return redirect("/contacto-dos/Victor/Robles/")
        return redirect("contacto", nombre="Victor", apellidos="Robles")

    return render(request, "pagina.html", {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "El nombre completo es:"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def create_article(request):
    return render(request, 'create_article.html')

def save_article(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        if len(title) <= 5:
            return HttpResponse("El titulo es muy pequeño")

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()
        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")

def create_full_article(request):
    if request.method == 'POST':
        form = FormArticle(request.POST)

        if form.is_valid():
            data_form = form.cleaned_data

            title = data_form['title']  # data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            # Crear mensaje flash (session que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')
    else:
        form = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': form
    })

def articulo(request):
    try:
        # articulo = Article.objects.get(pk=6)
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()
    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
    # ---- ORM en Django ----
    # articulos = Article.objects.all()
    # articulos = Article.objects.values_list('id', 'title', 'content', 'public', 'image')
    # articulos = Article.objects.order_by('id') # Order by
    # articulos = Article.objects.order_by('-id')
    # articulos = Article.objects.order_by('id')[0:1] # Order by and Limit 1
    # articulos = Article.objects.order_by('id')[:3]
    # articulos = Article.objects.order_by('id')[3:10]
    articulos = Article.objects.filter(public='1').order_by('-id')

    # Lookup de modelo Article
    # articulos = Article.objects.filter(title="Batman", id=6) # Where
    # articulos = Article.objects.filter(title__contains="articulo") # Parecido a LIKE
    # articulos = Article.objects.filter(title__exact="articulo") # Where
    # articulos = Article.objects.filter(title__iexact="Articulo") # Where sin case sensitive
    # articulos = Article.objects.filter(id__gt=12) # Greater than
    # articulos = Article.objects.filter(id__lt=12) # Less than
    # articulos = Article.objects.filter(id__lte=12, title__contains="articulo") # Less than or equal to
    # articulos = Article.objects.filter(id__lte=12, title__contains="articulo") # Less than or equal to AND LIKE
    # articulos = Article.objects.filter( Q(title__contains="2") | Q(public=True) ) # OR en consultas con el ORM

    # articulos = Article.objects.filter(
    #     title="Articulo",
    #     public=True
    # )

    # articulos = Article.objects.filter(
    #     title="Articulo"
    # ).exclude(
    #     public=True
    # )

    # ---- SQL en Django ----
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Articulo 2' AND public = 0")

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.delete()
    return redirect('articulos')
