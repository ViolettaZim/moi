class EmptyDataError(Exception):
    """Raised when input GeoDataFrame is empty."""
    pass


class InvalidCRSError(Exception):
    """Raised when CRS is not valid or missing."""
    pass


class InvalidRadiusError(Exception):
    """Raised when radius is negative or zero."""
    pass


class InvalidTreeDataError(Exception):
    """Raised when tree data contains invalid values."""
    pass
