from django.contrib import admin
from .models import (
    Appeals,
    Categories,
    Cities,
    Citizens,
    Employees,
    Messages,
    Processing,
    Services,
    Statuses,
    Streets,
    Users,
)

# Регистрация моделей в админке
admin.site.register(Appeals)
admin.site.register(Categories)
admin.site.register(Cities)
admin.site.register(Citizens)
admin.site.register(Employees)
admin.site.register(Messages)
admin.site.register(Processing)
admin.site.register(Services)
admin.site.register(Statuses)
admin.site.register(Streets)
admin.site.register(Users)