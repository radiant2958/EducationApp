from rest_framework import serializers
from .models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

    def get_lessons_count(self, obj):
        return obj.lessons.count() 

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
