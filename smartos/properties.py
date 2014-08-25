# -*- coding: utf-8 -*-


class VMSpecProperty(object):
    value = None
    can_update = True
    locked = False
    val_type = None
    choices = None

    def __init__(self, value=None, can_update=True, choices=None):
        self.can_update = can_update
        self.value = value
        self.choices = choices

    def set_value(self, value):
        if self.locked:
            raise ValueError("This VMSpecProperty object cannot be edited")

        available_vals = self.val_type if type(self.val_type) in (list, tuple) else [self.val_type]

        if type(value) not in available_vals:
            raise TypeError("Value of this spec must be one of the following types:", ", ".join(available_vals))

        if self.choices is not None and value not in self.choices:
            raise ValueError("Value of this spec must be one of the following:", ", ".join(self.choices))


class VMSpecBool(VMSpecProperty):
    val_type = bool

    def set_vale(self, value):
        super(VMSpecBool, self).set_value(value)
        self.value = value


class VMSpecInt(VMSpecProperty):
    val_type = int
    minimum = None
    maximum = None
    choices = None

    def __init__(self, value=None, can_update=None, minimum=None, maximum=None, choices=None):
        super(VMSpecInt, self).__init__(value, can_update, choices)
        self.minimum = minimum
        self.maximum = maximum

    def set_vale(self, value):
        super(VMSpecInt, self).set_value(value)

        if self.minimum is not None and value < self.minimum:
            raise ValueError("Requested value is lower than minimum", self.minimum)
        if self.maximum is not None and value > self.maximum:
            raise ValueError("Requested value is lower than maximum", self.maximum)

        self.value = value


class VMSpecString(VMSpecProperty):
    val_type = [str, unicode]
