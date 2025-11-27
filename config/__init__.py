"""
Configuration module initialization.
"""

from .settings import *

__all__ = [
    'PROJECT_ROOT',
    'DATA_DIR',
    'MODELS_DIR',
    'LOGS_DIR',
    'LANGUAGE',
    'NLU_MODEL_PATH',
    'DEFAULT_AUDIO_DEVICE_ID',
    'AUDIO_SAMPLE_RATE',
    'AUDIO_CHUNK_SIZE',
    'RECOGNITION_ENGINE',
    'RECOGNITION_TIMEOUT',
    'RECOGNITION_PHRASE_TIMEOUT',
    'TTS_ENGINE',
    'TTS_VOICE_ID',
    'LOG_LEVEL',
    'LOG_FORMAT',
    'LOG_FILE',
    'NLU_CONFIDENCE_THRESHOLD',
    'INTENT_CLASSIFIER_PATH',
    'SMART_HOME_API_KEY',
    'SMART_HOME_BASE_URL',
    'DEBUG_MODE',
]