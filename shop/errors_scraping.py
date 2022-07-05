class ScrapError(Exception):
    pass

class ScrapTimeoutError(ScrapError):
    pass

class ScrapHTTPError(ScrapError):
    pass