from flask import Flask, render_template, jsonify
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import whisper
import tempfile
import os
import time
from queue import Queue
from chatgpt_client import ChatGPTClient

app = Flask(__name__)
chatgpt = ChatGPTClient()
whisper_model = whisper.load_model("base")


def is_silent(audio_chunk, threshold=0.03):
    if audio_chunk.dtype != np.float32:
        audio_chunk = audio_chunk.astype(np.float32)
    volume_norm = np.linalg.norm(audio_chunk) / np.sqrt(len(audio_chunk))
    return volume_norm < threshold


def record_audio(silence_duration=3, sample_rate=16000):
    audio_buffer = Queue()
    silence_counter = 0
    speech_detected = False
    recorded_audio = []

    def audio_callback(indata, frames, time, status):
        if status:
            print(status)
        audio_buffer.put(indata.copy())

    chunk_duration = 0.1
    chunk_samples = int(sample_rate * chunk_duration)
    silence_chunks = int(silence_duration / chunk_duration)

    with sd.InputStream(callback=audio_callback,
                        channels=1,
                        samplerate=sample_rate,
                        blocksize=chunk_samples):
        while True:
            if not audio_buffer.empty():
                chunk = audio_buffer.get()
                recorded_audio.append(chunk)
                volume = np.linalg.norm(chunk) / np.sqrt(len(chunk))

                if not speech_detected and volume > 0.03:
                    speech_detected = True

                if speech_detected:
                    if volume < 0.03:
                        silence_counter += 1
                        if silence_counter >= silence_chunks:
                            break
                    else:
                        silence_counter = 0

            time.sleep(chunk_duration)

    if not speech_detected:
        return None

    return np.concatenate(recorded_audio)


def transcribe_audio(audio_data, sample_rate=16000):
    """Transcribe recorded audio to text."""
    try:
        # Create tempwavs directory if it doesn't exist
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tempwavs')
        os.makedirs(temp_dir, exist_ok=True)

        # Create a unique filename using timestamp
        timestamp = int(time.time())
        temp_path = os.path.join(temp_dir, f'audio_{timestamp}.wav')

        # Save and transcribe the audio
        wav.write(temp_path, sample_rate, audio_data)
        result = whisper_model.transcribe(temp_path)

        # Clean up
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return result["text"]
    except Exception as e:
        print(f"Error in transcription: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/record', methods=['POST'])
def record():
    try:
        # Record audio
        audio = record_audio()
        if audio is None:
            return jsonify({'error': 'No speech detected'}), 400

        # Transcribe audio
        transcript = transcribe_audio(audio)
        if transcript is None:
            return jsonify({'error': 'Transcription failed'}), 400

        # Get ChatGPT response
        response = chatgpt.get_response(transcript)

        return jsonify({
            'transcript': transcript,
            'response': response,
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)