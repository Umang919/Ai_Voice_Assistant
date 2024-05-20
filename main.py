import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import subprocess
import openai
import os


s = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "Your_OpenAI_Key"
    chatStr += f"Chirag: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def say(text):
    s.Speak(text)

def chategpt(prompt):
    openai.api_key = "Your_OpenAI_Key"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response)
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "some error occurred. sorry from jarvis"


if __name__ == '__main__':
    print('Hello...')
    say("Hello I am Jarvish AI")
    while True:
        print("Listening...")
        query = takecommand()
        # say(query)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")


        elif "open vs code".lower() in query.lower():
            subprocess.Popen(["C:\\Users\\chirag\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
            say(f"Opening vs code")

        elif "Using artificial intelligence".lower() in query.lower():
            chategpt(prompt=query)

        elif "turn off".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
