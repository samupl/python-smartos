# -*- coding: utf-8 -*-


class VMSpecProperty(object):
    value = None
    can_update = True
    locked = False
    val_type = None

    def __init__(self, value=None, can_update=True):
        self.can_update = can_update
        self.value = value

    def set_value(self, value):
        if self.locked:
            raise ValueError("This VMSpecProperty object cannot be edited")

        available_vals = self.val_type if type(self.val_type) in (list, tuple) else [self.val_type]
        if type(value) not in available_vals:
            raise TypeError("Value of this spec must be one of:", ", ".join(available_vals))


class VMSpecBool(VMSpecProperty):
    val_type = bool

    def set_vale(self, value):
        super(VMSpecBool, self).set_value(self, value)
        self.value = value


class VMSpecInt(VMSpecProperty):
    val_type = int
    minimum = None
    maximum = None

    def set_vale(self, value):
        super(VMSpecBool, self).set_value(self, value)

        if self.minimum is not None and value < self.minimum:
            raise ValueError("Requested value is lower than minimum", self.minimum)
        if self.maximum is not None and value > self.maximum:
            raise ValueError("Requested value is lower than maximum", self.maximum)

        self.value = value


class VMSpecString(VMSpecProperty):
    val_type = [str, unicode]
