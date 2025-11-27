"""
Settings and configuration module for pchome voice assistant.
"""

import os
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
MODELS_DIR = PROJECT_ROOT / 'models'
LOGS_DIR = PROJECT_ROOT / 'logs'

# Create directories if they don't exist
for directory in [DATA_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Language settings
LANGUAGE = os.getenv('PCHOME_LANGUAGE', 'en-US')
NLU_MODEL_PATH = MODELS_DIR / 'nlu_model.pkl'

# Audio settings
DEFAULT_AUDIO_DEVICE_ID = None  # Will use system default
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHUNK_SIZE = 1024

# Speech recognition settings
RECOGNITION_ENGINE = 'google'  # Options: google, wit.ai, sphinx
RECOGNITION_TIMEOUT = 5
RECOGNITION_PHRASE_TIMEOUT = 3

# Text-to-speech settings
TTS_ENGINE = 'pyttsx3'  # Options: pyttsx3, gtts
TTS_VOICE_ID = None  # Will use system default

# Logging settings
LOG_LEVEL = os.getenv('PCHOME_LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = LOGS_DIR / 'pchome.log'

# NLU settings
NLU_CONFIDENCE_THRESHOLD = 0.7
INTENT_CLASSIFIER_PATH = MODELS_DIR / 'intent_classifier.pkl'

# Home automation settings
SMART_HOME_API_KEY = os.getenv('PCHOME_SMART_HOME_API_KEY', '')
SMART_HOME_BASE_URL = os.getenv('PCHOME_SMART_HOME_BASE_URL', '')

# Debug settings
DEBUG_MODE = os.getenv('PCHOME_DEBUG', 'false').lower() == 'true'