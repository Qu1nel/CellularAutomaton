from click.testing import CliRunner

import src.cli as _cli
from src import config
from src.misc.states import ARGV, Mode


# noinspection PyTypeChecker
def test_cli_return_default() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == _cli.default_argv


# noinspection PyTypeChecker
def test_cli_docs_help() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--help"], standalone_mode=False)

    assert result.exit_code == 0

    assert config.CLI.Docs.logging in result.output
    assert config.CLI.Docs.hide_fps in result.output
    assert config.CLI.Docs.Mode.moore in result.output
    assert config.CLI.Docs.Mode.neumann in result.output


# noinspection PyTypeChecker
def test_cli_docs_version() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--version"], standalone_mode=False)

    assert result.exit_code == 0

    assert config.MetaInfo.version in result.output
    assert config.WindowConfig.caption in result.output


# noinspection PyTypeChecker
def test_cli_return_Moore() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--Moore"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_Moore_short() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-M"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_Neumann() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--Neumann"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.NEUMANN)


# noinspection PyTypeChecker
def test_cli_return_Neumann_short() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-N"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.NEUMANN)


# noinspection PyTypeChecker
def test_cli_return_logging() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--logging"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=True, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_logging_short() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-L"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=True, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_no_logging() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--no-logging"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_show_fps() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--show-fps"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_show_fps_short() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-S"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_no_show_fps() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--no-show-fps"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=False, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_log_show_fps_Neumann() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-L", "-S", "-N"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=True, show_fps=True, mode=Mode.NEUMANN)


# noinspection PyTypeChecker
def test_cli_return_no_log_show_fps_Moore() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--no-logging", "-S", "--Moore"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=False, show_fps=True, mode=Mode.MOORE)


# noinspection PyTypeChecker
def test_cli_return_log_no_show_fps_Neumann() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["-L", "--no-show-fps", "-N"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=True, show_fps=False, mode=Mode.NEUMANN)


# noinspection PyTypeChecker
def test_cli_return_log_show_fps_Moore() -> None:
    runner = CliRunner()
    result = runner.invoke(_cli.run, ["--logging", "--show-fps", "--Moore"], standalone_mode=False)

    assert result.exit_code == 0
    assert result.return_value == ARGV(logging=True, show_fps=True, mode=Mode.MOORE)
