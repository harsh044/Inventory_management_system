from rest_framework.views import APIView
from .models import Inventory
from rest_framework.response import Response
from rest_framework import status
from .serializers import InventorySerializer
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('Inventory management system')
class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        products = Inventory.objects.filter(user_id=request.user.id).all()
        serializer = InventorySerializer(products, many=True)
        logger.info(f"Response Data: {serializer.data}")
        if serializer is None:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AddProduct(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = InventorySerializer(data=request.data)

        if serializer.is_valid():
            logger.info(f"Response Data: Product Add Successfully.")
            Inventory.objects.create(
                user=request.user,
                product_name=request.data.get('product_name',None),
                product_price=request.data.get('product_price',None),
                product_descriptiom=request.data.get('product_descriptiom',None),
                product_category=request.data.get('product_category',None)
            )
            return Response({"Messages":"Product Add Successfully."},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateProduct(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        id = pk
        product = Inventory.objects.filter(id=id,user_id=request.user.id).last()
        serilaizer = InventorySerializer(product,data=request.data)
        if serilaizer.is_valid():
            update_product = Inventory.objects.filter(user_id=request.user.id,id=id).update(
                product_name=request.data["product_name"],
                product_price=request.data["product_price"],
                product_descriptiom=request.data["product_descriptiom"],
                product_category=request.data["product_category"]
                )
            logger.info(f"Response Data: Product Update Successfully.")
            return Response({"Message":"Product Updated Successfully."},status=status.HTTP_200_OK)
        return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteProduct(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,pk):
        id = pk
        product = Inventory.objects.filter(id=id,user_id=request.user.id).last()
        if product is None:
            return Response({"Message":"Product Not Found."},status=status.HTTP_404_NOT_FOUND)
        logger.info(f"Response Data: Product Delete Successfully.")
        product.delete()
        return Response({"Message":"Product Delete Successfully."})
