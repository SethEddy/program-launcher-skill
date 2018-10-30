
import re
import os
import fnmatch
import subprocess
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'MrWho'

LOGGER = getLogger(__name__)


class ProgramLauncher(MycroftSkill):
    def __init__(self):
        super(ProgramLauncherSkill, self).__init__(name="ProgramLauncher")

    def initialize(self):
        launch_intent = IntentBuilder("LaunchIntent"). \
            require("launchKeyword").build()
        self.register_intent(launch_intent, self.handle_launch_intent)
        
    def prog_name(self, message):
		text = message.data.get('utterance')
		rex = re.compile(r'\b \b', re.IGNORECASE)
		text_fix = rex.sub('*', text)	
		prog = fnmatch.filter(os.listdir('/usr/share/applications/'), "*" + text_fix + "*.*")
		return ("'%s'" % "".join(program))
    
    
    def handle_Launch_intent(self, message):
        self.speak_dialog("Launch", 'utterance')
        subprocess.call(['gtk-launch', prog_name])
		

    def stop(self):
        pass


def create_skill():
    return ProgramLauncher()

