import sys
import wave
import struct
import cgi
def main():
    with open(sys.argv[1], "rb") as inp_f:
        data = inp_f.read()
        with wave.open(sys.argv[2], "wb") as out_f:
            out_f.setnchannels(1)
            out_f.setsampwidth(2) # number of bytes
            out_f.setframerate(int(sys.argv[3]))
            out_f.writeframesraw(data)

if __name__ == "__main__":
    main()
