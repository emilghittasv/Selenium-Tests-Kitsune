import pytest
import os
from core.test_utilities import TestUtilities
from messages.contribute_page_messages import ContributePageMessages
from messages.homepage_messages import HomepageMessages


class TestHomepage(TestUtilities):
    @pytest.mark.smokeTest
    def test_join_our_community_card_learn_more_redirects_to_contribute_page(self):
        self.logger.info("Clicking on the 'Learn More' option")
        self.pages.homepage.click_learn_more_option()
        self.logger.info("Verifying that we are redirected to the 'Contribute' page successfully")

        assert (
            self.pages.contribute_page.current_url
            == ContributePageMessages.STAGE_CONTRIBUTE_PAGE_URL
        ), "We are not on the Contribute page!"

    @pytest.mark.smokeTest
    def test_join_our_community_card_has_the_correct_content(self):
        self.logger.info(
            "Verifying that the 'Join Our Community' card has the correct strings applied"
        )

        self.logger.info(os.environ['SIMPLE_TEST_USER'])
        self.logger.info(os.environ['SIMPLE_TEST_USER_PASSWORD'])

        assert (
            self.pages.homepage.get_community_card_title()
            == HomepageMessages.JOIN_OUR_COMMUNITY_CARD_TITLE
            and self.pages.homepage.get_community_card_description()
            == HomepageMessages.JOIN_OUR_COMMUNITY_CARD_DESCRIPTION
        ), "Incorrect strings are displayed"
