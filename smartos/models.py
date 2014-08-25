# -*- coding: utf-8 -*-
import json
from smartos.json_encoder import VMSpecJsonEncoder
from smartos.properties import VMSpecBool, VMSpecInt


class VMSpec(object):
    """
    http://wiki.smartos.org/display/DOC/vmadm+JSON+Quick+Reference
    """
    _spec = dict()

    def __init__(self):
        self._spec = {
            'brand': None,

            'disks': [
                {
                    "boot": VMSpecBool(value=False),
                    "block_size": VMSpecInt(value=8192, can_update=False),

                }
            ]
        }

    def render_json(self):
        return json.dumps(self._spec, cls=VMSpecJsonEncoder)


class VMTemplate(object):
    spec = VMSpec()


class KVMTemplate(VMTemplate):
    def __init__(self):
        self.spec.brand = 'kvm'


class ZoneTemplate(VMTemplate):
    def __init__(self):
        self.spec.brand = 'joyent'
