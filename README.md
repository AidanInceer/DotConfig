# DotDict

A simple package which converts a standard python dictionary to a dot accessible object.

## Installation

``` bash
pip install dot-dict
```

## Usage

``` python
from dotdict import DotDict

mydict = {
    "A": [1, 2, 3, 4],
    "B": {"C": 5},
    "D": "E",
    "F": None,
}

ddict = DotDict(mydict)

ddict.A
>>> [1, 2, 3, 4]

ddict.B
>>> {"C": 5}

ddict.B.C
>>> 5

ddict.D
>>> "E"

ddict.F
>>> None

```
