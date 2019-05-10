import django
django.setup()

from django.test import TestCase

from .models import EstruturaCurricular

class EstruturaCurricularTests(TestCase):

    def test_create_estrutura(self):
        """
                Teste de Unidade em Python.
        """
        bsi = EstruturaCurricular(sigla = '01A', ano_periodo = '2011.1', nome = 'SISTEMAS DE INFORMAÇÃO - Presencial - MT')

        self.assertEquals('01A',bsi.sigla)