from .base import FunctionTest
import time

class ItemValidationTest(FunctionTest):

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1:Buy milk')

        self.get_item_input_box().send_keys('\n')

        self.check_for_row_in_list_table('1:Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Make tea')
