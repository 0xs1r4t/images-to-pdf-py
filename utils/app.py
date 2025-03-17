#!/usr/bin/env python3
"""
Application module for the PDF conversion tool.
"""

import logging
from typing import List
from utils.image_collector import ImageCollector
from utils.pdf_converter import PDFConverter


class PDFConversionApp:
    """Main application class that orchestrates the conversion process."""

    def __init__(self, image_collector: ImageCollector, pdf_converter: PDFConverter):
        self.image_collector = image_collector
        self.pdf_converter = pdf_converter

    def convert(self, image_paths: List[str], output_path: str) -> bool:
        """Convert the provided images to a single PDF file."""
        try:
            images = self.image_collector.collect_images(image_paths)

            if not images:
                logging.error("No valid images found for conversion")
                return False

            self.pdf_converter.convert(images, output_path)
            return True
        except Exception as e:
            logging.error(f"Conversion failed: {str(e)}")
            return False
