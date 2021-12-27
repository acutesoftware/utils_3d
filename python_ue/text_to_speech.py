import pyttsx3 as pyttsx

def main():
    print('text to speech utils')
    create_wav_from_text(0, 'hi please pick 3 herbs', 'pick_herb.wav')


def create_wav_from_text(voice_id, txt, op_file):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id])

    engine.save_to_file(txt, op_file)
    
    # Wait until above command is not finished.
    engine.runAndWait()


def test_all_voices():
    """
    On a windows 10 PC the following voices are installed by default
        Microsoft David Desktop - English (United States)
        Microsoft Hazel Desktop - English (Great Britain)
        Microsoft Zira Desktop - English (United States)   
    """
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    print(voices)
    for voice in voices:
        engine.setProperty('voice', voice.id)  # changes the voice
        print(str(voice.name))
        engine.say('Hi from ' + str(voice.name))
        #engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()


main()