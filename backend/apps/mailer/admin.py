from django.contrib import admin

from .models import Mail, Mailing


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("subject", "message", "html_message", "text")
    search_fields = ["subject", "message"]


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("from_email", "created_at", "status")
    list_filter = ("status",)
    search_fields = ["from_email"]
    date_hierarchy = "created_at"
