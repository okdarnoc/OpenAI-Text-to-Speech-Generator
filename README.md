# OpenAI Text-to-Speech Generator with Mandarin Support

A Python script that leverages OpenAI's Text-to-Speech API to generate high-quality audio narration from Mandarin Chinese text. This tool is particularly useful for creating audiobooks, storytelling applications, or educational content in Mandarin.

## Features

- Converts Mandarin text to natural-sounding speech
- Uses OpenAI's advanced text-to-speech model
- Supports dramatic narrative style
- Handles file management with overwrite protection
- User-friendly command-line interface
- Generates MP3 audio files

## Prerequisites

- Python 3.6+
- OpenAI API key
- Required Python packages:
  - openai
  - base64
  - os

## Installation

1. Clone this repository:
```bash
git clone [your-repo-url]
```

2. Install required packages:
```bash
pip install openai
```

3. Set up your OpenAI API key:
   - Replace `'YOUR_API_KEY'` in the script with your actual OpenAI API key
   - Or set it as an environment variable

## Usage

1. Run the script:
```bash
python text_to_speech.py
```

2. Follow the prompts to:
   - Specify the output directory
   - Enter the desired filename
   - Confirm file overwrite if necessary

3. The script will generate an MP3 file with the narrated content

## Configuration

- Voice: Currently set to "ballad" for natural storytelling
- Output format: MP3
- Model: gpt-4o-audio-preview

## Code Example

```python
from openai import OpenAI
import base64
import os

client = OpenAI(api_key='YOUR_API_KEY')

# Generate audio from text
completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "ballad", "format": "mp3"},
    messages=[
        {
            "role": "user",
            "content": "Your Mandarin text here"
        }
    ]
)
```

## Error Handling

The script includes comprehensive error handling for:
- Invalid directory paths
- File system permissions
- API errors
- File handling issues

## Project Structure

```
.
├── README.md
├── requirements.txt
└── text_to_speech.py
```

## Output Example

The script will generate:
- An MP3 file containing the narrated content
- A confirmation message with the file path
- Any error messages if issues occur

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the Text-to-Speech API
- The open-source community for inspiration and tools

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/repo-name](https://github.com/yourusername/repo-name)

## Support

- Star the repository if you find it useful
- Report issues in the [Issues](https://github.com/yourusername/repo-name/issues) section
- For major changes, please open an issue first to discuss what you would like to change
