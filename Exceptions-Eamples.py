class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age must be a positive integer.")
def check_range(nums):
    if nums >10:
        raise InvalidAgeError("Age more than 10.")
try:
    check_age(1)
    check_range(15)

    print ("test")
except InvalidAgeError as e:
    print(f"Error: {e}")
