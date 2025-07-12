import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "naiversity.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import naiversity.users.signals  # noqa: F401, PLC0415
