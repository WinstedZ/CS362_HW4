import unittest
import assignment4

class TestCase(unittest.TestCase):

    def test_vol1(self):
        self.assertEqual(assignment4.Cube_volume(4),12)
    
    def test_vol2(self):
        self.assertEqual(assignment4.Cube_volume(-4),12)

    def test_vol3(self):
        self.assertEqual(assignment4.Cube_volume("z"),0)
    
    def test_vol4(self):
        self.assertEqual(assignment4.Cube_volume(4.5),13.5)

    def test_list1(self):
        self.assertEqual(assignment4.Average_element([1,2,3,4]),2.5)

    def test_list2(self):
        self.assertEqual(assignment4.Average_element(['a','b','c','d']),2.5)
    
    def test_list3(self):
        self.assertEqual(assignment4.Average_element([]),0)
    
    def test_name1(self):
        self.assertEqual(assignment4.Name_generator("Zakary","Winsted"),"Zakary Winsted")
    
    def test_name2(self):
        self.assertEqual(assignment4.Name_generator(0,1),"0 1")
    
    def test_name3(self):
        self.assertEqual(assignment4.Name_generator(["Zakary","Winsted","first","last"],"name"),"Zakary Winsted first last name")
    
    

if __name__ == '__main__':
      unittest.main(verbosity=2)