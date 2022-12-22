# Generated by Django 4.1.4 on 2022-12-20 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('segundo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('rua', models.CharField(max_length=120, verbose_name='Rua')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('complemento', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=120, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não Declarar')], max_length=1)),
                ('estado_civil', models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('v', 'Viúv(o/a)')], max_length=1)),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='segundo_app.endereco', verbose_name='Endereco')),
            ],
        ),
    ]
