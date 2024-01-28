import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QTextCursor, QFont
import openai

class WorkFluentChatbotGUI(QMainWindow):
    def __init__(self, api_key):
        super().__init__()
        #self.setGeometry(400, 150, 500, 800)

        openai.api_key = api_key
        self.languages = ["english", "spanish", "french", "german", "italian", "portuguese", "chinese", "japanese", "korean", "arabic"]

        self.init_ui()
        self.language = ""
        self.translation_type = ""
        self.user_input = ""

    def init_ui(self):
        self.setGeometry(100, 100, 700, 1000)
        self.setWindowTitle('WorkFluent Chatbot')

        font = QFont('Cambria', 12)
        QApplication.setFont(font)
        self.setStyleSheet('background-color: #FFE36E')

        self.conversation_text_edit = QTextEdit(self)
        self.conversation_text_edit.setReadOnly(True)
        self.conversation_text_edit.setStyleSheet('border-radius: 5px;background-color: #EDEDED')

        self.input_line_edit = QLineEdit(self)
        self.input_line_edit.setStyleSheet('border-radius: 5px;background-color: #EDEDED')

        self.translate_button = QPushButton('Send', self)
        self.translate_button.setStyleSheet('border-radius: 5px;background-color: #4CAF50; color: white')
        self.translate_button.clicked.connect(self.process_input)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setStyleSheet('border-radius: 5px; background-color: #FF4F4B; color: white')
        self.exit_button.clicked.connect(self.close)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.conversation_text_edit)
        layout1.addWidget(self.input_line_edit)
        #layout.addWidget(self.translate_button)
        #layout.addWidget(self.exit_button)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.translate_button)
        layout2.addWidget(self.exit_button)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addLayout(layout2)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.add_to_conversation("Beeyonce:\nHi, I'm Bee-yonce! I'm excited to help you on your language learning journey!")
        self.add_to_conversation(f"Choose a language to start learning in:\n ⋆ {'\n ⋆ '.join(self.languages)} \n")

    def add_to_conversation(self, text):
        current_text = self.conversation_text_edit.toPlainText()
        self.conversation_text_edit.setPlainText(current_text + '\n' + text)
        self.conversation_text_edit.moveCursor(QTextCursor.End)

    def process_input(self):
        user_input = self.input_line_edit.text().strip()

        if not user_input:
            return

        if user_input.lower() == 'stop':
            self.add_to_conversation("Bee-yonce:\nGoodbye! Have a bee-utiful day.\n\n")
            return

        if not self.language:
            if user_input.lower() in self.languages:
                self.language = user_input.lower()
                self.add_to_conversation(f"Bee-yonce:\nYou've chosen: {self.language.capitalize()}\n")
                self.add_to_conversation("Do you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')?\n\n")
            else:
                self.add_to_conversation("Bee-yonce:\nInvalid language. Choose a valid language to start learning in.\n\n")
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

                self.add_to_conversation(f"Bee-yonce:\nSelected translation type: {self.translation_type}")
                self.add_to_conversation(f'{prompt}\n\n')
            else:
                self.add_to_conversation("Bee-yonce:\nPlease choose 'direct' or 'phrases'.\n\n")
            self.input_line_edit.clear()
            return

        self.user_input = user_input
        self.perform_translation()

    def perform_translation(self):
        if self.translation_type == 'direct':
            phrase = self.user_input
            translated_phrase = self.get_translation(self.language, phrase)
            self.add_to_conversation(f"Bee-yonce:\n{phrase} in {self.language} is {translated_phrase}\n\n")
        elif self.translation_type == 'phrases':
            topic = self.user_input
            phrases = self.get_phrases(self.language, topic)
            self.add_to_conversation(f"Bee-yonce:\nHere are some work-related phrases on {topic}:\n{phrases}\n\n")

        # Ask the user for the next translation type
        self.add_to_conversation("Bee-yonce:\nDo you want a direct translation (type 'direct') or phrases on a topic (type 'phrases')?\n\n")
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
    api_key = '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'
    chatbot_gui = WorkFluentChatbotGUI(api_key)
    chatbot_gui.show()
    sys.exit(app.exec_())
