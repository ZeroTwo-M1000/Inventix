from exception.BaseExeption import BaseEx


class TokenError(BaseEx):
    status_code = 401
    detail = "Invalid token"


class NotAuthorizedError(BaseEx):
    status_code = 401
    detail = "Not authorized"
