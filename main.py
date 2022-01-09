import sys

from xcom3_bin_data.str_tab import StrTab

from xcom3_bin_data import agent, vehicle, organisation, building

from xcom3_bin_data import BinaryLoader, BinaryDescriptor


def load_string_tab(path: str, descriptor: BinaryDescriptor):
    with BinaryLoader(path, descriptor, StrTab) as loader:
        return loader()


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <path to ufo2p.exe>')
        sys.exit(1)

    path = sys.argv[1]
    with BinaryLoader(path, vehicle.VehicleBinary, vehicle.Vehicle) as loader:
        vehicles = [loader() for _ in range(33)]

    vehicle_names = load_string_tab(path, vehicle.VehicleNamesDescriptor)

    for name, veh in zip(vehicle_names, vehicles):
        print(f'{name} => {veh}\n')

    print(f'{vehicle_names[:]=}')

    org_names = load_string_tab(path, organisation.OrganisationNamesDescriptor)
    print(f'{org_names[:]=}')

    build_names = load_string_tab(path, building.BuildingNamesDescriptor)
    print(f'{build_names[:]=}')

    build_function_names = load_string_tab(path, building.BuildingFunctionNamesDescriptor)
    print(f'{build_function_names[:]=}')

    agent_type_names = load_string_tab(path, agent.AgentTypeNamesDescriptor)
    print(f'{agent_type_names[:]=}')

    print(f'{BinaryLoader(path, agent.AgentTypeNamesDescriptor, StrTab).load()[:]=}')


if __name__ == '__main__':
    main()
