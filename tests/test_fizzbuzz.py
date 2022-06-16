from coding_dojo.fizzbuzz import fizz_buzz

class TestFizzbuzz:
    def test_fizz_buzz(self):
        assert fizz_buzz(1) == [1]  

    def test_fizz_buzz_2(self):
        assert fizz_buzz(2) == [1,2]  
    
    def test_fizz_buzz_multiples_of_3(self):
        # assert fizz_buzz(3) == [1,2, "Fizz"]

        number = 3
        assert fizz_buzz(number)[number - 1] == "Fizz"
        
        number = 6
        assert fizz_buzz(number)[number - 1] == "Fizz"
    
    def test_fizz_buzz_4(self):
        assert fizz_buzz(4) == [1,2, "Fizz", 4]

    def test_fizz_buzz_5(self): 
        assert fizz_buzz(5) == [1,2, "Fizz", 4, "Buzz"]

    def test_fizz_buzz_multiples_of_5_3(self):
        # assert fizz_buzz(3) == [1,2, "Fizz"]

        number = 15
        assert fizz_buzz(number)[number - 1] == "FizzBuzz"