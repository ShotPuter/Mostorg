import os
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('Изображение')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    

def get_upload_path(instance, filename):
    #  задаем название файла названием slug`а продукта
    filename = instance.slug + '.' + filename.split('.')[1]  
    return os.path.join('images/', filename)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', 
        on_delete=models.CASCADE
        )
    name = models.CharField('Название',max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = RichTextField('Описание',config_name='awesome_ckeditor')
    price = models.DecimalField("Цена",max_digits=10, decimal_places=2)
    available = models.BooleanField("Наличие",default=True)
    stock = models.PositiveIntegerField("Количество",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("Фото",upload_to=get_upload_path)
      
    STATUS_CHOICES = (('Лучшее', 'Лучшее'),
                    ('Скидка', 'Скидка'))
    status = models.CharField('Статус', max_length=8, choices=STATUS_CHOICES, blank=True )
    degree = models.PositiveIntegerField('Оценка (звезд)')

                    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Callback(models.Model):
    name = models.CharField('Имя',max_length=100)
    phone= models.CharField("Телефон", max_length=100)
    description=models.TextField("Пожелание")
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField("Обработано?", default=False)
    class Meta:
        verbose_name='Обратная связь'
        verbose_name_plural = 'Обратная связь'
    def __str__(self):
        return self.phone


class Banner(models.Model):
    name = models.CharField("Название/титл", max_length=300)
    description = RichTextField("Описание",config_name='awesome_ckeditor')
    image = models.ImageField("Изображение")

    class Meta:
        verbose_name='Банер'
        verbose_name_plural = 'Банера'

    
class Testominal(models.Model):
    name=models.CharField("Имя Фамилия", max_length=200)
    work=models.CharField("Должность",max_length=200,blank=True)
    text = models.TextField("Текст")
    image=models.ImageField("Фото")
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name
    
        