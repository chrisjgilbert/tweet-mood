from django.test import TestCase
from django.test import Client
import pytest


class Webpage(TestCase):

    def test_root_irl_resolves_to_main_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
