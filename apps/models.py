from django.db import models

class Vidi(models.Model):
    class Meta:
        verbose_name='виды'
        verbose_name_plural='виды'
    vidi=models.CharField('виды',max_length=100)

    def __str__(self):
            return self.vidi    

class Cotegory(models.Model):
    class Meta:
        verbose_name='котегория'
        verbose_name_plural='котегория'
    cotegory=models.CharField('котегория',max_length=100)

    def __str__(self):
        return self.cotegory

class Size(models.Model):
    class Meta:
        verbose_name= 'размер'
        verbose_name_plural= 'размер'
    size=models.CharField('размер',max_length=20)

    def __str__(self):
        return self.size
    
class Color(models.Model):
    class Meta:
        verbose_name='цвет'
        verbose_name_plural='цвет'
    color=models.CharField('цвет',max_length=30)

    def __str__(self):
        return self.color
    
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(verbose_name='Slug')
    text=models.TextField(max_length=255,blank=True, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    count=models.DecimalField(max_digits=10, decimal_places=2)
    # size=models.ManyToManyField(Size,verbose_name='размер',blank=True,null=True)
    # color=models.ForeignKey(Color,on_delete=models.CASCADE,verbose_name='цвет')
    discount=models.PositiveIntegerField(default=0,blank=True, null=True)
    cotegory=models.ForeignKey(Cotegory, on_delete=models.CASCADE,verbose_name='котегория')
    vidi=models.ForeignKey(Vidi, on_delete=models.CASCADE, verbose_name='виды',blank=True, null=True)
    isActive=models.BooleanField('доступно',default=True,blank=True, null=True)
    image = models.ImageField('Фотография', upload_to='posts/', blank=True, null=True)
    
    def __str__(self):
        return self.title 
