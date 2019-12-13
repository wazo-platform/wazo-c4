import os

from click.testing import CliRunner
from wazotester import wazotester


TARGET = "router:5061"


def test_router_did_ko():
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_router_did_ko.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file, "-t", TARGET])
    assert result.exit_code == 0
