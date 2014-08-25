# -*- coding: utf-8 -*-
import json
from smartos.json_encoder import VMSpecJsonEncoder
from smartos.properties import VMSpecBool, VMSpecInt, VMSpecString


class VMSpec(object):
    """
    http://wiki.smartos.org/display/DOC/vmadm+JSON+Quick+Reference
    """
    spec = dict()

    def __init__(self):
        self.spec = {
            'brand': None,

            'disks': [
                {
                    "image_name": VMSpecString(value='', can_update=False),
                    "image_size": VMSpecBool(value=0),
                    "image_uuid": VMSpecString(value='', can_update=False),

                }
            ]
        }

    def render_json(self):
        #print self.spec
        dump = json.dumps(self.spec, cls=VMSpecJsonEncoder, indent=4, sort_keys=True)
        return dump


class VMTemplate(object):
    spec = VMSpec()


class KVMTemplate(VMTemplate):
    def __init__(self):
        self.spec.spec['disks'][0]['boot'] = VMSpecBool(value=False)
        self.spec.spec['disks'][0]['block_size'] = VMSpecInt(value=8192, can_update=False)
        self.spec.spec['disks'][0]['nocreate'] = VMSpecBool(value=False, can_update=False)
        self.spec.spec['disks'][0]['size'] = VMSpecInt(value=0, can_update=False, minimum=1)
        self.spec.spec['disks'][0]['media'] = VMSpecString(value='disk', choices=['disk', 'cdrom'])
        self.spec.spec['disks'][0]['model'] = VMSpecString(value='', choices=['virtio', 'ide', 'scsi'])
        self.spec.spec['disks'][0]['compression'] = VMSpecString(value='', choices=['on',
                                                                                    'off',
                                                                                    'lzjb',
                                                                                    'gzip',
                                                                                    'gzip-9',
                                                                                    'zle'])
        self.spec.spec['disks'][0]['zpool'] = VMSpecString(value='zones')


class ZoneTemplate(VMTemplate):
    def __init__(self):
        pass
