from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Подкадегория'
        verbose_name_plural = 'Подкадегории'

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        verbose_name='Категория')

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT,
        verbose_name='Подкатегория')

    code = models.IntegerField(verbose_name='Код')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    unit = models.CharField(max_length=50, verbose_name='Осн. ед изм.')
    full_name = models.CharField(max_length=120, verbose_name='Полное наименование')
    nds = models.CharField(max_length=20, verbose_name='Ставка НДС')

    remains = models.FloatField(
        null=True, blank=True,
        verbose_name='Остаток')

    price = models.FloatField(
        null=True, blank=True,
        verbose_name='Цена')

    reserve_on_firm = models.FloatField(
        null=True, blank=True,
        verbose_name='Резерв по фирме')

    remains_fact = models.FloatField(
        null=True, blank=True,
        verbose_name='Остаток факт.')

    val = models.TextField(
        null=True, blank=True,
        verbose_name='Вал')

    purchase = models.FloatField(
        null=True, blank=True,
        verbose_name='Закупка')

    country_of_origin = models.CharField(
        max_length=120, null=True, blank=True,
        verbose_name='Страна происхождения')

    gdt_number = models.CharField(
        max_length=50, null=True, blank=True,
        verbose_name='Номер ГДТ')

    storage_life = models.CharField(
        max_length=150, null=True, blank=True,
        verbose_name='Срок хранения')

    storage_conditions = models.TextField(
        null=True, blank=True,
        verbose_name='Условия хранения')

    cert_of_conformity = models.CharField(
        max_length=250, null=True, blank=True,
        verbose_name='Сертификат соответствия')

    gost_ty = models.TextField(
        null=True, blank=True,
        verbose_name='Нормативно технический документ (ГОСТ, ТУ)')

    basic_property = models.TextField(
        null=True, blank=True,
        verbose_name='Основное свойство')

    print_name = models.CharField(
        max_length=150, null=True, blank=True,
        verbose_name='Наименование для печати')

    articule = models.TextField(
        null=True, blank=True,
        verbose_name='Артикул')

    edizm_base = models.CharField(
        max_length=200, null=True, blank=True,
        verbose_name='Базовая ед изм.')

    base_weight = models.CharField(
        max_length=250, null=True, blank=True,
        verbose_name='Вес Базовый (кг)')

    base_barcode = models.TextField(
        null=True, blank=True,
        verbose_name='Штрихкод базовый')

    class Meta:
        verbose_name = 'Номенклатуру'
        verbose_name_plural = 'Номенклатура'
        ordering = ('name', 'remains',)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
