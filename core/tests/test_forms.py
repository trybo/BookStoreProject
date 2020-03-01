from django.test import SimpleTestCase
from core.forms import CheckoutForm

class TestForms(SimpleTestCase):

    def test_checkout_form_valid_data(self):
        form = CheckoutForm(data={
            'street_address': 'rak 25',
            'apartment_address': '23',
            'country': 'NZ',
            'zip': '12-099',
            'same_shipping_address': False,
            'save_info': False,
            'payment_option': 'P'
        })

        self.assertTrue(form.is_valid())

    def test_checkout_form_no_data(self):
        form = CheckoutForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
