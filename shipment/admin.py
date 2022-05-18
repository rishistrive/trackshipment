from django.contrib import admin
from .models import Product, Shipment, User, UserConfig, Widgets


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_supplier", "is_customer"]
    list_filter = ["is_supplier", "is_customer"]

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.register(Product)


class ShipmentAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "supplier":
            kwargs["queryset"] = User.objects.filter(is_supplier=True)
        if db_field.name == "customer":
            kwargs["queryset"] = User.objects.filter(is_customer=True)
        return super(ShipmentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


admin.site.register(Shipment, ShipmentAdmin)

class UserConfAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "widget", "status"]

    class Meta:
        model = UserConfig

admin.site.register(UserConfig, UserConfAdmin)
