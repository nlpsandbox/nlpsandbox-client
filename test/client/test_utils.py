from unittest.mock import patch

import nlpsandbox
from nlpsandboxclient import utils


def test_get_api_configuration():
    """Test getting API configuration"""
    configuration = nlpsandbox.Configuration()
    with patch.object(nlpsandbox, "Configuration",
                      return_value=configuration),\
         patch.object(utils, "check_url"):
        config = utils.get_api_configuration(host="0.0.0.0")
        assert config == configuration
