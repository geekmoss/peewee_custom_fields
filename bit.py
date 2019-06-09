from peewee import *


class RealBitField(Field):
    """
    Support for MySQL/MariaDB BIT type, represented as int 0 / 1

    0 is b'\\\\x00' and 1 is b'\\\\x01'


        >>> some_model.real_bit_field
        1
        >>> some_model.real_bit_field = 0
        >>> some_model.save()
    """
    field_type = 'bit'

    def db_value(self, value):
        return chr(value)

    def python_value(self, value):
        return ord(value)
    pass


class BoolBitField(Field):
    """
    Support for MySQL/MariaDB BIT type, represented as boolean

    False is b'\\\\x00' and True is b'\\\\x01'


        >>> some_model.real_bit_field
        True
        >>> some_model.real_bit_field = False
        >>> some_model.save()
    """
    field_type = 'bit'

    def db_value(self, value):
        return chr(int(value))

    def python_value(self, value):
        return bool(ord(value))
    pass
