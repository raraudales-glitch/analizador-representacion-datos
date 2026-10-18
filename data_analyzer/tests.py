from django.test import TestCase, Client
from django.urls import reverse

class AnalyzerTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_conversion_valida_binario(self):
        response = self.client.post(self.url, {'num_submit': '', 'num-number_input': '1010', 'num-base_choice': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '10')

    def test_conversion_valida_hexadecimal(self):
        response = self.client.post(self.url, {'num_submit': '', 'num-number_input': 'FF', 'num-base_choice': '16'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '255')

    def test_error_digito_invalido_base(self):
        response = self.client.post(self.url, {'num_submit': '', 'num-number_input': '102', 'num-base_choice': '2'})
        self.assertContains(response, 'El número contiene dígitos inválidos')

    def test_error_fuera_de_rango(self):
        response = self.client.post(self.url, {'num_submit': '', 'num-number_input': '70000', 'num-base_choice': '10'})
        self.assertContains(response, 'El valor convertido debe estar entre 0 y 65,535')

    def test_error_entrada_vacia(self):
        response = self.client.post(self.url, {'num_submit': '', 'num-number_input': '', 'num-base_choice': '10'})
        self.assertContains(response, 'El campo de entrada no puede estar vacío')

    def test_analisis_utf8_con_enie(self):
        response = self.client.post(self.url, {'text_submit': '', 'text-text_input': 'Niño'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'U+00F1')