import os
import unittest

from xcom3_bin_data.constants import NUM_VEHICLES, VEHICLE_DATA_OFFSET_END
from xcom3_bin_data import BinaryLoader
from xcom3_bin_data.vehicle import VehicleBinary, Vehicle


class VehiclesCase(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.getenv('UFO2P_PATH')

    def test_basic_load(self):
        with BinaryLoader(self.path, VehicleBinary, Vehicle) as loader:
            [loader() for _ in range(NUM_VEHICLES)]
            self.assertEqual(loader._fp.tell(), VEHICLE_DATA_OFFSET_END, 'Incorrect size of VehicleData array')


if __name__ == '__main__':
    unittest.main()
