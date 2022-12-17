import sys
import wave
def main():
    with open(sys.argv[1], "rb") as inp_f: #opens given file
        data = inp_f.read()
        with wave.open(sys.argv[2], "wb") as out_f:
            out_f.setnchannels(int(sys.argv[4])) # number of channels
            out_f.setsampwidth(int(sys.argv[5])) # number of bytes in sample width
            out_f.setframerate(int(sys.argv[3]))  # sample rate
            out_f.writeframesraw(data)

def printUsage():
        print('''\
Usage: Python3 wav.py [inputfilename] [outputfilename] [bitrate] [channels] [samplewidth]
        
        ''')

if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("FAILURE: Please ensure all arguments are supplied")
        printUsage()
    except FileNotFoundError:
        print("FAILURE: Please check your input file path")
        printUsage()
