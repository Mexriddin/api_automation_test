from services.commons.model import ErrorModel


class CommonSteps:
    @staticmethod
    def assert_error_msg(error_model: ErrorModel, code: int, error_message: str):
        assert error_model.code == code, f"Expected code:{code} but got {error_model.code}"
        assert error_message.strip() in error_model.message, (f"Expected \n'{error_message}', but got "
                                                              f"\n'{error_model.message}' message")
