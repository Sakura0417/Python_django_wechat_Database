from rest_framework import serializers
from .models import JDcommodityInfo


class JDSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = JDcommodityInfo
        # 和"__all__"等价
        fields = '__all__'