import re
import os
import fnmatch
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Mr Who'

LOGGER = getLogger(__name__)


class ProgramLauncherSkill(MycroftSkill):
    def __init__(self):
        super(ProgramLauncherSkill, self).__init__(name="ProgramLauncherSkill")

    def initialize(self):
        #self.add_event('recognizer_loop:utterance', self.handle_utterance)

        launch_intent = IntentBuilder("LaunchIntent"). \
            require("LaunchKeyword").build()
        self.register_intent(launch_intent, self.handle_launch_intent)
        
    def handle_launch_intent(self, message):
        utterance = message.data.get('utterance')
        rex = re.compile(r'\b \b', re.IGNORECASE)
        text = rex.sub('*', utterance)
        prog = fnmatch.filter(os.listdir('/usr/share/applications/'), "*" + text + "*.*")
        program = "'%s'" % "".join(prog)
        self.speak_dialog("Launch", program)
        subprocess.call(['gtk-launch', program])

    def stop(self):
        pass


def create_skill():
    return ProgramLauncherSkill()
