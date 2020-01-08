# SuggestClasses by LABENS/UFRN
Sistema de Sugestão de Horários para o BSI/UFRN.

## Lista de Requisitos Funcionais

O sistema SuggestClasses terá o cadastro de sugestões de horários para turmas de componentes curriculares de um curso em um certo período. Também manterá o horário aprovado das turmas e exibirá relatórios de horários para professores, alunos, por sala e por período.

Os requisitos funcionais detalhados estã na página wiki [Requisitos Funcionais](https://github.com/labens-ufrn/suggestclasses/wiki).

## Migrations

Ao modificar os models (em models.py), execute:

```shell script
$ python manage.py makemigrations core
$ python manage.py migrate
```

## Testes

Rodar os testes mantendo o banco de testes:

```shell script
python manage.py test --keepdb core/
```

Devemos acrescentar nas classes de testes:

```pythonstub
import django
django.setup()
```

Configurações para os testes:

```shell script
pip install nose
pip install coverage
export DJANGO_SETTINGS_MODULE=mysite.settings
```

### Executar os Testes de Unidade e Cobertura

```shell script
nosetests --with-xunit
nosetests --with-coverage --cover-package=core --cover-branches --cover-xml
```

## Executar o Sonar

```shell script
sonar-scanner \
  -Dsonar.projectKey=suggestclasses \
  -Dsonar.organization=labens-github \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=02254c57898053f6e25acfb70756ef6f840d4d35
```

# Outras Configurações

* Arquivo _.editorconfig_ de estilo de codificação adicionado.

##  Tabela com horários de aula

Matutino | Vespertino | Noturno
-------- | ---------- | -------
M1 – 07h00 às 07h50 | T1 – 13h00 às 13h50 | N1 – 18h45 às 19h35
M2 – 07h50 às 08h40 | T2 – 13h50 às 14h40 | N2 – 19h35 às 20h25
M3 – 08h55 às 09h45 | T3 – 14h55 às 15h45 | N3 – 20h35 às 21h25
M4 – 09h45 às 10h35 | T4 – 15h45 às 16h35 | N4 – 21h25 às 22h15
M5 – 10h50 às 11h40 | T5 – 16h50 às 17h40 |
M6 – 11h40 às 12h30 | T6 – 17h40 às 18h30 |

# Links

* https://automationpanda.com/2017/09/14/django-projects-in-pycharm-community-edition/
* http://craigthomas.ca/blog/2014/06/02/python-code-inspection-with-sonarqube/
* https://docs.sonarqube.org/display/PLUG/Python+Unit+Tests+Execution+Reports+Import
* https://stackoverflow.com/questions/34114427/django-upgrading-to-1-9-error-appregistrynotready-apps-arent-loaded-yet
* https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
