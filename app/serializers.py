from rest_framework import serializers
from app.models import Persion, Cars


class PersionModelSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Persion
        fields = '__all__'


class CarsModelSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'