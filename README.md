# DotDict

<a href="https://github.com/AidanInceer/DotDict">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-0.2.0-blue">
</a>

A simple package which converts a standard python dictionary to a dot accessible object.

## Installation

``` bash
pip install dot_notation_dict
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
