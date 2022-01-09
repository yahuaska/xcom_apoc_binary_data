from dataclasses import dataclass
from struct import Struct
from typing import cast

from xcom3_bin_data.str_tab import StrTabDescriptor
from xcom3_bin_data.constants import VEHICLE_DATA_OFFSET_START, VEHICLE_NAME_STRTAB_OFFSET_START, VEHICLE_NAME_STRTAB_OFFSET_END


@dataclass
class Vehicle:
    manufacturer: int
    movement_type: int
    animation_type: int
    size_x: int
    size_y: int
    size_z: int
    image_position_1: int
    image_position_2: int
    image_position_3: int
    image_position_4: int
    graphic_frame: int
    acceleration: int
    dimension_travel: int
    top_speed: int
    shadow_graphic: int
    shadow_position_1: int
    shadow_position_2: int
    shadow_position_3: int
    shadow_position_4: int
    loftemps_height: int
    loftemps_index: int
    unknown2: int
    unknown3: int
    constitution: int
    crash_constitution: int
    weight: int
    armour_rear: int
    armour_top: int
    armour_right: int
    armour_left: int
    armour_bottom: int
    armour_front: int
    passenger_capacity: int
    aggressiveness: int
    score: int
    equipment_layout: bytes
    equipment_screen_name: str
    unknown4: bytes
    unknown5: bytes
    loaded_equipment_slots: bytes

    def __post_init__(self):
        _str: bytes = cast(bytes, self.equipment_screen_name)
        self.equipment_screen_name = _str.decode().replace('\0', '')


class VehicleBinary:
    offset = VEHICLE_DATA_OFFSET_START
    fields_map = {
        'manufacturer': Struct('@H'),
        'movement_type': Struct('@H'),
        'animation_type': Struct('@H'),
        'size_x': Struct('@H'),
        'size_y': Struct('@H'),
        'size_z': Struct('@H'),
        'image_position_1': Struct('@H'),
        'image_position_2': Struct('@H'),
        'image_position_3': Struct('@H'),
        'image_position_4': Struct('@H'),
        'graphic_frame': Struct('@H'),
        'acceleration': Struct('@H'),
        # All dimension-capable craft have a non-zero value,
        # I don't know what the values (1-8) then mean...
        'dimension_travel': Struct('@H'),
        'top_speed': Struct('@H'),
        'shadow_graphic': Struct('@H'),
        'shadow_position_1': Struct('@H'),
        'shadow_position_2': Struct('@H'),
        'shadow_position_3': Struct('@H'),
        'shadow_position_4': Struct('@H'),
        # I /think/ the collision model is 'loftemps_height'
        # stacked 'loftemps_index'
        # - which explains why it is thought they're related to
        # 'where the guns fire from'
        # if the 'height' is used in that,
        # as well as the 'evade chance' - as smaller volumes
        # are harder to hit
        'loftemps_height': Struct('@H'),
        'loftemps_index': Struct('@H'),
        'unknown2': Struct('@H'),
        'unknown3': Struct('@H'),
        'constitution': Struct('@H'),
        'crash_constitution': Struct('@H'),
        'weight': Struct('@H'),
        'armour_rear': Struct('@H'),
        'armour_top': Struct('@H'),
        'armour_right': Struct('@H'),
        'armour_left': Struct('@H'),
        'armour_bottom': Struct('@H'),
        'armour_front': Struct('@H'),
        'passenger_capacity': Struct('@H'),
        'aggressiveness': Struct('@H'),
        'score': Struct('@H'),
        'equipment_layout': Struct('@B'),
        'equipment_screen_name': Struct('@8s'),
        'unknown4': Struct('@B'),
        'unknown5': Struct('@B'),
        'loaded_equipment_slots': Struct('@45B'),
    }


VehicleNamesDescriptor = StrTabDescriptor(VEHICLE_NAME_STRTAB_OFFSET_START, VEHICLE_NAME_STRTAB_OFFSET_END)
