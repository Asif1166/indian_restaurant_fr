from django.db import models

# Create your models here.

class Nos_Entrées(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Entrées')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Nans(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Nans')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Paratha(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Paratha')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Biriyani(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Biriyani')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Poulets(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Poulets')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Plats(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Plats')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class MENU(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Menu')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_légumes(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='légumes')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Crustacés(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Crustacés')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Frites(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Frites')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Viandes(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Viandes')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_sauces(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='sauces')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_desserts(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='desserts')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Boisson(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Boisson')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Cocktails(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Cocktails')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Lassis(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Lassis')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Nos_Chaudes(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Chaudes')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
class Café(models.Model):
    name = models.CharField(max_length=30, null=False)
    item_type = models.CharField(max_length=30, null=False, default='Café')
    description = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to='media/menu', null=False, blank=False)
    
    def __str__(self):
        return self.name
