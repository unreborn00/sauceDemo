from loginCreds import SauceDemo
from loginPage import LoginPage

sd = SauceDemo()
sd.open_website()
sd.get_username()
sd.get_password()

lp = LoginPage(sd)
lp.login_with_user(index=1)