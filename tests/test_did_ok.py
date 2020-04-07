import os

from click.testing import CliRunner
from wazotester import wazotester


TARGET = os.environ.get('TARGET', 'sbc:5060')
API_URL = os.environ.get('API_URL', 'http://rating-api:8000')


def test_did_ok():
    """Test an inbound call from a carrier to an IPBX mapping DID and domain.
    The call routing must be OK
    """
    base_dir = os.path.dirname(__file__)
    scenario_file = os.path.join(base_dir, "scenarios", "test_did_ok.yaml")
    runner = CliRunner()
    result = runner.invoke(wazotester, [scenario_file, "-t", TARGET])
    assert result.exit_code == 0
