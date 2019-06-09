from peewee import *
import msgpack


class UserConfigurationField(Field):
    field_type = 'blob'
    _uc = None

    class UC:
        def __init__(self, data):
            self._configuration: dict = msgpack.loads(data, raw=False) if data else {}
            pass

        def __getitem__(self, item):
            return self._configuration.get(item, None)

        def __setitem__(self, key, value):
            self._configuration[key] = value
            pass

        def __repr__(self):
            return f"<UserConfigurations, keys: {', '.join(self.keys())}>"

        def __iter__(self):
            return iter(self._configuration)

        def dump(self):
            return msgpack.dumps(self._configuration)

        def keys(self):
            return self._configuration.keys()

        def items(self):
            return self._configuration.items()

        def values(self):
            return self._configuration.values()
        pass

    def __init__(self, *args, **kwargs):
        self.field_type = kwargs.get("field_type", self.field_type)
        super(UserConfigurationField, self).__init__(*args, **kwargs)
        pass

    def db_value(self, value):
        return self._uc.dump()

    def python_value(self, value):
        self._uc = self.UC(value)
        return self._uc
    pass
