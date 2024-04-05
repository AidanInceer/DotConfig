from __future__ import annotations


class DotDict:
    def __init__(self, d: dict):

        for key, value in d.items():

            if isinstance(value, dict):
                setattr(self, key, DotDict(value))
            elif isinstance(value, list):
                setattr(
                    self,
                    key,
                    [
                        DotDict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            else:
                setattr(self, key, value)

    def __repr__(self):
        items = ", ".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return f"{type(self).__name__}: {{{items}}}"
