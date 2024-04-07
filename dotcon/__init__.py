from __future__ import annotations


class DotConfig:
    def __init__(self, d: dict):
        for key, value in d.items():
            if isinstance(value, dict):
                setattr(self, key, DotConfig(value))
            elif isinstance(value, list):
                setattr(
                    self,
                    key,
                    [
                        DotConfig(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            else:
                setattr(self, key, value)

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, DotConfig):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [
                    item.to_dict() if isinstance(item, DotConfig) else item
                    for item in value
                ]
            else:
                result[key] = value
        return result

    def __repr__(self):
        items = ", ".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return f"{type(self).__name__}: {{{items}}}"

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value

    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            raise AttributeError(
                f"{type(self).__name__} object has no attribute '{key}'"
            )

    def __delattr__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]
        else:
            raise AttributeError(f"{key} does not exist in attributes.")

    def __delitem__(self, key):
        if key in self.__dict__:
            del self.__dict__[key]
        else:
            print(f"{key} does not exist in attributes.")

    def pop(self, key):
        if key in self.__dict__:
            del self.__dict__[key]
        else:
            print(f"{key} does not exist in attributes.")

    def keys(self):
        return list(self.__dict__.keys())

    def items(self):
        return self.__dict__.items()
