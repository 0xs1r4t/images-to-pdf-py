#!/usr/bin/env python3
"""
Image to PDF Conversion Tool
A command line utility to convert multiple images into a single PDF file.
"""

from utils.image_processor import BasicImageProcessor
from utils.image_collector import ImageCollector
from utils.pdf_converter import ReportLabPDFConverter
from utils.app import PDFConversionApp
from utils.cli import parse_arguments, setup_logging


def main():
    """Main entry point for the application."""
    args = parse_arguments()
    setup_logging(args.verbose)

    # Create the application components
    image_processor = BasicImageProcessor()
    image_collector = ImageCollector(image_processor)
    pdf_converter = ReportLabPDFConverter()

    # Create and run the application
    app = PDFConversionApp(image_collector, pdf_converter)
    success = app.convert(args.images, args.output)

    if success:
        print(f"Successfully converted images to PDF: {args.output}")
    else:
        print("Failed to convert images to PDF. Check the logs for details.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
