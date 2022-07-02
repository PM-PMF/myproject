import django.utils.timezone as tmz
from django.db import models
from django.urls import reverse


class Student(models.Model):
    
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email=models.EmailField()
    
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']
    
    
        
class Article(models.Model):
    pub_date = models.DateField(default=tmz.now())
    headline = models.CharField(max_length=200)
    short_content = models.TextField()
    last_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    
        
    def __str__(self):
        return self.headline


