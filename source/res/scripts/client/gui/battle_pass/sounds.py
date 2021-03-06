# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_pass/sounds.py
import WWISE
from constants import DEFAULT_LANGUAGE
from gui.impl.gen import R
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager
from helpers import getClientLanguage
from math_utils import clamp
from shared_utils import CONST_CONTAINER

class BattlePassSounds(CONST_CONTAINER):
    _OVERLAY = 'bp_overlay'
    CONFIRM_BUY = 'bp_overlay_pay'
    REWARD_SCREEN = 'bp_reward_screen'
    TANK_POINTS_CAP = 'bp_tank_point_done'
    VIDEO_BEFORE_VOTING = 'bp_s02_video_final_level_progression_start'
    VIDEO_OPT1_FREE = 'bp_s02_video_not_purchased_tank_01_start'
    VIDEO_OPT2_FREE = 'bp_s02_video_not_purchased_tank_02_start'
    VIDEO_OPT1_PAID = 'bp_s02_video_purchased_character_01_start'
    VIDEO_OPT2_PAID = 'bp_s02_video_purchased_character_02_start'
    VIDEO_PAUSE = 'bp_video_pause'
    VIDEO_RESUME = 'bp_video_resume'
    VIDEO_STOP = 'bp_video_stop'

    @classmethod
    def getOverlay(cls, count):
        return '_'.join([cls._OVERLAY, str(clamp(1, 3, count))])


class BattlePassLanguageSwitch(CONST_CONTAINER):
    GROUP_NAME = 'SWITCH_ext_battle_pass_video_language'
    RU = 'SWITCH_ext_battle_pass_video_language_RU'
    EN = 'SWITCH_ext_battle_pass_video_language_EN'


class AwardVideoSoundControl(IVideoSoundManager):
    __LANGUAGE_STATES = {'ru': BattlePassLanguageSwitch.RU,
     'en': BattlePassLanguageSwitch.EN}
    __VIDEO_TO_SOUND = {R.videos.battle_pass.before_voting(): BattlePassSounds.VIDEO_BEFORE_VOTING,
     R.videos.battle_pass.c_2417_0(): BattlePassSounds.VIDEO_OPT1_FREE,
     R.videos.battle_pass.c_2417_1(): BattlePassSounds.VIDEO_OPT1_PAID,
     R.videos.battle_pass.c_14113_0(): BattlePassSounds.VIDEO_OPT2_FREE,
     R.videos.battle_pass.c_14113_1(): BattlePassSounds.VIDEO_OPT2_PAID}

    def __init__(self, videoID):
        self.__videoID = videoID

    def start(self):
        sound = self.__VIDEO_TO_SOUND.get(self.__videoID)
        if sound:
            WWISE.WW_setSwitch(BattlePassLanguageSwitch.GROUP_NAME, self.__selectLanguageState())
            WWISE.WW_eventGlobal(sound)

    def stop(self):
        WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_STOP)

    def pause(self):
        WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_PAUSE)

    def unpause(self):
        WWISE.WW_eventGlobal(BattlePassSounds.VIDEO_RESUME)

    def __selectLanguageState(self):
        language = getClientLanguage()
        if language not in self.__LANGUAGE_STATES:
            language = DEFAULT_LANGUAGE
        if language not in self.__LANGUAGE_STATES:
            language = 'en'
        return self.__LANGUAGE_STATES[language]
