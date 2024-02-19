import click

from src import config
from src.misc.states import ARGV, Mode

default_argv = ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


@click.command()
@click.version_option(version=config.MetaInfo.version, prog_name=config.WindowConfig.caption)
@click.option(*config.CLI.Param.logging, is_flag=True, default=False, help=config.CLI.Docs.logging)
@click.option(*config.CLI.Param.hide_fps, is_flag=True, default=True, help=config.CLI.Docs.hide_fps)
@click.option(*config.CLI.Param.moore, flag_value=Mode.MOORE.value, default=True, help=config.CLI.Docs.Mode.moore)
@click.option(*config.CLI.Param.neumann, flag_value=Mode.NEUMANN.value, help=config.CLI.Docs.Mode.neumann)
def run(logging: bool, show_fps: bool, mode: Mode) -> ARGV:
    """The entry point to the game of Live."""
    result = ARGV(logging=logging, show_fps=show_fps, mode=mode)
    return result
