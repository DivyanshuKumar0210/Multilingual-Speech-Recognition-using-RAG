import whisper
import argparse
import os

def main():
    output_folder = "text_data"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    model = whisper.load_model("base")
    transcription = model.transcribe(r"C:\Users\DIVYANSHU\OneDrive\Desktop\RAG-based-text-summarizer-and-translator\data\harvard.wav", fp16=False)

    # Define the file path within the output folder
    output_file_path = os.path.join(output_folder, "transcribed_text.txt")

    def save_text_to_file():
        with open(output_file_path, 'w') as file:
            file.write(transcription['text'])

    save_text_to_file()

if __name__ == "__main__":
    main()
    