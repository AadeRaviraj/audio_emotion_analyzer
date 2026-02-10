import faster_whisper
import librosa
import time

model = faster_whisper.WhisperModel(
    "tiny.en",
    device="cpu",
    compute_type="int8",
    cpu_threads=4
)

start = time.time()

y, sr = librosa.load("test.wav", sr=16000, mono=True)
segments, _ = model.transcribe(y)

for s in segments:
    print(s.text)

print("Time:", time.time() - start)
