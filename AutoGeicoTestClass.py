from selenium import webdriver
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains as action
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Auto_Geico_Test:

    chrome_options = webdriver.ChromeOptions

    driver = webdriver
    wait = WebDriverWait
    ErrorCount = 0
    CurrentModule = ""

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-icognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)

    # function for generic buttons
    def go_next(self):
        try:
            self.CurrentModule = "go_next"
            time.sleep(1)
            NextButton0 = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
            action(self.driver).move_to_element(NextButton0).click().click().perform()
        except Exception as err:
            self.error_message(err)

    def zip_input_0(self):
        self.driver.get('http://geico.com')
        zipInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(zipInput0).click().send_keys('60629').send_keys(u'\ue007').perform()
        return

    #Testing the 1st of 5 options -- "I need insurance right away"
    def customer_intent_0(self):
        CustomerIntent0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent0']")))
        CustomerIntent0.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        return

    # Testing the 2nd of 5 options -- "I am buying or just bought a car"
    def customer_intent_1(self):
        CustomerIntent1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent1']")))
        CustomerIntent1.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        return

    #Testing the 3rd of 5 options -- "I'm looking for a better price"
    def customer_intent_2(self):
        CustomerIntent2 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent2']")))
        CustomerIntent2.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        return

    #Testing the 4th of 5 options -- "I'm comparing rates for different cars"
    def customer_intent_3(self):
        CustomerIntent3 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent3']")))
        CustomerIntent3.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        return

    #Testing the 5th of 5 options -- "I'm just shopping today"
    def customer_intent_4(self):
        CustomerIntent4 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='collectIntent4']")))
        CustomerIntent4.click()
        BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        BeginQuoteButton0.click()
        return

    def customer_intent_5(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='button-bar']")
        #CustomerIntent5 = self.wait.until(ec.element_to_be_clickable((By.__class__, "button-bar")))
        CustomerIntent5 = self.driver.find_element_by_xpath("//*[@id='auto-customer-collect-intent-modal']/div/div/div/div[1]/div/div[2]/a")
        CustomerIntent5.click()
        #BeginQuoteButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Begin Quote')]")))
        #BeginQuoteButton0.click()
       # NextButton0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='btn.btn--primary']")))
        #NextButton0.click()
        return

      # skipping the Customer Intent/help page
    def skip_help_page_0(self):
        time.sleep(2)
        butbar = self.driver.find_element_by_class_name("button-bar")
        SkipA0 = butbar.find_element_by_class_name("skip-collect-intent.link--primary")
        action(self.driver).move_to_element(SkipA0).click().perform()

    #Testing the Next Button after selecting your Customer Intent
    def next_button_0(self):
        time.sleep(2)
        NextButton0 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton0.click()
        return

    #Entering first name into dialogue box
    def first_name_input_0(self):
        FirstNameInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'firstName')))
        action(self.driver).move_to_element(FirstNameInput0).click().send_keys('Abcdefghij').perform()
        return

    #Entering last name into dialogue box
    def last_name_input_0(self):
        LastNameInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'lastName')))
        action(self.driver).move_to_element(LastNameInput0).click().send_keys('Ioewmaowenglweirb').perform()
        return

    #Testing the Next Button after entering First and Last Name
    def next_button_1(self):
        time.sleep(2)
        NextButton1 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton1.click()
        return

    def month_dob_0(self):
        MonthDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-monthdob')))
        MonthDOB0.click()
        MonthDOB0.send_keys('08')
        return

    def day_dob_0(self):
        DayDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-daydob')))
        DayDOB0.click()
        DayDOB0.send_keys('08')

    def year_dob_0(self):
        YearDOB0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'date-yeardob')))
        YearDOB0.click()
        YearDOB0.send_keys('1990')
        return

    def next_button_2(self):
        time.sleep(2)
        NextButton2 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton2.click()
        return

