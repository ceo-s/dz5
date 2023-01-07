from use_functions import check_balance, Person

def test_only_clear_func():
    assert check_balance(Person) == "\nВаш баланс = 0"