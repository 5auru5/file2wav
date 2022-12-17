from dataclasses import dataclass
import wave
import tempfile

@dataclass()
class InputArgs():
    channels : int
    sample_width : int
    frame_rate : int
    
class WavConverter():
    def __init__():
        pass
    
    def convert(self, file, input_args : InputArgs):
        with open(file , "rb") as i_file:
            data = i_file.read()
            with wave.open(tempfile.TemporaryFile(), "wb") as out_f:
                out_f.setnchannels(input_args.channels) # number of channels
                out_f.setsampwidth(input_args.sample_width) # number of bytes in sample width
                out_f.setframerate(input_args.frame_rate)  # sample rate
                out_f.writeframesraw(data)
        return out_f
    