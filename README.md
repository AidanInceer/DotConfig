# DotConfig

<a href="https://github.com/AidanInceer/DotDict">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-0.2.1-blue">
</a>

A simple package which converts a standard python dictionary to a dot accessible configuration object.

## Installation

``` bash
pip install dotcon
```

## Usage

``` python
from dotcon import DotConfig

mydict = {
    "A": [1, 2, 3, 4],
    "B": {"C": 5},
    "D": "E",
    "F": None,
}

ddict = DotConfig(mydict)

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
