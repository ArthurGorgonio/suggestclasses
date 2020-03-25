# Generated by Django 3.0.2 on 2020-03-24 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20200322_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='siape',
        ),
        migrations.AddField(
            model_name='turma',
            name='docente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Docente'),
        ),
    ]