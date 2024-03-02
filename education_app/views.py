from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class LessonList(APIView):
    def get(self, request, product_id):
        lessons = Lesson.objects.filter(product_id=product_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
