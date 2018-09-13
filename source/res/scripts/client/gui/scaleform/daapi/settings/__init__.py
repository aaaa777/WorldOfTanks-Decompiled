# Embedded file name: scripts/client/gui/Scaleform/daapi/settings/__init__.py
from constants import IS_DEVELOPMENT
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.dialogs.FreeXPInfoWindow import FreeXPInfoWindow
from gui.Scaleform.daapi.view.dialogs.DismissTankmanDialog import DismissTankmanDialog
from gui.Scaleform.daapi.view.dialogs.IconPriceDialog import IconPriceDialog
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog
from gui.Scaleform.daapi.view.dialogs.DemountDeviceDialog import DemountDeviceDialog
from gui.Scaleform.daapi.view.lobby.VehicleInfoWindow import VehicleInfoWindow
from gui.Scaleform.daapi.view.lobby.VehicleSellDialog import VehicleSellDialog
from gui.Scaleform.daapi.view.lobby.PremiumForm import PremiumForm
from gui.Scaleform.daapi.view.lobby.PersonalCase import PersonalCase
from gui.Scaleform.daapi.view.lobby.eliteWindow.EliteWindow import EliteWindow
from gui.Scaleform.daapi.view.lobby.hangar.TmenXpPanel import TmenXpPanel
from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
from gui.Scaleform.daapi.view.lobby.header.QuestsControl import QuestsControl
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryPage import ProfileSummaryPage
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow import ProfileSummaryWindow
from gui.Scaleform.daapi.view.lobby.crewOperations.CrewOperationsPopOver import CrewOperationsPopOver
from gui.Scaleform.daapi.view.lobby.crewOperations.RetrainCrewWindow import RetrainCrewWindow
from gui.Scaleform.daapi.view.lobby.server_events import QuestsCurrentTab, QuestsFutureTab, EventsWindow
from gui.Scaleform.daapi.view.login.EULA import EULADlg
from gui.Scaleform.daapi.view.login.LegalInfoWindow import LegalInfoWindow
from gui.Scaleform.daapi.view.BattleLoading import BattleLoading
from gui.Scaleform.daapi.view.login.LoginCreateAnAccountWindow import LoginCreateAnAccountWindow
from gui.Scaleform.daapi.view.login.RssNewsFeed import RssNewsFeed
from gui.Scaleform.framework.WaitingView import WaitingView
from gui.Scaleform.managers.Cursor import Cursor
from gui.Scaleform.daapi.view.BattleResultsWindow import BattleResultsWindow
from gui.Scaleform.daapi.view.IntroPage import IntroPage
from gui.Scaleform.daapi.view.dialogs.CaptchaDialog import CaptchaDialog
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleDialog import ConfirmModuleDialog
from gui.Scaleform.daapi.view.lobby.ModuleInfoWindow import ModuleInfoWindow
from gui.Scaleform.daapi.view.lobby.LobbyMenu import LobbyMenu
from gui.Scaleform.daapi.view.lobby.BrowserWindow import BrowserWindow
from gui.Scaleform.daapi.view.lobby.DemonstratorWindow import DemonstratorWindow
from gui.Scaleform.daapi.view.lobby.exchange.ExchangeWindow import ExchangeWindow
from gui.Scaleform.daapi.view.lobby.exchange.ExchangeXPWindow import ExchangeXPWindow
from gui.Scaleform.daapi.view.dialogs.SystemMessageDialog import SystemMessageDialog
from gui.Scaleform.daapi.view.lobby.LobbyView import LobbyView
from gui.Scaleform.daapi.view.lobby.barracks.Barracks import Barracks
from gui.Scaleform.daapi.view.lobby.header.TutorialControl import TutorialControl
from gui.Scaleform.daapi.view.lobby.header.Ticker import Ticker
from gui.Scaleform.daapi.view.lobby.header.FightButton import FightButton
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
from gui.Scaleform.daapi.view.lobby.messengerBar import MessengerBar, ChannelCarousel, NotificationListButton
from gui.Scaleform.daapi.view.lobby.profile import ProfilePage, ProfileAwards, ProfileStatistics, ProfileTabNavigator, ProfileWindow, ProfileTechniqueWindow, ProfileTechniquePage
from gui.Scaleform.daapi.view.lobby.recruitWindow.RecruitWindow import RecruitWindow
from gui.Scaleform.daapi.view.lobby.settings import SettingsWindow
from gui.Scaleform.daapi.view.lobby.MinimapLobby import MinimapLobby
from gui.Scaleform.daapi.view.lobby.BattleQueue import BattleQueue
from gui.Scaleform.daapi.view.lobby.trainings import Trainings, TrainingSettingsWindow, TrainingRoom
from gui.Scaleform.daapi.view.lobby.customization.VehicleCustomization import VehicleCustomization
from gui.Scaleform.daapi.view.lobby.exchange.ExchangeFreeToTankmanXpWindow import ExchangeFreeToTankmanXpWindow
from gui.Scaleform.daapi.view.lobby.exchange.ExchangeVcoinWindow import ExchangeVcoinWindow
from gui.Scaleform.daapi.view.lobby.SkillDropWindow import SkillDropWindow
from gui.Scaleform.daapi.view.lobby.VehicleBuyWindow import VehicleBuyWindow
from gui.Scaleform.daapi.view.lobby.hangar import TechnicalMaintenance, TankCarousel, ResearchPanel, AmmunitionPanel, Crew, Params, Hangar
from gui.Scaleform.daapi.view.lobby.store.StoreTable import StoreTable
from gui.Scaleform.daapi.view.lobby.store.Inventory import Inventory
from gui.Scaleform.daapi.view.lobby.store.Shop import Shop
from gui.Scaleform.daapi.view.login import LoginView
from gui.Scaleform.daapi.view.login.LoginQueue import LoginQueue
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ViewTypes, ScopeTemplates
from gui.shared.events import LoadEvent, ShowPopoverEvent
from notification.NotificationListView import NotificationListView
from notification.NotificationPopUpViewer import NotificationPopUpViewer
VIEWS_SETTINGS = (ViewSettings(VIEW_ALIAS.LOGIN, LoginView, 'login.swf', ViewTypes.DEFAULT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.INTRO_VIDEO, IntroPage, 'introPage.swf', ViewTypes.DEFAULT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.CURSOR, Cursor, 'cursor.swf', ViewTypes.CURSOR, None, ScopeTemplates.GLOBAL_SCOPE),
 ViewSettings(VIEW_ALIAS.WAITING, WaitingView, 'waiting.swf', ViewTypes.WAITING, None, ScopeTemplates.GLOBAL_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY, LobbyView, 'lobby.swf', ViewTypes.DEFAULT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_HANGAR, Hangar, 'hangar.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_HANGAR, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_SHOP, Shop, 'shop.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_SHOP, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_INVENTORY, Inventory, 'inventory.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_INVENTORY, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_PROFILE, ProfilePage, 'profile.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_PROFILE, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_BARRACKS, Barracks, 'barracks.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_BARRACKS, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_CUSTOMIZATION, VehicleCustomization, 'vehicleCustomization.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_CUSTOMIZATION, ScopeTemplates.LOBBY_SUB_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_TRAININGS, Trainings, 'trainingForm.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_TRAININGS, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_TRAINING_ROOM, TrainingRoom, 'trainingRoom.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_TRAINING_ROOM, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.BATTLE_QUEUE, BattleQueue, 'battleQueue.swf', ViewTypes.LOBBY_SUB, LoadEvent.LOAD_BATTLE_QUEUE, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.BATTLE_LOADING, BattleLoading, 'battleLoading.swf', ViewTypes.DEFAULT, LoadEvent.LOAD_BATTLE_LOADING, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.TUTORIAL_LOADING, BattleLoading, 'tutorialLoading.swf', ViewTypes.DEFAULT, LoadEvent.LOAD_TUTORIAL_LOADING, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.FREE_X_P_INFO_WINDOW, FreeXPInfoWindow, 'freeXPInfoWindow.swf', ViewTypes.TOP_WINDOW, 'freeXPInfoWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.RECRUIT_WINDOW, RecruitWindow, 'recruitWindow.swf', ViewTypes.WINDOW, 'recruitWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.ELITE_WINDOW, EliteWindow, 'eliteWindow.swf', ViewTypes.WINDOW, 'eliteWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EXCHANGE_WINDOW, ExchangeWindow, 'exchangeWindow.swf', ViewTypes.WINDOW, 'exchangeWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.PROFILE_WINDOW, ProfileWindow, 'profileWindow.swf', ViewTypes.WINDOW, 'profileWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EXCHANGE_VCOIN_WINDOW, ExchangeVcoinWindow, 'exchangeVcoinWindow.swf', ViewTypes.WINDOW, 'exchangeVcoinWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EXCHANGE_XP_WINDOW, ExchangeXPWindow, 'exchangeXPWindow.swf', ViewTypes.WINDOW, 'exchangeXPWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EXCHANGE_FREE_TO_TANKMAN_XP_WINDOW, ExchangeFreeToTankmanXpWindow, 'exchangeFreeToTankmanXpWindow.swf', ViewTypes.WINDOW, 'exchangeFreeToTankmanXpWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.VEHICLE_BUY_WINDOW, VehicleBuyWindow, 'vehicleBuyWindow.swf', ViewTypes.TOP_WINDOW, 'vehicleBuyWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.CONFIRM_MODULE_DIALOG, ConfirmModuleDialog, 'confirmModuleWindow.swf', ViewTypes.TOP_WINDOW, 'confirmModuleDialog', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.SYSTEM_MESSAGE_DIALOG, SystemMessageDialog, 'systemMessageDialog.swf', ViewTypes.WINDOW, 'systemMessageDialog', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.RETRAIN_CREW, RetrainCrewWindow, 'retrainCrewWindow.swf', ViewTypes.TOP_WINDOW, 'retrainCrewWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.NOTIFICATIONS_LIST, NotificationListView, 'notificationsList.swf', ViewTypes.WINDOW, 'notificationsList', ShowPopoverEvent.SHOW_NOTIFICATIONS_LIST_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE),
 GroupedViewSettings(VIEW_ALIAS.CREW_OPERATIONS_POPOVER, CrewOperationsPopOver, 'crewOperationsPopOver.swf', ViewTypes.WINDOW, 'crewOperationsPopOver', ShowPopoverEvent.SHOW_CREW_OPERATIONS_POPOVER, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE),
 GroupedViewSettings(VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, BattleTypeSelectPopover, 'battleTypeSelectPopover.swf', ViewTypes.WINDOW, 'battleTypeSelectPopover', ShowPopoverEvent.SHOW_BATTLE_TYPE_SELECT_POPOVER_EVENT, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.VEHICLE_INFO_WINDOW, VehicleInfoWindow, 'vehicleInfo.swf', ViewTypes.WINDOW, 'vehicleInfoWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.LEGAL_INFO_WINDOW, LegalInfoWindow, 'legalInfoWindow.swf', ViewTypes.WINDOW, 'legalInfoWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.MODULE_INFO_WINDOW, ModuleInfoWindow, 'moduleInfo.swf', ViewTypes.WINDOW, 'moduleInfoWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.SETTINGS_WINDOW, SettingsWindow, 'settingsWindow.swf', ViewTypes.TOP_WINDOW, 'settingsWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.VEHICLE_SELL_DIALOG, VehicleSellDialog, 'vehicleSellDialog.swf', ViewTypes.TOP_WINDOW, 'vehicleSellWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.PERSONAL_CASE, PersonalCase, 'personalCase.swf', ViewTypes.WINDOW, 'personalCaseWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.TECHNICAL_MAINTENANCE, TechnicalMaintenance, 'technicalMaintenance.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.BATTLE_RESULTS, BattleResultsWindow, 'battleResults.swf', ViewTypes.WINDOW, 'BattleResultsWindow', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EVENTS_WINDOW, EventsWindow, 'questsWindow.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.TANKMAN_SKILLS_DROP_WINDOW, SkillDropWindow, 'skillDropWindow.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.TRAINING_SETTINGS_WINDOW, TrainingSettingsWindow, 'trainingWindow.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.DEMONSTRATOR_WINDOW, DemonstratorWindow, 'demonstratorWindow.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.BROWSER_WINDOW, BrowserWindow, 'browser.swf', ViewTypes.BROWSER, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EULA, EULADlg, 'EULADlg.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.EULA_FULL, EULADlg, 'EULAFullDlg.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.LOGIN_QUEUE, LoginQueue, 'LoginQueueWindow.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.LOGIN_CREATE_AN_ACC, LoginCreateAnAccountWindow, 'loginCreateAnAccount.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.SIMPLE_DIALOG, SimpleDialog, 'simpleDialog.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.DISMISS_TANKMAN_DIALOG, DismissTankmanDialog, 'dismissTankmanDialog.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.ICON_DIALOG, IconDialog, 'iconDialog.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.ICON_PRICE_DIALOG, IconPriceDialog, 'iconPriceDialog.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.DESTROY_DEVICE_DIALOG, IconDialog, 'destroyDeviceDialog.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.DEMOUNT_DEVICE_DIALOG, DemountDeviceDialog, 'demountDeviceDialog.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DYNAMIC_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.CAPTCHA_DIALOG, CaptchaDialog, 'CAPTCHA.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.LOBBY_MENU, LobbyMenu, 'lobbyMenu.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.LOBBY_SUB_SCOPE),
 GroupedViewSettings(VIEW_ALIAS.PREMIUM_DIALOG, PremiumForm, 'premiumForm.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.SHOP_TABLE, StoreTable, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.LOBBY_HEADER, LobbyHeader, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_TAB_NAVIGATOR, ProfileTabNavigator, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_SUMMARY_WINDOW, ProfileSummaryWindow, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_SUMMARY_PAGE, ProfileSummaryPage, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_AWARDS, ProfileAwards, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_STATISTICS, ProfileStatistics, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE, ProfileTechniquePage, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.PROFILE_TECHNIQUE_WINDOW, ProfileTechniqueWindow, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.SYSTEM_MESSAGES, NotificationPopUpViewer, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.MESSENGER_BAR, MessengerBar, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.NOTIFICATION_LIST_BUTTON, NotificationListButton, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.CHANNEL_CAROUSEL, ChannelCarousel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.CAROUSEL, TankCarousel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.AMMO_PANEL, AmmunitionPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.RSS_NEWS_FEED, RssNewsFeed, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.TMEN_XP_PANEL, TmenXpPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.PARAMS, Params, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.CREW, Crew, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(Hangar.COMPONENTS.RESEARCH_PANEL, ResearchPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.MINIMAP_LOBBY, MinimapLobby, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.TUTORIAL_CONTROL, TutorialControl, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.QUESTS_CONTROL, QuestsControl, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.FIGHT_BUTTON, FightButton, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.TICKER, Ticker, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.EVENTS_CURRENT_TAB, QuestsCurrentTab, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
 ViewSettings(VIEW_ALIAS.EVENTS_FUTURE_TAB, QuestsFutureTab, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))
RELEASE_PACKAGES = ['gui.Scaleform.daapi.view.lobby.prb_windows',
 'gui.Scaleform.daapi.view.lobby.techtree',
 'messenger.gui.Scaleform',
 'gui.Scaleform.daapi.view.lobby.cyberSport',
 'gui.Scaleform.daapi.view.lobby.historicalBattles',
 'gui.Scaleform.daapi.view.lobby.fortifications',
 'gui.Scaleform.daapi.view.lobby.inputChecker']
DEBUG_PACKAGES = ['gui.development.ui.GUIEditor']
if IS_DEVELOPMENT:
    VIEWS_PACKAGES = tuple(RELEASE_PACKAGES + DEBUG_PACKAGES)
else:
    VIEWS_PACKAGES = tuple(RELEASE_PACKAGES)
