import sys
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QFont
import openai


class WorkFluentChatbotGUI(QWidget):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.languages = ["english", "spanish", "french", "german", "italian", "portuguese", "chinese", "japanese", "korean", "arabic"]
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('WorkFluent Chatbot')
        self.setGeometry(100, 100, 375, 812)  # Set screen size to match iPhone 14 (375 x 812)

        # Set a fun and bubbly font
        font = QFont("Indie Flower", 14)  # Change to a more fun and bubbly font
        self.setFont(font)

        # Set background color for all windows
        self.setStyleSheet("background-color: #f6c935;")

        # Label Intro
        self.label_intro = QLabel("Hi, I'm Bee-yonce! I'm excited to help you on your language learning journey!\n", self)
        self.label_intro.setStyleSheet("color: black;")

        # Label Language
        self.label_language = QLabel("Choose a language to start learning in:", self)
        self.label_language.setStyleSheet("color: black;")

        # ComboBox Language
        self.comboBox_language = QComboBox(self)
        self.comboBox_language.addItems(self.languages)
        self.comboBox_language.setStyleSheet("background-color: #EDEDED; color: black; border-radius: 15px; font-size: 16px;")

        # Start Chat Button
        self.btn_start_chat = QPushButton("Start Chat", self)
        self.btn_start_chat.clicked.connect(self.start_chat)
        self.btn_start_chat.setStyleSheet("background-color: #8B4513; color: white; border-radius: 15px; font-size: 16px;")

        # Text Output Box
        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)
        self.text_output.setStyleSheet("background-color: #EDEDED; color: black; border-radius: 15px; font-size: 16px;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_intro)
        vbox.addWidget(self.label_language)
        vbox.addWidget(self.comboBox_language)
        vbox.addWidget(self.btn_start_chat)
        vbox.addWidget(self.text_output)

        self.setLayout(vbox)


    def start_chat(self):
        language = self.comboBox_language.currentText()

        if language == "stop" or language not in self.languages:
            self.text_output.append("Goodbye! Have a bee-utiful day.")
            return

        while True:
            translation_type, ok = self.get_user_input("Do you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')?")

            if not ok:
                break

            if translation_type == "direct":
                phrase, ok = self.get_user_input("Enter the phrase you want to translate:")

                if not ok:
                    break

                translated_phrase = self.get_translation(language, phrase)
                self.text_output.append(f"{phrase} in {language} is {translated_phrase}")
            elif translation_type == "phrases":
                topic, ok = self.get_user_input("Enter the topic you want phrases on:")

                if not ok:
                    break

                phrases = self.get_phrases(language, topic)
                self.text_output.append(f"Here are some work-related phrases on {topic}:\n{phrases}")
            else:
                self.text_output.append("Please choose 'direct' or 'phrases'.")

            continue_option, ok = self.get_user_input("What do you want to do next? (Type 'stop' to exit)")

            if not ok or continue_option == "stop":
                self.text_output.append("Goodbye! Have a bee-utiful day.")
                break

    def get_user_input(self, prompt):
        text, ok = QInputDialog.getText(self, "Input", prompt)
        return text.lower(), ok


    def get_translation(self, language, phrase):
        prompt = f"Translate the following phrase from the language the user is typing in to {language.capitalize()}: '{phrase}'"
        response = self.call_openai(prompt)
        return response.strip()

    def get_phrases(self, language, topic):
        prompt = f"Give me 5 work-related phrases on {topic} in {language.capitalize()}. First print it in whatever language the user is communicating with and then show it in the language they want it translated to."
        response = self.call_openai(prompt)
        return response.strip()

    def call_openai(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text


if __name__ == '__main__':
    # Replace 'YOUR_API_KEY' with your OpenAI API key
    api_key = 'YOUR_API_KEY'
    app = QApplication(sys.argv)
    chatbot_gui = WorkFluentChatbotGUI(api_key)
    chatbot_gui.show()
    sys.exit(app.exec_())
