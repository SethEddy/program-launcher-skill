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
        
    def prog_name(self):
                utterance = message.data.get('utterance')
                rex = re.compile(r'\b \b', re.IGNORECASE)
                text = rex.sub('*', utterance)
                prog = fnmatch.filter(os.listdir('/usr/share/applications/'), "*" + text + "*.*")
                return "'%s'" % "".join(prog)
    
    def handle_Launch_intent(self, message):
        #result = message.data.get('utterance')
        self.speak_dialog("Launch", prog_name)
        subprocess.call(['gtk-launch', prog_name])

    def stop(self):
        pass


def create_skill():
    return ProgramLauncherSkill()
