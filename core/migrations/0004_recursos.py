# Generated by Django 3.1.7 on 2021-03-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210326_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop-Mobile'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-users', 'Usuários')], max_length=20, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]
