from rest_framework import serializers
from .models import *

class MailSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Mail
        fields = '__all__'