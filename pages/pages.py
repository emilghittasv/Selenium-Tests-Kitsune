from selenium.webdriver.remote.webdriver import WebDriver
from pages.contribute_page import ContributePage
from pages.footer import FooterSection
from pages.homepage import Homepage
from pages.top_navbar import TopNavbar


class Pages:
    def __init__(self, driver: WebDriver):
        self.contribute_page = ContributePage(driver)
        self.homepage = Homepage(driver)
        self.footer_section = FooterSection(driver)
        self.top_navbar = TopNavbar(driver)