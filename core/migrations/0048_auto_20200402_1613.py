# Generated by Django 3.0.4 on 2020-04-02 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_curso_coordenador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentecurricular',
            options={'verbose_name': 'componente curricular', 'verbose_name_plural': 'componentes curriculares'},
        ),
        migrations.AlterModelOptions(
            name='estruturacurricular',
            options={'verbose_name': 'estrutura curricular', 'verbose_name_plural': 'estruturas curriculares'},
        ),
        migrations.AlterModelOptions(
            name='organizacaocurricular',
            options={'verbose_name': 'organização curricular', 'verbose_name_plural': 'organizações curriculares'},
        ),
        migrations.AlterModelOptions(
            name='sugestaoturma',
            options={'verbose_name': 'sugestão de turma', 'verbose_name_plural': 'sugestões de turmas'},
        ),
        migrations.AlterUniqueTogether(
            name='sugestaoturma',
            unique_together={('codigo_turma', 'componente', 'ano', 'periodo')},
        ),
        migrations.AlterUniqueTogether(
            name='turma',
            unique_together={('codigo_turma', 'componente', 'ano', 'periodo')},
        ),
    ]