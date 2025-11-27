"""
Test I/O module.
"""

import pytest
import sys
from pathlib import Path

# Add project root to Python path for tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import with absolute imports to avoid conflict with stdlib io module
import importlib.util
spec = importlib.util.spec_from_file_location("audio_input", project_root / "io" / "audio_input.py")
audio_input = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audio_input)

spec = importlib.util.spec_from_file_location("audio_output", project_root / "io" / "audio_output.py")
audio_output = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audio_output)

spec = importlib.util.spec_from_file_location("speech_recognition", project_root / "io" / "speech_recognition.py")
speech_recognition = importlib.util.module_from_spec(spec)
spec.loader.exec_module(speech_recognition)

spec = importlib.util.spec_from_file_location("text_to_speech", project_root / "io" / "text_to_speech.py")
text_to_speech = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_to_speech)

AudioInput = audio_input.AudioInput
AudioOutput = audio_output.AudioOutput
SpeechRecognizer = speech_recognition.SpeechRecognizer
TextToSpeech = text_to_speech.TextToSpeech


class TestAudioInput:
    """Test cases for AudioInput class."""
    
    def test_initialization(self):
        """Test AudioInput initialization."""
        audio_input = AudioInput()
        assert audio_input.device_id is None
        assert audio_input.sample_rate == 16000
    
    def test_initialization_with_params(self):
        """Test AudioInput initialization with parameters."""
        device_id = 1
        sample_rate = 44100
        audio_input = AudioInput(device_id, sample_rate)
        assert audio_input.device_id == device_id
        assert audio_input.sample_rate == sample_rate
    
    def test_start_stop_recording(self):
        """Test starting and stopping recording."""
        audio_input = AudioInput()
        # Should not raise any exceptions
        audio_input.start_recording()
        audio_input.stop_recording()
    
    def test_get_audio_data(self):
        """Test getting audio data."""
        audio_input = AudioInput()
        result = audio_input.get_audio_data()
        assert result is None


class TestAudioOutput:
    """Test cases for AudioOutput class."""
    
    def test_initialization(self):
        """Test AudioOutput initialization."""
        audio_output = AudioOutput()
        assert audio_output.device_id is None
    
    def test_play_audio(self, sample_audio_data):
        """Test playing audio."""
        audio_output = AudioOutput()
        # Should not raise any exceptions
        audio_output.play_audio(sample_audio_data)


class TestSpeechRecognizer:
    """Test cases for SpeechRecognizer class."""
    
    def test_initialization(self):
        """Test SpeechRecognizer initialization."""
        recognizer = SpeechRecognizer()
        assert recognizer.engine == 'google'
        assert recognizer.language == 'en-US'
    
    def test_initialization_with_params(self):
        """Test SpeechRecognizer initialization with parameters."""
        engine = 'sphinx'
        language = 'fr-FR'
        recognizer = SpeechRecognizer(engine, language)
        assert recognizer.engine == engine
        assert recognizer.language == language
    
    def test_recognize(self, sample_audio_data):
        """Test speech recognition."""
        recognizer = SpeechRecognizer()
        text, confidence = recognizer.recognize(sample_audio_data)
        assert text == ""
        assert confidence == 0.0


class TestTextToSpeech:
    """Test cases for TextToSpeech class."""
    
    def test_initialization(self):
        """Test TextToSpeech initialization."""
        tts = TextToSpeech()
        assert tts.engine == 'pyttsx3'
        assert tts.voice_id is None
    
    def test_speak(self, sample_text):
        """Test text-to-speech conversion."""
        tts = TextToSpeech()
        # Should not raise any exceptions
        tts.speak(sample_text)