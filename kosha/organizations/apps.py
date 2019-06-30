from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrganizationsConfig(AppConfig):
    name = "kosha.organizations"
    verbose_name = _("Organizations")

    def ready(self):
        try:
            import kosha.organizations.signals  # noqa F401
        except ImportError:
            pass
