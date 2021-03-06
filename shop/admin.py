from django.contrib import admin

from .models import Category, Product, Callback, Banner, Testominal
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
#myModels = [Category, Product]

class CallbackAdmin(admin.ModelAdmin):
    list_display =['name',  'phone','description','active','created_at' ]
    list_filter = [ 'created_at']
    list_editable = ['active']
    


admin.site.register(Callback, CallbackAdmin)

class BanerAdmin(admin.ModelAdmin):
	list_display=['name','description']

admin.site.register(Banner,BanerAdmin)

class TestominalAdmin(admin.ModelAdmin):
	list_display=['name']

admin.site.register(Testominal,TestominalAdmin)