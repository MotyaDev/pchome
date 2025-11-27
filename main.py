#!/usr/bin/env python3
"""
Main entry point for the pchome voice assistant.
"""

import argparse
import logging
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.settings import LOG_LEVEL, LOG_FORMAT


def setup_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper()),
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('pchome.log')
        ]
    )


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='pchome - Smart voice assistant to control your home'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--config', '-c',
        type=str,
        default='config/settings.yaml',
        help='Path to configuration file'
    )
    
    parser.add_argument(
        '--device-id', '-d',
        type=int,
        help='Audio device ID for input'
    )
    
    parser.add_argument(
        '--language', '-l',
        type=str,
        default='en-US',
        help='Language for speech recognition (default: en-US)'
    )
    
    return parser.parse_args()


def main():
    """Main entry point for the voice assistant."""
    args = parse_arguments()
    
    # Override log level if verbose flag is set
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting pchome voice assistant...")
    logger.info(f"Using language: {args.language}")
    logger.info(f"Config file: {args.config}")
    
    if args.device_id:
        logger.info(f"Using audio device ID: {args.device_id}")
    
    # TODO: Initialize and start voice assistant components
    logger.info("Voice assistant initialized successfully")
    logger.info("Ready to accept voice commands...")


if __name__ == '__main__':
    main()