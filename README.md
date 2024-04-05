# Multilingual-Speech-Recognition-using-RAG

The project is a multifaceted text processing and conversational AI endeavor. It includes three main components:

Audio Transcription: Utilizing the Whisper library, the project offers a script (transcribe_audio_to_text.py) to transcribe audio files into text format. This script provides the functionality to load the Whisper model, transcribe audio input, and save the transcribed text to a file.

Data Storage for Language Processing: The project includes a script (create_db.py) to generate a data store for language processing tasks. It employs text documents, audio and video files and converts them into a Chroma database using HuggingFace embeddings, facilitating efficient storage and retrieval of linguistic data.

Chatbot Implementation: The project integrates a simple chatbot using pre-trained models from HuggingFace to perform summarization and translation tasks (translate_or_summarize.py). The chatbot prompts users to choose between summarizing or translating text, interacts with HuggingFaceHub for model inference, and incorporates a ChatPromptTemplate to format inputs for the models.

## Tasks

##### Following are the subtasks that were done in this project
- **Task 1**: Extracting text from audios and videos.
- **Task 2**: Creating a vector database for storing embeddings.
- **Task 3**: Creating a summarizer and translator using opensource LLMs.
  
- **Python-based**: Entirely coded in Python.


### Brief explanation of how RAG works

RAG (Retrieval-Augmented Generation) integrates retrieval-based and generation-based models by leveraging a large knowledge base to retrieve relevant information and augment the generation process. The retrieval component efficiently searches for pertinent passages, which are then used to enhance the quality and relevance of generated text. RAG models are fine-tuned on specific tasks or domains, enabling them to produce more accurate, informative, and domain-specific outputs. This approach improves relevance, fact-checking, and domain-specific generation capabilities, making RAG a powerful tool for generating high-quality text based on input queries or prompts.


## Installation & Running

**Important!:** Ensure you have Python installed on your system. 

**Note:** This is a CLI based application. You can add a streamlit UI if you want.

Clone this repository:

```bash
git clone [repository-link]
```
Go to the cloned folder:

```bash
cd [repository-directory]
```

Install the required packages:

```bash
pip install -r requirements.txt
```
after all the dependencies are installed run this command to install openai whisper
```bash
pip install git+https://github.com/openai/whisper.git
```
Running the application:

- running transcribe_audio_to_text.py
```bash
python transcribe_audio_to_text.py "path to your audio/video data"
```
- running create_db.py
```bash
python create_db.py
```
- running translate_or_summarize.py
- follow the prompts you're given to get desired results
```bash
python translate_or_summarize.py
```
**Note:** 
- Make sure the you face no error in running create_db.py
- You may face an error like 'The system cannot find the file specified', in that case you have to download ffmpeg package, copy 'ffmpeg.exe' file, and paste it in the directory where the files of this repository are stored.
