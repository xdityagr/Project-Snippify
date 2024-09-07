class RequiredArgumentMissing(Exception):
    def __init__(self, missing, context) -> None:
        message = f"Required Argument Missing, '{missing}' -> {context}"
        super().__init__(message)

class WrongArgumentFormat(Exception):
    def __init__(self, arg, context) -> None:
        message = f"Wrong format of the Argument Input, '{arg}' -> {context}"
        super().__init__(message)

# Errors = [RequiredArgumentMissing, WrongArgumentFormat]