import csv
import urllib.request
from dateutil.parser import parse
import os
import django

django.setup()
from core.models import Curso, Centro, Departamento, ComponenteCurricular, EstruturaCurricular, OrganizacaoCurricular, \
    Docente, Turma

DADOS_PATH = '/home/taciano/dev/workspace/suggestclasses/dados'


def main():
    print("Lendo dados sobre o CERES/UFRN ...!")
    os.chdir(DADOS_PATH)
    print(os.getcwd())

    # downloads_dados()
    # centros()  # Adicionamos apenas o CERES.
    # departamentos()
    # cursos()
    # componentes()
    # estruturas()
    # organizacao()
    # criar_docentes()
    criar_turmas()


def centros():
    # Cadastrando o Centro CERES
    centro = Centro(id_unidade=1482, codigo=1800, nome='Centro de Ensino Superior do Seridó',
                    sigla='CERES', endereco='Rua Joaquim Gregório, Penedo, Caicó - RN',
                    site='http://www.ceres.ufrn.br/')
    centro.save()


def departamentos():
    # Buscando o Centro CERES
    ceres = Centro.objects.get(id_unidade=1482)

    with open('unidades.csv') as csvfile:
        unidades = csv.reader(csvfile, delimiter=';')
        next(unidades)  # skip header

        for row in unidades:

            id_dep = row[0]
            codigo_dep = row[1]
            nome_dep = row[2]
            sigla_dep = row[3]
            municipio = row[6]

            id_unidade_responsavel = row[9].strip()
            tipo_unidade_organizacional = row[17].strip()

            if id_unidade_responsavel == '1482' and (tipo_unidade_organizacional == 'DEPARTAMENTO'
                                                     or tipo_unidade_organizacional == 'ASSESSORIA'):
                print(id_dep)
                print(codigo_dep)
                print(nome_dep)
                print(sigla_dep)
                print(municipio)
                print(tipo_unidade_organizacional)
                print(id_unidade_responsavel)
                d = Departamento(id_unidade=id_dep, codigo=codigo_dep, nome=nome_dep, sigla=sigla_dep,
                                 endereco=municipio,
                                 centro=ceres)
                d.save()


def cursos():
    print("Criando cursos para o CERES ...!")
    # Buscando o Centro CERES
    ceres = Centro.objects.get(id_unidade=1482)

    with open('cursos-ufrn.csv') as csvfile:
        cursos_ufrn = csv.reader(csvfile, delimiter=';')
        next(cursos_ufrn)  # skip header

        for row in cursos_ufrn:

            id_curso = row[0]
            nome_curso = row[1]
            nivel_ensino = row[5]
            grau_academico = row[6]
            modalidade_educacao = row[7]
            turno = row[10]
            id_unidade_responsavel = row[14]

            if id_unidade_responsavel == '1482':
                print(id_curso)
                print(nome_curso)
                print(nivel_ensino)
                print(grau_academico)
                print(modalidade_educacao)
                print(turno)
                print(id_unidade_responsavel)
                c = Curso(codigo=id_curso, nome=nome_curso, nivel=nivel_ensino, grau=grau_academico,
                          modalidade=modalidade_educacao, turno=turno, centro=ceres)
                c.save()


def componentes():
    print("Criando Componentes para os Departamentos do CERES ...!")

    with open('componentes-curriculares-presenciais.csv') as csvfile:
        componentes_ceres = csv.reader(csvfile, delimiter=';')
        next(componentes_ceres)  # skip header

        for row in componentes_ceres:

            unidade_responsavel = row[5].strip()

            if Departamento.objects.filter(nome=unidade_responsavel).exists():
                depto = Departamento.objects.get(nome=unidade_responsavel)
                print("Departamento " + depto.sigla)

                id_componente = row[0]
                tipo_componente = row[1]
                codigo_componente = row[2]
                nivel_componente = row[3]
                nome_componente = row[4]
                unidade_responsavel = row[5].strip()
                ch_teorico = row[6]
                ch_pratico = row[7]
                ch_estagio = row[8]
                ch_total = row[9]
                ch_dedicada_docente = row[10]
                ch_ead = row[11]
                cr_max_ead = row[12]
                equivalencia = row[16]
                pre_requisito = row[17]
                co_requisito = row[18]
                ementa = row[19]
                bibliografia = row[20]
                objetivos = row[21]
                conteudo = row[22]
                competencias_habilidades = row[23]
                referencias = row[24]
                ano_programa = row[25]
                periodo_programa = row[26]
                modalidade = row[27]
                curso_componente = row[28]

                # if depto.id_unidade == 9726 or depto.id_unidade == 235:
                print(id_componente)

                cc = ComponenteCurricular(id_componente=id_componente, tipo=tipo_componente,
                                          codigo=codigo_componente, nivel=nivel_componente, nome=nome_componente,
                                          ch_teorica=ch_teorico, ch_pratica=ch_pratico, ch_estagio=ch_estagio,
                                          ch_total=ch_total, ch_docente=ch_dedicada_docente, ch_ead=ch_ead,
                                          cr_max_ead=cr_max_ead, equivalencia=equivalencia,
                                          requisito=pre_requisito, corequisito=co_requisito, ementa=ementa,
                                          modalidade=modalidade, departamento=depto)
                cc.save()


