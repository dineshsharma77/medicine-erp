from django.contrib import admin

# Register your models here.
from .models import Medicine, Dealer, Brand, Staff,User

admin.site.register(Medicine)
admin.site.register(Dealer)
admin.site.register(Brand)
admin.site.register(Staff)
admin.site.register(User)

