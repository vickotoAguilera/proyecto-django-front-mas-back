from django.apps import AppConfig


class CursosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cursos'

    # aca aplico el parche oficial de Django (Ticket #35844 / PR #18824)
    # para asegurar compatibilidad completa con Python 3.14 al renderizar el Admin y plantillas
    def ready(self):
        from copy import copy
        from django.template import context

        def base_context_copy(ctx):
            duplicate = context.BaseContext()
            duplicate.__class__ = ctx.__class__
            duplicate.__dict__ = copy(ctx.__dict__)
            duplicate.dicts = ctx.dicts[:]
            return duplicate

        context.BaseContext.__copy__ = base_context_copy

