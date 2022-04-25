from django.contrib import admin

from PROJECT.web.models import Quotes, Projects, Portfolio, CV, ContactModel


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'type', 'description')



@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'image')


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactModel)
class Contact(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'subject', 'content')
