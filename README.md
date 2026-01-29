# 🌸 Aesthetic Vibe Finder

> Transform feelings, scenes & dreams into curated visual moodboards. Live demo at: [moodboard-predictor](https://martasolerebri.github.io/moodboard-predictor/)


An experimental AI-powered application that bridges the gap between human emotion and visual aesthetics. Simply describe a vibe, feeling, or scene, and get a beautifully curated moodboard that captures its essence.

---

## Features

- **Intelligent Keyword Extraction**: Uses Groq's LLaMA 3.1 to extract visual concepts from natural language
- **Aesthetic Refinement**: Processes descriptions into search-optimized aesthetic queries
- **Live Image Search**: Fetches curated images using DuckDuckGo Search
- **Beautiful UI**: Glassmorphic design with smooth animations
- **Responsive Design**: Works seamlessly on desktop and mobile devices

---

## How It Works

1. **User Input**: Describe any vibe, scene, or feeling in natural language
2. **Keyword Extraction**: Groq API analyzes the text and extracts 4-8 visual keywords
3. **Image Search**: DuckDuckGo search fetches matching aesthetic images
4. **Moodboard Display**: Results are presented in a responsive masonry grid

### Pipeline Architecture

```
User Description
      ↓
Groq LLaMA 3.1 (Keyword Extraction)
      ↓
Visual Keywords
      ↓
DuckDuckGo Image Search
      ↓
Curated Moodboard
```

---

## Quick Start

### Prerequisites

- Python 3.10+
- [Groq API Key](https://console.groq.com/) (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/martasolerebri/moodboard-predictor.git
   cd moodboard-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 7860
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:7860` and open `index.html`

### Docker Deployment

```bash
# Build the image
docker build -t vibe-finder .

# Run the container
docker run -p 7860:7860 --env-file .env vibe-finder
```

---

## Project Structure

```
moodboard-predictor/
├── main.py                 # FastAPI application
├── src/
│   ├── keyword_extractor.py   # Groq-powered keyword extraction
│   └── scraper.py             # DuckDuckGo image search
├── index.html              # Frontend interface
├── style.css               # Glassmorphic styling
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
└── README.md              # This file
```

---

## API Reference

### POST `/predict`

Generate a moodboard from a text description.

**Request Body:**
```json
{
  "text": "Victorian tea party in a rainy garden with old books",
  "num_images": 9
}
```

**Response:**
```json
{
  "final_prompt": "Victorian tea party rainy garden old books vintage",
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    ...
  ]
}
```

### GET `/health`

Check API health and pipeline status.

**Response:**
```json
{
  "status": "healthy",
  "pipeline": "Groq -> T5",
  "groq_available": true,
  "t5_loaded": true
}
```

---

## Technologies Used

- **Backend**
  - [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
  - [Groq](https://groq.com/) - Ultra-fast LLM inference (LLaMA 3.1)
  - [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) - Privacy-focused image search
  - [Transformers](https://huggingface.co/transformers/) - Hugging Face model support

- **Frontend**
  - Vanilla JavaScript - No framework dependencies
  - CSS3 Glassmorphism - Modern aesthetic design
  - Google Fonts - Italiana & Quicksand

---

## Example Queries

Try these prompts to see the magic:

- "Cottagecore afternoon with wildflowers and vintage lace"
- "Cyberpunk Tokyo streets at night with neon reflections"
- "Minimalist Scandinavian bedroom with warm morning light"
- "Gothic Victorian library with candlelight and leather books"
- "Dreamy pastel sunset over lavender fields"

---

## Configuration

### Keyword Extraction Settings

Modify `keyword_extractor.py` to adjust extraction behavior:

```python
temperature=0.3,     # Lower = more focused, Higher = more creative
max_tokens=50,       # Maximum keywords length
top_p=0.9            # Nucleus sampling parameter
```

### Image Search Settings

Modify `scraper.py` for search preferences:

```python
region="wt-wt",      # Worldwide results
safesearch="on",     # Content filtering
size="Medium",       # Image size preference
type_image="photo"   # Image type
```

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Future Enhancements

- User authentication and saved moodboards
- Export moodboards as PDF or Pinterest boards
- Color palette extraction from results
- Multi-language support
- Advanced filtering (color, era, style)
- Social sharing capabilities

---

## Authors

[Marta Soler](https://github.com/martasolerebri), [Clàudia Salgado](https://github.com/claudiasalgado), [Javier Gracia](https://github.com/javigracia03), [Jorge Greus](https://github.com/jorgitogh) - Master's Degree Project

---

*Last Updated: January 2026*