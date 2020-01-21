# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/lobby/loot_box/loot_box_helper.py
import logging
import BigWorld
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from optional_bonuses import BONUS_MERGERS
_logger = logging.getLogger(__name__)

def getMergedLootBoxBonuses(bonusesList):
    result = {}
    for bonuses in bonusesList:
        for bonusName, bonusValue in bonuses.iteritems():
            if bonusName in BONUS_MERGERS:
                BONUS_MERGERS[bonusName](result, bonusName, bonusValue, False, 1, None)
            _logger.warning('BONUS_MERGERS has not bonus %s', bonusName)

    return result


def showRestrictedSysMessage():

    def _showRestrictedSysMessage():
        SystemMessages.pushMessage(text=backport.text(R.strings.lootboxes.restrictedMessage.body()), type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH, messageData={'header': backport.text(R.strings.lootboxes.restrictedMessage.header())})

    BigWorld.callback(0.0, _showRestrictedSysMessage)
