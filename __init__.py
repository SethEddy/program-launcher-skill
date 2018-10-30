from mycroft import MycroftSkill, intent_file_handler


class ProgramLauncher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('launcher.program.intent')
    def handle_launcher_program(self, message):
        self.speak_dialog('launcher.program')


def create_skill():
    return ProgramLauncher()

