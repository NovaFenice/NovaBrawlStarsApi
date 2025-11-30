class ApiError(Exception):
    """
    Generic error returned by the Brawl Stars API.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"API Error [{code}] {message}" if code else message)
        self.code = code

class InvalidTokenError(Exception):
    """
    Raised when the provided API token is invalid or missing.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"Invalid Token [{code}] {message}" if code else message)
        self.code = code

class NotFoundError(Exception):
    """
    Raised when a requested resource (player, brawler, etc.) is not found.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"Not Found [{code}] {message}" if code else message)
        self.code = code
    
class RateLimitError(Exception):
    """
    Raised when the API rate limit has been exceeded.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"Rate Limit [{code}] {message}" if code else message)
        self.code = code

class UnexpectedError(Exception):
    """
    Raised when an unexpected error occurs.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"Unexpected Error [{code}] {message}" if code else message)
        self.code = code

class ServiceErrorMaintenance(Exception):
    """
    Raised when the service is under maintenance.
    """
    def __init__(self, message: str, code: int | None=None):
        super().__init__(f"Service Maintenance [{code}] {message}" if code else message)
        self.code = code