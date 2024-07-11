import sys
import os
import whisper

MODEL = "base"

# format_filename means to get the filename without the path and extension
def format_filename(filename):
    return filename.split("/")[-1].split(".")[0]

# save_output means to save the output to a file
def save_output(output_name, output):
    if not os.path.exists("output"):
        os.mkdir("output")

    try:
        with open(output_name, "w") as f:
            f.write(output)
    except Exception as e:
        print(f"Error saving output: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]

    if not os.path.exists(audio_file):
        print(f"File {audio_file} not found")
        sys.exit(1)

    print(f"Loading model {MODEL}")
    model = whisper.load_model(MODEL)

    print("Transcribing...")
    result = model.transcribe(audio_file)

    output_name = format_filename(audio_file)

    print(f"Saving result to output/{output_name}.txt")
    save_output(f"output/{output_name}.txt", result["text"])

if __name__ == "__main__":
    main()

