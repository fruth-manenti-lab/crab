import sys

sys.path.insert(1, '../')
sys.path.insert(1, '../scripts/')

from radioroc_client import (
    AcquisitionConfig,
    DEFAULT_CONFIG,
    RadiorocDevice,
    RadiorocSerial,
    default_run_dir,
    parse_channels,
)

from radioroc_cli_common import (
    add_connection_args,
    add_write_safety_args,
    apply_preset_defaults,
    connection_config_from_args,
    load_preset_from_argv,
    run_metadata,
    settings_from_args,
)

from radioroc.transport import RadiorocConnectionConfig
from radioroc.application import CancellationToken
from radioroc.application.acquisition import AcquisitionJob, AcquisitionJobConfig
DEFAULT_N_EVENTS = 1000

def acquire(channels, threshold, delay):
    connection = RadiorocConnectionConfig()
    print(connection)
    pass

if __name__ == "__main__":
    acquire([], 10, 10)
