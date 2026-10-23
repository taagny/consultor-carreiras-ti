"""Shim de compatibilidade do Experta para versões modernas do Python (3.10+).

Em Python 3.10+, várias classes abstratas de coleção foram removidas do módulo
`collections` e residem em `collections.abc`. Este shim assegura a retrocompatibilidade
atribuindo-as a `collections` antes da importação do `experta`.
"""

import collections
import collections.abc

# Nomes exigidos para compatibilidade com experta e frozendict
_COLLECTIONS_ATTRIBUTES = (
    "Mapping",
    "MutableMapping",
    "Sequence",
    "Iterable",
    "Callable",
)

for _attr in _COLLECTIONS_ATTRIBUTES:
    if not hasattr(collections, _attr) and hasattr(collections.abc, _attr):
        setattr(collections, _attr, getattr(collections.abc, _attr))
