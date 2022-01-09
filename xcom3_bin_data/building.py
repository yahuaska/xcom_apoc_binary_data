from xcom3_bin_data.str_tab import StrTabDescriptor
from xcom3_bin_data.constants import (
    BUILDING_NAME_STRTAB_OFFSET_START,
    BUILDING_NAME_STRTAB_OFFSET_END,
    BUILDING_FUNCTION_STRTAB_OFFSET_START,
    BUILDING_FUNCTION_STRTAB_OFFSET_END
)

BuildingNamesDescriptor = StrTabDescriptor(BUILDING_NAME_STRTAB_OFFSET_START,
                                           BUILDING_NAME_STRTAB_OFFSET_END)

BuildingFunctionNamesDescriptor = StrTabDescriptor(BUILDING_FUNCTION_STRTAB_OFFSET_START,
                                                   BUILDING_FUNCTION_STRTAB_OFFSET_END)
