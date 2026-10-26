from django.db import models

# Create your models here.

class Article(models.Model): #Entidad

    #Propiedades
    #cadena de texto corta con un límite máximo de 150 caracteres
    title = models.CharField(max_length=150, verbose_name="Titulo")

    #campo de texto largo sin límite estricto para almacenar el cuerpo del texto
    content = models.TextField(verbose_name="Contenido")

    #almacena la ruta del archivo, con 'null' como valor por defecto si no se carga ninguna
    image = models.ImageField(default='null',verbose_name="Imagen", upload_to="articles")

    #campo booleano (True/False) para indicar si el artículo está público o en borrador
    public = models.BooleanField(verbose_name="¿Publicado?")

    #asigna de forma automática la fecha y hora exactas únicamente al crear el registro por primera vez
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado")

    #actualiza automáticamente la fecha y hora cada vez que el registro es modificado y guardado
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Modificado")

    class Meta:
        #poner nombre en singular
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title} {public}"

class Category(models.Model): #Entidad
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        #poner nombre en singular
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"