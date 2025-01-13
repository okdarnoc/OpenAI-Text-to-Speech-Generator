# OpenAI Text-to-Speech Generator with Mandarin Support
# This script converts text to speech using OpenAI's API with support for Mandarin Chinese

from openai import OpenAI
import base64
import os

# Initialize the OpenAI client with API key
client = OpenAI(api_key='YOUR_API_KEY')  # Replace with your actual API key

def create_output_directory():
    """
    Prompts user for output directory and creates it if it doesn't exist.
    Returns the validated directory path.
    """
    while True:
        output_dir = input("Enter the directory path where you want to save the audio file: ").strip()
        if output_dir:
            try:
                os.makedirs(output_dir, exist_ok=True)
                return output_dir
            except Exception as e:
                print(f"Error creating directory: {str(e)}")
                print("Please enter a valid directory path.")
        else:
            print("Directory path cannot be empty.")

def get_output_filename(output_dir):
    """
    Prompts user for filename and handles file existence checks.
    Returns the full filepath for the output file.
    """
    while True:
        filename = input("Enter the desired filename (without .mp3 extension): ").strip()
        if filename:
            full_filename = f"{filename}.mp3"
            full_path = os.path.join(output_dir, full_filename)
            if os.path.exists(full_path):
                overwrite = input("File already exists. Do you want to overwrite it? (y/n): ").lower()
                if overwrite != 'y':
                    continue
            return full_path
        else:
            print("Filename cannot be empty.")

def generate_audio(filepath, text_content):
    """
    Generates audio from text using OpenAI's API and saves it to the specified filepath.
    
    Args:
        filepath (str): Path where the audio file will be saved
        text_content (str): The text content to convert to speech
    """
    try:
        # Create completion with both text and audio outputs
        completion = client.chat.completions.create(
            model="gpt-4o-audio-preview",
            modalities=["text", "audio"],
            audio={"voice": "ballad", "format": "mp3"},
            messages=[
                {
                    "role": "user",
                    "content": text_content
                }
            ]
        )

        # Print the text response
        print("\nText Response:")
        print(completion.choices[0])

        # Decode and save the audio file
        mp3_bytes = base64.b64decode(completion.choices[0].message.audio.data)
        with open(filepath, "wb") as f:
            f.write(mp3_bytes)
        print(f"\nAudio file successfully generated at: {filepath}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get output directory and filename from user
    output_dir = create_output_directory()
    output_path = get_output_filename(output_dir)
    
    # Your Mandarin text content here
    text_content = """
    Language:
    Use Mandarin to tell the story. Don't miss or rewrite any bits. Be dramatic.         

    Story Prompt:
    我與父親不相見已有二年餘了...
    """ # (rest of the text content)
    
    # Generate the audio file
    generate_audio(output_path, text_content)

if __name__ == "__main__":
    main()
