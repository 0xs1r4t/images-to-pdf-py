#!/usr/bin/env python3
"""
Command-line interface module for the PDF conversion tool.
"""

import argparse
import logging


def setup_logging(verbose: bool = False):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert multiple images to a single PDF file."
    )
    parser.add_argument(
        "images", nargs="+", help="Paths to image files to be converted"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.pdf",
        help="Output PDF file path (default: output.pdf)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    return parser.parse_args()
