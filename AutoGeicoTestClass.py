from selenium import webdriver
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains as action
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"C:\Users\GaryTsokatos\PycharmProjects\Trial Run\Drivers\chromedriver.exe")
wait = WebDriverWait(driver, 10)

class Auto_Geico_Test:

    def __init__(self):
        self.driver = driver
        self.wait = wait

    def zip_input_0(self):
        self.driver.get('http://geico.com')
        zipInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(zipInput0).click().send_keys('60640').send_keys(u'\ue007').perform()
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
    def skip_help_page(self):
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

    def street_input_0(self):
        StreetInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'street')))
        action(self.driver).move_to_element(StreetInput0).click().send_keys('164561 Random').perform()
        return

    def apt_input_0(self):
        AptInput0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'apt')))
        action(self.driver).move_to_element(AptInput0).click().send_keys('3 Random').perform()
        return

    def zip_input_1(self):
        ZipInput1 = self.wait.until(ec.element_to_be_clickable((By.ID, 'zip')))
        action(self.driver).move_to_element(ZipInput1).click().send_keys('12345').perform()
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

    def anti_theft_device(self):
        # index guide
        # 0 = no anti theft, 1 = alarm only/active disabling device, 2 = passive disabling device
        def select_specific_antitheft_device(self, index):
            try:
                time.sleep(3)
                AntiTheftDeviceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='antiTheftDevice']"))
                AntiTheftDeviceSelect0.select_by_index(index)
            except:
                print("no anti-theft device")

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

#skipped ahead to Driver Info, missing a couple Nexts and other options; am labeling Next Buttons below according to the Excel spreadsheet, beginning on cell Q3

    def gender_select_0(self):
        GenderSelect0 = self.wait.until(ec.element_to_be_clickable((By.ID, 'gender')))

        return
