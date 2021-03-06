"""Custom admin views for the ``user_profile`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from user_profile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """Customized admin for the ``UserProfile`` model."""
    list_display = ('user', 'user_email', 'display_name', 'username')
    search_fields = ['username', 'user__email', 'display_name']

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = _('User email')


admin.site.register(UserProfile, UserProfileAdmin)
