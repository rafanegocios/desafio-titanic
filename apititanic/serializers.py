from  rest_framework import serializers

class SurvivalSerializers(serializers.Serializer):
    PassengerId = serializers.IntegerField()
    Survived = serializers.BooleanField()
    Pclass = serializers.IntegerField()
    Name = serializers.CharField(max_length=255)
    Sex = serializers.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    Age = serializers.FloatField(allow_null=True)  
    SibSp = serializers.IntegerField()
    Parch = serializers.IntegerField()
    Ticket = serializers.CharField(max_length=50)
    Fare = serializers.FloatField()
    Cabin = serializers.CharField(max_length=50, allow_null=True) 
    Embarked = serializers.ChoiceField(allow_null=True, choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')])
        