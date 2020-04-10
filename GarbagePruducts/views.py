from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import JDcommodityInfo
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
from .serializers import JDSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def commodity_list(request,format=None):
    if request.method == 'GET':
        commodity = JDcommodityInfo.objects.all()
        serializer = JDSerializer(commodity, many=True)
        print("get方式*************")
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)

