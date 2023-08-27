from functools import lru_cache
from typing import Dict, Type

from core.base import AppEnvTypes, BaseAppSettings
from core.app import AppSettings
from core.dev import DevAppSettings
from core.prod import ProdAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    # AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()

settings = get_app_settings()
