#
# Copyright 2017-2018 Government of Canada
# Public Services and Procurement Canada - buyandsell.gc.ca
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import logging.config
import os
import yaml


def load_global_config(path=None):
    """Load the application config file."""
    if not path:
        app_path = os.path.dirname(__file__)
        path = os.environ.get('CONFIG_PATH', os.path.join(app_path, 'config.yaml'))
    # Load the config file
    with open(path) as config_file:
        global_config = yaml.load(config_file)
    return global_config or {}

def load_server_config(global_config, env=True):
    """
        Extract the server configuration from the app config and apply optional
        overrides from the environment.
    """
    if env is True:
        env = os.environ
    elif not env:
        env = {}
    env_name = env.get('ENVIRONMENT', 'default').lower()
    if 'server' not in global_config or env_name not in global_config['server']:
        raise ValueError("Environment not defined by application config: {}".format(env_name))
    config = global_config['server'][env_name]
    # Inherit environment variables
    for k, v in env.items():
        if v != '':
            config[k] = v
    return config

def init_logging(global_config, logging_env=None):
    """Initialize the application logger using dictConfig."""
    if not global_config:
        return False
    if not logging_env:
        logging_env = 'default'
    log_config = None
    if 'logging' in global_config:
        if logging_env in global_config['logging']:
            log_config = global_config['logging'][logging_env]
            try:
                logging.config.dictConfig(log_config)
            except ValueError as err:
                raise ValueError("Invalid logging configuration") from err
        else:
            print("Logger not defined: {}".format(logging_env))
    else:
        print("No loggers defined by application config")
    return log_config