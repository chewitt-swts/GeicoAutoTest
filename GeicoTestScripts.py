
from AutoGeicoTestClass import Auto_Geico_Test
from VehicleTestModules import VehicleTestModules
import sys


#Precondition methods used to get initial conditions for a test case.
def preconditionA(anObject):
    #these are the steps from test case(s) A in order in order to do test case B01
    anObject.zip_input_0()
    anObject.skip_help_page_0()
    anObject.next_button_0()
    return

    #these are the steps from test cases A and B in order to do test case C01
def preconditionB(anObject):
    preconditionA(anObject)
    anObject.first_name_input_0()
    anObject.last_name_input_0()
    anObject.next_button_1()
    return

    #these are the steps from test cases A, B, and C in order to do test case D01
def preconditionC(anObject):
    preconditionB(anObject)
    anObject.month_dob_0()
    anObject.day_dob_0()
    anObject.year_dob_0()
    anObject.next_button_2()
    return

    #these are the steps from test cases A, B, C and D in order to do test case E01
def preconditionD(anObject):
    preconditionC(anObject)
    anObject.street_input_0()
    anObject.zip_input_1()
    anObject.next_button_3()
    try:
        anObject.verify_address_0()
        anObject.next_button_4()
    except:
        print("unable to locate verify address")
    return

def preconditionE(anObject):
    preconditionD(anObject)
    anObject.vehicle_not_listed_class_0()
    anObject.next_button_x()
    return

#TC_G01
try:
    Test_G01 = VehicleTestModules()
    #preconditionE(Test_G01)

    Test_G01.select_specific_vehicle(1, 2, 3)
    print("test G01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test G01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test G01:")
    print(err.__module__)
    print(str(err))


#GEICO HELP TEST CASES
#TC_A01
try:
    Test_A01 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A01.zip_input_0()
    Test_A01.customer_intent_0()
    Test_A01.next_button_0()
    print("test case A01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A01:")
    print(err.__module__)


#TC_A02
try:
    Test_A02 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A02.zip_input_0()
    Test_A02.customer_intent_1()
    Test_A02.next_button_0()
    print("test case A02 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A02:")
    print(err.__module__)


#TC A03
try:
    Test_A03 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A03.zip_input_0()
    Test_A03.customer_intent_2()
    Test_A03.next_button_0()
    print("test case A03 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A03:")
    print(err.__module__)

#TC_A04
try:
    Test_A04 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A04.zip_input_0()
    Test_A04.customer_intent_3()
    Test_A04.next_button_0()
    print("test case A04 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A04:")
    print(err.__module__)


#TC_A05
try:
    Test_A05 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A05.zip_input_0()
    Test_A05.customer_intent_4()
    Test_A05.next_button_0()
    print("test case A05 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A05:")
    print(err.__module__)


#TC A06
try:
    Test_A06 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A06.zip_input_0()
    Test_A06.customer_intent_5()
    Test_A06.next_button_0()
    print("test case A06 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test A06' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A06:")
    print(err.__module__)

#
#TC_B01 - WHAT IS YOUR NAME
try:
    Test_B01 = Auto_Geico_Test() #creating Test case object
    preconditionA(Test_B01) #does initial setup for test B01

    Test_B01.first_name_input_0()
    Test_B01.last_name_input_0()
    Test_B01.next_button_1()
    print("test case B01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test B01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test B01:")
    print(err.__module__)

#TC_C01 - WHEN WERE YOU BORN
try:
    Test_C01 = Auto_Geico_Test()
    preconditionB(Test_C01)

    Test_C01.month_dob_0()
    Test_C01.day_dob_0()
    Test_C01.year_dob_0()
    Test_C01.next_button_2()
    print("test case C01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test C01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test C01:")
    print(err.__module__)

#TC_D01 - WHAT'S YOUR ADDRESS,APARTMENT, ZIP CODE
try:
    Test_D01 = Auto_Geico_Test()
    preconditionC(Test_D01)

    Test_D01.street_input_0()
    #Test_D01.apt_input_0()
    Test_D01.zip_input_1()
    Test_D01.next_button_3()
    Test_D01.verify_address_0()
    Test_D01.next_button_4()
    #Test_D01.have_you_moved()
    print("test D01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test D01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test D01:")
    print(err.__module__)

