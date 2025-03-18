import unittest
from UnitTesting.white_box import (
    is_even,
    divide,
    get_grade,
    is_triangle,
    check_number_status,
    validate_password,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory,
    VendingMachine,
    TrafficLight,
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem,
    BankingSystem,
    Product,
    ShoppingCart,
)


class TestSourceCode(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle(self):
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(1, 1, 3), "No, it's not a triangle.")

    def test_check_number_status(self):
        self.assertEqual(check_number_status(10), "Positive")
        self.assertEqual(check_number_status(-10), "Negative")
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password(self):
        self.assertTrue(validate_password("Password1!"))
        self.assertFalse(validate_password("pass"))
        self.assertFalse(validate_password("password"))

    def test_calculate_total_discount(self):
        self.assertEqual(calculate_total_discount(50), 0)
        self.assertEqual(calculate_total_discount(200), 20)
        self.assertEqual(calculate_total_discount(600), 120)

    def test_calculate_order_total(self):
        items = [{"quantity": 3, "price": 10}, {"quantity": 7, "price": 20}]
        self.assertEqual(calculate_order_total(items), 173)

    def test_calculate_items_shipping_cost(self):
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_validate_login(self):
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")
        self.assertEqual(validate_login("usr", "pass"), "Login Failed")

    def test_verify_age(self):
        self.assertEqual(verify_age(25), "Eligible")
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_categorize_product(self):
        self.assertEqual(categorize_product(25), "Category A")
        self.assertEqual(categorize_product(75), "Category B")
        self.assertEqual(categorize_product(150), "Category C")
        self.assertEqual(categorize_product(250), "Category D")

    def test_validate_email(self):
        self.assertEqual(validate_email("test@example.com"), "Valid Email")
        self.assertEqual(validate_email("test"), "Invalid Email")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(150), "Invalid Temperature")

    def test_validate_credit_card(self):
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("123"), "Invalid Card")

    def test_validate_date(self):
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")

    def test_check_flight_eligibility(self):
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_validate_url(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_calculate_quantity_discount(self):
        self.assertEqual(calculate_quantity_discount(3), "No Discount")
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

    def test_check_file_size(self):
        self.assertEqual(check_file_size(500000), "Valid File Size")
        self.assertEqual(check_file_size(2000000), "Invalid File Size")

    def test_check_loan_eligibility(self):
        self.assertEqual(check_loan_eligibility(25000, 750), "Not Eligible")
        self.assertEqual(check_loan_eligibility(40000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_calculate_shipping_cost(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)
        self.assertEqual(calculate_shipping_cost(6, 40, 40, 40), 20)

    def test_grade_quiz(self):
        self.assertEqual(grade_quiz(8, 1), "Pass")
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(4, 5), "Fail")

    def test_authenticate_user(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")
        self.assertEqual(authenticate_user("user123", "password123"), "User")
        self.assertEqual(authenticate_user("user", "pass"), "Invalid")

    def test_get_weather_advisory(self):
        self.assertEqual(
            get_weather_advisory(35, 80), "High Temperature and Humidity. Stay Hydrated."
        )
        self.assertEqual(get_weather_advisory(-5, 30), "Low Temperature. Bundle Up!")
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

    def test_vending_machine(self):
        vm = VendingMachine()
        self.assertEqual(vm.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(vm.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(vm.insert_coin(), "Invalid operation in current state.")

    def test_traffic_light(self):
        tl = TrafficLight()
        self.assertEqual(tl.get_current_state(), "Red")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Green")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Yellow")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Red")

    def test_user_authentication(self):
        ua = UserAuthentication()
        self.assertEqual(ua.login(), "Login successful")
        self.assertEqual(ua.logout(), "Logout successful")
        self.assertEqual(ua.logout(), "Invalid operation in current state")

    def test_document_editing_system(self):
        des = DocumentEditingSystem()
        self.assertEqual(des.save_document(), "Document saved successfully")
        self.assertEqual(des.edit_document(), "Editing resumed")
        self.assertEqual(des.edit_document(), "Invalid operation in current state")

    def test_elevator_system(self):
        es = ElevatorSystem()
        self.assertEqual(es.move_up(), "Elevator moving up")
        self.assertEqual(es.stop(), "Elevator stopped")
        self.assertEqual(es.move_down(), "Elevator moving down")
        self.assertEqual(es.stop(), "Elevator stopped")

    def test_banking_system(self):
        bs = BankingSystem()
        self.assertTrue(bs.authenticate("user123", "pass123"))
        self.assertFalse(bs.authenticate("user123", "wrongpass"))

    def test_shopping_cart(self):
        product1 = Product("Apple", 1.0)
        product2 = Product("Banana", 0.5)
        cart = ShoppingCart()
        cart.add_product(product1, 2)
        cart.add_product(product2, 3)
        cart.view_cart()
        cart.remove_product(product1, 1)
        cart.view_cart()
        cart.checkout()


if __name__ == "__main__":
    unittest.main()