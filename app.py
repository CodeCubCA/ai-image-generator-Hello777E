import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
from datetime import datetime

# Load environment variables
load_dotenv()

# Configuration
MODEL_NAME = "black-forest-labs/FLUX.1-schnell"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Style presets
STYLE_PRESETS = {
    "None": "",
    "Anime": ", anime style, vibrant colors, Studio Ghibli inspired, detailed illustration",
    "Realistic": ", photorealistic, highly detailed, 8K resolution, professional photography",
    "Digital Art": ", digital painting, artstation trending, concept art, highly detailed",
    "Watercolor": ", watercolor painting, soft colors, artistic, traditional art",
    "Oil Painting": ", oil painting, classical art, textured brushstrokes, museum quality",
    "Cyberpunk": ", cyberpunk style, neon lights, futuristic, sci-fi, high tech",
    "Fantasy": ", fantasy art, magical, enchanted, epic, dreamlike atmosphere"
}

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #FF5252;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎨 AI Image Generator")
st.markdown("Generate stunning images from text descriptions using AI")

# Check if API token is configured
if not HUGGINGFACE_TOKEN or HUGGINGFACE_TOKEN == "your_token_here":
    st.error("⚠️ HuggingFace API token not configured!")
    st.info("""
    **Setup Instructions:**
    1. Go to https://huggingface.co/settings/tokens
    2. Create a new token with "Write" permissions
    3. Copy the token
    4. Create a `.env` file in the project root
    5. Add: `HUGGINGFACE_TOKEN=your_token_here`
    6. Restart the application
    """)
    st.stop()

# Initialize the InferenceClient
try:
    client = InferenceClient(token=HUGGINGFACE_TOKEN)
except Exception as e:
    st.error(f"Failed to initialize HuggingFace client: {str(e)}")
    st.stop()

# Initialize session state for image history
if 'image_history' not in st.session_state:
    st.session_state.image_history = []

# Sidebar with information (must be before main content to define selected_style)
with st.sidebar:
    st.header("ℹ️ About")

    # Style Preset Selector
    st.subheader("🎨 Style Presets")
    selected_style = st.selectbox(
        "Choose a style:",
        options=list(STYLE_PRESETS.keys()),
        index=0,
        help="Select a preset style to enhance your prompts automatically"
    )

    if selected_style != "None":
        st.caption(f"✨ Style will add: {STYLE_PRESETS[selected_style]}")

    st.divider()

    # Tips Section
    st.subheader("💡 Tips for Better Results")
    st.markdown("""
    - **Be specific** and detailed in descriptions
    - **Add style keywords**: photorealistic, oil painting, digital art
    - **Mention lighting**: sunset, dramatic lighting, soft glow
    - **Include colors & mood**: vibrant, dark, cheerful
    - **Specify quality**: 4k, high detail, professional
    """)

    st.divider()

    # Example Prompts
    st.subheader("✨ Example Prompts")
    st.markdown("""
    **Landscape:**
    > A serene mountain landscape at sunset, photorealistic, 4k

    **Character:**
    > A cute corgi puppy in a flower field, sunny day, high detail

    **Abstract:**
    > Abstract geometric shapes, vibrant colors, modern art style

    **Sci-Fi:**
    > Futuristic cyberpunk city at night, neon lights, cinematic
    """)

    st.divider()

    # Usage Note
    st.info("💬 **Note:** Free tier has rate limits. Please use responsibly.")

# User input
st.markdown("### Describe your image")
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Example: A serene landscape with mountains at sunset, photorealistic, 4k",
    height=100,
    help="Describe the image you want to generate in detail"
)

# Image size selection
st.markdown("### Image Size")
size_options = {
    "Square (512x512)": (512, 512),
    "Portrait (512x768)": (512, 768),
    "Landscape (768x512)": (768, 512)
}

selected_size = st.selectbox(
    "Choose image dimensions:",
    options=list(size_options.keys()),
    index=0,
    help="Select the aspect ratio for your generated image"
)

width, height = size_options[selected_size]
st.caption(f"📐 Selected size: {width}x{height} pixels")

