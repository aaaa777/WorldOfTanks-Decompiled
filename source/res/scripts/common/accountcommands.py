# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/AccountCommands.py
from streamIDs import STREAM_ID_ACCOUNT_CMDS_MIN, STREAM_ID_ACCOUNT_CMDS_MAX
RES_FAILURE = -1
RES_WRONG_ARGS = -2
RES_NON_PLAYER = -3
RES_SHOP_DESYNC = -4
RES_COOLDOWN = -5
RES_HIDDEN_DOSSIER = -6
RES_CENTER_DISCONNECTED = -7
RES_TUTORIAL_DISABLED = -8
RES_NOT_AVAILABLE = -10
RES_BOOTCAMP_DISABLED = -11
RES_BOOTCAMP_ALREADY_RUNNING = -12
RES_DISABLED = -13
RES_SUCCESS = 0
RES_STREAM = 1
RES_CACHE = 2

def isCodeValid(code):
    return code >= 0


CMD_RESERVED = 0
CMD_SYNC_DATA = 100
CMD_EQUIP = 101
CMD_EQUIP_OPTDEV = 102
CMD_EQUIP_SHELLS = 103
CMD_EQUIP_EQS = 104
CMD_EQUIP_TMAN = 105
CMD_REPAIR = 106
CMD_VEH_SETTINGS = 107
CMD_SET_AND_FILL_LAYOUTS = 108
CMD_VEH_APPLY_STYLE = 116
CMD_SELL_C11N_ITEMS = 117
CMD_BUY_C11N_ITEMS = 118
CMD_VEH_APPLY_OUTFIT = 119
CMD_RESET_C11N_ITEMS_NOVELTY = 120
CMD_SELECT_POTAPOV_QUESTS = 124
CMD_GET_POTAPOV_QUEST_REWARD = 125
CMD_BUY_POTAPOV_QUEST_TILE = 126
CMD_BUY_POTAPOV_QUEST_SLOT = 127
CMD_RESET_POTAPOV_QUESTS = 128
CMD_PAUSE_POTAPOV_QUESTS = 129
CMD_TMAN_ADD_SKILL = 151
CMD_TMAN_DROP_SKILLS = 152
CMD_TMAN_RESPEC = 153
CMD_TMAN_PASSPORT = 154
CMD_TRAINING_TMAN = 155
CMD_TMAN_MULTI_RESPEC = 156
CMD_RETURN_CREW = 157
CMD_TMAN_CHANGE_ROLE = 158
CMD_TMAN_RECRUIT = 159
CMD_TMAN_EQUIP_CREW_SKIN = 160
CMD_TMAN_UNEQUIP_CREW_SKIN = 161
CMD_LEARN_CREW_BOOK = 162
CMD_UNLOCK = 201
CMD_EXCHANGE = 202
CMD_FREE_XP_CONV = 203
CMD_PREMIUM = 204
CMD_BUY_SLOT = 205
CMD_BUY_BERTHS = 206
CMD_VEHICLE_CHANGE_NATION = 207
CMD_SYNC_SHOP = 300
CMD_BUY_VEHICLE = 301
CMD_BUY_ITEM = 302
CMD_BUY_TMAN = 303
CMD_SELL_VEHICLE = 304
CMD_SELL_ITEM = 305
CMD_DISMISS_TMAN = 306
CMD_VERIFY_FIN_PSWD = 307
CMD_BUY_AND_EQUIP_ITEM = 308
CMD_BUY_AND_EQUIP_TMAN = 309
CMD_SELL_MULTIPLE_ITEMS = 310
CMD_PRB_JOIN = 400
CMD_PRB_LEAVE = 401
CMD_PRB_READY = 402
CMD_PRB_NOT_READY = 403
CMD_PRB_ASSIGN = 404
CMD_PRB_SWAP_TEAM = 405
CMD_PRB_CH_ARENA = 406
CMD_PRB_CH_ROUND = 407
CMD_PRB_OPEN = 408
CMD_PRB_CH_COMMENT = 409
CMD_PRB_CH_ARENAVOIP = 410
CMD_PRB_TEAM_READY = 411
CMD_PRB_TEAM_NOT_READY = 412
CMD_PRB_KICK = 414
CMD_PRB_CH_GAMEPLAYSMASK = 416
CMD_PRB_ACCEPT_INVITE = 417
CMD_PRB_DECLINE_INVITE = 418
CMD_PRB_SWAP_TEAMS_WITHIN_GROUP = 419
CMD_PRB_SWAP_GROUPS_WITHIN_TEAM = 420
CMD_REQ_SERVER_STATS = 501
CMD_REQ_QUEUE_INFO = 502
CMD_REQ_PLAYER_INFO = 503
CMD_REQ_ACCOUNT_DOSSIER = 504
CMD_REQ_VEHICLE_DOSSIER = 505
CMD_REQ_PLAYER_CLAN_INFO = 506
CMD_REQ_PLAYER_GLOBAL_RATING = 507
CMD_REQ_PLAYERS_GLOBAL_RATING = 508
CMD_REQ_PREBATTLES = 520
CMD_REQ_PREBATTLES_BY_CREATOR = 521
CMD_REQ_PREBATTLE_ROSTER = 523
CMD_SYNC_DOSSIERS = 600
CMD_ENQUEUE_RANDOM = 700
CMD_DEQUEUE_RANDOM = 701
CMD_ENQUEUE_TUTORIAL = 702
CMD_DEQUEUE_TUTORIAL = 703
CMD_ENQUEUE_UNIT_ASSEMBLER = 704
CMD_DEQUEUE_UNIT_ASSEMBLER = 705
CMD_ENQUEUE_EVENT_BATTLES = 708
CMD_DEQUEUE_EVENT_BATTLES = 709
CMD_ENQUEUE_SANDBOX = 710
CMD_DEQUEUE_SANDBOX = 711
CMD_ENQUEUE_FALLOUT_CLASSIC = 712
CMD_DEQUEUE_FALLOUT_CLASSIC = 713
CMD_ENQUEUE_FALLOUT_MULTITEAM = 714
CMD_DEQUEUE_FALLOUT_MULTITEAM = 715
CMD_ENQUEUE_RANKED_BATTLES = 716
CMD_DEQUEUE_RANKED_BATTLES = 717
CMD_ENQUEUE_BOOTCAMP = 718
CMD_DEQUEUE_BOOTCAMP = 719
CMD_REQUEST_BOOTCAMP_QUIT = 720
CMD_REQUEST_BOOTCAMP_START = 721
CMD_GAMEPLAY_CHOICE = 722
CMD_SELECT_BADGES = 800
CMD_SET_CLIENT_RANK = 801
CMD_SET_CLIENT_MAX_RANK = 803
CMD_SET_CLIENT_SHIELDS = 804
CMD_ENQUEUE_EPIC = 900
CMD_DEQUEUE_EPIC = 901
CMD_FORCE_EPIC_DEV_START = 903
CMD_UPDATE_SELECTED_EPIC_META_ABILITY = 905
CMD_INCREASE_EPIC_META_ABILITY = 906
CMD_RESET_EPIC_META_GAME = 907
CMD_TRIGGER_EPIC_META_GAME_PRESTIGE = 908
CMD_CLAIM_EPIC_META_MAX_PRESTIGE_REWARD = 909
CMD_GET_FREE_EPIC_DISCOUNT = 910
CMD_SET_LANGUAGE = 1000
CMD_MAKE_DENUNCIATION = 1100
CMD_COMPLETE_TUTORIAL = 1150
CMD_BAN_UNBAN_USER = 1400
CMD_REQ_BATTLE_RESULTS = 1500
CMD_BATTLE_RESULTS_RECEIVED = 1501
CMD_ADD_INT_USER_SETTINGS = 1600
CMD_DEL_INT_USER_SETTINGS = 1601
CMD_GET_AVATAR_SYNC = 1602
CMD_LOG_CLIENT_UX_EVENTS = 1603
CMD_LOG_CLIENT_XMPP_EVENTS = 1604
CMD_UPDATE_USER_RELATIONS = 1605
CMD_NOTIFICATION_REPLY = 1800
CMD_SET_DOSSIER_FIELD = 2000
CMD_SET_MONEY = 10001
CMD_ADD_XP = 10002
CMD_ADD_TMAN_XP = 10003
CMD_UNLOCK_ALL = 10004
CMD_SET_RANKED_INFO = 10005
CMD_RESET_INVENTORY_LOCKS = 10006
CMD_FORCE_QUEUE = 10008
CMD_INVITATION_ACCEPT = 10010
CMD_INVITATION_DECLINE = 10011
CMD_INVITATION_SEND = 10012
CMD_ACTIVATE_GOODIE = 10013
CMD_BUY_GOODIE = 10014
CMD_TMAN_RESTORE = 10015
CMD_VEHICLE_TRADE_IN = 10016
CMD_QUERY_BALANCE_INFO = 10017
CMD_RUN_QUEST = 10018
CMD_PAWN_FREE_AWARD_LIST = 10019
CMD_ADD_FREE_AWARD_LISTS = 10020
CMD_DRAW_FREE_AWARD_LISTS = 10021
CMD_COMPLETE_PERSONAL_MISSION = 10022
CMD_GET_TANKMAN_GIFT = 10023
CMD_UNLOCK_LINKED_SET_MISSION = 10024
CMD_LOCK_LINKED_SET_MISSION = 10025
CMD_CHOOSE_QUEST_REWARD = 10026
CMD_PROCESS_RECEIPT_LIST = 10027
CMD_LOOTBOX_OPEN = 10028
CMD_LOOTBOX_GETINFO = 10029
CMD_BPF_CONVERT_FRAGMENTS = 1024
CMD_BPF_ADD_FRAGMENTS_DEV = 1025
CMD_BPF_MARK_FRAGMENTS_SEEN = 1026
CMD_BPF_STAMP = 1027
CMD_BUY_FL_REWARD_VEH = 10030
CMD_TMAN_ADD_CREW_SKIN = 10031
CMD_APPLY_ADDITIONAL_XP = 10032
CMD_SET_MAPS_BLACK_LIST = 10033
CMD_SET_PREMIUM = 10034
CMD_RESET_SESSION_STAT = 10035
CMD_ADD_CREW_BOOK = 10036
CMD_GET_SINGLE_TOKEN = 10037
CMD_SET_ANONYMIZER_STATE = 10038
CMD_SET_BATTLE_NAMES = 10039
CMD_FLUSH_ARENA_RELATIONS = 10040
CMD_EQUIP_ENHANCEMENT = 10041
PLAYER_CMD_NAMES = dict([ (v, k) for k, v in globals().items() if k.startswith('CMD_') ])

