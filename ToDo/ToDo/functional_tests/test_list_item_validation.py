from .base import FunctionTest
import time

class ItemValidationTest(FunctionTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1:Buy milk')

        self.get_item_input_box().send_keys('\n')

        self.check_for_row_in_list_table('1:Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Make tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1:Buy wellies')

        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1:Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        self.get_item_input_box().send_keys('a')
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
