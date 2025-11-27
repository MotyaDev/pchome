"""
Test core module.
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add project root to Python path for tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from core.assistant import VoiceAssistant
from core.exceptions import PchomeError, AudioError, NLUError


class TestVoiceAssistant:
    """Test cases for VoiceAssistant class."""
    
    def test_initialization(self, logger):
        """Test VoiceAssistant initialization."""
        assistant = VoiceAssistant()
        assert assistant.config == {}
        assert assistant.logger is not None
    
    def test_initialization_with_config(self, logger):
        """Test VoiceAssistant initialization with config."""
        config = {'test': 'value'}
        assistant = VoiceAssistant(config)
        assert assistant.config == config
    
    def test_start(self, logger):
        """Test starting the voice assistant."""
        assistant = VoiceAssistant()
        # Should not raise any exceptions
        assistant.start()
    
    def test_stop(self, logger):
        """Test stopping the voice assistant."""
        assistant = VoiceAssistant()
        # Should not raise any exceptions
        assistant.stop()


class TestExceptions:
    """Test cases for custom exceptions."""
    
    def test_pchome_error(self):
        """Test PchomeError exception."""
        with pytest.raises(PchomeError):
            raise PchomeError("Test error")
    
    def test_audio_error(self):
        """Test AudioError exception."""
        with pytest.raises(AudioError):
            raise AudioError("Audio error")
    
    def test_nlu_error(self):
        """Test NLUError exception."""
        with pytest.raises(NLUError):
            raise NLUError("NLU error")