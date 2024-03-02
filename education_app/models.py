from django.db import models

from django.conf import settings

class Product(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    min_group_size = models.IntegerField()
    max_group_size = models.IntegerField()

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_accesses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')
    access_granted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user} -> {self.product}'
    
class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Group(models.Model):
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='enrolled_groups')
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name
    
    @property
    def student_count(self):
        return self.students.count()




