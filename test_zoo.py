import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_invalid1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'invalid')

    def test_invalid2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-3), 'invalid')
    
    def test_child1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    
    def test_child2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)

    def test_child3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)
    
    def test_child4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teen2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test_teen3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_teen4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_teen5_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    
    def test_mid1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_mid2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(22), 150)

    def test_mid3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(55), 150)
    
    def test_mid4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)
    
    def test_mid4_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_old1_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_old2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

if __name__ == '__main__':
    unittest.main()