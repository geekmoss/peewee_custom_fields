class DictField(Field):
    """
    MSG Pack in Blob field as Dict
    """
    field_type = 'blob'
    _dict = {}

    class Dict:
        def __init__(self, data=None, dct=None):
            if dct:
                self.data = dct
                pass
            else:
                self.data: dict = msgpack.loads(data, raw=False) if data else {}
                pass
            pass

        def __getitem__(self, item):
            return self.data.get(item, None)

        def __setitem__(self, key, value):
            self.data[key] = value
            pass

        def __repr__(self):
            return f"<DictField, keys: {', '.join(map(str, self.keys()))}>"

        def __iter__(self):
            return iter(self.data)

        def __delitem__(self, key):
            del self.data[key]

        def __bool__(self):
            return bool(self.data)

        def __dict__(self):
            return self.data

        def dump(self):
            return msgpack.dumps(self.data)

        def keys(self):
            return self.data.keys()

        def items(self):
            return self.data.items()

        def values(self):
            return self.data.values()

        def dict(self):
            return self.data
        pass

    def db_value(self, value: Union[Dict, dict]):
        return value.dump() if isinstance(value, self.Dict) else (self.Dict(dct=value)).dump()

    def python_value(self, value):
        return self.Dict(value)
    pass
