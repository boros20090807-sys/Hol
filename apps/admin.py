from django.contrib import admin 
from .models import Post,Size,Color,Cotegory,Vidi

@admin.register(Vidi)
class VidiAdmin(admin.ModelAdmin):
    list_displey=("vidi",)

@admin.register(Cotegory)
class CotegoryAdmin(admin.ModelAdmin):
    list_displey=("Cotegory",)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display=("size",)
    
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=("color",)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','slug','isActive')
    search_fields = ('title',)
    list_filter = ('isActive',)
    readonly_fields = ('isActive',)

