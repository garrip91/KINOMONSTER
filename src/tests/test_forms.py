from django.test import TestCase

from KinomonsterApp.forms import UserLoginForm


class UserLoginFormTest(TestCase):

    def test_form_data_field_label(self):
        form = UserLoginForm()
        self.assertEqual(form.fields['username'].label == None or form.fields['username'].label == 'renewal date')
        self.assertEqual(form.fields['password'].label == None or form.fields['password'].label == 'renewal date')