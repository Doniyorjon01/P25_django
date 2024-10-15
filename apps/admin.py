from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.models import Category, Product, User

admin.site.register(Category)
admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        if obj.headshot:
            return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
                url=obj.headshot.url,
                width=obj.headshot.width,
                height=obj.headshot.height,
            ))
        return "Hech qanday surat mavjud emas"
