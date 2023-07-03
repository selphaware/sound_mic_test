import sounddevice as sd
import soundfile as sf
import tempfile

# Constants
SAMPLE_RATE = 44100  # Sample rate is traditionally set to 44100 Hz
DURATION = 10  # Duration in seconds

# Create a temporary file for storage
temp_file = tempfile.mktemp(prefix='soundfile_', suffix='.wav')

print("Recording Audio for 10 secs")
# Record Audio
myrecording = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=2)
sd.wait()  # Wait for the recording to finish
sf.write(temp_file, myrecording, SAMPLE_RATE)

print("Playing Back Audio")
# Play Back Audio
data, samplerate = sf.read(temp_file)
sd.play(data, samplerate)
sd.wait()  # Wait for the playback to finish

print("Done")
