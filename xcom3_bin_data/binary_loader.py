from struct import Struct
from typing import Protocol, Callable, Optional, IO


class BinaryDescriptor(Protocol):
    offset: int
    fields_map: dict[str, Struct]


class BinaryLoader:
    def __init__(self, path: str, binary_descriptor: BinaryDescriptor, cls: Callable):
        self._ufo2p_path = path
        self._binary_descriptor = binary_descriptor
        self._cls = cls

        self._fp: Optional[IO] = None

    def __enter__(self):
        self._fp = open(self._ufo2p_path, 'rb')
        self._fp.__enter__()
        self._fp.seek(self._binary_descriptor.offset)
        return self

    def __exit__(self, err_type, err_value, traceback):
        self._fp.__exit__(err_type, err_value, traceback)
        self._fp.close()
        self._fp = None

    def __call__(self):
        kwargs = {}
        assert self._fp is not None
        for k, v in self._binary_descriptor.fields_map.items():
            v = v.unpack(self._fp.read(v.size))
            # unpack always returns tuple, even if there's only one element
            if len(v) == 1:
                v = v[0]
            kwargs[k] = v
        return self._cls(**kwargs)

    def load(self):
        with self as _:
            return self()
