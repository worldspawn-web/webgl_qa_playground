# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

def initialize_devices(serial_numbers):
    devices = []
    for serial in serial_numbers:
        try:
            dev = connect_device("Android:///" + serial)
            poco_instance = AndroidUiautomationPoco(dev)
            devices.append((dev, poco_instance))
            print(f"Successfully connected to device: {serial}")
        except Exception as e:
            print(f"Failed to connect to device: {serial}. Error: {str(e)}")
    return devices

def run_tests_on_device(dev, poco_instance):
    set_current(dev)
    auto_setup(__file__)
    
    assert_exists(Template(r"tpl1739549485285.png", record_pos=(-0.212, -0.039), resolution=(2400, 1080)), "Please fill in the test point.")

    
    print(f"Tests completed on device: {dev}")

def main():
    serial_numbers = ["fcd13e3e", "25a36417"]  # Замените на ваши серийные номера
    devices = initialize_devices(serial_numbers)
    
    for dev, poco_instance in devices:
        run_tests_on_device(dev, poco_instance)

if __name__ == "__main__":
    main()