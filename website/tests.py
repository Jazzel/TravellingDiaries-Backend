from django.test import TestCase
from website.models import Page

# Create your tests here.
class WebsiteTests(TestCase):
    def test_page_is_created_successfully(self):
        page = Page(
            name='Home',
            slug='home'
        )
        page.save()