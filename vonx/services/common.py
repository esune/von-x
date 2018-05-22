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

from . import issuer, prover, manager


class StandardServiceManager(manager.ServiceManager):
    """
    A standard ServiceManager with IssuerManager and ProverManager services
    """

    def init_services(self):
        super(StandardServiceManager, self).init_services()

        # Issuer manager - handles ready, status, submit_cred
        self._services['issuer'] = issuer.init_issuer_manager(self)

        # Prover manager - handles construct_proof
        self._services['prover'] = prover.init_prover_manager(self)