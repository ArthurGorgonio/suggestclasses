import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from core.bo.curso import get_cursos
from core.bo.sala import get_salas
from django.test import TestCase
from core.tests.povoar_testes import criar_dados, remover_dados
from core.dao.centro_dao import get_ceres, get_centro_by_id, get_centros
from dados import povoar
from core.dao.componente_dao import get_componentes_by_depto
from core.dao.departamento_dao import get_depto_by_id, get_departamentos


class CentroDAOTests(TestCase):

    def setUp(self):
        criar_dados()

    def tearDown(self):
        remover_dados()

    def test_get_centros(self):
        centros = get_centros()

        self.assertIsNotNone(centros, 'Testando centros')
        self.assertTrue(len(centros) > 0, 'Testando centros')

    def test_get_ceres(self):
        id_centro = 9999
        codigo = 9999
        sigla = 'CTESTE'
        nome = 'Centro de Teste'
        endereco = 'Rua Joaquim Gregório, Penedo, Caicó - RN'
        site = 'https://www.ceres.ufrn.br/'

        centro = get_centro_by_id(9999)

        self.assertEqual(id_centro, centro.id_unidade, 'Testando Id Unidade')
        self.assertEqual(codigo, centro.codigo, 'Testando Código')
        self.assertEqual(sigla, centro.sigla, 'Testando Sigla')
        self.assertEqual(nome, centro.nome, 'Testando Nome')
        self.assertEqual(endereco, centro.endereco, 'Testando Endereço')
        self.assertEqual(site, centro.site, 'Testando Site')

        centro = get_centro_by_id(6666)
        self.assertIsNone(centro)

    def test_get_centro(self):
        id_centro = 9999
        codigo = 9999
        sigla = 'CTESTE'
        nome = 'Centro de Teste'
        endereco = 'Rua Joaquim Gregório, Penedo, Caicó - RN'
        site = 'https://www.ceres.ufrn.br/'

        centro = get_centro_by_id(id_centro)

        self.assertEqual(id_centro, centro.id_unidade, 'Testando Id Unidade')
        self.assertEqual(codigo, centro.codigo, 'Testando Código')
        self.assertEqual(sigla, centro.sigla, 'Testando Sigla')
        self.assertEqual(nome, centro.nome, 'Testando Nome')
        self.assertEqual(endereco, centro.endereco, 'Testando Endereço')
        self.assertEqual(site, centro.site, 'Testando Site')

    def test_get_deptos_centro(self):
        deptos = get_departamentos()

        self.assertIsNotNone(deptos, 'Testando departamentos dos centros')
        self.assertTrue(len(deptos) > 0, 'Testando qtd departamentos')


class ComponenteDAOTests(TestCase):

    def setUp(self):
        criar_dados()

    def tearDown(self):
        remover_dados()

    def test_get_componentes_by_depto(self):
        depto = get_depto_by_id(9998)
        ccs = get_componentes_by_depto(depto)

        self.assertEqual(4, len(ccs), 'Testando componentes')


class SalaTests(TestCase):

    def setUp(self):
        criar_dados()

    def tearDown(self):
        remover_dados()

    def test_get_salas(self):
        salas = get_salas()

        self.assertIsNotNone(salas, 'Testando salas')
        self.assertTrue(len(salas) > 0, 'Testando salas')


class CursoTests(TestCase):

    def setUp(self):
        criar_dados()

    def tearDown(self):
        remover_dados()

    def test_get_salas(self):
        cursos = get_cursos()

        self.assertIsNotNone(cursos, 'Testando cursos')
        self.assertTrue(len(cursos) > 0, 'Testando cursos')
