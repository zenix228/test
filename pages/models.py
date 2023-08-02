from django.db import models

class clothe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='clothe/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
class product1(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='clothe/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class product2(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='clothe/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']

class product3(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='clothe/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        
class product4(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='clothe/%Y/%m/%d',blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']