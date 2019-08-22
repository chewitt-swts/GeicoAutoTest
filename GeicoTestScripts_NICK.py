
from AutoGeicoTestClass import Auto_Geico_Test
import sys

TestDriver = Auto_Geico_Test()

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

def Test_A01():
    #GEICO HELP TEST CASES
    #TC_A01 - I NEED INSURANCE RIGHT AWAY
    try:

        TestDriver.zip_input_0()
        TestDriver.customer_intent_0()
        TestDriver.next_button_0()
        print("test case A01 ran successfully")
        TestDriver.close_browser()
    except Exception as err:
        print('Test A01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A01:")
        print(err.__module__)

def Test_A02():
    #TC_A02 - I'M BUYING OR JUST BOUGHT A CAR
    try:
        TestDriver.zip_input_0()
        TestDriver.customer_intent_1()
        TestDriver.next_button_0()
        print("test case A02 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test A02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A02:")
        print(err.__module__)

def Test_A03():
    #TC A03 - i'M LOOKING FOR A BETTER PRICE
    try:
        TestDriver.zip_input_0()
        TestDriver.customer_intent_2()
        TestDriver.next_button_0()
        print("test case A03 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test A03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A03:")
        print(err.__module__)
def Test_A04():
    #TC_A04 - I'M COMPARING RATES FOR DIFFERENT CARS
    try:
        TestDriver.zip_input_0()
        TestDriver.customer_intent_3()
        TestDriver.next_button_0()
        print("test case A04 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test A04' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A04:")
        print(err.__module__)

def Test_A05():
    #TC_A05 - I'M JUST SHOPPING TODAY
    try:
        TestDriver.zip_input_0()
        TestDriver.customer_intent_4()
        TestDriver.next_button_0()
        print("test case A05 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test A05' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A05:")
        print(err.__module__)

def Test_A06():
    #TC A06 - SKIP
    try:
        TestDriver.zip_input_0()
        TestDriver.customer_intent_5()
        TestDriver.next_button_0()
        print("test case A06 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test A06' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test A06:")
        print(err.__module__)

def Test_B01():
    #TC_B01 - WHAT IS YOUR NAME
    try:
        TestDriver.first_name_input_0()
        TestDriver.last_name_input_0()
        TestDriver.next_button_1()
        print("test case B01 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test B01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test B01:")
        print(err.__module__)

def Test_C01():
    #TC_C01 - WHEN WERE YOU BORN
    try:
        TestDriver.month_dob_0()
        TestDriver.day_dob_0()
        TestDriver.year_dob_0()
        TestDriver.next_button_2()
        print("test case C01 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test C01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test C01:")
        print(err.__module__)

def Test_D01():
    #TC_D01 - WHAT'S YOUR ADDRESS,APARTMENT, ZIP CODE
    #TODO look back at this and make sure it is accurate, we haven't fleshed this out entirely
    try:
        TestDriver.street_input_0()
        #Test_D01.apt_input_0()
        TestDriver.zip_input_1()
        TestDriver.next_button_3()
        TestDriver.verify_address_0()
        TestDriver.next_button_4()
        #Test_D01.have_you_moved()
        print("test D01 ran successfully")
        TestDriver.close_browser()
    except Exception as err:
        print('Test D01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test D01:")
        print(err.__module__)

def Test_E01():
    #TODO need to add preconditions to E01 - E5.11 lots of work to do here
    #TC_E01 - DRIVER INFORMATION - SELECT GENDER
    try:

        TestDriver.gender_select_0()
        TestDriver.close_browser()
        print("test E01 ran successfully")

    except Exception as err:
        print('Test E01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E01:")
        print(err.__module__)
        print(str(err))

def Test_E02():
    #TC_E02 - DRIVER INFORMATION - MARITAL STATUS AND SOCIAL SECURITY NUMBER
    try:
        TestDriver.marital_status_0()
        TestDriver.social_security_number_0()
        TestDriver.next_button_x()
        TestDriver.social_security_number_2()
        TestDriver.next_button_x()
        TestDriver.social_security_number_1()
        TestDriver.next_button_x()
        print("test E02 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test E02' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E02:")
        print(err.__module__)
        print(str(err))

def Test_E03():
    #TC_E03 - DRIVER INFORMATION - HOME INFORMATION
    try:
        TestDriver.home_ownership_0()
        TestDriver.next_button_x()
        print("test E03 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test E03' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E03:")
        print(err.__module__)
        print(str(err))

def Test_E04o1():
    #TC_E04.1 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "YES"
    try:
        TestDriver.current_insured_status_1()
        TestDriver.next_button_x()
        TestDriver.current_insurance_disclosure_0()
        TestDriver.current_insurance_disclosure_1()
        TestDriver.previous_insurance_disclosure_3()
        TestDriver.next_button_x()
        TestDriver.driving_history_1()
        TestDriver.next_button_x()
        print("test E04o1 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test E04o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E04o1:")
        print(err.__module__)
        print(str(err))

def Test_E04o2():
    #TC_E04.2 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I HAVEN'T NEEDED INSURANCE"
    try:
        TestDriver.current_insured_status_2()
        TestDriver.next_button_x()
        TestDriver.driving_history_1()
        TestDriver.next_button_x()
        print("test E04o2 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test E04o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E04o2:")
        print(err.__module__)
        print(str(err))


def Test_E04o3():
    #TC_E04.3 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, MY INSUARANCE RAN OUT"
    try:
        TestDriver.current_insured_status_3()
        TestDriver.next_button_x()
        TestDriver.previous_insurance_disclosure_0()
        TestDriver.previous_insurance_disclosure_1()
        TestDriver.previous_insurance_disclosure_3()
        TestDriver.next_button_x()
        TestDriver.driving_history_1()
        TestDriver.next_button_x()
        print("test E04o3 ran successfully")
        Test_E04o3.close_browser()

    except Exception as err:
        print('Test E04o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E04o3:")
        print(err.__module__)
        print(str(err))

def Test_E04o4():
    #TC_E04.4 - DRIVER INFORMATION - AUTO INSURANCE HISTORY - "NO, I WAS DEPLOYED"
    try:
        TestDriver.current_insured_status_4()
        TestDriver.next_button_x()
        print("test E04o4 ran successfully")
        TestDriver.close_browser()

    except Exception as err:
        print('Test E04o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E04o4:")
        print(err.__module__)
        print(str(err))

def Test_XX01():
    #TODO these need to be added to our list of test cases in the master spreadsheet, and assigned a test case id
    #TC_XX01 - DRIVER INFORMATION - EDUCATION
    try:
        TestDriver.education_level_0()
        TestDriver.next_button_x()
        print("test E04o4 ran successfully")

    except Exception as err:
        print('Test XX01' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test XX01:")
        print(err.__module__)
        print(str(err))

def Test_E05o1():
    #TC_E05o1 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A PRIVATE COMPANY/ORGANIZATION OR SELF EMPLOYED"
    try:
        TestDriver.employment_status_0()
        TestDriver.next_button_x()
        TestDriver.current_occupation_0()
        TestDriver.current_occupation_1()
        TestDriver.next_button_x()
        print("test E05o1 ran successfully")

    except Exception as err:
        print('Test E05o1' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o1:")
        print(err.__module__)
        print(str(err))

def Test_E05o2():
    #TC_E05o2 - DRIVER INFORMATION - EMPLOYMENT STATUS - "ACTIVE MILITARY DUTY"
    try:

        TestDriver.employment_status_0()
        TestDriver.employment_status_1()
        TestDriver.employment_status_2()
        TestDriver.next_button_x()
        print("test E05o2 ran successfully")

    except Exception as err:
        print('Test E05o2' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o2:")
        print(err.__module__)
        print(str(err))

def Test_E05o3():
    #TC_E05o3 - DRIVER INFORMATION - EMPLOYMENT STATUS - "FEDERAL GOVERNMENT AND POSTAL SERVICE"
    try:

        TestDriver.employment_status_0()
        TestDriver.employment_status_3()
        TestDriver.next_button_x()
        print("test E05o3 ran successfully")

    except Exception as err:
        print('Test E05o3' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o3:")
        print(err.__module__)
        print(str(err))

def Test_E05o4():
    #TC_E05o4 - DRIVER INFORMATION - EMPLOYMENT STATUS - "A STAE/LOCAL/MUNICIPAL GOVERNMENT"
    try:
        TestDriver.employment_status_0()
        TestDriver.employment_status_3()
        TestDriver.next_button_x()
        print("test E05o4 ran successfully")

    except Exception as err:
        print('Test E05o4' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o4:")
        print(err.__module__)
        print(str(err))

def Test_E05o5():
    #TC_E05o5 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM A FULL TIME STUDENT"
    try:
        TestDriver.employment_status_0()
        TestDriver.next_button_x()
        print("test E05o4 ran successfully")

    except Exception as err:
        print('Test E05o5' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o5:")
        print(err.__module__)
        print(str(err))

def Test_E05o6():
    #TC_E05o6 - DRIVER INFORMATION - EMPLOYMENT STATUS - "I AM CURRENTLY A HOMEMAKER"
    try:

        Test_E05o6.employment_status_0()
        Test_E05o6.next_button_x()
        print("test E05o6 ran successfully")

    except Exception as err:
        print('Test E05o6' + ' test automation observed an error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        print(err.args)
        print("An error occured while running automation test for Geico Test E05o6:")
        print(err.__module__)
        print(str(err))

def Test_E05o7():
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

def Test_E05o8():
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

def Test_E05o9():
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

def Test_E05o10():
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

def Test_E05o11():
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