#TC_E01 - DRIVER INFORMATION - SELECT GENDER
try:
    Test_E01 = Auto_Geico_Test()
    # preconditionD(Test_E01)

    Test_E01.vehicle_not_listed_class_0()
    Test_E01.next_button_x()
    print("test E01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E01:")
    print(err.__module__)
    print(str(err))

#TC_G01 - ADDING NEW VEHICLE INFORMATION/YEAR, MAKE, MODEL (1981 - 2020)
try:
    Test_G01 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_G01.select_specific_vehicle(1, 2, 3)
    print("test G01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test G01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test G01:")
    print(err.__module__)
    print(str(err))

#TC_G02 - ADDING NEW VEHICLE INFORMATION/YEAR, MAKE, MODEL (PRE 1981)
try:
    Test_G02 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_G02.select_specific_vehicle(1, 2, 3)
    print("test G02 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test G02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test G02:")
    print(err.__module__)
    print(str(err))

# TC_G02 - ADDING NEW VEHICLE INFORMATION/YEAR, MAKE, MODEL (PRE 1981)
try:
    Test_G02 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_G02.add_vehicle_pre1981(1, 2, 3)
    print("test G02 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test G02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test G02:")
    print(err.__module__)
    print(str(err))

#TC_H01 - SPECIAL FEATURES: BODY STYLE
try:
    Test_H01 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_H01.select_body_styles()
    print("test H01 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test H01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test H01:")
    print(err.__module__)
    print(str(err))

#TC_H02 - SPECIAL FEATURES: ANTI-THEFT DEVICE
try:
    Test_H02 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_H02.select_antitheft_devices()
    print("test H02 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test H02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test H02:")
    print(err.__module__)
    print(str(err))

#TC_H03 - SPECIAL FEATURES: ANTI-LOCK BRAKES
try:
    Test_H03 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_H03.select_antilock_brakes()
    print("test H03 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test H03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test H03:")
    print(err.__module__)
    print(str(err))

#TC_H04 - SPECIAL FEATURES: NEW COST
try:
    Test_H04 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_H04.select_new_costs()
    print("test H01 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test H04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test H04:")
    print(err.__module__)
    print(str(err))

#TC_I01 - VEHICLE OWNERSHIP - OWNED
try:
    Test_I01 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_I01.select_ownership(0, 1, 2)
    print("test I01 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test I01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test I01:")
    print(err.__module__)
    print(str(err))

#TC_I02 - VEHICLE OWNERSHIP - FINANCED
try:
    Test_I02 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_I02.select_ownership(0, 1, 2)
    print("test I02 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test I02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test I02:")
    print(err.__module__)
    print(str(err))

#TC_I03 - VEHICLE OWNERSHIP - LEASED
try:
    Test_I03 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_I03.select_ownership(0, 1, 2)
    print("test I03 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test I03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test I03:")
    print(err.__module__)
    print(str(err))

#TC_J01 - ADDING PRIMARY USE - COMMUTE
try:
    Test_J01 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_J01.select_ownership(0, 1, 2)
    print("test J01 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test J01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test J01:")
    print(err.__module__)
    print(str(err))

#TC_J02 - ADDING PRIMARY USE - PLEASURE
try:
    Test_J02 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_J02.select_ownership(0, 1, 2)
    print("test J02 ran successfully")
    Test_A01.close_browser()

except Exception as err:
    print('Test J02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test J02:")
    print(err.__module__)
    print(str(err))

#TC_J03 - ADDING PRIMARY USE - BUSINESS
try:
    Test_J03 = VehicleTestModules
    # preconditionD(Test_E0)

    Test_J03.select_ownership(0, 1, 2)
    print("test J03 ran successfully")
    Test_A01.close_browser()
except Exception as err:
    print('Test J03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test J03:")
    print(err.__module__)
    print(str(err))

































'''
#TC B01
zip input()
customer intent
enter first name
enter last name
select next
#
'''







