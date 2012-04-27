# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

from katello.client.api.base import KatelloAPI
from katello.client.utils.encoding import u_str

class SystemGroupAPI(KatelloAPI):
    """
    Connection class to access environment calls
    """
    def system_groups(self, org_id, query = {}):
        path = "/api/organizations/%s/system_groups" % org_id
        return self.server.GET(path, query)[1]

    def system_group(self, org_id, system_group_id, query = {}):
        path = "/api/organizations/%s/system_groups/%s" % (org_id, system_group_id)
        return self.server.GET(path, query)[1]
    
    def system_group_by_name(self, org_id, system_group_name, query = {}):
        path = "/api/organizations/%s/system_groups/" % org_id
        system_group = self.server.GET(path, {"name" : system_group_name})[1]
        if len(system_group) > 0:
            return self.system_group(org_id, system_group[0]["id"])
        else:
            return None

    def system_group_systems(self, org_id, system_group_id, query = {}):
        path = "/api/organizations/%s/system_groups/%s/systems" % (org_id, system_group_id)
        return self.server.GET(path, query)[1]
    
    def lock(self, org_id, system_group_id, query = {}):
        path = "/api/organizations/%s/system_groups/%s/lock" % (org_id, system_group_id)
        return self.server.POST(path, query)[1]

    def unlock(self, org_id, system_group_id, query = {}):
        path = "/api/organizations/%s/system_groups/%s/unlock" % (org_id, system_group_id)
        return self.server.POST(path, query)[1]

    def create(self, org_id, name, description):
        data = { 
            "system_group" : {
                "name": name,
                "description": description
            }
        }

        path = "/api/organizations/%s/system_groups/" % (org_id)
        return self.server.POST(path, data)[1]
