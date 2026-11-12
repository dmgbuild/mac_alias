"""Macros for the Zensical documentation build."""

from importlib.metadata import version


def define_env(env):
    """Expose the installed package version to the documentation pages."""
    env.variables["release"] = version("mac_alias")
