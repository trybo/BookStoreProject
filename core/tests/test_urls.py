from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import HomeView, CheckoutView, OrderSummaryView, BookDetailView, add_to_cart, remove_from_cart, remove_single_book_from_cart

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('core:home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_checkout_url_resolves(self):
        url = reverse('core:checkout')
        self.assertEquals(resolve(url).func.view_class, CheckoutView)

    def test_order_summary_url_resolves(self):
        url = reverse('core:order-summary')
        self.assertEquals(resolve(url).func.view_class, OrderSummaryView)

    def test_product_url_resolves(self):
        url = reverse('core:product', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, BookDetailView)

    def test_add_to_cart_url_resolves(self):
        url = reverse('core:add-to-cart', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_remove_from_cart_url_resolves(self):
        url = reverse('core:remove-from-cart', args=['some-slug'])
        self.assertEquals(resolve(url).func, remove_from_cart)

    def test_remove_single_book_from_cart_url_resolves(self):
        url = reverse('core:remove-single-book-from-cart', args=['some-slug'])
        self.assertEquals(resolve(url).func, remove_single_book_from_cart)
