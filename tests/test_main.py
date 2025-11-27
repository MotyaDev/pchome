"""
Test main entry point.
"""

import pytest
import subprocess
import sys
from pathlib import Path


class TestMain:
    """Test cases for main.py entry point."""
    
    def test_main_runs_without_errors(self):
        """Test that main.py can run without errors."""
        main_path = Path(__file__).parent.parent / 'main.py'
        
        # Run main.py with --help to test basic functionality
        result = subprocess.run(
            [sys.executable, str(main_path), '--help'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        assert result.returncode == 0
        assert 'pchome' in result.stdout
        assert 'Smart voice assistant' in result.stdout
    
    def test_main_with_verbose_flag(self):
        """Test main.py with verbose flag."""
        main_path = Path(__file__).parent.parent / 'main.py'
        
        result = subprocess.run(
            [sys.executable, str(main_path), '--verbose', '--help'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        assert result.returncode == 0
    
    def test_main_with_language_flag(self):
        """Test main.py with language flag."""
        main_path = Path(__file__).parent.parent / 'main.py'
        
        result = subprocess.run(
            [sys.executable, str(main_path), '--language', 'fr-FR', '--help'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        assert result.returncode == 0