#!/usr/bin/env python3
"""
Image collector module for collecting and validating image files.
"""

import os
import logging
from typing import List
from PIL import Image
from utils.image_processor import ImageProcessor


class ImageCollector:
    """Responsible for collecting and validating image files."""

    def __init__(self, processor: ImageProcessor):
        self.processor = processor

    def collect_images(self, image_paths: List[str]) -> List[Image.Image]:
        """Collect and process images from the provided paths."""
        processed_images = []

        for path in image_paths:
            if not os.path.exists(path):
                logging.warning(f"Image path does not exist: {path}")
                continue

            try:
                img = self.processor.process(path)
                processed_images.append(img)
            except Exception as e:
                logging.error(f"Failed to process {path}: {str(e)}")

        return processed_images
