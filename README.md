# 🇳🇵 Nepali Number Plate Recognition System: Utilities

## 📜 Overview

This project is a comprehensive Automatic Number Plate Recognition (ANPR) system specifically designed to handle the unique challenges of vehicle number plates in Nepal. Unlike many regions with a single standard, Nepal utilizes **three distinct number plate formats** (Embossed, Provincial, and Regional), making localization and OCR a complex task.

This system leverages a custom-trained **YOLO** model to first detect and classify the type of number plate in an image. It then applies a robust computer vision preprocessing pipeline to enhance the plate for accurate text extraction using **EasyOCR**.

## 🎯 The Challenge: Diverse Nepali Number Plates

The primary motivation for this project was the high variability in Nepali number plates. A one-size-fits-all approach fails because of three co-existing formats:

1.  **Embossed Plates:** Modern, standardized plates with embossed characters and a uniform font.
2.  **Provincial Plates (Bagmati):** Hand-painted or printed plates with Province-specific prefixes and variable fonts.
3.  **Regional Plates (Mechi/Koshi):** Older, legacy plates with regional prefixes and significant variations in font, color, and condition.

This project was built to reliably handle all three types.

## ✨ Key Features

-   🔎 **Multi-Type Plate Detection:** Utilizes a custom-trained **YOLOv7** model to accurately localize number plates and classify them into one of the three types.
-   📊 **Custom Nepali Dataset:** Trained on a carefully curated dataset of over **1500+ images** of Nepali vehicles, which were manually labeled to ensure high accuracy.
-   🖼️ **Advanced Image Preprocessing:** Implements a specialized computer vision pipeline to normalize the detected plates for OCR, including:
    -   Monochrome Conversion
    -   Image Sharpening
    -   Angle Correction (Deskewing)
-   ✍️ **Accurate Text Extraction:** Leverages the powerful **EasyOCR** library to extract clean, readable text from the preprocessed plate images.
-   🚀 **Data Augmentation Pipeline:** Includes a pipeline for augmenting vehicle and plate images, which was crucial for robust model training.

## ⚙️ Project Pipeline: How It Works

The system follows a clear, multi-stage process to go from a raw vehicle image to extracted text:

1.  **Input Image:** The system takes an image of a vehicle as input.
2.  **Plate Localization & Classification:** The custom YOLO model scans the image to find the number plate. It draws a bounding box around the plate and simultaneously classifies it as `Embossed`, `Provincial`, or `Regional`.
3.  **Image Cropping & Preprocessing:** The area defined by the bounding box is cropped. This sub-image is then passed through the preprocessing pipeline:
    -   **Deskewing:** The image is rotated to ensure the plate is perfectly horizontal.
    -   **Grayscale Conversion:** The image is converted to monochrome to simplify feature detection.
    -   **Sharpening:** A sharpening filter is applied to make the characters more distinct.
4.  **Text Extraction (EasyOCR):** The clean, processed plate image is fed into EasyOCR, which reads the characters and returns the final number plate text.

## 🛠️ Tech Stack

-   **Deep Learning / ML:** Python, PyTorch, Ultralytics YOLOv7
-   **Computer Vision:** OpenCV, Pillow
-   **OCR Engine:** EasyOCR
-   **Data Handling:** NumPy, Pandas

## 📊 The Dataset

A core component of this project's success is the custom dataset.
-   **Size:** 1500+ images of vehicles across Nepal.
-   **Labeling:** Each image was **manually annotated** with bounding boxes for the number plates and classified into one of the three categories.
-   **Diversity:** The dataset includes a wide variety of lighting conditions, angles, and vehicle types to ensure the model is robust.

> *Note: Due to privacy and ownership, the dataset is not publicly available at this time.*
## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgements

-   [Ultralytics](https://github.com/ultralytics) for the powerful YOLO framework.
-   [Jaided AI](https://github.com/JaidedAI/EasyOCR) for the accessible and effective EasyOCR library.
-   The OpenCV team.
