"""
    Setup dependency injection file
"""

from dependency_injector import providers, containers
from apps.integration_1S.tasks import IntegrationController


class Integration1C(containers.DeclarativeContainer):
    integration1c = providers.Singleton(IntegrationController)
