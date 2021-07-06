import os
from enum import Enum


class Environment(str, Enum):
    DEVELOPMENT = "DEVELOPMENT"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"


def get_environment() -> Environment:
    """Get the current environment"""
    raw = os.environ.get("ENVIRONMENT", Environment.DEVELOPMENT.value)
    normalized = raw.strip().upper()
    return {
        Environment.PRODUCTION.value: Environment.PRODUCTION,
        Environment.STAGING.value: Environment.STAGING,
    }.get(normalized, Environment.DEVELOPMENT)


def get_required_environment_variable(environment_variable: str) -> str:
    """Get an environment variable or throw if it doesn't exist in the environment"""
    value = os.environ.get(environment_variable)
    if value is None:
        raise EnvironmentError(
            f"Expected Environment Variable '{environment_variable}'"
        )
    return value
