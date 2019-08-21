
from AutoGeicoTestClass import Auto_Geico_Test
from VehicleTestModules import VehicleTestModules
import sys


#Precondition methods used to get initial conditions for a test case.
def preconditionA(testCaseObject):
    #these are the steps from test case(s) A in order in order to do test case B01
    testCaseObject.zip_input_0()
    testCaseObject.skip_help_page_0()
    testCaseObject.next_button_0()
    return

    #these are the steps from test cases A and B in order to do test case C01
def preconditionB(testCaseObject):
    preconditionA(testCaseObject)
    testCaseObject.first_name_input_0()
    testCaseObject.last_name_input_0()
    testCaseObject.next_button_1()
    return

    #these are the steps from test cases A, B, and C in order to do test case D01
def preconditionC(testCaseObject):
    preconditionB(testCaseObject)
    testCaseObject.month_dob_0()
    testCaseObject.day_dob_0()
    testCaseObject.year_dob_0()
    testCaseObject.next_button_2()
    return

    #these are the steps from test cases A, B, C and D in order to do test case E01
def preconditionD(testCaseObject):
    preconditionC(testCaseObject)
    testCaseObject.street_input_0()
    testCaseObject.zip_input_1()
    testCaseObject.next_button_3()
    try:
        testCaseObject.verify_address_0()
        testCaseObject.next_button_4()
    except:
        print("unable to locate verify address")
    return

def preconditionE(testCaseObject):
    preconditionD(testCaseObject)
    testCaseObject.vehicle_not_listed_class_0()
    testCaseObject.next_button_x()
    return

#TC_G01
try:
    Test_G01 = VehicleTestModules()
    #preconditionE(Test_G01)

    Test_G01.select_specific_vehicle(1, 2, 3)
    print("test G01 ran successfully")

