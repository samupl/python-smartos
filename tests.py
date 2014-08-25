# -*- coding: utf-8 -*-
from smartos.models import VMTemplate, KVMTemplate


vm_tpl = KVMTemplate()
print vm_tpl.spec.render_json()
#vm_tpl.print_attributes()
