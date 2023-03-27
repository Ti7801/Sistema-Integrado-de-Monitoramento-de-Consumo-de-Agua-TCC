# Generated by Django 3.2.16 on 2023-03-23 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('cidade', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=20)),
                ('rua', models.CharField(max_length=40)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=20)),
                ('consumo_total', models.IntegerField(default=0, max_length=100)),
                ('consumo_ultimo_mes', models.IntegerField(default=0, max_length=100)),
                ('consumo_inicio_mes', models.IntegerField(default=0, max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InterfaceWeb.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='InterfaceWebUser',
            fields=[
                ('id_adm', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=40)),
                ('login', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id_fatura', models.AutoField(primary_key=True, serialize=False)),
                ('consumo_mensal', models.CharField(max_length=100)),
                ('mes', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=10)),
                ('valor_pagar', models.CharField(max_length=20)),
                ('fatura_paga', models.CharField(choices=[(True, 'Sim'), (False, 'Nao')], max_length=5)),
                ('fatura_nome', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='InterfaceWeb.cliente')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='InterfaceWeb.endereco')),
            ],
        ),
    ]