# -*- coding: utf-8 -*-
from smartos.models import VMTemplate


vm_tpl = VMTemplate()
print vm_tpl.spec.render_json()
#vm_tpl.print_attributes()
