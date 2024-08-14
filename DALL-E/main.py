import streamlit as st
from diffusers import StableDiffusionPipeline  # Ensure this import works
import torch
from PIL import Image
import io


# Load the pre-trained Stable Diffusion model
@st.cache_resource()
def load_model():
    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    return model


def generate_image(model, prompt: str, num_images: int = 1):
    images = []
    for _ in range(num_images):
        output = model(prompt)
        st.write(output.keys())  # Inspect the output keys
        image = output["images"][0]  # Adjust this line based on the actual output key
        images.append(image)
    return images


def resize_image(image: Image, size: tuple):
    return image.resize(size, Image.ANTIALIAS)


# Web Interface
def main():
    st.title("AI Image Generator with Streamlit")

    # Load the model
    model = load_model()

    # Get user input for the image description
    prompt = st.text_input("Enter a description for the image", "A futuristic city at sunset")

    # Get user input for number of images
    num_images = st.slider("Number of images to generate", 1, 5, 1)

    # Get user input for image resizing
    resize = st.checkbox("Resize image?")
    width = height = None
    if resize:
        width = st.number_input("Width", value=512)
        height = st.number_input("Height", value=512)

    # Generate the image
    if st.button("Generate Image"):
        with st.spinner("Generating images..."):
            images = generate_image(model, prompt, num_images)

        # Display and allow download of generated images
        for idx, image in enumerate(images):
            if resize and width and height:
                image = resize_image(image, (width, height))
            st.image(image, caption=f"Generated Image {idx + 1}")

            buf = io.BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(label="Download Image", data=byte_im, file_name=f"generated_image_{idx + 1}.png",
                               mime="image/png")


if __name__ == "__main__":
    main()
