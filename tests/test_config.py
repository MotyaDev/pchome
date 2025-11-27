"""
Test configuration module.
"""

import pytest
import os
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to Python path for tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestConfig:
    """Test cases for configuration module."""
    
    def test_project_paths_exist(self):
        """Test that project directories are created."""
        from config.settings import (
            PROJECT_ROOT, DATA_DIR, MODELS_DIR, LOGS_DIR
        )
        
        assert PROJECT_ROOT.exists()
        assert DATA_DIR.exists()
        assert MODELS_DIR.exists()
        assert LOGS_DIR.exists()
    
    def test_default_settings(self):
        """Test default configuration values."""
        from config.settings import (
            LANGUAGE, LOG_LEVEL, TTS_ENGINE, RECOGNITION_ENGINE
        )
        
        assert LANGUAGE == 'en-US'
        assert LOG_LEVEL == 'INFO'
        assert TTS_ENGINE == 'pyttsx3'
        assert RECOGNITION_ENGINE == 'google'
    
    def test_environment_override(self):
        """Test that environment variables override defaults."""
        with patch.dict(os.environ, {'PCHOME_LANGUAGE': 'fr-FR'}):
            # Reimport to get updated value
            import importlib
            import config.settings
            importlib.reload(config.settings)
            
            assert config.settings.LANGUAGE == 'fr-FR'