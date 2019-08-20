from VehicleTestModules import VehicleTestModules
from selenium import webdriver

gvt = VehicleTestModules()

ErrorCount = 0

while True:
    try:

        # this goes through  the flow of adding a vehicle
        gvt.get_to_vehicle_page()
        gvt.select_specific_vehicle(2, 5, 4)
        gvt.select_specific_body_style(1)           # doesnt always run
        gvt.select_specific_new_costs(2)            # doesnt always run
        gvt.select_antilock_brakes(0)               # doesnt always run
        gvt.select_specific_antitheft_device(0)     # doesnt always run
        gvt.select_ownership(1)
        gvt.select_primary_use(2)
        gvt.select_annual_mileage(2)

    except Exception as err:

        ErrorCount = ErrorCount + 1
        print("Exception thrown on module:\t" + str(gvt.CurrentModule))
        print(str(err))