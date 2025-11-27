"""
Test configuration and fixtures.
"""

import pytest
import logging
import sys
from pathlib import Path

# Add project root to Python path for tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def logger():
    """Provide a test logger."""
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger(__name__)


@pytest.fixture
def sample_audio_data():
    """Provide sample audio data for testing."""
    # TODO: Generate actual sample audio data
    return b"sample_audio_data"


@pytest.fixture
def sample_text():
    """Provide sample text for testing."""
    return "Hello, this is a test message."