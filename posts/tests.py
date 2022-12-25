from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostTest( TestCase ):
    # test 1
    @classmethod
    def setUpTestData( cls ):
        cls.post = Post.objects.create( text="This is a test!" )
    
    # test 2
    def test_model_content(self):
        self.assertEqual( self.post.text, "This is a test!" )

    # test 3
    def test_url_exists_at_correct_location( self ):
        response = self.client.get("/")
        self.assertEqual( response.status_code, 200 )

    #test 4
    # def test_url_available_by_name(self):
    #     response = self.client.get( reverse("home") )
    #     self.assertEqual( response.status_code, 200 )

    # # test 5
    # def test_template_name_correct(self):
    #     response = self.client.get( reverse("home") )
    #     self.assertTemplateUsed( response, "home.html" )

    # # test 6
    # def test_template_content(self):
    #     response = self.client.get( reverse("home") )
    #     self.assertContains( response, "This is a test!" )

    # test_homepage
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual( response.status_code, 200 )
        self.assertTemplateUsed( response, "home.html" )
        self.assertContains( response, "This is a test!" )

    
