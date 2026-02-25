from calculator.quick_calc import QuickCalc

def test_addition_flow():
    calc = QuickCalc()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_after_calculation():
    calc = QuickCalc()
    calc.result = calc.add(10, 5)
    cleared = calc.clear()
    assert cleared == 0
