from __future__ import annotations

from typing import Union


class DotDict(dict):
    def __getattr__(self, attr: Union[DotDict, dict, list, str]):
        """
        Retrieve the value of the attribute from the configuration dictionary.

        If the attribute exists in the configuration dictionary, it returns the value.
        If the value is a dictionary, it returns a new instance of DotDict with
        the value as the configuration dictionary.
        If the value is a list, it returns a new list with each item converted to
        DotDict if it is a dictionary, otherwise it returns the item as is.

        Args:
            attr (str): The name of the attribute to retrieve.

        Returns:
            The value of the attribute.

        Raises:
            AttributeError: If the attribute does not exist in the configuration dictionary.
        """
        if attr in self:
            value = self[attr]
            if isinstance(value, dict):
                return DotDict(value)
            elif isinstance(value, list):
                return [
                    (
                        DotDict(item[0])
                        if isinstance(item, list)
                        and len(item) == 1
                        and isinstance(item[0], dict)
                        else (DotDict(item) if isinstance(item, dict) else item)
                    )
                    for item in value
                ]
            return value
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{attr}'"
        )

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
