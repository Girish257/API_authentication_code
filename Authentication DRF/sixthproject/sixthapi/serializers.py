from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True) # only for one field



    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')
    name =serializers.CharField(validators = [start_with_r])



    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll','city']  # for multiple
        # extra_kwargs = {'name':{'read_only': True}}  # another way



    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value
    

    # Object level validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm .lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data
    
    

        
    
    
    
   