def estruturas():
    print("Criando Estruturas Curriculares para os Cursos do CERES ...!")

    with open('estruturas-curriculares.csv') as csvfile:
        estruturas_ceres = csv.reader(csvfile, delimiter=';')
        next(estruturas_ceres)  # skip header

        for row in estruturas_ceres:

            curso_ufrn = row[3]

            if Curso.objects.filter(codigo=curso_ufrn).exists():
                curso_ceres = Curso.objects.get(codigo=curso_ufrn)
                print(curso_ceres)

                id_curriculo = row[0]
                codigo = row[1]
                nome_matriz = row[2]
                id_curso = row[3]
                nome_curso = row[4]
                semestre_conclusao_minimo = row[5] if row[5] != '' else None
                semestre_conclusao_ideal = row[6] if row[6] != '' else None
                semestre_conclusao_maximo = row[7] if row[7] != '' else None
                meses_conclusao_minimo = row[8] if row[8] != '' else None
                meses_conclusao_ideal = row[9] if row[9] != '' else None
                meses_conclusao_maximo = row[10] if row[10] != '' else None
                cr_total_minimo = row[11] if row[11] != '' else None
                ch_total_minima = row[12] if row[12] != '' else None
                ch_optativas_minima = row[13] if row[13] != '' else None
                ch_complementar_minima = row[14] if row[14] != '' else None
                max_eletivos = row[15] if row[15] != '' else None
                ch_nao_atividade_obrigatoria = row[16] if row[16] != '' else None
                cr_nao_atividade_obrigatorio = row[17] if row[17] != '' else None
                ch_atividade_obrigatoria = row[18] if row[18] != '' else None
                cr_minimo_semestre = row[19] if row[19] != '' else None
                cr_ideal_semestre = row[20] if row[20] != '' else None
                cr_maximo_semestre = row[21] if row[21] != '' else None
                ch_minima_semestre = row[22] if row[22] != '' else None
                ch_ideal_semestre = row[23] if row[23] != '' else None
                ch_maxima_semestre = row[24] if row[24] != '' else None
                periodo_entrada_vigor = row[25] if row[25] != '' else None
                ano_entrada_vigor = row[26] if row[26] != '' else None
                observacao = row[27]

                ec = EstruturaCurricular(id_curriculo=id_curriculo, codigo=codigo, nome=nome_matriz,
                                         semestre_conclusao_minimo=semestre_conclusao_minimo,
                                         semestre_conclusao_ideal=semestre_conclusao_ideal,
                                         semestre_conclusao_maximo=semestre_conclusao_maximo,
                                         meses_conclusao_minimo=meses_conclusao_minimo,
                                         meses_conclusao_ideal=meses_conclusao_ideal,
                                         meses_conclusao_maximo=meses_conclusao_maximo,
                                         cr_total_minimo=cr_total_minimo, ch_total_minima=ch_total_minima,
                                         ch_optativas_minima=ch_optativas_minima,
                                         ch_complementar_minima=ch_complementar_minima, max_eletivos=max_eletivos,
                                         ch_nao_atividade_obrigatoria=ch_nao_atividade_obrigatoria,
                                         cr_nao_atividade_obrigatorio=cr_nao_atividade_obrigatorio,
                                         ch_atividade_obrigatoria=ch_atividade_obrigatoria,
                                         cr_minimo_semestre=cr_minimo_semestre,
                                         cr_ideal_semestre=cr_ideal_semestre, cr_maximo_semestre=cr_maximo_semestre,
                                         ch_minima_semestre=ch_minima_semestre, ch_ideal_semestre=ch_ideal_semestre,
                                         ch_maxima_semestre=ch_maxima_semestre,
                                         periodo_entrada_vigor=periodo_entrada_vigor,
                                         ano_entrada_vigor=ano_entrada_vigor, observacao=observacao, curso=curso_ceres)
                ec.save()


