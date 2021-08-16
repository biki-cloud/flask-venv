# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# with sr.AudioFile("kr.wav") as source:
#     audio = r.record(source)
#
# # text = r.recognize_google(audio, language='ja-JP')
# text = r.recognize_google(audio, language='ja-JP')
#
# print(text)
# brew install portaudio
# brew install gcc
import speech_recognition as sr


# https://syachiku-python.com/%E3%80%90%E5%AE%8C%E5%85%A8%E6%94%BB%E7%95%A5%E3%80%91python%E3%81%A7%E8%87%AA%E4%BD%9C%E3%81%AE%E9%9F%B3%E5%A3%B0%E8%AA%8D%E8%AD%98%E3%82%92%E3%82%AA%E3%83%95%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%A7/
def learning():
    r = sr.Recognizer()
    cnt = 0
    list = []
    with sr.Microphone() as source:
        while (4 > cnt):  # ここの数を増やせば、よりタフネスが上がります
            r.adjust_for_ambient_noise(source)
            print("=== 何か、話しかけてください ===")
            audio = r.listen(source)
            print("[o] ===> オーディオGET")
            print("=== CMU Sphinx音声解析中 ===")
            # text = r.recognize_sphinx(audio)
            text = r.recognize_sphinx(audio, language="kr-KR")
            print("You said : " + text)
            list.append(text)
            cnt = cnt + 1
    print(list)


def get_speaking_value():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("=== 何か、話しかけてください ===")
        audio = r.listen(source)
        print("[o] ===> オーディオGET")

    try:
        print("=== CMU Sphinx音声解析中 ===")
        text = r.recognize_sphinx(audio)
        if (text in ['come on it', 'oh my', 'come on that', 'oh my']):  # ここで英語->日本語変換判断
            print("You said : " + "とまれ")
    except:
        print("error")
        pass
    try:
        print("=== Google Speech Recognition音声解析中 ===")
        text = r.recognize_google(audio, language="ja-JP")
        print("You said : " + text)
    except:
        print("error")
        pass


if __name__ == "__main__":
    learning()
    # get_speaking_value()
