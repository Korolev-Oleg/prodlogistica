# Generated by Django 2.2.12 on 2020-08-04 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name', 'remains'), 'verbose_name': 'Номенклатуру', 'verbose_name_plural': 'Номенклатура'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкадегория', 'verbose_name_plural': 'Подкадегории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.SubCategory', verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Подкатегория'),
        ),
    ]
