[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zrsH8x_3)

# AI Image Generator

A web application that generates images from text descriptions using HuggingFace's Inference API and Streamlit.

## Features

- Simple and clean web interface
- Text-to-image generation using FLUX.1-schnell model
- Real-time image generation
- Error handling for common issues
- Loading indicators
- Helpful prompt suggestions

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get HuggingFace API Token

1. Go to https://huggingface.co/settings/tokens
2. Click "New token"
3. Give it a name (e.g., "AI Image Generator")
4. Select **"Write"** permissions (or at minimum "Make calls to the serverless Inference API")
   - **Important:** Read-only tokens will NOT work!
5. Click "Generate token"
6. Copy the token (starts with `hf_`)

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` and add your token:
   ```
   HUGGINGFACE_TOKEN=hf_your_actual_token_here
   ```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Enter a detailed description of the image you want to generate
2. Click "Generate Image"
3. Wait 10-30 seconds for the image to be generated
4. View your generated image
5. Right-click to save the image

## Example Prompts

- "A serene landscape with mountains at sunset, photorealistic, 4k"
- "A futuristic city at night, neon lights, cyberpunk style"
- "A cute corgi puppy playing in a flower field, sunny day, high detail"
- "Abstract geometric shapes, vibrant colors, modern art style"

## Tips for Better Results

- Be specific and detailed in your descriptions
- Include style keywords (e.g., "photorealistic", "oil painting", "digital art")
- Mention lighting, colors, and mood
- Specify quality (e.g., "4k", "high detail", "professional photography")

## Troubleshooting

### "API token not configured"
- Make sure you created a `.env` file
- Check that your token is correctly copied
- Restart the application after adding the token

### "Authentication failed"
- Verify your token has "Write" permissions
- Check that the token hasn't expired
- Try generating a new token

### "Rate limit reached"
- Free tier has usage limits
- Wait a few minutes before trying again
- Consider upgrading your HuggingFace account

## Technical Details

- **Framework:** Streamlit
- **API:** HuggingFace Inference API
- **Model:** black-forest-labs/FLUX.1-schnell
- **Library:** huggingface_hub (InferenceClient)

## Project Structure

```
ai-image-generator/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .env               # Your API token (not in git)
├── .env.example       # Template for .env
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## License

This project is for educational purposes.
