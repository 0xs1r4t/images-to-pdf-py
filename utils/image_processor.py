#!/usr/bin/env python3
"""
Image processor module for handling image processing operations.
"""

from abc import ABC, abstractmethod
import logging
from PIL import Image


class ImageProcessor(ABC):
    """Abstract base class for image processing operations."""

    @abstractmethod
    def process(self, image_path: str) -> Image.Image:
        """Process an image file."""
        pass


class BasicImageProcessor(ImageProcessor):
    """Basic implementation of image processor that opens and validates images."""

    def process(self, image_path: str) -> Image.Image:
        """Open and validate an image file."""
        try:
            img = Image.open(image_path)
            return img
        except Exception as e:
            logging.error(f"Failed to process image {image_path}: {str(e)}")
            raise
