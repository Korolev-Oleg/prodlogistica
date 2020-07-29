from django.contrib import admin
from .models import Product, Category, SubCategory

all = (
    'code', 'name', 'unit', 'full_name', 'nds', 'country_of_origin', 'gdt_number',
    'storage_life', 'storage_conditions', 'cert_of_conformity', 'gost_ty', 'basic_property', 'print_name', 'articule',
    'edizm_base', 'base_weight', 'base_barcode', 'remains', 'reserve_on_firm', 'remains_fact', 'price', 'val',
    'purchase',)


class ProductsAdmin(admin.ModelAdmin):
    search_fields = all
    list_display = ('code', 'name', 'category', 'sub_category', 'remains')
    list_filter = ('category', 'sub_category')
    list_display_links = ('code', 'name',)
    show_full_result_count = 1

    def get_list_display(self, request):
        """переопределяет представление list_display для разных пользователей"""
        if request.user.is_superuser:
            return 'code', 'name', 'category', 'sub_category', 'remains',
        else:
            return 'code', 'name'


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
