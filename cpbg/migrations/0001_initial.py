# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('road_address', models.TextField(unique=True)),
                ('address_pin', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comcat1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_name', models.CharField(unique=True, max_length=100)),
                ('search_rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Company2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.TextField(null=True, blank=True)),
                ('search_rank', models.IntegerField(default=0)),
                ('company_categories', models.ManyToManyField(to='cpbg.Comcat1')),
            ],
        ),
        migrations.CreateModel(
            name='Compos4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_name', models.CharField(max_length=100)),
                ('address_of_position', models.ForeignKey(blank=True, to='cpbg.Address3', null=True)),
                ('position_of_company', models.ForeignKey(to='cpbg.Company2')),
            ],
        ),
        migrations.CreateModel(
            name='Edomain1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain_name', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Email6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_name', models.CharField(max_length=25)),
                ('domain_of_email', models.ForeignKey(to='cpbg.Edomain1')),
            ],
        ),
        migrations.CreateModel(
            name='Landline5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('landline_number', models.CharField(max_length=100)),
                ('is_landline_for_fax', models.BooleanField()),
                ('landline_for_position', models.ForeignKey(blank=True, to='cpbg.Compos4', null=True)),
                ('landline_in_address', models.ForeignKey(to='cpbg.Address3')),
                ('landline_of_company', models.ForeignKey(to='cpbg.Company2')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile6',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Person5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=100)),
                ('search_rank', models.IntegerField(default=0)),
                ('company_of_person', models.ForeignKey(blank=True, to='cpbg.Company2', null=True)),
                ('person_for_position', models.ForeignKey(blank=True, to='cpbg.Compos4', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stdcode1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('std_code', models.IntegerField(unique=True)),
                ('std_area', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='mobile6',
            name='mobile_of_person',
            field=models.ForeignKey(to='cpbg.Person5'),
        ),
        migrations.AddField(
            model_name='landline5',
            name='std_for_landline',
            field=models.ForeignKey(to='cpbg.Stdcode1'),
        ),
        migrations.AddField(
            model_name='email6',
            name='email_of_person',
            field=models.ForeignKey(blank=True, to='cpbg.Person5', null=True),
        ),
        migrations.AddField(
            model_name='email6',
            name='email_of_position',
            field=models.ForeignKey(blank=True, to='cpbg.Compos4', null=True),
        ),
        migrations.AddField(
            model_name='company2',
            name='domain_for_company',
            field=models.ForeignKey(blank=True, to='cpbg.Edomain1', null=True),
        ),
        migrations.AddField(
            model_name='address3',
            name='address_of_company',
            field=models.ForeignKey(to='cpbg.Company2'),
        ),
    ]