class LOCK_REASON:
    NONE = 0
    ON_ARENA = 1
    IN_QUEUE = 2
    PREBATTLE = 4
    UNIT = 8
    BREAKER = 16
    ANY_MASK = 255


LOCK_REASON_NAMES = dict([ (v, k) for k, v in LOCK_REASON.__dict__.items() if not k.startswith('__') ])

class BUY_VEHICLE_FLAG:
    NONE = 0
    CREW = 1
    SHELLS = 16


class VEHICLE_SETTINGS_FLAG:
    NONE = 0
    XP_TO_TMAN = 1
    AUTO_REPAIR = 2
    AUTO_LOAD = 4
    AUTO_EQUIP = 8
    GROUP_0 = 16
    ORIGINAL_CREW = 32
    NO_BATTLE = 64
    AUTO_EQUIP_BOOSTER = 128
    AUTO_RENT_CUSTOMIZATION = 256


class VEHICLE_EXTRA_SETTING_FLAG:
    NONE = 0
    NOT_ACTIVE_IN_NATION_GROUP = 1
    WIPE_MASK = NOT_ACTIVE_IN_NATION_GROUP


REQUEST_ID_PREBATTLES = STREAM_ID_ACCOUNT_CMDS_MIN
REQUEST_ID_PREBATTLE_ROSTER = STREAM_ID_ACCOUNT_CMDS_MIN + 1
REQUEST_ID_NO_RESPONSE = STREAM_ID_ACCOUNT_CMDS_MIN + 2
REQUEST_ID_NON_CLIENT = STREAM_ID_ACCOUNT_CMDS_MIN + 3
REQUEST_ID_UNRESERVED_MIN = STREAM_ID_ACCOUNT_CMDS_MIN + 20
REQUEST_ID_UNRESERVED_MAX = STREAM_ID_ACCOUNT_CMDS_MAX
