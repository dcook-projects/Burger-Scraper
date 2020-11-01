import unittest
import scraping
import burger_data as bd


class BurgerTests(unittest.TestCase):
    def setUp(self):
        # Burgers used in test_equality and test_str
        self.burger1 = bd.Burger("a", "cheeseburger", 7.99)
        self.burger2 = bd.Burger("a", "cheeseburger", 7.99)
        self.burger3 = bd.Burger("b", "cheeseburger", 7.99)

    def test_equality(self):
        self.assertEqual(self.burger1, self.burger2, "Burger 1 and Burger 2 are supposed to be equal, but are not.")
        self.assertNotEqual(self.burger1, self.burger3, "Burger 1 and Burger 3 should be equal.")
        self.assertNotEqual(self.burger2, self.burger3, "Burger 2 and Burger 3 should be equal.")
        self.assertTrue(self.burger1 < self.burger3)

        burger_list = [self.burger1]
        if self.burger2 not in burger_list:
            burger_list.append(self.burger2)

        self.assertEqual(len(burger_list), 1, "Too many burgers in the list")

    def test_string(self):
        self.assertEqual(str(self.burger1), str(self.burger2))
        self.assertNotEqual(str(self.burger2), str(self.burger3))

    def test_burger_bros(self):
        burgers = []
        scraping.get_burger_bros(burgers)
        self.assertEqual(len(burgers), 3)

    def test_longboard_cafe(self):
        burgers = []
        scraping.get_longboard_cafe(burgers)
        self.assertEqual(len(burgers), 7)

    def test_gordon_biersch(self):
        burgers = []
        scraping.get_gordon_biersch(burgers)
        self.assertEqual(len(burgers), 5)

    def test_wegmans_burger(self):
        burgers = []
        scraping.get_wegmans_burger(burgers)
        self.assertEqual(len(burgers), 6)

    def test_abbey_burger_bistro(self):
        burgers = []
        scraping.get_abbey_burger_bistro(burgers)
        self.assertEqual(len(burgers), 11)

    def test_alaska_stand(self):
        burgers = []
        scraping.get_alaska_stand(burgers)
        self.assertEqual(len(burgers), 14)

    def test_doghaus_biergarten(self):
        burgers = []
        scraping.get_doghaus_biergarten(burgers)
        self.assertEqual(len(burgers), 9)


if __name__ == "__main__":
    unittest.main()
