import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QTextCursor
import openai

class WorkFluentChatbotGUI(QMainWindow):
    def __init__(self, api_key):
        super().__init__()

        openai.api_key = api_key
        self.languages = ["english", "spanish", "french", "german", "italian", "portuguese", "chinese", "japanese", "korean", "arabic"]

        self.init_ui()
        self.language = ""
        self.translation_type = ""
        self.user_input = ""

    def init_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('WorkFluent Chatbot')

        self.conversation_text_edit = QTextEdit(self)
        self.conversation_text_edit.setReadOnly(True)

        self.input_line_edit = QLineEdit(self)

        self.translate_button = QPushButton('Send', self)
        self.translate_button.clicked.connect(self.process_input)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.conversation_text_edit)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.exit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.add_to_conversation("Hi, I'm Bee-yonce! I'm excited to help you on your language learning journey!")
        self.add_to_conversation(f"Choose a language to start learning in:\n{', '.join(self.languages)}")

    def add_to_conversation(self, text):
        current_text = self.conversation_text_edit.toPlainText()
        self.conversation_text_edit.setPlainText(current_text + '\n' + text)
        self.conversation_text_edit.moveCursor(QTextCursor.End)

    def process_input(self):
        user_input = self.input_line_edit.text().strip()

        if not user_input:
            return

        if user_input.lower() == 'stop':
            self.add_to_conversation("Goodbye! Have a bee-utiful day.")
            return

        if not self.language:
            if user_input.lower() in self.languages:
                self.language = user_input.lower()
                self.add_to_conversation(f"Selected language: {self.language.capitalize()}")
                self.add_to_conversation("Do you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')?")
            else:
                self.add_to_conversation("Invalid language. Choose a valid language to start learning in.")
            self.input_line_edit.clear()
            return

        if not self.translation_type:
            if user_input.lower() in ['direct', 'phrases']:
                self.translation_type = user_input.lower()

                # Customize the prompt based on the translation type
                prompt = (
                    "What phrase do you want to translate?"
                    if self.translation_type == 'direct'
                    else "What topic are you interested in?"
                )

                self.add_to_conversation(f"Selected translation type: {self.translation_type}")
                self.add_to_conversation(prompt)
            else:
                self.add_to_conversation("Please choose 'direct' or 'phrases'.")
            self.input_line_edit.clear()
            return

        self.user_input = user_input
        self.perform_translation()

    def perform_translation(self):
        if self.translation_type == 'direct':
            phrase = self.user_input
            translated_phrase = self.get_translation(self.language, phrase)
            self.add_to_conversation(f"{phrase} in {self.language} is {translated_phrase}")
        elif self.translation_type == 'phrases':
            topic = self.user_input
            phrases = self.get_phrases(self.language, topic)
            self.add_to_conversation(f"Here are some work-related phrases on {topic}:\n{phrases}")

        # Ask the user for the next translation type
        self.add_to_conversation("Do you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')?")
        self.translation_type = ""
        self.user_input = ""
        self.input_line_edit.clear()

    def get_translation(self, language, phrase):
        prompt = f"Translate the following phrase from the language the user is typing in to {language.capitalize()}: '{phrase}'"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()

    def get_phrases(self, language, topic):
        prompt = f"Give me 5 work-related phrases on {topic} in {language.capitalize()}. First print it in whatever language the user is communicating with and then show it in the language they want it translated to."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=200
        )
        return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    api_key = 'YOUR_KEY'
    chatbot_gui = WorkFluentChatbotGUI(api_key)
    chatbot_gui.show()
    sys.exit(app.exec_())
