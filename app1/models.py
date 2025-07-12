from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=8)
    st_img=models.ImageField(upload_to='st_pics/')
    email=models.EmailField()

    def __str__(self) -> str:
        return f'{self.name}'
    
