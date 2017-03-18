from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import m2m_changed, post_migrate


class WorkshopsConfig(AppConfig):
    name = "pydaygal.workshops"

    def ready(self):
        from pydaygal.workshops.signals import register_workshops_handler
        from pydaygal.workshops.signals import create_workshops_group

        user_model = get_user_model()
        m2m_changed.connect(register_workshops_handler, sender=user_model.groups.through)
        post_migrate.connect(create_workshops_group)
