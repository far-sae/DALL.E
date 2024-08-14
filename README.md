
# AI Image Generator with Streamlit

![Streamlit](https://img.shields.io/badge/Streamlit-1.0.0-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellowgreen)

## Overview

This repository contains a web application that generates AI-powered images based on textual descriptions using a model similar to DALL-E. The app is built with Streamlit, utilizing the `diffusers` library and the Stable Diffusion model for high-quality image generation.

### Features

- **Text-to-Image Generation**: Generate images from simple textual descriptions.
- **Batch Generation**: Generate multiple images in one go.
- **Image Resizing**: Resize generated images on-the-fly.
- **Optimized Performance**: Utilizes GPU for fast generation, with mixed precision and reduced inference steps for speed.

## Demo

![Demo](path/to/demo.gif)

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8 or higher
- CUDA-enabled GPU (optional but recommended for faster performance)

### Clone the Repository

\`\`\`bash
git clone https://github.com/farz-sae/DALL.E.git
cd DALL.E
\`\`\`

### Create a Virtual Environment

\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scriptsctivate`
\`\`\`

### Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Required Python Packages

- `torch` (with CUDA support)
- `diffusers`
- `transformers`
- `streamlit`
- `Pillow`

These are automatically installed with the `requirements.txt` file.

### Running the Application

\`\`\`bash
streamlit run app.py
\`\`\`

Open your web browser and go to `http://localhost:8501` to use the application.

## Usage

1. **Enter a Description**: Type in a textual description of the image you want to generate.
2. **Set the Number of Images**: Use the slider to set how many images you want to generate.
3. **Resize Option**: Optionally, set the width and height to resize the generated images.
4. **Generate**: Click the "Generate Image" button to create your images.
5. **Download**: Download the generated images directly from the app.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your changes to your fork.
5. Submit a pull request.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the `diffusers` and `transformers` libraries.
- [Streamlit](https://streamlit.io/) for providing an easy-to-use framework for creating web apps.