except Exception as err:
    print('Test G01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test G01:")
    print(err.__module__)
    print(str(err))


#GEICO HELP TEST CASES
#TC_A01 - I NEED INSURANCE RIGHT AWAY
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


#TC_A02 - I'M BUYING OR JUST BOUGHT A CAR
try:
    Test_A02 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A02.zip_input_0()
    Test_A02.customer_intent_1()
    Test_A02.next_button_0()
    print("test case A02 ran successfully")
    Test_A02.close_browser()

except Exception as err:
    print('Test A02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A02:")
    print(err.__module__)


#TC A03 - i'M LOOKING FOR A BETTER PRICE
try:
    Test_A03 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A03.zip_input_0()
    Test_A03.customer_intent_2()
    Test_A03.next_button_0()
    print("test case A03 ran successfully")
    Test_A03.close_browser()

except Exception as err:
    print('Test A03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A03:")
    print(err.__module__)

#TC_A04 - I'M COMPARING RATES FOR DIFFERENT CARS
try:
    Test_A04 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A04.zip_input_0()
    Test_A04.customer_intent_3()
    Test_A04.next_button_0()
    print("test case A04 ran successfully")
    Test_A04.close_browser()

except Exception as err:
    print('Test A04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A04:")
    print(err.__module__)


#TC_A05 - I'M JUST SHOPPING TODAY
try:
    Test_A05 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A05.zip_input_0()
    Test_A05.customer_intent_4()
    Test_A05.next_button_0()
    print("test case A05 ran successfully")
    Test_A05.close_browser()

except Exception as err:
    print('Test A05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test A05:")
    print(err.__module__)


#TC A06 - SKIP
try:
    Test_A06 = Auto_Geico_Test() #creating an object to use the class that has the functionality that is needed for test cases

    Test_A06.zip_input_0()
    Test_A06.customer_intent_5()
    Test_A06.next_button_0()
    print("test case A06 ran successfully")
    Test_A06.close_browser()

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
    Test_B01.close_browser()

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
    Test_C01.close_browser()

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
    Test_D01.close_browser()
except Exception as err:
    print('Test D01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test D01:")
    print(err.__module__)


#TC_E01 - DRIVER INFORMATION - SELECT GENDER
try:
    Test_E01 = Auto_Geico_Test()
    # preconditionX(Test_E01)

    Test_E01.gender_select_0()
    Test_E01.close_browser()
    print("test E01 ran successfully")

except Exception as err:
    print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E01:")
    print(err.__module__)
    print(str(err))

#TC_E02 - DRIVER INFORMATION - MARITAL STATUS AND SOCIAL SECURITY NUMBER
try:
    Test_E02 = Auto_Geico_Test()
    # preconditionX(Test_E01)

    Test_E02.marital_status_0()
    Test_E02.social_security_number_0()
    Test_E02.next_button_x()
    Test_E02.social_security_number_2()
    Test_E02.next_button_x()
    Test_E02.social_security_number_1()
    Test_E02.next_button_x()
    print("test E02 ran successfully")
    Test_E02.close_browser()

except Exception as err:
    print('Test E02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E02:")
    print(err.__module__)
    print(str(err))

#TC_E03 - DRIVER INFORMATION - HOME INFORMATION
try:
    Test_E03 = Auto_Geico_Test()
    # preconditionX(Test_E03)

    Test_E03.home_ownership_0()
    Test_E03.next_button_x()
    print("test E03 ran successfully")
    Test_E03.close_browser()

except Exception as err:
    print('Test E03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E03:")
    print(err.__module__)
    print(str(err))

#TC_E04.1 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "YES"
try:
    Test_E04o1 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E04o1.current_insured_status_1()
    Test_E04o1.next_button_x()
    Test_E04o1.current_insurance_disclosure_0()
    Test_E04o1.current_insurance_disclosure_1()
    Test_E04o1.previous_insurance_disclosure_3()
    Test_E04o1.next_button_x()
    Test_E04o1.driving_history_1()
    Test_E04o1.next_button_x()
    print("test E04o1 ran successfully")
    Test_E04o1.close_browser()

except Exception as err:
    print('Test E04o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o1:")
    print(err.__module__)
    print(str(err))

#TC_E04.2 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I HAVEN'T NEEDED INSURANCE"
try:
    Test_E04o2 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E04o2.current_insured_status_2()
    Test_E04o2.next_button_x()
    Test_E04o2.driving_history_1()
    Test_E04o2.next_button_x()
    print("test E04o2 ran successfully")
    Test_E04o2.close_browser()

except Exception as err:
    print('Test E04o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o2:")
    print(err.__module__)
    print(str(err))

#TC_E04.3 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, MY INSUARANCE RAN OUT"
try:
    Test_E04o3 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E04o3.current_insured_status_3()
    Test_E04o3.next_button_x()
    Test_E04o3.previous_insurance_disclosure_0()
    Test_E04o3.previous_insurance_disclosure_1()
    Test_E04o3.previous_insurance_disclosure_3()
    Test_E04o3.next_button_x()
    Test_E04o3.driving_history_1()
    Test_E04o3.next_button_x()
    print("test E04o3 ran successfully")
    Test_E04o3.close_browser()

except Exception as err:
    print('Test E04o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o3:")
    print(err.__module__)
    print(str(err))

#TC_E04.4 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I WAS DEPLOYED"
try:
    Test_E04o4 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E04o4.current_insured_status_4()
    Test_E04o4.next_button_x()
    print("test E04o4 ran successfully")
    Test_E04o4.close_browser()

except Exception as err:
    print('Test E04o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E04o4:")
    print(err.__module__)
    print(str(err))

#TC_XX01 - DRIVER INFORMATION - EDUCATION
try:
    Test_XX01 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_XX01.education_level_0()
    Test_XX01.next_button_x()
    print("test E04o4 ran successfully")

except Exception as err:
    print('Test XX01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test XX01:")
    print(err.__module__)
    print(str(err))

#TC_E05o1 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
try:
    Test_E05o1 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o1.employment_status_0()
    Test_E05o1.next_button_x()
    Test_E05o1.current_occupation_0()
    Test_E05o1.current_occupation_1()
    Test_E05o1.next_button_x()
    print("test E05o1 ran successfully")

except Exception as err:
    print('Test E05o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o1:")
    print(err.__module__)
    print(str(err))

#TC_E05o2 - DRIVER INFORMATION - EMPLOYMENT STATUS - "ACTIVE MILITARY DUTY"
try:
    Test_E05o2 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o2.employment_status_0()
    Test_E05o2.employment_status_1()
    Test_E05o2.employment_status_2()
    Test_E05o2.next_button_x()
    print("test E05o2 ran successfully")

except Exception as err:
    print('Test E05o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o2:")
    print(err.__module__)
    print(str(err))

#TC_E05o3 - DRIVER INFORMATION - EMPLOYMENT STATUS - "FEDERAL GOVERNMENT AND POSTAL SERVICE"
try:
    Test_E05o3 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o3.employment_status_0()
    Test_E05o3.employment_status_3()
    Test_E05o3.next_button_x()
    print("test E05o3 ran successfully")

except Exception as err:
    print('Test E05o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o3:")
    print(err.__module__)
    print(str(err))

#TC_E05o4 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A STAE/LOCAL/MUNICIPAL GOVERNMENT"
try:
    Test_E05o4 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o4.employment_status_0()
    Test_E05o4.employment_status_3()
    Test_E05o4.next_button_x()
    print("test E05o4 ran successfully")

except Exception as err:
    print('Test E05o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o4:")
    print(err.__module__)
    print(str(err))

#TC_E05o5 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM A FULL TIME STUDENT"
try:
    Test_E05o5 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o5.employment_status_0()
    Test_E05o5.next_button_x()
    print("test E05o4 ran successfully")

except Exception as err:
    print('Test E05o5' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o5:")
    print(err.__module__)
    print(str(err))

#TC_E05o6 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM CURRENTLY A HOMEMAKER"
try:
    Test_E05o6 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o6.employment_status_0()
    Test_E05o6.next_button_x()
    print("test E05o6 ran successfully")

except Exception as err:
    print('Test E05o6' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o6:")
    print(err.__module__)
    print(str(err))

#TC_E05o7 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM NOT CURRENTLY EMPLOYED"
try:
    Test_E05o7 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o7.employment_status_0()
    Test_E05o7.next_button_x()
    print("test E05o7 ran successfully")

except Exception as err:
    print('Test E05o7' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05O7:")
    print(err.__module__)
    print(str(err))

#TC_E05o8 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
try:
    Test_E05o7 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o7.employment_status_0()
    Test_E05o7.next_button_x()
    Test_E05o7.current_occupation_0()
    Test_E05o7.current_occupation_1()
    Test_E05o7.next_button_x()
    print("test E05o7 ran successfully")

except Exception as err:
    print('Test E05o7' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05O7:")
    print(err.__module__)
    print(str(err))

#TC_E05o9 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED MILITARY"
try:
    Test_E05o9 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o9.employment_status_0()
    Test_E05o9.employment_status_1()
    Test_E05o9.employment_status_2()
    Test_E05o9.next_button_x()
    print("test E05o9 ran successfully")

except Exception as err:
    print('Test E05o9' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o9:")
    print(err.__module__)
    print(str(err))

#TC_E05o10 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED FEDERAL GOVERNMENT AND POSTAL SERVICE"
try:
    Test_E05o10 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o10.employment_status_0()
    Test_E05o10.employment_status_3()
    Test_E05o10.next_button_x()
    print("test E05o10 ran successfully")

except Exception as err:
    print('Test E05o10' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o10:")
    print(err.__module__)
    print(str(err))

#TC_E05o11 - DRIVER INFORMATION - EMPLOYMENT STATUS - "RETIRED STAE/LOCAL/MUNICIPAL GOVERNMENT"
try:
    Test_E05o11 = Auto_Geico_Test()
    # preconditionX(Test_E04)

    Test_E05o11.employment_status_0()
    Test_E05o11.employment_status_3()
    Test_E05o11.next_button_x()
    print("test E05o11 ran successfully")

except Exception as err:
    print('Test E05o11' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(err.args)
    print("An error occured while running automation test for Geico Test E05o10:")
    print(err.__module__)
    print(str(err))






