# -*- coding: utf-8 -*-
from json import JSONEncoder
from smartos.properties import VMSpecProperty


class VMSpecJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, VMSpecProperty):
            return o.value