def organizacao():
    print("Criando Estruturas Curriculares para os Cursos do CERES ...!")

    with open('curriculo-componente-graduacao.csv') as csvfile:
        ccg = csv.reader(csvfile, delimiter=';')
        next(ccg)  # skip header

        for row in ccg:

            id_estrutura = row[1]
            id_componente_curricular = row[2]

            if EstruturaCurricular.objects.filter(id_curriculo=id_estrutura).exists():
                ec = EstruturaCurricular.objects.get(id_curriculo=id_estrutura)

                if ComponenteCurricular.objects.filter(id_componente=id_componente_curricular).exists():
                    cc = ComponenteCurricular.objects.get(id_componente=id_componente_curricular)

                    id_curriculo_componente = row[0]
                    id_curriculo = row[1]
                    id_componente_curricular = row[2]
                    semestre_oferta = row[3]
                    tipo_vinculo_componente = row[4]
                    nivel_ensino = row[5]

                    oc = OrganizacaoCurricular(id_curriculo_componente=id_curriculo_componente, estrutura=ec,
                                               componente=cc, semestre=semestre_oferta,
                                               tipo_vinculo=tipo_vinculo_componente, nivel=nivel_ensino)
                    oc.save()


def criar_docentes():
    print("Criando Docentes do CERES ...!")

    with open('docentes.csv') as csvfile:
        docentes = csv.reader(csvfile, delimiter=';')
        next(docentes)  # skip header

        for row in docentes:
            siape = row[0]
            nome = row[1]
            sexo = row[2]
            formacao = row[3]
            tipo_jornada_trabalho = row[4]
            vinculo = row[5]
            categoria = row[6]
            classe_funcional = row[7]
            id_unidade_lotacao = row[8]
            lotacao = row[9]
            admissao_str = row[10]
            # https://stackabuse.com/converting-strings-to-datetime-in-python/
            admissao = parse(admissao_str)

            if id_unidade_lotacao == '1482' or Departamento.objects.filter(id_unidade=id_unidade_lotacao).exists():
                print(nome)
                print(lotacao)

                professor = Docente(siape=siape, nome=nome, sexo=sexo, formacao=formacao,
                                    tipo_jornada_trabalho=tipo_jornada_trabalho,
                                    vinculo=vinculo, categoria=categoria, classe_funcional=classe_funcional,
                                    id_unidade_lotacao=id_unidade_lotacao, lotacao=lotacao, admissao=admissao)
                professor.save()


def criar_turmas():
    print("Criando Turmas 2019.1 e 2019.2 para os Cursos do CERES ...!")

    with open('turmas-2019.2.csv') as csvfile:
        turmas = csv.reader(csvfile, delimiter=';')
        next(turmas)  # skip header

        for row in turmas:

            siape = row[2] if row[2] != '' else None
            id_componente_curricular = row[5]

            if ComponenteCurricular.objects.filter(id_componente=id_componente_curricular).exists():
                cc = ComponenteCurricular.objects.get(id_componente=id_componente_curricular)
                print(cc)

                docente = None
                if siape != '' and Docente.objects.filter(siape=siape).exists():
                    # Professores Substitutos e Temporários não estão na lista
                    docente = Docente.objects.get(siape=siape)
                    print(docente)

                id_turma = row[0]
                codigo_turma = row[1]
                matricula_docente_externo = row[3] if row[3] != '' else None

                if row[3] != '' and row[3] is not None:
                    print(matricula_docente_externo)

                observacao = row[4].strip()
                ch_dedicada_periodo = row[6] if row[6] != '' else None
                nivel_ensino = row[7]
                campus_turma = row[8]
                local = row[9]
                ano = row[10] if row[10] != '' else None
                periodo = row[11] if row[11] != '' else None
                data_inicio_str = row[12]
                data_inicio = parse(data_inicio_str)
                data_fim_str = row[13]
                data_fim = parse(data_fim_str)
                descricao_horario = row[14]
                total_solicitacoes = row[15] if row[15] != '' else None
                capacidade_aluno = row[16]
                tipo = row[17] if row[17] != '' else None
                distancia = row[18] if row[18] == 'true' else False
                data_consolidacao_str = row[19] if row[19] != '' else None
                data_consolidacao = data_consolidacao_str if data_consolidacao_str is None \
                    else parse(data_consolidacao_str)
                agrupadora = row[20] if row[20] == 'true' else False
                id_turma_agrupadora = row[21] if row[21] != '' else None
                qtd_aulas_lancadas = row[22] if row[22] != '' else None
                situacao_turma = row[23]
                convenio = row[24]
                modalidade_participantes = row[25]

                turma = Turma(id_turma=id_turma, codigo_turma=codigo_turma, siape=siape,
                              matricula_docente_externo=matricula_docente_externo, observacao=observacao,
                              componente=cc, ch_dedicada_periodo=ch_dedicada_periodo,
                              nivel_ensino=nivel_ensino, campus_turma=campus_turma, local=local, ano=ano,
                              periodo=periodo, data_inicio=data_inicio, data_fim=data_fim,
                              descricao_horario=descricao_horario, total_solicitacoes=total_solicitacoes,
                              capacidade_aluno=capacidade_aluno, tipo=tipo, distancia=distancia,
                              data_consolidacao=data_consolidacao, agrupadora=agrupadora,
                              id_turma_agrupadora=id_turma_agrupadora, qtd_aulas_lancadas=qtd_aulas_lancadas,
                              situacao_turma=situacao_turma, convenio=convenio,
                              modalidade_participantes=modalidade_participantes)
                turma.save()


