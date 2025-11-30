class ApiError(Exception):
    """
    Generic error returned by the Brawl Stars API.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...

class InvalidTokenError(Exception):
    """
    Raised when the provided API token is invalid or missing.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...

class NotFoundError(Exception):
    """
    Raised when a requested resource (player, brawler, etc.) is not found.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...

class RateLimitError(Exception):
    """
    Raised when the API rate limit has been exceeded.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...

class UnexpectedError(Exception):
    """
    Raised when an unexpected error occurs.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...

class ServiceErrorMaintenance(Exception):
    """
    Raised when the service is under maintenance.
    """
    code: int | None
    def __init__(self, message: str, code: int | None = ...) -> None: ...