"""
Test NLU module.
"""

import pytest
import sys
from pathlib import Path

# Add project root to Python path for tests
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from nlu.intent_classifier import IntentClassifier
from nlu.entity_extractor import EntityExtractor


class TestIntentClassifier:
    """Test cases for IntentClassifier class."""
    
    def test_initialization(self):
        """Test IntentClassifier initialization."""
        classifier = IntentClassifier()
        assert classifier.model is None
        assert classifier.model_path is None
    
    def test_initialization_with_model_path(self):
        """Test IntentClassifier initialization with model path."""
        model_path = "/path/to/model.pkl"
        classifier = IntentClassifier(model_path)
        assert classifier.model_path == model_path
    
    def test_predict(self):
        """Test intent prediction."""
        classifier = IntentClassifier()
        intent, confidence = classifier.predict("test text")
        assert intent == "unknown"
        assert confidence == 0.0
    
    def test_train(self):
        """Test model training."""
        classifier = IntentClassifier()
        training_data = [("hello", "greeting"), ("goodbye", "farewell")]
        # Should not raise any exceptions
        classifier.train(training_data)


class TestEntityExtractor:
    """Test cases for EntityExtractor class."""
    
    def test_initialization(self):
        """Test EntityExtractor initialization."""
        extractor = EntityExtractor()
        assert extractor.model is None
        assert extractor.model_path is None
    
    def test_extract(self):
        """Test entity extraction."""
        extractor = EntityExtractor()
        entities = extractor.extract("test text")
        assert entities == {}
    
    def test_train(self):
        """Test model training."""
        extractor = EntityExtractor()
        training_data = [{"text": "test", "entities": []}]
        # Should not raise any exceptions
        extractor.train(training_data)