import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Apple:
    def añaddirAirpods3ToCart(driver):
        clickOnAirpod = driver.find_element(By.XPATH, "//a[@class='ac-gn-link ac-gn-link-airpods']")
        clickOnAirpod.click()

        time.sleep(5)

        driver.execute_script("window.scrollTo(0,1250)")

        time.sleep(5)

        buyButtonAirpods = driver.find_element(By.XPATH,
                                               "//a[@aria-label='Buy AirPods (3rd generation)']//span[@class='icon-copy'][normalize-space()='Buy']")
        buyButtonAirpods.click()

        time.sleep(5)

        driver.execute_script("window.scrollTo(0,550)")
        magSafeOption = driver.find_element(By.XPATH, "//span[contains(text(), 'MagSafe Charging Case')]")
        magSafeOption.click()

        addToCart = driver.find_element(By.XPATH, "//button[@id='add-to-cart']")
        addToCart.click()

        time.sleep(5)


    #################################################

    def añadirIphoneSetoCart(driver):
        clickOnIphone = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[5]')
        clickOnIphone.click()

        time.sleep(3)

        driver.execute_script("window.scroll(0, 2550)")

        time.sleep(3)

        buyButtonIphoneSE = driver.find_element(By.XPATH,
                                                "//li[@class='typography-hero-copy cta-link']//a[@aria-label='Buy iPhone SE'][normalize-space()='Buy']")
        buyButtonIphoneSE.click()

        time.sleep(3)

        iphoneColor = driver.find_element(By.XPATH, '//ul[@class="colornav-items"]//child::li[2]')
        iphoneColor.click()

        time.sleep(5)

        iphoneStorage = driver.find_element(By.XPATH, "//span[contains(text(), '256')]")
        iphoneStorage.click()

        time.sleep(3)

        noTradeInOption = driver.find_element(By.XPATH, "//*[contains(text(), 'No trade-in')]")
        noTradeInOption.click()

        time.sleep(3)

        payInFull = driver.find_element(By.XPATH, "//*[contains(text(), 'Pay the total amount today.')]")
        payInFull.click()

        time.sleep(3)

        selectCarrier = driver.find_element(By.XPATH, '//ul[@aria-labelledby="carrierModel"]//child::div[5]')
        selectCarrier.click()

        time.sleep(3)

        selectNoAppleCare = driver.find_element(By.XPATH, "//*[contains(text(), 'No AppleCare+ coverage')]")
        selectNoAppleCare.click()

        time.sleep(3)

        addToBag = driver.find_element(By.XPATH, '//button[@name = "add-to-cart"]')
        addToBag.click()

        time.sleep(10)


        #####################################################

    def añadirIphone14ProToCart(driver):
        clickOnIphone = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[5]')
        clickOnIphone.click()

        time.sleep(3)

        driver.execute_script("window.scroll(0,1450)")

        buyButtonIphone14Pro = driver.find_element(By.XPATH, "//a[@data-analytics-title= 'buy - iphone 14 pro']")
        buyButtonIphone14Pro.click()

        time.sleep(3)

        selectIphone14Pro = driver.find_element(By.XPATH,
                                                '//span[@class = "form-selector-title"][contains(text(), "iPhone 14 Pro")]')
        selectIphone14Pro.click()

        time.sleep(3)

        selectIphoneColor = driver.find_element(By.XPATH, '//ul[@class="colornav-items"]//child::li[3]')
        selectIphoneColor.click()

        time.sleep(3)

        selectIphone14ProStorage = driver.find_element(By.XPATH,
                                                       '//span[@class = "form-selector-title"][contains(text(), "128")]')
        selectIphone14ProStorage.click()

        time.sleep(3)

        noTradeInOption = driver.find_element(By.XPATH, "//*[contains(text(), 'No trade-in')]")
        noTradeInOption.click()

        time.sleep(3)

        payInFull = driver.find_element(By.XPATH, "//*[contains(text(), 'Pay the total amount today.')]")
        payInFull.click()

        time.sleep(3)

        selectCarrier = driver.find_element(By.XPATH, '//ul[@aria-labelledby="carrierModel"]//child::div[5]')
        selectCarrier.click()

        time.sleep(3)

        selectNoAppleCare = driver.find_element(By.XPATH, "//*[contains(text(), 'No AppleCare+ coverage')]")
        selectNoAppleCare.click()

        time.sleep(3)

        addToBag = driver.find_element(By.XPATH, '//button[@name = "add-to-cart"]')
        addToBag.click()

        time.sleep(10)

    #################################################

    def removerItem(driver):
        shoppingBagNavBar = driver.find_element(By.XPATH, '//ul[@class="ac-gn-list"]//child::li[13]')
        shoppingBagNavBar.click()

        time.sleep(9)

        bag = driver.find_element(By.XPATH, '//ul[@class = "ac-gn-bagview-nav-list "]//child::li[1]')
        bag.click()

        time.sleep(6)

        # to change the item to remove just change the index of bag-item, actual index is 2
        removeItem = driver.find_element(By.XPATH,
                                         '//li[@class= "rs-bag-item rs-iteminfo-wrap"][@data-autom="bag-item-2"]//child::button[@class="rs-iteminfo-remove as-buttonlink"] ')
        removeItem.click()

        time.sleep(8)

    ##################################################

    def checkOutApplePurchase(driver):
        checkOut = driver.find_element(By.XPATH, '//button[@id="shoppingCart.actions.checkout"]')
        checkOut.click()

        time.sleep(3)

        continueAsGuest = driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")
        continueAsGuest.click()

        time.sleep(3)

        inputLocation = driver.find_element(By.XPATH,
                                            '//input[@id="checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput"]')
        inputLocation.send_keys("New York")
        time.sleep(3)
        inputLocation.send_keys(Keys.ENTER)

        selectStore = driver.find_element(By.XPATH,
                                          '//ul[@class="rt-storelocator-store-group form-selector-group"]//child::li[5]')
        selectStore.click()

        time.sleep(3)

        dateToPickUp = driver.find_element(By.XPATH, '//ul[@class="rs-pickup-slotgroup"]//child::li[2]')
        dateToPickUp.click()

        time.sleep(3)

        timeToPickUp = Select(driver.find_element(By.XPATH,
                                                  '//select[@id="checkout.fulfillment.pickupTab.pickup.timeSlot.dateTimeSlots.timeSlotValue"]'))
        timeToPickUp.select_by_visible_text('8:45 a.m. – 9:00 a.m.')

        time.sleep(3)

        continuePickUpDetails = driver.find_element(By.XPATH, '//button[@id="rs-checkout-continue-button-bottom"]')
        continuePickUpDetails.click()

        time.sleep(3)

        firstName = driver.find_element(By.XPATH, "//input[@name='firstName']")
        firstName.send_keys('Darlin Manuel')
        lastName = driver.find_element(By.XPATH, "//input[@name='lastName']")
        lastName.send_keys('Casado Perez')
        emailAddress = driver.find_element(By.XPATH, "//input[@name='emailAddress']")
        emailAddress.send_keys('darlinmanuelcasdo@gmail.com')
        phoneNumber = driver.find_element(By.XPATH, "//input[@name='fullDaytimePhone']")
        phoneNumber.send_keys('8291546257')

        btnPayment = driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']")
        btnPayment.click()