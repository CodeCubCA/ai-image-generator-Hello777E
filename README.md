---
title: AI Image Generator
emoji: 🎨
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.31.0"
app_file: app.py
pinned: false
---

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zrsH8x_3)

# 🎨 AI Image Generator

A powerful web application that transforms text descriptions into stunning AI-generated images using HuggingFace's FLUX.1-schnell model and Streamlit.

## ✨ Features

- **Text-to-Image Generation** - Create images from natural language descriptions
- **8 Style Presets** - Anime, Realistic, Digital Art, Watercolor, Oil Painting, Cyberpunk, Fantasy, and more
- **Multiple Image Sizes** - Square (512x512), Portrait (512x768), and Landscape (768x512)
- **Image History Gallery** - Keep track of up to 10 recently generated images
- **Download Functionality** - Save images with timestamped filenames
- **Real-time Preview** - See enhanced prompts before generation
- **Intuitive UI** - Clean, user-friendly interface with helpful tips and examples

## 🚀 Technologies Used

- **Python 3.8+** - Programming language
- **Streamlit** - Web framework for the UI
- **HuggingFace Inference API** - AI model hosting
- **FLUX.1-schnell** - Fast, high-quality text-to-image model
- **Pillow (PIL)** - Image processing library
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- HuggingFace account (free)

### Setup Steps

**1. Clone the repository**
```bash
git clone https://github.com/CodeCubCA/ai-image-generator-Hello777E.git
cd ai-image-generator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Get your HuggingFace API Token**
- Go to [HuggingFace Settings](https://huggingface.co/settings/tokens)
- Click "New token"
- Name: "AI Image Generator"
- Select **"Write"** permissions (required for Inference API)
- Click "Generate token"
- Copy the token (starts with `hf_`)

**4. Configure environment variables**
```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your token
HUGGINGFACE_TOKEN=hf_your_actual_token_here
```

**5. Run the application**
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 🎯 How to Use

1. **Select a Style Preset** (Optional)
   - Choose from 8 artistic styles in the sidebar
   - Or keep "None" to use your original prompt

2. **Enter Your Prompt**
   - Describe the image you want to create
   - Be specific and detailed

3. **Choose Image Size**
   - Square (512x512) - Default
   - Portrait (512x768) - Vertical images
   - Landscape (768x512) - Horizontal images

4. **Generate**
   - Click "🎨 Generate Image"
   - Wait 10-30 seconds for AI to create your image

5. **Download & Explore**
   - Download images with the "⬇️ Download" button
   - View your image history below
   - Clear history anytime with "🗑️ Clear History"

## 💡 Example Prompts

**Landscape:**
```
A serene mountain landscape at sunset, photorealistic, 4k
```

**Character:**
```
A cute corgi puppy in a flower field, sunny day, high detail
```

**Sci-Fi:**
```
Futuristic cyberpunk city at night, neon lights, cinematic
```

**Abstract:**
```
Abstract geometric shapes, vibrant colors, modern art style
```

## 🎨 Style Presets

The app includes 8 pre-configured artistic styles that automatically enhance your prompts:

- **Anime** - Studio Ghibli inspired illustrations
- **Realistic** - Photorealistic, 8K quality photography
- **Digital Art** - Concept art, trending on ArtStation
- **Watercolor** - Soft, traditional watercolor paintings
- **Oil Painting** - Classical art with textured brushstrokes
- **Cyberpunk** - Neon-lit, futuristic sci-fi aesthetics
- **Fantasy** - Magical, enchanted, epic atmospheres
- **None** - Use your original prompt without modifications

## 📁 Project Structure

```
ai-image-generator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Your API token (gitignored)
├── .env.example       # Template for .env
├── .gitignore         # Files to ignore in git
└── README.md          # This documentation
```

## 🔧 Troubleshooting

**"API token not configured"**
- Ensure you created a `.env` file in the project root
- Verify your token is correctly copied (starts with `hf_`)
- Restart the application after adding the token

**"Authentication failed"**
- Your token must have "Write" permissions
- Check if the token has expired
- Generate a new token if needed

**"Rate limit reached"**
- HuggingFace free tier has usage limits
- Wait a few minutes before generating again
- Consider upgrading your HuggingFace account for higher limits

**Application won't start**
- Ensure Python 3.8+ is installed: `python --version`
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check if port 8501 is available

## 🤝 Contributing

This is a student project for educational purposes. Feel free to fork and experiment!

## 📝 License

This project is for educational purposes as part of a coding assignment.

## 🙏 Acknowledgments

- **HuggingFace** - For providing the Inference API
- **Streamlit** - For the amazing web framework
- **Black Forest Labs** - For the FLUX.1-schnell model
