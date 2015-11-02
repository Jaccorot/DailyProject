from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from todolist.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
        self.assertTrue(response.content.strip().startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>Todo List</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
