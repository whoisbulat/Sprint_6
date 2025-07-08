import pytest
from pages.main_page import MainPageHelper
from data import QuestiosData




class TestQuestion:
    @pytest.mark.parametrize('data',
                             [(QuestiosData.QUESTION_DATA_1),
                              (QuestiosData.QUESTION_DATA_2),
                              (QuestiosData.QUESTION_DATA_3),
                              (QuestiosData.QUESTION_DATA_4),
                              (QuestiosData.QUESTION_DATA_5),
                              (QuestiosData.QUESTION_DATA_6),
                              (QuestiosData.QUESTION_DATA_7),
                              (QuestiosData.QUESTION_DATA_8)
                              ])
    def test_question(self, driver, data):
        main_page = MainPageHelper(driver)
        main_page.go_to_site()
        main_page.close_cookie()
        main_page.get_question(data)
        assert main_page.get_answer(data) == data[1]



























