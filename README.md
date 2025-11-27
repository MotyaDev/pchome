# pchome

Smart voice assistant to control your home.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd pchome
```

2. Create and activate a virtual environment:
```bash
# Using venv
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using virtualenv
python3 -m virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Run the voice assistant with default settings:
```bash
python main.py
```

Run with verbose logging:
```bash
python main.py --verbose
```

Specify language for speech recognition:
```bash
python main.py --language en-US
```

Specify audio device ID:
```bash
python main.py --device-id 1
```

Use custom configuration file:
```bash
python main.py --config /path/to/config.yaml
```

## Project Structure

```
pchome/
├── core/                   # Core application logic
│   ├── __init__.py
│   ├── assistant.py        # Main voice assistant class
│   └── exceptions.py       # Custom exceptions
├── nlu/                    # Natural Language Understanding
│   ├── __init__.py
│   ├── intent_classifier.py
│   └── entity_extractor.py
├── io/                     # Input/Output handling
│   ├── __init__.py
│   ├── audio_input.py      # Microphone input
│   ├── audio_output.py     # Speaker output
│   ├── speech_recognition.py
│   └── text_to_speech.py
├── config/                 # Configuration
│   ├── __init__.py
│   └── settings.py         # Application settings
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   ├── test_config.py
│   ├── test_core.py
│   ├── test_nlu.py
│   └── test_io.py
├── data/                   # Data files (auto-created)
├── models/                 # Model files (auto-created)
├── logs/                   # Log files (auto-created)
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Configuration

The application can be configured through:

1. Environment variables (prefixed with `PCHOME_`)
2. Configuration files
3. Command line arguments

Key environment variables:
- `PCHOME_LANGUAGE`: Speech recognition language (default: en-US)
- `PCHOME_LOG_LEVEL`: Logging level (default: INFO)
- `PCHOME_DEBUG`: Enable debug mode (default: false)

## Development

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=.
```

Run specific test file:
```bash
pytest tests/test_main.py
```

### Code Formatting

Format code with Black:
```bash
black .
```

Lint code with Flake8:
```bash
flake8 .
```

## Dependencies

- **SpeechRecognition**: Speech-to-text conversion
- **PyAudio**: Audio I/O
- **spaCy**: Natural language processing
- **scikit-learn**: Machine learning utilities
- **pyttsx3**: Text-to-speech synthesis
- **gTTS**: Alternative text-to-speech
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Linting

## License

[Add your license here]
