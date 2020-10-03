from rest_framework import serializers
from users.models import User, Profile, Address

class UserProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Profile
        fields = ('phoneNumber','gender','DateOfBirth')
    

class AddressSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Address
        fields = '__all__'
    
    
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email','password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        profile_data = validated_data.pop('profile')
        Profile.objects.create(user=user, **profile_data)
        return user    


class ProfileSerializer(serializers.ModelSerializer): 
    friends = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    permanentAddress = serializers.SerializerMethodField()
    companyAddress = serializers.SerializerMethodField()
    isFriend = serializers.SerializerMethodField()
  
    class Meta:
        model = Profile
        fields = ('name','phoneNumber','gender','DateOfBirth','friends','image','companyAddress','permanentAddress','isFriend')

    def get_friends(self, obj):
        return obj.friends.count()
    
    def get_name(self, obj):
        return obj.user.username

    def get_permanentAddress(self, obj):
        try:
            return obj.comAddress.street
        except:
            return None
    
    def get_companyAddress(self, obj):
        try:
            return obj.comAddress.street
        except:
            return None

    def get_isFriend(self, obj):
        request = self.context.get('request')
        if request in obj.friends.all():
            return True
        else:
            return False

