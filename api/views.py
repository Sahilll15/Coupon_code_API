from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Coupon
from .serializers import CouponSerializer

@api_view(['GET'])
def getData(request):
    data = Coupon.objects.all()
    serializer = CouponSerializer(data, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDataById(request, pk):
    try:
        coupon = Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        return Response({'error': 'Coupon not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CouponSerializer(coupon, context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def createData(request):
    serializer = CouponSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateData(request, pk):
    try:
        coupon = Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        return Response({'error': 'Coupon not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CouponSerializer(coupon, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteData(request, pk):
    try:
        coupon = Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        return Response({'error': 'Coupon not found'}, status=status.HTTP_404_NOT_FOUND)

    coupon.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
