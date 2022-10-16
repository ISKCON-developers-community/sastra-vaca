import wave

def combine_audio_files(files: list, outfile: str = "sounds.wav"):
    first_file = files[0]
    for i in range(len(files)-1):
        combine_two_files([first_file, files[i+1]], outfile)
        first_file = outfile

def combine_two_files(files: list, outfile: str = "sounds.wav"):
    data= []
    for infile in files:
        try:
            w = wave.open(infile, 'rb')
        except:
            w = wave.open('.empty.vav', 'rb')

        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()