#what is your address funtions
    def street_input_0(self):
        StreetInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'street')))
        action(self.driver).move_to_element(StreetInput0).click().send_keys('6609 S Karlov').perform()
        return

    def apt_input_0(self):
        AptInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'apt')))
        action(self.driver).move_to_element(AptInput0).click().send_keys('3').perform()
        return

    def zip_input_1(self):
        ZipInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(ZipInput1).click().send_keys('60629').perform()
        return

    def next_button_3(self):
        time.sleep(2)
        NextButton3 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton3.click()
        return

    def verify_address_0(self):
        OriginalAddressLabel0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='originalAddress']")))
        OriginalAddressLabel0.click()
        return

    def next_button_4(self):
        NextButton4 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton4.click()
        return

    def have_you_moved(self):
        HasMovedInLast2MonthsLabel1 = self.driver.find_element_by_xpath("//label[@for='hasMovedInLast2Months1']")
        action(self.driver).move_to_element(HasMovedInLast2MonthsLabel1).click().send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        return

    def next_button_3(self):
        time.sleep(2)
        NextButton3 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton3.click()
        return

    def vehicle_not_listed_class_0(self):
        time.sleep(4)
        VehicleNotListed = self.driver.find_element_by_xpath("//label[@for='chkVehicle2']")
        VehicleNotListed.click()
        return

    def next_button_x(self):
        time.sleep(2)
        NextButtonx = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButtonx.click()
        return

    def select_antitheft_devices(self):
        try:
            self.CurrentModule = "select_antitheft_devices"

            AntiTheftDeviceSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='antiTheftDevice']"))))

            ATDOption = 0

            while ATDOption < len(AntiTheftDeviceSelect0.options):
                AntiTheftDeviceSelect0.select_by_index(ATDOption)
                ATDOption = ATDOption + 1
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = no anti theft, 1 = alarm only/active disabling device, 2 = passive disabling device
    def select_specific_antitheft_device(self, index):
        try:
            self.CurrentModule = "select_specific_antitheft_device"
            AntiTheftDeviceSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='antiTheftDevice']"))))
            AntiTheftDeviceSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = owned, 1 = financed, 2 = leased


    def select_ownership(self, index):
        try:
            time.sleep(3)

            if index == 0:
                VehicleOwned0 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned0']")
                action(self.driver).move_to_element(VehicleOwned0).click().perform()
            if index == 1:
                VehicleOwned1 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned1']")
                action(self.driver).move_to_element(VehicleOwned1).click().perform()
            if index == 2:
                VehicleOwned2 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned2']")
                action(self.driver).move_to_element(VehicleOwned2).click().perform()
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # index guide
    # 0 = commute, 1 = pleasure, 2 = business


    def select_primary_use(self, index):
        try:
            time.sleep(3)

            if index == 0:
                PrimaryUse0 = self.driver.find_element_by_xpath("//label[@for='primaryUse0']")
                action(self.driver).move_to_element(PrimaryUse0).click().perform()
                self.primary_use_commute(1, 200)
            if index == 1:
                PrimaryUse1 = self.driver.find_element_by_xpath("//label[@for='primaryUse1']")
                action(self.driver).move_to_element(PrimaryUse1).click().perform()
            if index == 2:
                PrimaryUse2 = self.driver.find_element_by_xpath("//label[@for='primaryUse2']")
                action(self.driver).move_to_element(PrimaryUse2).click().perform()
                self.primary_use_business(1)
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # menu options for commuting
    def primary_use_commute(self, index, miles):
        try:
            time.sleep(1)
            DaysDrivenSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='daysDriven']"))
            DaysDrivenSelect0.select_by_index(index)

            MilesDrivenInput0 = self.driver.find_element_by_xpath("//input[@id='milesDriven']")
            action(self.driver).move_to_element(MilesDrivenInput0).click().send_keys(str(miles)).perform()
        except Exception as err:
            print("Exception thrown:\t" + str(err))


    def select_annual_mileage(self, index):
        try:
            time.sleep(1)
            AnnualMileageSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='annualMileage']"))
            AnnualMileageSelect0.select_by_index(index)
        except Exception as err:
            print("Exception thrown:\t" + str(err))


    def primary_use_business(self, index):
        try:
            time.sleep(1)
            TypeOfBusinessUseSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='typeOfBusinessUse']"))
            TypeOfBusinessUseSelect0.select_by_index(index)
        except Exception as err:
            print("Exception thrown:\t" + str(err))

    # only use this to pass through this stage, not good for testing functionality
    # indices available is reliant on the previous elements
    def select_specific_vehicle(self, year_index, make_index, model_index):
        try:
            self.CurrentModule = "select_specific_vehicle"
            VehicleYearSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
            VehicleYearSelect0.select_by_index(year_index)
            VehicleMakeSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))
            VehicleMakeSelect0.select_by_index(make_index)
            VehicleModelSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))
            VehicleModelSelect0.select_by_index(model_index)

            self.go_next()

        except Exception as err:
            self.error_message_vehicle(err, year_index, make_index, model_index)

    # only use this to pass through this stage, not good for testing functionality
    # indices available is reliant on the previous elements
    def select_specific_vehicle_unlisted(self, year_index, make_index, model_index):
        try:
            self.CurrentModule = "select_specific_vehicle"
            VehicleYearSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYearunlisted']"))))
            VehicleYearSelect0.select_by_index(year_index)
            VehicleMakeSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMakeunlisted']"))))
            VehicleMakeSelect0.select_by_index(make_index)
            VehicleModelSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModelunlisted']"))))
            VehicleModelSelect0.select_by_index(model_index)

            self.go_next()

        except Exception as err:
            self.error_message_vehicle(err, year_index, make_index, model_index)

    def select_vehicles(self):

        self.CurrentModule = "select_vehicles"

        ### NOW WE CAN TEST FOR THE ADDING OF VEHCILES ###

        VehicleYearSelect0 = Select(
            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))

        YearOption = 0

        while YearOption < len(VehicleYearSelect0.options) - 1:
            try:
                VehicleYearSelect0.select_by_index(YearOption)
            except:
                VehicleYearSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
                VehicleYearSelect0.select_by_index(YearOption)

            VehicleMakeSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))

            MakeOption = 1
            while MakeOption < len(VehicleMakeSelect0.options):
                try:
                    VehicleMakeSelect0.select_by_index(MakeOption)
                except:
                    VehicleMakeSelect0 = Select(
                        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleMake']"))))
                    VehicleMakeSelect0.select_by_index(MakeOption)

                VehicleModelSelect0 = Select(
                    self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))

                ModelOption = 1
                while ModelOption < len(VehicleModelSelect0.options):  # it really starts to slow down over here
                    try:
                        VehicleModelSelect0.select_by_index(ModelOption)
                    except:
                        VehicleModelSelect0 = Select(
                            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleModel']"))))
                        VehicleModelSelect0.select_by_index(ModelOption)

                    # time.sleep(1)
                    ModelOption = ModelOption + 1
                MakeOption = MakeOption + 1
            YearOption = YearOption + 1

    def add_vehicle_pre1981(self, year, make, model):
        try:
            self.CurrentModule = "add_vehicle_pre1981"

            VehicleYearSelect0 = Select(
                self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='vehicleYear']"))))
            VehicleYearSelect0.select_by_index(len(VehicleYearSelect0.options) - 1)

            ActualVehicleYearInput0 = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//input[@id='actualVehicleYear']")))
            action(self.driver).move_to_element(ActualVehicleYearInput0).click().send_keys(
                str(year)).perform()

            OtherMakeInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherMake']")))
            action(self.driver).move_to_element(OtherMakeInput0).click().send_keys(str(make)).perform()

            OtherModelInput0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='otherModel']")))
            action(self.driver).move_to_element(OtherModelInput0).click().send_keys(str(model)).perform()

            self.go_next()
        except Exception as err:
            self.error_message_vehicle(err, year, make, model)

    def select_body_styles(self):
        try:
            self.CurrentModule = "select_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStyles']"))))

            BSSOption = 0
            while BSSOption < len(BodyStylesSelect0.options):
                BodyStylesSelect0.select_by_index(BSSOption)
                BSSOption = BSSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_body_style(self, index):
        try:
            self.CurrentModule = "select_specific_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStyles']"))))

            BodyStylesSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_specific_body_style_unlisted(self, index):
        try:
            self.CurrentModule = "select_specific_body_styles"

            BodyStylesSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='bodyStylesunlisted']"))))

            BodyStylesSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_new_costs(self):

        try:
            self.CurrentModule = "select_new_costs"

            CostNewValueSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='costNewValue']"))))

            CNVSOption = 0
            while CNVSOption < len(CostNewValueSelect0.options):
                CostNewValueSelect0.select_by_index(CNVSOption)
                CNVSOption = CNVSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_new_costs(self, index):

        try:
            self.CurrentModule = "select_specific_new_costs"

            CostNewValueSelect0 = Select(self.wait.until(ec.element_to_be_clickable((By.XPATH, "//select[@id='costNewValue']"))))
            CostNewValueSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_antilock_brakes(self, index):
        try:

            self.CurrentModule = "select_antilock_brakes"

            if index == 0:
                AntilockBrakesLabel0 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakes0']")))
                action(self.driver).move_to_element(AntilockBrakesLabel0).click().perform()
                self.go_next()
            if index == 1:
                AntilockBrakesLabel1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//label[@for='hasAntilockBrakes1']")))
                action(self.driver).move_to_element(AntilockBrakesLabel1).click().perform()
                self.go_next()

        except Exception as err:
            self.error_message(err)

    #skipped ahead to Driver Info, missing a couple Nexts and other options; am labeling Next Buttons below according to the Excel spreadsheet, beginning on cell Q3

    def name_change_0(self):
        NameChange0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'changeName')))
        NameChange0.click()

        FirstNameInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'firstName')))
        action(self.driver).move_to_element(FirstNameInput1).click().send_keys('Abcdefghij').perform()

        LastNameInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'lastName')))
        action(self.driver).move_to_element(LastNameInput1).click().send_keys('Ioewmaowenglweirb').perform()

        return

    def gender_select_0(self):
        #index values: value "F" = female; value "M" = Male

        GenderSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='gender']"))
        GenderSelect0.select_by_value('M')

        NextButton4 = self.driver.find_element_by_xpath('//*[@id="question-breakdown"]/div/div[4]/div[2]/div[1]/div/div/button')
        NextButton4.click()
        return

    def marital_status_0(self):
        #Index values for dropdown: "S" = Single; "D" = Divorced; "M" = Married; "B" = Civil Union; "E" = Separated; "W" = Widowed

        MaritalStatusSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='maritalStatus']"))
        MaritalStatusSelect0.select_by_value('S')
        return

    def social_security_number_0(self):
        #negative test case to determine whether element will accept alphabet characters
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('Ioewmaowenglweirb').perform()
        return

    def social_security_number_1(self):
        #test case to determine whether element will accept 8 numeric characters (the full length of a SSN)
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('12345678').perform()
        return

    def social_security_number_2(self):
        #test case to determine whether element will accept fewer than 8 numeric characters (a partial SSN)
        SocialSecurityNumber0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'ssn')))
        action(self.driver).move_to_element(SocialSecurityNumber0).click().send_keys('123456').perform()
        return

    # these functions get you to the page to add vehicles
    def get_to_vehicle_page(self):
        self.driver.get("https://www.geico.com/")
        self.zip_input_0()
        self.skip_help_page()
        self.go_next()
        self.first_name_input_0()
        self.last_name_input_0()
        self.go_next()
        self.month_dob_0()
        self.day_dob_0()
        self.year_dob_0()
        self.go_next()
        self.street_input_0()
        self.apt_input_0()
        self.zip_input_1()
        self.go_next()
        self.vehicle_not_listed_class_0()
        self.go_next()


    def error_message(self, err):
        self.ErrorCount = self.ErrorCount + 1
        print("Exception thrown on module:\t" + str(self.CurrentModule))
        print(str(err))
        print("Error Count:\t" + str(self.ErrorCount))

    def error_message_vehicle(self, err, year, make, model):
        self.error_message(err)
        print("Year:\t" + str(year) + " Make:\t" + str(make) + " Model:\t" + str(model))


    #Testing "Own" radio button on Do You Own Or Rent Your Home? page
    def home_ownership_0(self):
        OwnLabel0 = self.driver.find_element_by_xpath("//label[@for='ownOrRentHome0']")
        action(self.driver).move_to_element(OwnLabel0).click().perform()
        return

    #Testing "Rent" radio button on Do You Own Or Rent Your Home? page
    def home_ownership_0(self):
        RentLabel0 = self.driver.find_element_by_xpath("//label[@for='ownOrRentHome1']")
        action(self.driver).move_to_element(RentLabel0).click().perform()
        return

    #testing each option in the Do You Currently Have Auto Insurance? dropdown menu
    def current_insured_status_0(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(0)
        return

    def current_insured_status_1(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(1)
        return

    def current_insured_status_2(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(2)
        return

    def current_insured_status_3(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(3)
        return

    def current_insured_status_4(self):
        #dropdown values: blank value is index 0; "O" = Yes, index 1; "N" = No, I haven't needed insurance, index 2; "R" = No, my insurance ran out, index 3; "D" = No, I was deployed, index 4
        HasAutoInsurance0 = Select(self.driver.find_element_by_xpath("//select[@id='hasAutoInsurance']"))
        HasAutoInsurance0.select_by_index(4)
        return

    #Testing each element on the Previous Insurance disclosure page (title: "Tell us more about your previous insurance").
    # 3 major element groups on this page: a dropdown menu where you can select how many years you had been continuously covered by previous insurer when your insurance ran out; 2 radio buttons for the question "Have you had insurance within the last 30 days?"; and another dropdown menu labelled "Previous Bodily Injury Limits"
    def previous_insurance_disclosure_0(self):
        #Testing 1st dropdown menu.
        #Dropdown index/values: index 0/value is blank; index 1/value "0" = Less than 1; index 2/value "1" = 1; index 3/value "2" = 2; index 4/value "3" = 3; index 5/value "4" = 4; index 6/value "5" = 5; index 7/value "6" = 6; index 8/value "7" = 7; index 9/value "8" = 8; index 10/value "9" = 9; index 11/value "10" = 10; index 12/value "11" = 11 or more
        PreviousInsuranceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='yearsInsured']"))
        PreviousInsuranceSelect0.select_by_index(3)
        return

    def previous_insurance_disclosure_1(self):
        #Testing radio button elements
        Last30DaysYes = self.driver.find_element_by_xpath("//label[@for='lastInsurance0']")
        action(self.driver).move_to_element(Last30DaysYes).click().perform()
        return

    def previous_insurance_disclosure_2(self):
        #Testing radio button elements
        Last30DaysNo = self.driver.find_element_by_xpath("//label[@for='lastInsurance1']")
        action(self.driver).move_to_element(Last30DaysNo).click().perform()
        return

    def previous_insurance_disclosure_3(self):
        #Testing Previous Bodily Injury Limits dropdown menu.
        #Dropdown index/values: index 0/value is blank; index 1/value "025" = "$25,000/$50,000"; index 2/value "051" = "$50,000/$100,000" ; index 3/value "120" = "$100,000/$200,000"; index 4/value "130" = "$100,000/$300,000"; index 5/value "330" = "$300,000/$300,000"; index 6/value "250" = "$250,000/$500,000 or higher"; index 7/value "997" = "Not Sure"
        PreviousBILimits0 = Select(self.driver.find_element_by_xpath("//select[@id='currentBILimits']"))
        PreviousBILimits0.select_by_index(3)
        return

    def current_insurance_disclosure_0(self):
        #
