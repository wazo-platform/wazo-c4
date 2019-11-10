import os

from click.testing import CliRunner
from wazotester import wazotester


TARGET = "sbc:5060"


def test_domain_ok_failover_within_dialog():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_domain_ok-failover_within_dialog.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file, "-t", TARGET])
    assert result.exit_code == 0

