from django.contrib import admin
# Register your models here.
from .models import DB_teach, Tutor, Tutor_infor


admin.site.register(DB_teach)
admin.site.register(Tutor)
admin.site.register(Tutor_infor)