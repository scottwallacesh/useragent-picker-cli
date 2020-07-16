import pytest
from click.testing import CliRunner
from ua_gen import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    for _ in range(1, 1000):
        assert len(result.output.strip()) > 10

def test_cli_with_option(runner):
    result = runner.invoke(cli.main, ['--as-cowboy'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'Howdy, world.'


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['Chris'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, Chris.'