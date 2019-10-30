import os

from click.testing import CliRunner
from wazotester import wazotester


def test_did_ok():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_did_ok.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_did_ko():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_did_ko.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_domain_ok():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_domain_ok.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_domain_ko():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_domain_ko.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_outbound_ok():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_outbound_ok.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_outbound_ko_no_carrier():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(
        base_dir, "scenarios", "test_outbound_ko-no-carrier.yaml"
    )
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0


def test_outbound_ko_no_ipbx():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_outbound_ko-no-ipbx.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file])
    assert result.exit_code == 0
