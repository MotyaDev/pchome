"""
Custom exceptions for pchome voice assistant.
"""


class PchomeError(Exception):
    """Base exception class for pchome."""
    pass


class AudioError(PchomeError):
    """Exception raised for audio-related errors."""
    pass


class NLUError(PchomeError):
    """Exception raised for natural language understanding errors."""
    pass


class ConfigurationError(PchomeError):
    """Exception raised for configuration-related errors."""
    pass


class SmartHomeError(PchomeError):
    """Exception raised for smart home integration errors."""
    pass