import numb3rs

def test_valid_ip():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("10.0.0.0") == True
    assert numb3rs.validate("172.16.0.0") == True

def test_invalid_ip():
    assert numb3rs.validate("256.0.0.1") == False
    assert numb3rs.validate("192.168.0.256") == False
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("192.168.0.-1") == False
    assert numb3rs.validate("192.168.0.1a") == False

def test_mixed_validity():
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("192.168.0.256") == False
    assert numb3rs.validate("10.0.0.0") == True
    assert numb3rs.validate("172.16.0.0") == True
    assert numb3rs.validate("192.168.0") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("192.168.0.-1") == False
    assert numb3rs.validate("192.168.0.1a") == False

def run_tests():
    test_valid_ip()
    test_invalid_ip()
    test_mixed_validity()

if __name__ == "__main__":
    run_tests()