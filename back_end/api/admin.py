from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Day)
admin.site.register(Birthday)

admin.site.register(Member)
admin.site.register(Filtter)
admin.site.register(Match)
