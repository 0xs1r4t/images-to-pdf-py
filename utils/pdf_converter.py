#!/usr/bin/env python3
"""
PDF converter module for converting images to PDF.
"""

from abc import ABC, abstractmethod
from typing import List
import logging
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFConverter(ABC):
    """Abstract base class for PDF conversion operations."""

    @abstractmethod
    def convert(self, images: List[Image.Image], output_path: str) -> None:
        """Convert images to PDF."""
        pass


class ReportLabPDFConverter(PDFConverter):
    """PDF converter implementation using ReportLab."""

    def convert(self, images: List[Image.Image], output_path: str) -> None:
        """Convert a list of images to a single PDF file."""
        if not images:
            raise ValueError("No images provided for conversion")

        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        for img in images:
            # Resize image to fit the page while maintaining aspect ratio
            img_width, img_height = img.size
            aspect = img_width / img_height

            if img_width > img_height:
                # Landscape orientation
                new_width = width - 40  # 20px margin on each side
                new_height = new_width / aspect
            else:
                # Portrait orientation
                new_height = height - 40  # 20px margin on each side
                new_width = new_height * aspect

            # Center the image on the page
            x = (width - new_width) / 2
            y = (height - new_height) / 2

            # Draw the image
            c.drawImage(img.filename, x, y, width=new_width, height=new_height)
            c.showPage()

        c.save()
        logging.info(f"PDF created successfully at {output_path}")
