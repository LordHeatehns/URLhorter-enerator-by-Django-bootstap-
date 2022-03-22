from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from .models import Shorter
# Create your tests here.
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.shorter_url = reverse('shorter',args=['HGXp7e9'])
        Shorter.objects.create(
            created='12/8/2022',
            times_followed='1',
            long_url='https://geekflare.com/build-url-shortener-app-in-django/#anchor-creating-the-url-shortener-app' ,
            short_url='HGXp7e9',
        )
      

    def test_project_home_Get(self):

        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_project_home_POST(self):
        
        response = self.client.post(self.home_url,{
            'created':'12/8/2022',
            'times_followed':'1',
            'long_url':'https://geekflare.com/build-url-shortener-app-in-django/#anchor-creating-the-url-shortener-app' ,
            'short_url':'HGXp7e9',
        })

        self.assertEqual(response.status_code,200)
    
    def test_str_url(self):
       response = self.client.get(self.shorter_url)


       self.assertEqual(response.status_code, 302)
               
        
        


      

    

        



    

