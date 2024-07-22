from dependency_injector import containers, providers
from .services import ImageTransformerService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    image_transformer = providers.Factory(
        ImageTransformerService,
        eye_drawer_type=config.eye_drawer_type
    )
