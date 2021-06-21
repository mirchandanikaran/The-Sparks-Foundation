from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from selenium.webdriver.support.select import Select


wDriver = webdriver.Edge(executable_path = "D:\\VS Code\\msedgedriver.exe")
print(wDriver.title)
print(wDriver.current_url)
wDriver.get("https://www.thesparksfoundationsingapore.org/")
print("\nTest Cases")

# Test case #1: Title
print("\nTest case #1:")
if wDriver.title:
    print("\nTitle verified successfully: ", wDriver.title)
else:
    print("\nTitle verification failed!\n")

# Test case #2: To find the logo of the given webpage
print("\nTest case #2:")
try:
    wDriver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Logo verified\n')
    time.sleep(3)
except NoSuchElementException:
    print('Logo not present.\n')

# Test case #3: Check if navbar appears
print("Test case #3:")
try:
    wDriver.find_element_by_class_name("navbar")
    print("Navbar verification successful!\n")
except NoSuchElementException:
    print("Navbar verification failed!\n")

# Test case #4: Home button
print("Test case #4:")
try:
    wDriver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home button is working!\n")
except NoSuchElementException:
    print("Home link broken!\n")

# Test case #5: About Us Page
print("Test case #5:")
try:
    wDriver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    wDriver.find_element_by_link_text('Corporate Partners').click()
    time.sleep(3)
    print('Page visit successful\n')
except NoSuchElementException:
    print("Page does not exist.\n")
    time.sleep(3)

# Test case #6: Policy Page
print('Test case #6:')
try:
    wDriver.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    wDriver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    wDriver.find_element_by_link_text('Code of Ethics and Conduct').click()
    time.sleep(3)
    print('Policy page verified!\n')
except NoSuchElementException:
    print('No new tab opened.\n')

# Test case #7: Programs page
print('TestCase 7:')
try:
    wDriver.find_element_by_link_text('Student Scholarship Program').click()
    time.sleep(3)
    wDriver.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(3)
    wDriver.find_element_by_link_text('Student SOS Program').click()
    time.sleep(3)
    print('Programs Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase #8: Checking 'Contact us Page'
print("Test case #8:")
try:
    wDriver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    info = wDriver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if info.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print('Contact information is correct!')
    else:
        print('Contact information is incorrect!')
    print("Contact page verification successful!\n")
except NoSuchElementException:
    print("Contact page verification unsuccessful!")

# Test case #9: Links Page
print("Test case #9:")
try:
    wDriver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    wDriver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    wDriver.find_element_by_link_text('AI in Education').click()
    time.sleep(3)
    print('LINKS Verfication Successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# Test case #10: Checking the Form
print("Test Case #10:")
try:
    wDriver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    wDriver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    wDriver.find_element_by_name('Name').send_keys('John Smith')
    time.sleep(3)
    wDriver.find_element_by_name('Email').send_keys('johnsmith@businesswisdomtoday.com')
    time.sleep(3)
    select = Select(wDriver.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Intern')
    time.sleep(3)
    wDriver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form verification successful!\n")
except NoSuchElementException:
    print("Form verification failed!\n")
    time.sleep(3)
cls=wDriver.close()

print('Test session succesful.')