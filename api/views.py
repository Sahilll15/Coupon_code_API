from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Coupon
from .serializers import CouponSerializer
from rest_framework import status


@api_view(['GET'])
def getData(request):
    data = Coupon.objects.all()
    serializer = CouponSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createData(request):
    serializer = CouponSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
