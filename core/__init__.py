"""
Core module for pchome voice assistant.
"""

from .assistant import VoiceAssistant
from .exceptions import PchomeError

__all__ = ['VoiceAssistant', 'PchomeError']