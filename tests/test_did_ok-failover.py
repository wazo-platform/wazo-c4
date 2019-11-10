import os

from click.testing import CliRunner
from wazotester import wazotester


TARGET = "sbc:5060"


def test_did_ok_failover():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_did_ok-failover.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file, "-t", TARGET])
    assert result.exit_code == 0
