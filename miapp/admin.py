from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    
    # mostrar campos de solo lectura
    readonly_fields = ('created_at', 'updated_at')
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el título del panel
admin.site.site_header = "Django ADSO - SENA"
admin.site.site_title = "Django ADSO - SENA"
admin.site.index_title = "Panel de Gestión"