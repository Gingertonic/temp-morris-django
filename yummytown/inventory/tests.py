from django.test import Client, TestCase
from django.urls import reverse
from .models import Category, Item

# Create your tests here.
class BaseTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_category = Category.objects.create(code="CDT", name="condiment")
        cls.test_item_a = Item.objects.create(name="ketchup", cat=cls.test_category)
        cls.test_item_b = Item.objects.create(name="mustard", cat=cls.test_category)

class TestBasicViews(BaseTestCase):
    client = Client()

    def test_about(self):
        resp = self.client.get(reverse('inventory-how-to'))
        assert "inventory/about.html" in [t.name for t in resp.templates]

    def test_index(self):
        resp = self.client.get(reverse('inventory-index'))
        assert "items" in resp.context
        assert resp.context["items"].count() == 2

    def test_show(self):
        resp = self.client.get(reverse('show-item', args=[2]))
        assert "item" in resp.context
        assert resp.context["item"].name == "mustard"
        assert resp.context["item"].cat.code == "CDT"
