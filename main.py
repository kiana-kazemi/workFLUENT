import openai

class WorkFluentChatbot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.languages = ["english", "spanish", "french", "german", "italian", "portuguese", "chinese", "japanese", "korean", "arabic"]

    def start_chat(self):
        print("Hi, I'm Bee-yonce! I'm excited to help you on your language learning journey!\n")

        language = self.get_user_language()

        if language == "stop" or language not in self.languages:
            print("Goodbye! Have a bee-utiful day.")
            return

        while True:
            translation_type = input("Do you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')? ").lower()

            if translation_type == "direct":
                phrase = input("Enter the phrase you want to translate: ")
                translated_phrase = self.get_translation(language, phrase)
                print(f"{phrase} in {language} is {translated_phrase}")
            elif translation_type == "phrases":
                topic = input("Enter the topic you want phrases on: ")
                phrases = self.get_phrases(language, topic)
                print(f"Here are some work-related phrases on {topic}:\n{phrases}")
            else:
                print("Please choose 'direct' or 'phrases'.")

            continue_option = input("What do you want to do next? (Type 'stop' to exit, or press Enter to continue) ").lower()
            if continue_option == "stop":
                print("Goodbye! Have a bee-utiful day.")
                break

    def get_user_language(self):
        print("Choose a language to start learning in:\n{}".format("\n".join(self.languages)))
        return input("(Type 'stop' to exit)\n").lower()

    def get_translation(self, language, phrase):
        prompt = f"Translate the following phrase from the language the user is typing in to {language.capitalize()}: '{phrase}'"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def get_phrases(self, language, topic):
        prompt = f"Give me 5 work related phrases on {topic} in {language.capitalize()}. First print it in whatever language the user is communicating with and then show it in the language they want it translated to."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()


# Replace 'YOUR_API_KEY' with your OpenAI API key
api_key = 'YOU-API-KEY'
chatbot = WorkFluentChatbot(api_key)
chatbot.start_chat()