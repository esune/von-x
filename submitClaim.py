#! /usr/local/bin/python3

#
# "requests" must be installed - pip3 install requests
#

import json
import os
import requests
import sys

agent_url = os.environ.get('AGENT_URL', 'http://localhost:5000')

if len(sys.argv) < 2:
    raise ValueError("Expected JSON file path(s)")
claim_paths = sys.argv[1:]

for claim_path in claim_paths:
    with open(claim_path) as f:
        claim = json.load(f)

        print('Submitting claim {}'.format(claim_path))

        try:
            response = requests.post(
                '{}/submit_claim'.format(agent_url),
                json=claim
            )
            result_json = response.json()
        except Exception as e:
            raise Exception(
                'Could not submit claim. '
                'Are von_connect_orgbook and TheOrgBook running?') from e

        print('Response from von_connect_orgbook:\n\n{}\n'.format(result_json))
