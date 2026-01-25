# 🎤 Piper Voice Showcase

Interactive Jupyter notebook demo showcasing 4 different Piper TTS voices, including LibriTTS with 904 unique speakers.

## 📋 Overview

This project demonstrates high-quality text-to-speech synthesis using [Piper TTS](https://github.com/rhasspy/piper), a fast, local neural text-to-speech system. Switch between different voice models and explore hundreds of unique speakers with an interactive player.

## 📖 Demo Content Preview

The voices synthesize the following research article excerpt from `demo.md`:

<details open>
<summary><strong>📄 Click to expand/collapse demo text</strong></summary>

> ### Coordinating the Crowd: Multi-Agent AI Systems
> 
> #### 1. Opening
> 
> When a swarm of drones choreographs a light show, a fleet of autonomous vehicles negotiates traffic, or a customer-service bot team drafts a legal brief, the common thread is a distributed intelligence that outperforms any single agent. Yet the mechanics that let dozens or hundreds of learning agents cooperate remain an active frontier.
> 
> This article traces the evolution of collaboration mechanisms in multi-agent AI systems, from foundational architectures to emergent communication protocols...
> 
> #### 2. Key Approaches - Three Core Paradigms
> 
> | Approach | Strength | Limitation |
> |----------|----------|------------|
> | **Role-based coordination** | 85% efficiency in structured environments | Rigid; poor adaptability |
> | **Emergent communication** | Handles 40% more edge cases | Requires extensive training |
> | **Learning-driven coordination** | Improves 15% per iteration | High computational cost |
> 
> #### 3. Performance Metrics
> 
> - AI agents using emergent protocols: **92% task completion** vs. 67%
> - Multi-agent RL systems: **34% reduced** coordination overhead
> - Distributed frameworks: scaled to **500+ agents** vs. ~50 previously
> 
> #### 4. Practical Implications
> 
> Three recommendations for practitioners:
> 1. Start with role-based coordination for well-defined tasks
> 2. Layer emergent communication for adaptability
> 3. Use RL fine-tuning for optimization
> 
> *Full text available in [`demo.md`](demo.md)*

</details>

**Key features demonstrated:**
- 📊 Table linearization (converts markdown tables to spoken format)
- 📝 Citation handling (processes Doc-X, Web-Y, Arxiv-Z references)
- 🔢 Number normalization (percentages, metrics)
- 📖 Section formatting (numbered headings)
- ✨ Markdown cleanup (bold, italic, links removed for natural speech)

---

## 🎙️ Voice Samples

Listen to how each voice model synthesizes this content *(download to play)*:

### Heather
*Natural, conversational female voice (medium quality)*

📥 [Download heather.wav](wav/heather.wav) *(~500KB)*

### Michael
*Balanced, natural male voice (medium quality)*

📥 [Download michael.wav](wav/mike.wav) *(~500KB)*

### Lessac
*Professional, natural speech with best overall quality (high quality)*

📥 [Download lessac.wav](wav/lessac.wav) *(~800KB)*

### LibriTTS
*High-quality voice with 904 diverse speakers to choose from*

📥 [Download libritts_speaker_0.wav](wav/libritts_speaker_0.wav) *(~800KB)*

---

💡 **To listen:** Download the files above or run the interactive notebook locally for instant playback with all 904 LibriTTS speakers.
---

## 🚀 Features

- **4 Voice Models**: Choose between Heather, Michael, Lessac, and LibriTTS
- **904 Speakers**: LibriTTS offers 904 unique speaker voices
- **Interactive UI**: Dropdown selection with keyboard navigation (+ / − buttons)
- **Auto-play**: Instantly hear voices as you switch
- **Persistent Storage**: All generated audio saved to `wav/` folder
- **Smart Preprocessing**: Converts markdown to natural speech with citation handling

## 📦 Requirements
```bash
pip install piper-tts ipywidgets
```

Additional files required:
- `tts_preprocessing.py` - TTS preprocessing module
- `demo.md` - Demo text content

## 💻 Usage

1. Ensure `demo.md` exists in the project directory
2. Run all notebook cells
3. Execute `create_player()` to launch the interactive player
4. Select voices from dropdown or use +/− buttons for LibriTTS speakers
5. Generated audio files are automatically saved to `wav/` folder

## 📁 Project Structure
```
.
├── notebook.ipynb          # Main Jupyter notebook
├── demo.md                 # Demo text content
├── tts_preprocessing.py    # TTS preprocessing module
├── models/                 # Downloaded Piper voice models
│   └── piper/
├── wav/                    # Generated audio files
│   ├── heather.wav
│   ├── michael.wav
│   ├── lessac.wav
│   └── libritts_speaker_*.wav
└── README.md
```

## 🔧 Technical Details

- **Models**: Downloaded from [Hugging Face](https://huggingface.co/rhasspy/piper-voices)
- **Format**: 16-bit PCM WAV files
- **Sample Rate**: Varies by model (typically 22050 Hz)
- **Lazy Loading**: Models are only downloaded and loaded when first selected
- **Preprocessing Pipeline**: 
  - Unicode normalization
  - Table linearization
  - Citation formatting
  - Section structuring
  - Abbreviation expansion
  - Pause insertion for natural rhythm

## 📄 License

This project uses Piper TTS. Please refer to the [Piper repository](https://github.com/rhasspy/piper) for licensing information on the models and software.

## 🙏 Credits

- [Piper TTS](https://github.com/rhasspy/piper) by Rhasspy
- Voice models from [Hugging Face](https://huggingface.co/rhasspy/piper-voices)