# Generate button
if st.button("🎨 Generate Image", type="primary"):
    if not prompt:
        st.warning("Please enter a prompt to generate an image.")
    else:
        try:
            with st.spinner("🎨 Creating your image... This may take 10-30 seconds"):
                # Combine prompt with style preset
                enhanced_prompt = prompt + STYLE_PRESETS[selected_style]

                # Show enhanced prompt if style is applied
                if selected_style != "None":
                    with st.expander("📝 Enhanced Prompt Preview"):
                        st.text(enhanced_prompt)

                # Generate image using InferenceClient
                image = client.text_to_image(
                    prompt=enhanced_prompt,
                    model=MODEL_NAME,
                    width=width,
                    height=height
                )

                # Display the generated image
                st.success("✨ Image generated successfully!")
                st.image(image, caption=f"Generated: {prompt}", use_container_width=True)

                # Save to history
                timestamp = datetime.now()
                image_data = {
                    'image': image,
                    'prompt': prompt,
                    'enhanced_prompt': enhanced_prompt,
                    'style': selected_style,
                    'timestamp': timestamp,
                    'size': f"{width}x{height}"
                }
                st.session_state.image_history.insert(0, image_data)

                # Limit to 10 images
                if len(st.session_state.image_history) > 10:
                    st.session_state.image_history = st.session_state.image_history[:10]

                # Download button
                st.markdown("---")

                # Convert image to bytes for download
                buf = BytesIO()
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()

                # Generate filename with timestamp
                timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")
                filename = f"ai_generated_{timestamp_str}.png"

                # Download button
                st.download_button(
                    label="⬇️ Download Image",
                    data=byte_im,
                    file_name=filename,
                    mime="image/png",
                    use_container_width=True
                )

                st.caption("💡 You can also right-click on the image and select 'Save image as...'")

        except Exception as e:
            error_message = str(e)

            # Handle common errors
            if "rate limit" in error_message.lower():
                st.error("⚠️ Rate limit reached. Please wait a few minutes and try again.")
                st.info("The free tier has usage limits. Consider waiting or upgrading your HuggingFace account.")
            elif "unauthorized" in error_message.lower() or "401" in error_message:
                st.error("⚠️ Authentication failed. Please check your API token.")
                st.info("Make sure your token has 'Write' permissions or at minimum 'Make calls to the serverless Inference API'")
            elif "not found" in error_message.lower() or "404" in error_message:
                st.error("⚠️ Model not found or not accessible.")
                st.info(f"The model '{MODEL_NAME}' may not be available. Try a different model.")
            else:
                st.error(f"⚠️ An error occurred: {error_message}")
                st.info("Please try again or check your internet connection.")

# Image History Gallery
if len(st.session_state.image_history) > 0:
    st.markdown("---")
    st.markdown("## 📸 Image History")

    # Header with count and clear button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption(f"Showing {len(st.session_state.image_history)} image(s)")
    with col2:
        if st.button("🗑️ Clear History"):
            st.session_state.image_history = []
            st.rerun()

    st.markdown("---")

    # Display images in grid (2 columns)
    for idx in range(0, len(st.session_state.image_history), 2):
        cols = st.columns(2)

        for col_idx, col in enumerate(cols):
            img_idx = idx + col_idx
            if img_idx < len(st.session_state.image_history):
                img_data = st.session_state.image_history[img_idx]

                with col:
                    # Display image
                    st.image(img_data['image'], use_container_width=True)

                    # Prompt and metadata
                    with st.expander(f"📝 Prompt #{img_idx + 1}"):
                        st.markdown(f"**Original Prompt:**")
                        st.text(img_data['prompt'])

                        if img_data['style'] != "None":
                            st.markdown(f"**Style:** {img_data['style']}")
                            st.markdown(f"**Enhanced Prompt:**")
                            st.text(img_data['enhanced_prompt'])

                        st.markdown(f"**Size:** {img_data['size']}")
                        st.markdown(f"**Generated:** {img_data['timestamp'].strftime('%I:%M:%S %p')}")

                    # Download button for each image
                    buf = BytesIO()
                    img_data['image'].save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    timestamp_str = img_data['timestamp'].strftime("%Y%m%d_%H%M%S")
                    filename = f"ai_generated_{timestamp_str}.png"

                    st.download_button(
                        label="⬇️ Download",
                        data=byte_im,
                        file_name=filename,
                        mime="image/png",
                        use_container_width=True,
                        key=f"download_{img_idx}"
                    )

                    st.markdown("---")
