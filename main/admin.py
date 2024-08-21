from django.contrib import admin
from .models import Category, Item, Business

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'url_identifier')
    search_fields = ('name','owner', 'url_identifier')
    readonly_fields = ('url_identifier',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'business', 'name','image']
    ordering = ['id']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # If the user is a superuser, they can see all categories
        if request.user.is_superuser:
            return qs
        # Otherwise, filter the categories to only show those related to the user's business
        return qs.filter(business__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "business" and not request.user.is_superuser:
            kwargs["queryset"] = Business.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price']
    ordering = ['id']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # If the user is a superuser, they can see all items
        if request.user.is_superuser:
            return qs
        # Otherwise, filter the items to only show those related to the user's business
        return qs.filter(category__business__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category" and not request.user.is_superuser:
            kwargs["queryset"] = Category.objects.filter(business__owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Business, BusinessAdmin)