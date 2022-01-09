from dataclasses import dataclass
from struct import Struct
from typing import cast


class StrTabDescriptor:
    def __init__(self, start_offset: int, end_offset: int):
        self.offset = start_offset
        self._end_offset = end_offset
        self.fields_map = {
            'strings': Struct(f'@{self._end_offset - self.offset}s'),
        }


@dataclass
class StrTab:
    strings: list[str]

    def __post_init__(self):
        _bytes = cast(bytes, self.strings)
        self.strings = [s.decode('ascii') for s in _bytes.split(b'\0')]

    def __iter__(self):
        return self.strings.__iter__()

    def __getitem__(self, idx):
        return self.strings[idx]
