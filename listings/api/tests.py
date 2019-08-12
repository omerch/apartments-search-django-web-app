from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class ListingAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testcfeuser', email='test@test.com')
        user_obj.set_password('somerandompassword')
        user_obj.save()
        listing = Listing.objects.create(
            user=user_obj, 
            title='new title apartment', 
            description='This is test apartment') 


    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)