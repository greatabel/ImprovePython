def validate_old(name):
    if len(name) < 10:
        raise ValueError

# validate_old('joe')

class NameTooShortException(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortException(name)

def handle_validation_error(ValueError):
    print('#'*10)
# validate('joe')

class BaseValidationError(ValueError):
    pass


class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass

try:
    validate('joe')
except NameTooShortException as err:
    handle_validation_error(err)