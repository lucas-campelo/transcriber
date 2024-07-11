# Transcriber

This code is designed to transcribe an audio file into text using the Whisper speech recognition model from OpenAI. I mainly use it to create transcriptions of meetings with clients so I can format them into meeting minutes.

I used a Python virtual environment to install the dependencies, so I decided to leave a requirements file to make installation easier using `pip`. The document is `requirements.txt`.

To run the code, simply pass the path of an audio file (I have only tested it with `.m4a` files) as an argument.

```shell
python main.py [path]
```

It's important to ensure that all Whisper dependencies (such as `ffmpeg`) are installed and to follow the recommendations in the [repository](https://github.com/openai/whisper?tab=readme-ov-file#setup).

The code does not download the model because an SSL verification is required to download it directly from OpenAI. Therefore, I preferred to download and install it manually. Just place the model in `/home/$USER/.cache/whisper/` (I also suggest renaming it to the model name, such as "base", as the file usually comes with a name like "Whisper base", for example).

The transcription is saved in a folder named `output`.