def downloads_dados():
    """Download de arquivos CSV de http://dados.ufrn.br"""

    download_departamentos()
    download_cursos()
    download_componentes()
    download_estruturas()
    download_curriculos()
    download_docentes()
    download_turmas()


def download_departamentos():
    print("Download do CSV dos Departamentos do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/da6451a5-1a59-4630-bdc2-97f6be4a59c2/resource/3f2e4e32-ef1a-4396-8037' \
          '-cbc22a89d97f/download/unidades.csv'
    file_name = 'unidades.csv'
    urllib.request.urlretrieve(url, file_name)


def download_cursos():
    print("Download do CSV dos Cursos do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/08b0dc59-faa9-4281-bd1e-2a39f532489e/resource/949be3d1-e85b-4d0f-9f60' \
          '-1d9a7484bb06/download/cursos-ufrn.csv'
    file_name = 'cursos-ufrn.csv'
    urllib.request.urlretrieve(url, file_name)


def download_componentes():
    print("Download do CSV dos Componentes do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/3fea67e8-6916-4ed0-aaa6-9a8ca06a9bdc/resource/9a3521d2-4bc5-4fda-93f0' \
          '-f701c8a20727/download/componentes-curriculares-presenciais.csv'
    file_name = 'componentes-curriculares-presenciais.csv'
    urllib.request.urlretrieve(url, file_name)


def download_estruturas():
    print("Download do CSV das Estruturas Curriculares do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/e7c24910-75c1-451b-9097-e4352488dd69/resource/94cc35b0-6560-44f3-8c67' \
          '-98cff965f23c/download/estruturas-curriculares.csv'
    file_name = 'estruturas-curriculares.csv'
    urllib.request.urlretrieve(url, file_name)


def download_curriculos():
    print("Download do CSV dos Organização Curricular do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/82aca3f1-f7ee-425e-bf1e-b6a1d6811bf4/resource/3f25d054-c5d2-4bf2-8cd4' \
          '-8e0a2e4f63ce/download/curriculo-componente-graduacao.csv '
    file_name = 'curriculo-componente-graduacao.csv'
    urllib.request.urlretrieve(url, file_name)


def download_turmas():
    print("Download do CSV das Turmas 2019.1 do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/1e42cd66-69d6-48d5-a346' \
          '-d46766fd2c9c/download/turmas-2019.1.csv'
    file_name = "turmas-2019.1.csv"
    urllib.request.urlretrieve(url, file_name)

    print("Download do CSV das Turmas 2019.2 do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/1938623d-fb07-41a4-a55a-1691f7c3b8b5/resource/d9c2863e-d1b2-4afd-b7dd' \
          '-09517d5ed17d/download/turmas-2019.2.csv'
    file_name = "turmas-2019.2.csv"
    urllib.request.urlretrieve(url, file_name)


def download_docentes():
    print("Download do CSV dos Docentes do CERES/UFRN ...!")
    url = 'http://dados.ufrn.br/dataset/8bf1a468-48ff-4f4d-95ee-b17b7a3a5592/resource/ff0a457e-76fa-4aca-ad99' \
          '-48aebd7db070/download/docentes.csv'
    file_name = "docentes.csv"
    urllib.request.urlretrieve(url, file_name)


if __name__ == "__main__":
    main()
