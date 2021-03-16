from django.contrib import admin
from .models import Intro, Teaser, Hizmetler, Ekip, Adres, GMaps

# Register your models here.


class IntroAdmin(admin.ModelAdmin):
    list_display = ('hosgeldin_mesaji',)


class TeaserAdmin(admin.ModelAdmin):
    list_display = ('teaser',)


class HizmetlerAdmin(admin.ModelAdmin):
    list_display = ('satis', 'ikinci_el', 'servis', 'yedek_parca')


class EkipAdmin(admin.ModelAdmin):
    list_display = ('ekip',)


class AdresAdmin(admin.ModelAdmin):
    list_display = ('adres_bir', 'adres_iki', 'sabit_tel', 'mobil_tel')


class GMapsAdmin(admin.ModelAdmin):
    list_display = ('harita',)


admin.site.register(Intro, IntroAdmin)
admin.site.register(Teaser, TeaserAdmin)
admin.site.register(Hizmetler, HizmetlerAdmin)
admin.site.register(Ekip, EkipAdmin)
admin.site.register(Adres, AdresAdmin)
admin.site.register(GMaps, GMapsAdmin)
