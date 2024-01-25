# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #

from .functions import *
from .types import *

if typing.TYPE_CHECKING:
    from aiotdlib.client import Client


class API:
    """
    This class contains all TDJson API methods
    """

    class Types:
        # Types and Functions
        ANY = "*"

        ACCEPT_CALL = "acceptCall"
        ACCEPT_TERMS_OF_SERVICE = "acceptTermsOfService"
        ACCOUNT_TTL = "accountTtl"
        ACTIVATE_STORY_STEALTH_MODE = "activateStoryStealthMode"
        ADD_APPLICATION_CHANGELOG = "addApplicationChangelog"
        ADD_CHAT_FOLDER_BY_INVITE_LINK = "addChatFolderByInviteLink"
        ADD_CHAT_MEMBER = "addChatMember"
        ADD_CHAT_MEMBERS = "addChatMembers"
        ADD_CHAT_TO_LIST = "addChatToList"
        ADD_CONTACT = "addContact"
        ADD_CUSTOM_SERVER_LANGUAGE_PACK = "addCustomServerLanguagePack"
        ADD_FAVORITE_STICKER = "addFavoriteSticker"
        ADD_FILE_TO_DOWNLOADS = "addFileToDownloads"
        ADD_LOCAL_MESSAGE = "addLocalMessage"
        ADD_LOG_MESSAGE = "addLogMessage"
        ADD_MESSAGE_REACTION = "addMessageReaction"
        ADD_NETWORK_STATISTICS = "addNetworkStatistics"
        ADD_PROXY = "addProxy"
        ADD_RECENT_STICKER = "addRecentSticker"
        ADD_RECENTLY_FOUND_CHAT = "addRecentlyFoundChat"
        ADD_SAVED_ANIMATION = "addSavedAnimation"
        ADD_SAVED_NOTIFICATION_SOUND = "addSavedNotificationSound"
        ADD_STICKER_TO_SET = "addStickerToSet"
        ADDED_REACTION = "addedReaction"
        ADDED_REACTIONS = "addedReactions"
        ADDRESS = "address"
        ALLOW_BOT_TO_SEND_MESSAGES = "allowBotToSendMessages"
        ANIMATED_CHAT_PHOTO = "animatedChatPhoto"
        ANIMATED_EMOJI = "animatedEmoji"
        ANIMATION = "animation"
        ANIMATIONS = "animations"
        ANSWER_CALLBACK_QUERY = "answerCallbackQuery"
        ANSWER_CUSTOM_QUERY = "answerCustomQuery"
        ANSWER_INLINE_QUERY = "answerInlineQuery"
        ANSWER_PRE_CHECKOUT_QUERY = "answerPreCheckoutQuery"
        ANSWER_SHIPPING_QUERY = "answerShippingQuery"
        ANSWER_WEB_APP_QUERY = "answerWebAppQuery"
        ARCHIVE_CHAT_LIST_SETTINGS = "archiveChatListSettings"
        ASSIGN_APP_STORE_TRANSACTION = "assignAppStoreTransaction"
        ASSIGN_GOOGLE_PLAY_TRANSACTION = "assignGooglePlayTransaction"
        ATTACHMENT_MENU_BOT = "attachmentMenuBot"
        ATTACHMENT_MENU_BOT_COLOR = "attachmentMenuBotColor"
        AUDIO = "audio"
        AUTHENTICATION_CODE_INFO = "authenticationCodeInfo"
        AUTHENTICATION_CODE_TYPE = "authenticationCodeType"
        AUTHENTICATION_CODE_TYPE_CALL = "authenticationCodeTypeCall"
        AUTHENTICATION_CODE_TYPE_FIREBASE_ANDROID = "authenticationCodeTypeFirebaseAndroid"
        AUTHENTICATION_CODE_TYPE_FIREBASE_IOS = "authenticationCodeTypeFirebaseIos"
        AUTHENTICATION_CODE_TYPE_FLASH_CALL = "authenticationCodeTypeFlashCall"
        AUTHENTICATION_CODE_TYPE_FRAGMENT = "authenticationCodeTypeFragment"
        AUTHENTICATION_CODE_TYPE_MISSED_CALL = "authenticationCodeTypeMissedCall"
        AUTHENTICATION_CODE_TYPE_SMS = "authenticationCodeTypeSms"
        AUTHENTICATION_CODE_TYPE_TELEGRAM_MESSAGE = "authenticationCodeTypeTelegramMessage"
        AUTHORIZATION_STATE = "authorizationState"
        AUTHORIZATION_STATE_CLOSED = "authorizationStateClosed"
        AUTHORIZATION_STATE_CLOSING = "authorizationStateClosing"
        AUTHORIZATION_STATE_LOGGING_OUT = "authorizationStateLoggingOut"
        AUTHORIZATION_STATE_READY = "authorizationStateReady"
        AUTHORIZATION_STATE_WAIT_CODE = "authorizationStateWaitCode"
        AUTHORIZATION_STATE_WAIT_EMAIL_ADDRESS = "authorizationStateWaitEmailAddress"
        AUTHORIZATION_STATE_WAIT_EMAIL_CODE = "authorizationStateWaitEmailCode"
        AUTHORIZATION_STATE_WAIT_OTHER_DEVICE_CONFIRMATION = "authorizationStateWaitOtherDeviceConfirmation"
        AUTHORIZATION_STATE_WAIT_PASSWORD = "authorizationStateWaitPassword"
        AUTHORIZATION_STATE_WAIT_PHONE_NUMBER = "authorizationStateWaitPhoneNumber"
        AUTHORIZATION_STATE_WAIT_REGISTRATION = "authorizationStateWaitRegistration"
        AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS = "authorizationStateWaitTdlibParameters"
        AUTO_DOWNLOAD_SETTINGS = "autoDownloadSettings"
        AUTO_DOWNLOAD_SETTINGS_PRESETS = "autoDownloadSettingsPresets"
        AUTOSAVE_SETTINGS = "autosaveSettings"
        AUTOSAVE_SETTINGS_EXCEPTION = "autosaveSettingsException"
        AUTOSAVE_SETTINGS_SCOPE = "autosaveSettingsScope"
        AUTOSAVE_SETTINGS_SCOPE_CHANNEL_CHATS = "autosaveSettingsScopeChannelChats"
        AUTOSAVE_SETTINGS_SCOPE_CHAT = "autosaveSettingsScopeChat"
        AUTOSAVE_SETTINGS_SCOPE_GROUP_CHATS = "autosaveSettingsScopeGroupChats"
        AUTOSAVE_SETTINGS_SCOPE_PRIVATE_CHATS = "autosaveSettingsScopePrivateChats"
        AVAILABLE_REACTION = "availableReaction"
        AVAILABLE_REACTIONS = "availableReactions"
        BACKGROUND = "background"
        BACKGROUND_FILL = "backgroundFill"
        BACKGROUND_FILL_FREEFORM_GRADIENT = "backgroundFillFreeformGradient"
        BACKGROUND_FILL_GRADIENT = "backgroundFillGradient"
        BACKGROUND_FILL_SOLID = "backgroundFillSolid"
        BACKGROUND_TYPE = "backgroundType"
        BACKGROUND_TYPE_FILL = "backgroundTypeFill"
        BACKGROUND_TYPE_PATTERN = "backgroundTypePattern"
        BACKGROUND_TYPE_WALLPAPER = "backgroundTypeWallpaper"
        BACKGROUNDS = "backgrounds"
        BAN_CHAT_MEMBER = "banChatMember"
        BANK_CARD_ACTION_OPEN_URL = "bankCardActionOpenUrl"
        BANK_CARD_INFO = "bankCardInfo"
        BASIC_GROUP = "basicGroup"
        BASIC_GROUP_FULL_INFO = "basicGroupFullInfo"
        BLOCK_LIST = "blockList"
        BLOCK_LIST_MAIN = "blockListMain"
        BLOCK_LIST_STORIES = "blockListStories"
        BLOCK_MESSAGE_SENDER_FROM_REPLIES = "blockMessageSenderFromReplies"
        BOT_COMMAND = "botCommand"
        BOT_COMMAND_SCOPE = "botCommandScope"
        BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS = "botCommandScopeAllChatAdministrators"
        BOT_COMMAND_SCOPE_ALL_GROUP_CHATS = "botCommandScopeAllGroupChats"
        BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS = "botCommandScopeAllPrivateChats"
        BOT_COMMAND_SCOPE_CHAT = "botCommandScopeChat"
        BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS = "botCommandScopeChatAdministrators"
        BOT_COMMAND_SCOPE_CHAT_MEMBER = "botCommandScopeChatMember"
        BOT_COMMAND_SCOPE_DEFAULT = "botCommandScopeDefault"
        BOT_COMMANDS = "botCommands"
        BOT_INFO = "botInfo"
        BOT_MENU_BUTTON = "botMenuButton"
        CALL = "call"
        CALL_DISCARD_REASON = "callDiscardReason"
        CALL_DISCARD_REASON_DECLINED = "callDiscardReasonDeclined"
        CALL_DISCARD_REASON_DISCONNECTED = "callDiscardReasonDisconnected"
        CALL_DISCARD_REASON_EMPTY = "callDiscardReasonEmpty"
        CALL_DISCARD_REASON_HUNG_UP = "callDiscardReasonHungUp"
        CALL_DISCARD_REASON_MISSED = "callDiscardReasonMissed"
        CALL_ID = "callId"
        CALL_PROBLEM = "callProblem"
        CALL_PROBLEM_DISTORTED_SPEECH = "callProblemDistortedSpeech"
        CALL_PROBLEM_DISTORTED_VIDEO = "callProblemDistortedVideo"
        CALL_PROBLEM_DROPPED = "callProblemDropped"
        CALL_PROBLEM_ECHO = "callProblemEcho"
        CALL_PROBLEM_INTERRUPTIONS = "callProblemInterruptions"
        CALL_PROBLEM_NOISE = "callProblemNoise"
        CALL_PROBLEM_PIXELATED_VIDEO = "callProblemPixelatedVideo"
        CALL_PROBLEM_SILENT_LOCAL = "callProblemSilentLocal"
        CALL_PROBLEM_SILENT_REMOTE = "callProblemSilentRemote"
        CALL_PROTOCOL = "callProtocol"
        CALL_SERVER = "callServer"
        CALL_SERVER_TYPE = "callServerType"
        CALL_SERVER_TYPE_TELEGRAM_REFLECTOR = "callServerTypeTelegramReflector"
        CALL_SERVER_TYPE_WEBRTC = "callServerTypeWebrtc"
        CALL_STATE = "callState"
        CALL_STATE_DISCARDED = "callStateDiscarded"
        CALL_STATE_ERROR = "callStateError"
        CALL_STATE_EXCHANGING_KEYS = "callStateExchangingKeys"
        CALL_STATE_HANGING_UP = "callStateHangingUp"
        CALL_STATE_PENDING = "callStatePending"
        CALL_STATE_READY = "callStateReady"
        CALLBACK_QUERY_ANSWER = "callbackQueryAnswer"
        CALLBACK_QUERY_PAYLOAD = "callbackQueryPayload"
        CALLBACK_QUERY_PAYLOAD_DATA = "callbackQueryPayloadData"
        CALLBACK_QUERY_PAYLOAD_DATA_WITH_PASSWORD = "callbackQueryPayloadDataWithPassword"
        CALLBACK_QUERY_PAYLOAD_GAME = "callbackQueryPayloadGame"
        CAN_BOT_SEND_MESSAGES = "canBotSendMessages"
        CAN_PURCHASE_PREMIUM = "canPurchasePremium"
        CAN_SEND_STORY = "canSendStory"
        CAN_SEND_STORY_RESULT = "canSendStoryResult"
        CAN_SEND_STORY_RESULT_ACTIVE_STORY_LIMIT_EXCEEDED = "canSendStoryResultActiveStoryLimitExceeded"
        CAN_SEND_STORY_RESULT_MONTHLY_LIMIT_EXCEEDED = "canSendStoryResultMonthlyLimitExceeded"
        CAN_SEND_STORY_RESULT_OK = "canSendStoryResultOk"
        CAN_SEND_STORY_RESULT_PREMIUM_NEEDED = "canSendStoryResultPremiumNeeded"
        CAN_SEND_STORY_RESULT_WEEKLY_LIMIT_EXCEEDED = "canSendStoryResultWeeklyLimitExceeded"
        CAN_TRANSFER_OWNERSHIP = "canTransferOwnership"
        CAN_TRANSFER_OWNERSHIP_RESULT = "canTransferOwnershipResult"
        CAN_TRANSFER_OWNERSHIP_RESULT_OK = "canTransferOwnershipResultOk"
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_NEEDED = "canTransferOwnershipResultPasswordNeeded"
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_TOO_FRESH = "canTransferOwnershipResultPasswordTooFresh"
        CAN_TRANSFER_OWNERSHIP_RESULT_SESSION_TOO_FRESH = "canTransferOwnershipResultSessionTooFresh"
        CANCEL_DOWNLOAD_FILE = "cancelDownloadFile"
        CANCEL_PASSWORD_RESET = "cancelPasswordReset"
        CANCEL_PRELIMINARY_UPLOAD_FILE = "cancelPreliminaryUploadFile"
        CHANGE_IMPORTED_CONTACTS = "changeImportedContacts"
        CHANGE_PHONE_NUMBER = "changePhoneNumber"
        CHANGE_STICKER_SET = "changeStickerSet"
        CHAT = "chat"
        CHAT_ACTION = "chatAction"
        CHAT_ACTION_CANCEL = "chatActionCancel"
        CHAT_ACTION_CHOOSING_CONTACT = "chatActionChoosingContact"
        CHAT_ACTION_CHOOSING_LOCATION = "chatActionChoosingLocation"
        CHAT_ACTION_CHOOSING_STICKER = "chatActionChoosingSticker"
        CHAT_ACTION_RECORDING_VIDEO = "chatActionRecordingVideo"
        CHAT_ACTION_RECORDING_VIDEO_NOTE = "chatActionRecordingVideoNote"
        CHAT_ACTION_RECORDING_VOICE_NOTE = "chatActionRecordingVoiceNote"
        CHAT_ACTION_START_PLAYING_GAME = "chatActionStartPlayingGame"
        CHAT_ACTION_TYPING = "chatActionTyping"
        CHAT_ACTION_UPLOADING_DOCUMENT = "chatActionUploadingDocument"
        CHAT_ACTION_UPLOADING_PHOTO = "chatActionUploadingPhoto"
        CHAT_ACTION_UPLOADING_VIDEO = "chatActionUploadingVideo"
        CHAT_ACTION_UPLOADING_VIDEO_NOTE = "chatActionUploadingVideoNote"
        CHAT_ACTION_UPLOADING_VOICE_NOTE = "chatActionUploadingVoiceNote"
        CHAT_ACTION_WATCHING_ANIMATIONS = "chatActionWatchingAnimations"
        CHAT_ACTION_BAR = "chatActionBar"
        CHAT_ACTION_BAR_ADD_CONTACT = "chatActionBarAddContact"
        CHAT_ACTION_BAR_INVITE_MEMBERS = "chatActionBarInviteMembers"
        CHAT_ACTION_BAR_JOIN_REQUEST = "chatActionBarJoinRequest"
        CHAT_ACTION_BAR_REPORT_ADD_BLOCK = "chatActionBarReportAddBlock"
        CHAT_ACTION_BAR_REPORT_SPAM = "chatActionBarReportSpam"
        CHAT_ACTION_BAR_REPORT_UNRELATED_LOCATION = "chatActionBarReportUnrelatedLocation"
        CHAT_ACTION_BAR_SHARE_PHONE_NUMBER = "chatActionBarSharePhoneNumber"
        CHAT_ACTIVE_STORIES = "chatActiveStories"
        CHAT_ADMINISTRATOR = "chatAdministrator"
        CHAT_ADMINISTRATOR_RIGHTS = "chatAdministratorRights"
        CHAT_ADMINISTRATORS = "chatAdministrators"
        CHAT_AVAILABLE_REACTIONS = "chatAvailableReactions"
        CHAT_AVAILABLE_REACTIONS_ALL = "chatAvailableReactionsAll"
        CHAT_AVAILABLE_REACTIONS_SOME = "chatAvailableReactionsSome"
        CHAT_BACKGROUND = "chatBackground"
        CHAT_EVENT = "chatEvent"
        CHAT_EVENT_ACTION = "chatEventAction"
        CHAT_EVENT_ACTIVE_USERNAMES_CHANGED = "chatEventActiveUsernamesChanged"
        CHAT_EVENT_AVAILABLE_REACTIONS_CHANGED = "chatEventAvailableReactionsChanged"
        CHAT_EVENT_DESCRIPTION_CHANGED = "chatEventDescriptionChanged"
        CHAT_EVENT_FORUM_TOPIC_CREATED = "chatEventForumTopicCreated"
        CHAT_EVENT_FORUM_TOPIC_DELETED = "chatEventForumTopicDeleted"
        CHAT_EVENT_FORUM_TOPIC_EDITED = "chatEventForumTopicEdited"
        CHAT_EVENT_FORUM_TOPIC_PINNED = "chatEventForumTopicPinned"
        CHAT_EVENT_FORUM_TOPIC_TOGGLE_IS_CLOSED = "chatEventForumTopicToggleIsClosed"
        CHAT_EVENT_FORUM_TOPIC_TOGGLE_IS_HIDDEN = "chatEventForumTopicToggleIsHidden"
        CHAT_EVENT_HAS_AGGRESSIVE_ANTI_SPAM_ENABLED_TOGGLED = "chatEventHasAggressiveAntiSpamEnabledToggled"
        CHAT_EVENT_HAS_PROTECTED_CONTENT_TOGGLED = "chatEventHasProtectedContentToggled"
        CHAT_EVENT_INVITE_LINK_DELETED = "chatEventInviteLinkDeleted"
        CHAT_EVENT_INVITE_LINK_EDITED = "chatEventInviteLinkEdited"
        CHAT_EVENT_INVITE_LINK_REVOKED = "chatEventInviteLinkRevoked"
        CHAT_EVENT_INVITES_TOGGLED = "chatEventInvitesToggled"
        CHAT_EVENT_IS_ALL_HISTORY_AVAILABLE_TOGGLED = "chatEventIsAllHistoryAvailableToggled"
        CHAT_EVENT_IS_FORUM_TOGGLED = "chatEventIsForumToggled"
        CHAT_EVENT_LINKED_CHAT_CHANGED = "chatEventLinkedChatChanged"
        CHAT_EVENT_LOCATION_CHANGED = "chatEventLocationChanged"
        CHAT_EVENT_MEMBER_INVITED = "chatEventMemberInvited"
        CHAT_EVENT_MEMBER_JOINED = "chatEventMemberJoined"
        CHAT_EVENT_MEMBER_JOINED_BY_INVITE_LINK = "chatEventMemberJoinedByInviteLink"
        CHAT_EVENT_MEMBER_JOINED_BY_REQUEST = "chatEventMemberJoinedByRequest"
        CHAT_EVENT_MEMBER_LEFT = "chatEventMemberLeft"
        CHAT_EVENT_MEMBER_PROMOTED = "chatEventMemberPromoted"
        CHAT_EVENT_MEMBER_RESTRICTED = "chatEventMemberRestricted"
        CHAT_EVENT_MESSAGE_AUTO_DELETE_TIME_CHANGED = "chatEventMessageAutoDeleteTimeChanged"
        CHAT_EVENT_MESSAGE_DELETED = "chatEventMessageDeleted"
        CHAT_EVENT_MESSAGE_EDITED = "chatEventMessageEdited"
        CHAT_EVENT_MESSAGE_PINNED = "chatEventMessagePinned"
        CHAT_EVENT_MESSAGE_UNPINNED = "chatEventMessageUnpinned"
        CHAT_EVENT_PERMISSIONS_CHANGED = "chatEventPermissionsChanged"
        CHAT_EVENT_PHOTO_CHANGED = "chatEventPhotoChanged"
        CHAT_EVENT_POLL_STOPPED = "chatEventPollStopped"
        CHAT_EVENT_SIGN_MESSAGES_TOGGLED = "chatEventSignMessagesToggled"
        CHAT_EVENT_SLOW_MODE_DELAY_CHANGED = "chatEventSlowModeDelayChanged"
        CHAT_EVENT_STICKER_SET_CHANGED = "chatEventStickerSetChanged"
        CHAT_EVENT_TITLE_CHANGED = "chatEventTitleChanged"
        CHAT_EVENT_USERNAME_CHANGED = "chatEventUsernameChanged"
        CHAT_EVENT_VIDEO_CHAT_CREATED = "chatEventVideoChatCreated"
        CHAT_EVENT_VIDEO_CHAT_ENDED = "chatEventVideoChatEnded"
        CHAT_EVENT_VIDEO_CHAT_MUTE_NEW_PARTICIPANTS_TOGGLED = "chatEventVideoChatMuteNewParticipantsToggled"
        CHAT_EVENT_VIDEO_CHAT_PARTICIPANT_IS_MUTED_TOGGLED = "chatEventVideoChatParticipantIsMutedToggled"
        CHAT_EVENT_VIDEO_CHAT_PARTICIPANT_VOLUME_LEVEL_CHANGED = "chatEventVideoChatParticipantVolumeLevelChanged"
        CHAT_EVENT_LOG_FILTERS = "chatEventLogFilters"
        CHAT_EVENTS = "chatEvents"
        CHAT_FOLDER = "chatFolder"
        CHAT_FOLDER_ICON = "chatFolderIcon"
        CHAT_FOLDER_INFO = "chatFolderInfo"
        CHAT_FOLDER_INVITE_LINK = "chatFolderInviteLink"
        CHAT_FOLDER_INVITE_LINK_INFO = "chatFolderInviteLinkInfo"
        CHAT_FOLDER_INVITE_LINKS = "chatFolderInviteLinks"
        CHAT_INVITE_LINK = "chatInviteLink"
        CHAT_INVITE_LINK_COUNT = "chatInviteLinkCount"
        CHAT_INVITE_LINK_COUNTS = "chatInviteLinkCounts"
        CHAT_INVITE_LINK_INFO = "chatInviteLinkInfo"
        CHAT_INVITE_LINK_MEMBER = "chatInviteLinkMember"
        CHAT_INVITE_LINK_MEMBERS = "chatInviteLinkMembers"
        CHAT_INVITE_LINKS = "chatInviteLinks"
        CHAT_JOIN_REQUEST = "chatJoinRequest"
        CHAT_JOIN_REQUESTS = "chatJoinRequests"
        CHAT_JOIN_REQUESTS_INFO = "chatJoinRequestsInfo"
        CHAT_LIST = "chatList"
        CHAT_LIST_ARCHIVE = "chatListArchive"
        CHAT_LIST_FOLDER = "chatListFolder"
        CHAT_LIST_MAIN = "chatListMain"
        CHAT_LISTS = "chatLists"
        CHAT_LOCATION = "chatLocation"
        CHAT_MEMBER = "chatMember"
        CHAT_MEMBER_STATUS = "chatMemberStatus"
        CHAT_MEMBER_STATUS_ADMINISTRATOR = "chatMemberStatusAdministrator"
        CHAT_MEMBER_STATUS_BANNED = "chatMemberStatusBanned"
        CHAT_MEMBER_STATUS_CREATOR = "chatMemberStatusCreator"
        CHAT_MEMBER_STATUS_LEFT = "chatMemberStatusLeft"
        CHAT_MEMBER_STATUS_MEMBER = "chatMemberStatusMember"
        CHAT_MEMBER_STATUS_RESTRICTED = "chatMemberStatusRestricted"
        CHAT_MEMBERS = "chatMembers"
        CHAT_MEMBERS_FILTER = "chatMembersFilter"
        CHAT_MEMBERS_FILTER_ADMINISTRATORS = "chatMembersFilterAdministrators"
        CHAT_MEMBERS_FILTER_BANNED = "chatMembersFilterBanned"
        CHAT_MEMBERS_FILTER_BOTS = "chatMembersFilterBots"
        CHAT_MEMBERS_FILTER_CONTACTS = "chatMembersFilterContacts"
        CHAT_MEMBERS_FILTER_MEMBERS = "chatMembersFilterMembers"
        CHAT_MEMBERS_FILTER_MENTION = "chatMembersFilterMention"
        CHAT_MEMBERS_FILTER_RESTRICTED = "chatMembersFilterRestricted"
        CHAT_MESSAGE_SENDER = "chatMessageSender"
        CHAT_MESSAGE_SENDERS = "chatMessageSenders"
        CHAT_NEARBY = "chatNearby"
        CHAT_NOTIFICATION_SETTINGS = "chatNotificationSettings"
        CHAT_PERMISSIONS = "chatPermissions"
        CHAT_PHOTO = "chatPhoto"
        CHAT_PHOTO_INFO = "chatPhotoInfo"
        CHAT_PHOTO_STICKER = "chatPhotoSticker"
        CHAT_PHOTO_STICKER_TYPE = "chatPhotoStickerType"
        CHAT_PHOTO_STICKER_TYPE_CUSTOM_EMOJI = "chatPhotoStickerTypeCustomEmoji"
        CHAT_PHOTO_STICKER_TYPE_REGULAR_OR_MASK = "chatPhotoStickerTypeRegularOrMask"
        CHAT_PHOTOS = "chatPhotos"
        CHAT_POSITION = "chatPosition"
        CHAT_SOURCE = "chatSource"
        CHAT_SOURCE_MTPROTO_PROXY = "chatSourceMtprotoProxy"
        CHAT_SOURCE_PUBLIC_SERVICE_ANNOUNCEMENT = "chatSourcePublicServiceAnnouncement"
        CHAT_STATISTICS = "chatStatistics"
        CHAT_STATISTICS_CHANNEL = "chatStatisticsChannel"
        CHAT_STATISTICS_SUPERGROUP = "chatStatisticsSupergroup"
        CHAT_STATISTICS_ADMINISTRATOR_ACTIONS_INFO = "chatStatisticsAdministratorActionsInfo"
        CHAT_STATISTICS_INVITER_INFO = "chatStatisticsInviterInfo"
        CHAT_STATISTICS_MESSAGE_INTERACTION_INFO = "chatStatisticsMessageInteractionInfo"
        CHAT_STATISTICS_MESSAGE_SENDER_INFO = "chatStatisticsMessageSenderInfo"
        CHAT_THEME = "chatTheme"
        CHAT_TYPE = "chatType"
        CHAT_TYPE_BASIC_GROUP = "chatTypeBasicGroup"
        CHAT_TYPE_PRIVATE = "chatTypePrivate"
        CHAT_TYPE_SECRET = "chatTypeSecret"
        CHAT_TYPE_SUPERGROUP = "chatTypeSupergroup"
        CHATS = "chats"
        CHATS_NEARBY = "chatsNearby"
        CHECK_AUTHENTICATION_BOT_TOKEN = "checkAuthenticationBotToken"
        CHECK_AUTHENTICATION_CODE = "checkAuthenticationCode"
        CHECK_AUTHENTICATION_EMAIL_CODE = "checkAuthenticationEmailCode"
        CHECK_AUTHENTICATION_PASSWORD = "checkAuthenticationPassword"
        CHECK_AUTHENTICATION_PASSWORD_RECOVERY_CODE = "checkAuthenticationPasswordRecoveryCode"
        CHECK_CHANGE_PHONE_NUMBER_CODE = "checkChangePhoneNumberCode"
        CHECK_CHAT_FOLDER_INVITE_LINK = "checkChatFolderInviteLink"
        CHECK_CHAT_INVITE_LINK = "checkChatInviteLink"
        CHECK_CHAT_USERNAME = "checkChatUsername"
        CHECK_CHAT_USERNAME_RESULT = "checkChatUsernameResult"
        CHECK_CHAT_USERNAME_RESULT_OK = "checkChatUsernameResultOk"
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_CHATS_TOO_MANY = "checkChatUsernameResultPublicChatsTooMany"
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_GROUPS_UNAVAILABLE = "checkChatUsernameResultPublicGroupsUnavailable"
        CHECK_CHAT_USERNAME_RESULT_USERNAME_INVALID = "checkChatUsernameResultUsernameInvalid"
        CHECK_CHAT_USERNAME_RESULT_USERNAME_OCCUPIED = "checkChatUsernameResultUsernameOccupied"
        CHECK_CHAT_USERNAME_RESULT_USERNAME_PURCHASABLE = "checkChatUsernameResultUsernamePurchasable"
        CHECK_CREATED_PUBLIC_CHATS_LIMIT = "checkCreatedPublicChatsLimit"
        CHECK_EMAIL_ADDRESS_VERIFICATION_CODE = "checkEmailAddressVerificationCode"
        CHECK_LOGIN_EMAIL_ADDRESS_CODE = "checkLoginEmailAddressCode"
        CHECK_PASSWORD_RECOVERY_CODE = "checkPasswordRecoveryCode"
        CHECK_PHONE_NUMBER_CONFIRMATION_CODE = "checkPhoneNumberConfirmationCode"
        CHECK_PHONE_NUMBER_VERIFICATION_CODE = "checkPhoneNumberVerificationCode"
        CHECK_RECOVERY_EMAIL_ADDRESS_CODE = "checkRecoveryEmailAddressCode"
        CHECK_STICKER_SET_NAME = "checkStickerSetName"
        CHECK_STICKER_SET_NAME_RESULT = "checkStickerSetNameResult"
        CHECK_STICKER_SET_NAME_RESULT_NAME_INVALID = "checkStickerSetNameResultNameInvalid"
        CHECK_STICKER_SET_NAME_RESULT_NAME_OCCUPIED = "checkStickerSetNameResultNameOccupied"
        CHECK_STICKER_SET_NAME_RESULT_OK = "checkStickerSetNameResultOk"
        CLEAN_FILE_NAME = "cleanFileName"
        CLEAR_ALL_DRAFT_MESSAGES = "clearAllDraftMessages"
        CLEAR_AUTOSAVE_SETTINGS_EXCEPTIONS = "clearAutosaveSettingsExceptions"
        CLEAR_IMPORTED_CONTACTS = "clearImportedContacts"
        CLEAR_RECENT_EMOJI_STATUSES = "clearRecentEmojiStatuses"
        CLEAR_RECENT_REACTIONS = "clearRecentReactions"
        CLEAR_RECENT_STICKERS = "clearRecentStickers"
        CLEAR_RECENTLY_FOUND_CHATS = "clearRecentlyFoundChats"
        CLICK_ANIMATED_EMOJI_MESSAGE = "clickAnimatedEmojiMessage"
        CLICK_CHAT_SPONSORED_MESSAGE = "clickChatSponsoredMessage"
        CLICK_PREMIUM_SUBSCRIPTION_BUTTON = "clickPremiumSubscriptionButton"
        CLOSE = "close"
        CLOSE_CHAT = "closeChat"
        CLOSE_SECRET_CHAT = "closeSecretChat"
        CLOSE_STORY = "closeStory"
        CLOSE_WEB_APP = "closeWebApp"
        CLOSED_VECTOR_PATH = "closedVectorPath"
        CONFIRM_QR_CODE_AUTHENTICATION = "confirmQrCodeAuthentication"
        CONFIRM_SESSION = "confirmSession"
        CONNECTED_WEBSITE = "connectedWebsite"
        CONNECTED_WEBSITES = "connectedWebsites"
        CONNECTION_STATE = "connectionState"
        CONNECTION_STATE_CONNECTING = "connectionStateConnecting"
        CONNECTION_STATE_CONNECTING_TO_PROXY = "connectionStateConnectingToProxy"
        CONNECTION_STATE_READY = "connectionStateReady"
        CONNECTION_STATE_UPDATING = "connectionStateUpdating"
        CONNECTION_STATE_WAITING_FOR_NETWORK = "connectionStateWaitingForNetwork"
        CONTACT = "contact"
        COUNT = "count"
        COUNTRIES = "countries"
        COUNTRY_INFO = "countryInfo"
        CREATE_BASIC_GROUP_CHAT = "createBasicGroupChat"
        CREATE_CALL = "createCall"
        CREATE_CHAT_FOLDER = "createChatFolder"
        CREATE_CHAT_FOLDER_INVITE_LINK = "createChatFolderInviteLink"
        CREATE_CHAT_INVITE_LINK = "createChatInviteLink"
        CREATE_FORUM_TOPIC = "createForumTopic"
        CREATE_INVOICE_LINK = "createInvoiceLink"
        CREATE_NEW_BASIC_GROUP_CHAT = "createNewBasicGroupChat"
        CREATE_NEW_SECRET_CHAT = "createNewSecretChat"
        CREATE_NEW_STICKER_SET = "createNewStickerSet"
        CREATE_NEW_SUPERGROUP_CHAT = "createNewSupergroupChat"
        CREATE_PRIVATE_CHAT = "createPrivateChat"
        CREATE_SECRET_CHAT = "createSecretChat"
        CREATE_SUPERGROUP_CHAT = "createSupergroupChat"
        CREATE_TEMPORARY_PASSWORD = "createTemporaryPassword"
        CREATE_VIDEO_CHAT = "createVideoChat"
        CUSTOM_REQUEST_RESULT = "customRequestResult"
        DATABASE_STATISTICS = "databaseStatistics"
        DATE = "date"
        DATE_RANGE = "dateRange"
        DATED_FILE = "datedFile"
        DEEP_LINK_INFO = "deepLinkInfo"
        DELETE_ACCOUNT = "deleteAccount"
        DELETE_ALL_CALL_MESSAGES = "deleteAllCallMessages"
        DELETE_ALL_REVOKED_CHAT_INVITE_LINKS = "deleteAllRevokedChatInviteLinks"
        DELETE_CHAT = "deleteChat"
        DELETE_CHAT_FOLDER = "deleteChatFolder"
        DELETE_CHAT_FOLDER_INVITE_LINK = "deleteChatFolderInviteLink"
        DELETE_CHAT_HISTORY = "deleteChatHistory"
        DELETE_CHAT_MESSAGES_BY_DATE = "deleteChatMessagesByDate"
        DELETE_CHAT_MESSAGES_BY_SENDER = "deleteChatMessagesBySender"
        DELETE_CHAT_REPLY_MARKUP = "deleteChatReplyMarkup"
        DELETE_COMMANDS = "deleteCommands"
        DELETE_FILE = "deleteFile"
        DELETE_FORUM_TOPIC = "deleteForumTopic"
        DELETE_LANGUAGE_PACK = "deleteLanguagePack"
        DELETE_MESSAGES = "deleteMessages"
        DELETE_PASSPORT_ELEMENT = "deletePassportElement"
        DELETE_PROFILE_PHOTO = "deleteProfilePhoto"
        DELETE_REVOKED_CHAT_INVITE_LINK = "deleteRevokedChatInviteLink"
        DELETE_SAVED_CREDENTIALS = "deleteSavedCredentials"
        DELETE_SAVED_ORDER_INFO = "deleteSavedOrderInfo"
        DELETE_STICKER_SET = "deleteStickerSet"
        DELETE_STORY = "deleteStory"
        DESTROY = "destroy"
        DEVICE_TOKEN = "deviceToken"
        DEVICE_TOKEN_APPLE_PUSH = "deviceTokenApplePush"
        DEVICE_TOKEN_APPLE_PUSH_VO_IP = "deviceTokenApplePushVoIP"
        DEVICE_TOKEN_BLACK_BERRY_PUSH = "deviceTokenBlackBerryPush"
        DEVICE_TOKEN_FIREBASE_CLOUD_MESSAGING = "deviceTokenFirebaseCloudMessaging"
        DEVICE_TOKEN_HUAWEI_PUSH = "deviceTokenHuaweiPush"
        DEVICE_TOKEN_MICROSOFT_PUSH = "deviceTokenMicrosoftPush"
        DEVICE_TOKEN_MICROSOFT_PUSH_VO_IP = "deviceTokenMicrosoftPushVoIP"
        DEVICE_TOKEN_SIMPLE_PUSH = "deviceTokenSimplePush"
        DEVICE_TOKEN_TIZEN_PUSH = "deviceTokenTizenPush"
        DEVICE_TOKEN_UBUNTU_PUSH = "deviceTokenUbuntuPush"
        DEVICE_TOKEN_WEB_PUSH = "deviceTokenWebPush"
        DEVICE_TOKEN_WINDOWS_PUSH = "deviceTokenWindowsPush"
        DICE_STICKERS = "diceStickers"
        DICE_STICKERS_REGULAR = "diceStickersRegular"
        DICE_STICKERS_SLOT_MACHINE = "diceStickersSlotMachine"
        DISABLE_ALL_SUPERGROUP_USERNAMES = "disableAllSupergroupUsernames"
        DISABLE_PROXY = "disableProxy"
        DISCARD_CALL = "discardCall"
        DISCONNECT_ALL_WEBSITES = "disconnectAllWebsites"
        DISCONNECT_WEBSITE = "disconnectWebsite"
        DOCUMENT = "document"
        DOWNLOAD_FILE = "downloadFile"
        DOWNLOADED_FILE_COUNTS = "downloadedFileCounts"
        DRAFT_MESSAGE = "draftMessage"
        EDIT_CHAT_FOLDER = "editChatFolder"
        EDIT_CHAT_FOLDER_INVITE_LINK = "editChatFolderInviteLink"
        EDIT_CHAT_INVITE_LINK = "editChatInviteLink"
        EDIT_CUSTOM_LANGUAGE_PACK_INFO = "editCustomLanguagePackInfo"
        EDIT_FORUM_TOPIC = "editForumTopic"
        EDIT_INLINE_MESSAGE_CAPTION = "editInlineMessageCaption"
        EDIT_INLINE_MESSAGE_LIVE_LOCATION = "editInlineMessageLiveLocation"
        EDIT_INLINE_MESSAGE_MEDIA = "editInlineMessageMedia"
        EDIT_INLINE_MESSAGE_REPLY_MARKUP = "editInlineMessageReplyMarkup"
        EDIT_INLINE_MESSAGE_TEXT = "editInlineMessageText"
        EDIT_MESSAGE_CAPTION = "editMessageCaption"
        EDIT_MESSAGE_LIVE_LOCATION = "editMessageLiveLocation"
        EDIT_MESSAGE_MEDIA = "editMessageMedia"
        EDIT_MESSAGE_REPLY_MARKUP = "editMessageReplyMarkup"
        EDIT_MESSAGE_SCHEDULING_STATE = "editMessageSchedulingState"
        EDIT_MESSAGE_TEXT = "editMessageText"
        EDIT_PROXY = "editProxy"
        EDIT_STORY = "editStory"
        EMAIL_ADDRESS_AUTHENTICATION = "emailAddressAuthentication"
        EMAIL_ADDRESS_AUTHENTICATION_APPLE_ID = "emailAddressAuthenticationAppleId"
        EMAIL_ADDRESS_AUTHENTICATION_CODE = "emailAddressAuthenticationCode"
        EMAIL_ADDRESS_AUTHENTICATION_GOOGLE_ID = "emailAddressAuthenticationGoogleId"
        EMAIL_ADDRESS_AUTHENTICATION_CODE_INFO = "emailAddressAuthenticationCodeInfo"
        EMAIL_ADDRESS_RESET_STATE = "emailAddressResetState"
        EMAIL_ADDRESS_RESET_STATE_AVAILABLE = "emailAddressResetStateAvailable"
        EMAIL_ADDRESS_RESET_STATE_PENDING = "emailAddressResetStatePending"
        EMOJI_CATEGORIES = "emojiCategories"
        EMOJI_CATEGORY = "emojiCategory"
        EMOJI_CATEGORY_TYPE = "emojiCategoryType"
        EMOJI_CATEGORY_TYPE_CHAT_PHOTO = "emojiCategoryTypeChatPhoto"
        EMOJI_CATEGORY_TYPE_DEFAULT = "emojiCategoryTypeDefault"
        EMOJI_CATEGORY_TYPE_EMOJI_STATUS = "emojiCategoryTypeEmojiStatus"
        EMOJI_REACTION = "emojiReaction"
        EMOJI_STATUS = "emojiStatus"
        EMOJI_STATUSES = "emojiStatuses"
        EMOJIS = "emojis"
        ENABLE_PROXY = "enableProxy"
        ENCRYPTED_CREDENTIALS = "encryptedCredentials"
        ENCRYPTED_PASSPORT_ELEMENT = "encryptedPassportElement"
        END_GROUP_CALL = "endGroupCall"
        END_GROUP_CALL_RECORDING = "endGroupCallRecording"
        END_GROUP_CALL_SCREEN_SHARING = "endGroupCallScreenSharing"
        ERROR = "error"
        FILE = "file"
        FILE_DOWNLOAD = "fileDownload"
        FILE_DOWNLOADED_PREFIX_SIZE = "fileDownloadedPrefixSize"
        FILE_PART = "filePart"
        FILE_TYPE = "fileType"
        FILE_TYPE_ANIMATION = "fileTypeAnimation"
        FILE_TYPE_AUDIO = "fileTypeAudio"
        FILE_TYPE_DOCUMENT = "fileTypeDocument"
        FILE_TYPE_NONE = "fileTypeNone"
        FILE_TYPE_NOTIFICATION_SOUND = "fileTypeNotificationSound"
        FILE_TYPE_PHOTO = "fileTypePhoto"
        FILE_TYPE_PHOTO_STORY = "fileTypePhotoStory"
        FILE_TYPE_PROFILE_PHOTO = "fileTypeProfilePhoto"
        FILE_TYPE_SECRET = "fileTypeSecret"
        FILE_TYPE_SECRET_THUMBNAIL = "fileTypeSecretThumbnail"
        FILE_TYPE_SECURE = "fileTypeSecure"
        FILE_TYPE_STICKER = "fileTypeSticker"
        FILE_TYPE_THUMBNAIL = "fileTypeThumbnail"
        FILE_TYPE_UNKNOWN = "fileTypeUnknown"
        FILE_TYPE_VIDEO = "fileTypeVideo"
        FILE_TYPE_VIDEO_NOTE = "fileTypeVideoNote"
        FILE_TYPE_VIDEO_STORY = "fileTypeVideoStory"
        FILE_TYPE_VOICE_NOTE = "fileTypeVoiceNote"
        FILE_TYPE_WALLPAPER = "fileTypeWallpaper"
        FINISH_FILE_GENERATION = "finishFileGeneration"
        FIREBASE_AUTHENTICATION_SETTINGS = "firebaseAuthenticationSettings"
        FIREBASE_AUTHENTICATION_SETTINGS_ANDROID = "firebaseAuthenticationSettingsAndroid"
        FIREBASE_AUTHENTICATION_SETTINGS_IOS = "firebaseAuthenticationSettingsIos"
        FORMATTED_TEXT = "formattedText"
        FORUM_TOPIC = "forumTopic"
        FORUM_TOPIC_ICON = "forumTopicIcon"
        FORUM_TOPIC_INFO = "forumTopicInfo"
        FORUM_TOPICS = "forumTopics"
        FORWARD_MESSAGES = "forwardMessages"
        FOUND_CHAT_MESSAGES = "foundChatMessages"
        FOUND_FILE_DOWNLOADS = "foundFileDownloads"
        FOUND_MESSAGES = "foundMessages"
        FOUND_POSITIONS = "foundPositions"
        FOUND_WEB_APP = "foundWebApp"
        GAME = "game"
        GAME_HIGH_SCORE = "gameHighScore"
        GAME_HIGH_SCORES = "gameHighScores"
        GET_ACCOUNT_TTL = "getAccountTtl"
        GET_ACTIVE_LIVE_LOCATION_MESSAGES = "getActiveLiveLocationMessages"
        GET_ACTIVE_SESSIONS = "getActiveSessions"
        GET_ALL_PASSPORT_ELEMENTS = "getAllPassportElements"
        GET_ALL_STICKER_EMOJIS = "getAllStickerEmojis"
        GET_ANIMATED_EMOJI = "getAnimatedEmoji"
        GET_APPLICATION_CONFIG = "getApplicationConfig"
        GET_APPLICATION_DOWNLOAD_LINK = "getApplicationDownloadLink"
        GET_ARCHIVE_CHAT_LIST_SETTINGS = "getArchiveChatListSettings"
        GET_ARCHIVED_STICKER_SETS = "getArchivedStickerSets"
        GET_ARCHIVED_STORIES = "getArchivedStories"
        GET_ATTACHED_STICKER_SETS = "getAttachedStickerSets"
        GET_ATTACHMENT_MENU_BOT = "getAttachmentMenuBot"
        GET_AUTHORIZATION_STATE = "getAuthorizationState"
        GET_AUTO_DOWNLOAD_SETTINGS_PRESETS = "getAutoDownloadSettingsPresets"
        GET_AUTOSAVE_SETTINGS = "getAutosaveSettings"
        GET_BACKGROUND_URL = "getBackgroundUrl"
        GET_BACKGROUNDS = "getBackgrounds"
        GET_BANK_CARD_INFO = "getBankCardInfo"
        GET_BASIC_GROUP = "getBasicGroup"
        GET_BASIC_GROUP_FULL_INFO = "getBasicGroupFullInfo"
        GET_BLOCKED_MESSAGE_SENDERS = "getBlockedMessageSenders"
        GET_BOT_INFO_DESCRIPTION = "getBotInfoDescription"
        GET_BOT_INFO_SHORT_DESCRIPTION = "getBotInfoShortDescription"
        GET_BOT_NAME = "getBotName"
        GET_CALLBACK_QUERY_ANSWER = "getCallbackQueryAnswer"
        GET_CALLBACK_QUERY_MESSAGE = "getCallbackQueryMessage"
        GET_CHAT = "getChat"
        GET_CHAT_ACTIVE_STORIES = "getChatActiveStories"
        GET_CHAT_ADMINISTRATORS = "getChatAdministrators"
        GET_CHAT_AVAILABLE_MESSAGE_SENDERS = "getChatAvailableMessageSenders"
        GET_CHAT_EVENT_LOG = "getChatEventLog"
        GET_CHAT_FOLDER = "getChatFolder"
        GET_CHAT_FOLDER_CHAT_COUNT = "getChatFolderChatCount"
        GET_CHAT_FOLDER_CHATS_TO_LEAVE = "getChatFolderChatsToLeave"
        GET_CHAT_FOLDER_DEFAULT_ICON_NAME = "getChatFolderDefaultIconName"
        GET_CHAT_FOLDER_INVITE_LINKS = "getChatFolderInviteLinks"
        GET_CHAT_FOLDER_NEW_CHATS = "getChatFolderNewChats"
        GET_CHAT_HISTORY = "getChatHistory"
        GET_CHAT_INVITE_LINK = "getChatInviteLink"
        GET_CHAT_INVITE_LINK_COUNTS = "getChatInviteLinkCounts"
        GET_CHAT_INVITE_LINK_MEMBERS = "getChatInviteLinkMembers"
        GET_CHAT_INVITE_LINKS = "getChatInviteLinks"
        GET_CHAT_JOIN_REQUESTS = "getChatJoinRequests"
        GET_CHAT_LISTS_TO_ADD_CHAT = "getChatListsToAddChat"
        GET_CHAT_MEMBER = "getChatMember"
        GET_CHAT_MESSAGE_BY_DATE = "getChatMessageByDate"
        GET_CHAT_MESSAGE_CALENDAR = "getChatMessageCalendar"
        GET_CHAT_MESSAGE_COUNT = "getChatMessageCount"
        GET_CHAT_MESSAGE_POSITION = "getChatMessagePosition"
        GET_CHAT_NOTIFICATION_SETTINGS_EXCEPTIONS = "getChatNotificationSettingsExceptions"
        GET_CHAT_PINNED_MESSAGE = "getChatPinnedMessage"
        GET_CHAT_PINNED_STORIES = "getChatPinnedStories"
        GET_CHAT_SCHEDULED_MESSAGES = "getChatScheduledMessages"
        GET_CHAT_SPARSE_MESSAGE_POSITIONS = "getChatSparseMessagePositions"
        GET_CHAT_SPONSORED_MESSAGES = "getChatSponsoredMessages"
        GET_CHAT_STATISTICS = "getChatStatistics"
        GET_CHATS = "getChats"
        GET_CHATS_FOR_CHAT_FOLDER_INVITE_LINK = "getChatsForChatFolderInviteLink"
        GET_CLOSE_FRIENDS = "getCloseFriends"
        GET_COMMANDS = "getCommands"
        GET_CONNECTED_WEBSITES = "getConnectedWebsites"
        GET_CONTACTS = "getContacts"
        GET_COUNTRIES = "getCountries"
        GET_COUNTRY_CODE = "getCountryCode"
        GET_CREATED_PUBLIC_CHATS = "getCreatedPublicChats"
        GET_CURRENT_STATE = "getCurrentState"
        GET_CUSTOM_EMOJI_REACTION_ANIMATIONS = "getCustomEmojiReactionAnimations"
        GET_CUSTOM_EMOJI_STICKERS = "getCustomEmojiStickers"
        GET_DATABASE_STATISTICS = "getDatabaseStatistics"
        GET_DEEP_LINK_INFO = "getDeepLinkInfo"
        GET_DEFAULT_CHAT_PHOTO_CUSTOM_EMOJI_STICKERS = "getDefaultChatPhotoCustomEmojiStickers"
        GET_DEFAULT_EMOJI_STATUSES = "getDefaultEmojiStatuses"
        GET_DEFAULT_MESSAGE_AUTO_DELETE_TIME = "getDefaultMessageAutoDeleteTime"
        GET_DEFAULT_PROFILE_PHOTO_CUSTOM_EMOJI_STICKERS = "getDefaultProfilePhotoCustomEmojiStickers"
        GET_EMOJI_CATEGORIES = "getEmojiCategories"
        GET_EMOJI_REACTION = "getEmojiReaction"
        GET_EMOJI_SUGGESTIONS_URL = "getEmojiSuggestionsUrl"
        GET_EXTERNAL_LINK = "getExternalLink"
        GET_EXTERNAL_LINK_INFO = "getExternalLinkInfo"
        GET_FAVORITE_STICKERS = "getFavoriteStickers"
        GET_FILE = "getFile"
        GET_FILE_DOWNLOADED_PREFIX_SIZE = "getFileDownloadedPrefixSize"
        GET_FILE_EXTENSION = "getFileExtension"
        GET_FILE_MIME_TYPE = "getFileMimeType"
        GET_FORUM_TOPIC = "getForumTopic"
        GET_FORUM_TOPIC_DEFAULT_ICONS = "getForumTopicDefaultIcons"
        GET_FORUM_TOPIC_LINK = "getForumTopicLink"
        GET_FORUM_TOPICS = "getForumTopics"
        GET_GAME_HIGH_SCORES = "getGameHighScores"
        GET_GROUP_CALL = "getGroupCall"
        GET_GROUP_CALL_INVITE_LINK = "getGroupCallInviteLink"
        GET_GROUP_CALL_STREAM_SEGMENT = "getGroupCallStreamSegment"
        GET_GROUP_CALL_STREAMS = "getGroupCallStreams"
        GET_GROUPS_IN_COMMON = "getGroupsInCommon"
        GET_IMPORTED_CONTACT_COUNT = "getImportedContactCount"
        GET_INACTIVE_SUPERGROUP_CHATS = "getInactiveSupergroupChats"
        GET_INLINE_GAME_HIGH_SCORES = "getInlineGameHighScores"
        GET_INLINE_QUERY_RESULTS = "getInlineQueryResults"
        GET_INSTALLED_STICKER_SETS = "getInstalledStickerSets"
        GET_INTERNAL_LINK = "getInternalLink"
        GET_INTERNAL_LINK_TYPE = "getInternalLinkType"
        GET_JSON_STRING = "getJsonString"
        GET_JSON_VALUE = "getJsonValue"
        GET_LANGUAGE_PACK_INFO = "getLanguagePackInfo"
        GET_LANGUAGE_PACK_STRING = "getLanguagePackString"
        GET_LANGUAGE_PACK_STRINGS = "getLanguagePackStrings"
        GET_LOCALIZATION_TARGET_INFO = "getLocalizationTargetInfo"
        GET_LOG_STREAM = "getLogStream"
        GET_LOG_TAG_VERBOSITY_LEVEL = "getLogTagVerbosityLevel"
        GET_LOG_TAGS = "getLogTags"
        GET_LOG_VERBOSITY_LEVEL = "getLogVerbosityLevel"
        GET_LOGIN_URL = "getLoginUrl"
        GET_LOGIN_URL_INFO = "getLoginUrlInfo"
        GET_MAP_THUMBNAIL_FILE = "getMapThumbnailFile"
        GET_MARKDOWN_TEXT = "getMarkdownText"
        GET_ME = "getMe"
        GET_MENU_BUTTON = "getMenuButton"
        GET_MESSAGE = "getMessage"
        GET_MESSAGE_ADDED_REACTIONS = "getMessageAddedReactions"
        GET_MESSAGE_AVAILABLE_REACTIONS = "getMessageAvailableReactions"
        GET_MESSAGE_EMBEDDING_CODE = "getMessageEmbeddingCode"
        GET_MESSAGE_FILE_TYPE = "getMessageFileType"
        GET_MESSAGE_IMPORT_CONFIRMATION_TEXT = "getMessageImportConfirmationText"
        GET_MESSAGE_LINK = "getMessageLink"
        GET_MESSAGE_LINK_INFO = "getMessageLinkInfo"
        GET_MESSAGE_LOCALLY = "getMessageLocally"
        GET_MESSAGE_PUBLIC_FORWARDS = "getMessagePublicForwards"
        GET_MESSAGE_STATISTICS = "getMessageStatistics"
        GET_MESSAGE_THREAD = "getMessageThread"
        GET_MESSAGE_THREAD_HISTORY = "getMessageThreadHistory"
        GET_MESSAGE_VIEWERS = "getMessageViewers"
        GET_MESSAGES = "getMessages"
        GET_NETWORK_STATISTICS = "getNetworkStatistics"
        GET_OPTION = "getOption"
        GET_PASSPORT_AUTHORIZATION_FORM = "getPassportAuthorizationForm"
        GET_PASSPORT_AUTHORIZATION_FORM_AVAILABLE_ELEMENTS = "getPassportAuthorizationFormAvailableElements"
        GET_PASSPORT_ELEMENT = "getPassportElement"
        GET_PASSWORD_STATE = "getPasswordState"
        GET_PAYMENT_FORM = "getPaymentForm"
        GET_PAYMENT_RECEIPT = "getPaymentReceipt"
        GET_PHONE_NUMBER_INFO = "getPhoneNumberInfo"
        GET_PHONE_NUMBER_INFO_SYNC = "getPhoneNumberInfoSync"
        GET_POLL_VOTERS = "getPollVoters"
        GET_PREFERRED_COUNTRY_LANGUAGE = "getPreferredCountryLanguage"
        GET_PREMIUM_FEATURES = "getPremiumFeatures"
        GET_PREMIUM_LIMIT = "getPremiumLimit"
        GET_PREMIUM_STATE = "getPremiumState"
        GET_PREMIUM_STICKER_EXAMPLES = "getPremiumStickerExamples"
        GET_PREMIUM_STICKERS = "getPremiumStickers"
        GET_PROXIES = "getProxies"
        GET_PROXY_LINK = "getProxyLink"
        GET_PUSH_RECEIVER_ID = "getPushReceiverId"
        GET_RECENT_EMOJI_STATUSES = "getRecentEmojiStatuses"
        GET_RECENT_INLINE_BOTS = "getRecentInlineBots"
        GET_RECENT_STICKERS = "getRecentStickers"
        GET_RECENTLY_OPENED_CHATS = "getRecentlyOpenedChats"
        GET_RECENTLY_VISITED_T_ME_URLS = "getRecentlyVisitedTMeUrls"
        GET_RECOMMENDED_CHAT_FOLDERS = "getRecommendedChatFolders"
        GET_RECOVERY_EMAIL_ADDRESS = "getRecoveryEmailAddress"
        GET_REMOTE_FILE = "getRemoteFile"
        GET_REPLIED_MESSAGE = "getRepliedMessage"
        GET_SAVED_ANIMATIONS = "getSavedAnimations"
        GET_SAVED_NOTIFICATION_SOUND = "getSavedNotificationSound"
        GET_SAVED_NOTIFICATION_SOUNDS = "getSavedNotificationSounds"
        GET_SAVED_ORDER_INFO = "getSavedOrderInfo"
        GET_SCOPE_NOTIFICATION_SETTINGS = "getScopeNotificationSettings"
        GET_SECRET_CHAT = "getSecretChat"
        GET_STATISTICAL_GRAPH = "getStatisticalGraph"
        GET_STICKER_EMOJIS = "getStickerEmojis"
        GET_STICKER_SET = "getStickerSet"
        GET_STICKERS = "getStickers"
        GET_STORAGE_STATISTICS = "getStorageStatistics"
        GET_STORAGE_STATISTICS_FAST = "getStorageStatisticsFast"
        GET_STORY = "getStory"
        GET_STORY_AVAILABLE_REACTIONS = "getStoryAvailableReactions"
        GET_STORY_NOTIFICATION_SETTINGS_EXCEPTIONS = "getStoryNotificationSettingsExceptions"
        GET_STORY_VIEWERS = "getStoryViewers"
        GET_SUGGESTED_FILE_NAME = "getSuggestedFileName"
        GET_SUGGESTED_STICKER_SET_NAME = "getSuggestedStickerSetName"
        GET_SUITABLE_DISCUSSION_CHATS = "getSuitableDiscussionChats"
        GET_SUPERGROUP = "getSupergroup"
        GET_SUPERGROUP_FULL_INFO = "getSupergroupFullInfo"
        GET_SUPERGROUP_MEMBERS = "getSupergroupMembers"
        GET_SUPPORT_NAME = "getSupportName"
        GET_SUPPORT_USER = "getSupportUser"
        GET_TEMPORARY_PASSWORD_STATE = "getTemporaryPasswordState"
        GET_TEXT_ENTITIES = "getTextEntities"
        GET_THEME_PARAMETERS_JSON_STRING = "getThemeParametersJsonString"
        GET_THEMED_EMOJI_STATUSES = "getThemedEmojiStatuses"
        GET_TOP_CHATS = "getTopChats"
        GET_TRENDING_STICKER_SETS = "getTrendingStickerSets"
        GET_USER = "getUser"
        GET_USER_FULL_INFO = "getUserFullInfo"
        GET_USER_LINK = "getUserLink"
        GET_USER_PRIVACY_SETTING_RULES = "getUserPrivacySettingRules"
        GET_USER_PROFILE_PHOTOS = "getUserProfilePhotos"
        GET_USER_SUPPORT_INFO = "getUserSupportInfo"
        GET_VIDEO_CHAT_AVAILABLE_PARTICIPANTS = "getVideoChatAvailableParticipants"
        GET_VIDEO_CHAT_RTMP_URL = "getVideoChatRtmpUrl"
        GET_WEB_APP_LINK_URL = "getWebAppLinkUrl"
        GET_WEB_APP_URL = "getWebAppUrl"
        GET_WEB_PAGE_INSTANT_VIEW = "getWebPageInstantView"
        GET_WEB_PAGE_PREVIEW = "getWebPagePreview"
        GROUP_CALL = "groupCall"
        GROUP_CALL_ID = "groupCallId"
        GROUP_CALL_PARTICIPANT = "groupCallParticipant"
        GROUP_CALL_PARTICIPANT_VIDEO_INFO = "groupCallParticipantVideoInfo"
        GROUP_CALL_RECENT_SPEAKER = "groupCallRecentSpeaker"
        GROUP_CALL_STREAM = "groupCallStream"
        GROUP_CALL_STREAMS = "groupCallStreams"
        GROUP_CALL_VIDEO_QUALITY = "groupCallVideoQuality"
        GROUP_CALL_VIDEO_QUALITY_FULL = "groupCallVideoQualityFull"
        GROUP_CALL_VIDEO_QUALITY_MEDIUM = "groupCallVideoQualityMedium"
        GROUP_CALL_VIDEO_QUALITY_THUMBNAIL = "groupCallVideoQualityThumbnail"
        GROUP_CALL_VIDEO_SOURCE_GROUP = "groupCallVideoSourceGroup"
        HASHTAGS = "hashtags"
        HIDE_SUGGESTED_ACTION = "hideSuggestedAction"
        HTTP_URL = "httpUrl"
        IDENTITY_DOCUMENT = "identityDocument"
        IMPORT_CONTACTS = "importContacts"
        IMPORT_MESSAGES = "importMessages"
        IMPORTED_CONTACTS = "importedContacts"
        INLINE_KEYBOARD_BUTTON = "inlineKeyboardButton"
        INLINE_KEYBOARD_BUTTON_TYPE = "inlineKeyboardButtonType"
        INLINE_KEYBOARD_BUTTON_TYPE_BUY = "inlineKeyboardButtonTypeBuy"
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK = "inlineKeyboardButtonTypeCallback"
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_GAME = "inlineKeyboardButtonTypeCallbackGame"
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_WITH_PASSWORD = "inlineKeyboardButtonTypeCallbackWithPassword"
        INLINE_KEYBOARD_BUTTON_TYPE_LOGIN_URL = "inlineKeyboardButtonTypeLoginUrl"
        INLINE_KEYBOARD_BUTTON_TYPE_SWITCH_INLINE = "inlineKeyboardButtonTypeSwitchInline"
        INLINE_KEYBOARD_BUTTON_TYPE_URL = "inlineKeyboardButtonTypeUrl"
        INLINE_KEYBOARD_BUTTON_TYPE_USER = "inlineKeyboardButtonTypeUser"
        INLINE_KEYBOARD_BUTTON_TYPE_WEB_APP = "inlineKeyboardButtonTypeWebApp"
        INLINE_QUERY_RESULT = "inlineQueryResult"
        INLINE_QUERY_RESULT_ANIMATION = "inlineQueryResultAnimation"
        INLINE_QUERY_RESULT_ARTICLE = "inlineQueryResultArticle"
        INLINE_QUERY_RESULT_AUDIO = "inlineQueryResultAudio"
        INLINE_QUERY_RESULT_CONTACT = "inlineQueryResultContact"
        INLINE_QUERY_RESULT_DOCUMENT = "inlineQueryResultDocument"
        INLINE_QUERY_RESULT_GAME = "inlineQueryResultGame"
        INLINE_QUERY_RESULT_LOCATION = "inlineQueryResultLocation"
        INLINE_QUERY_RESULT_PHOTO = "inlineQueryResultPhoto"
        INLINE_QUERY_RESULT_STICKER = "inlineQueryResultSticker"
        INLINE_QUERY_RESULT_VENUE = "inlineQueryResultVenue"
        INLINE_QUERY_RESULT_VIDEO = "inlineQueryResultVideo"
        INLINE_QUERY_RESULT_VOICE_NOTE = "inlineQueryResultVoiceNote"
        INLINE_QUERY_RESULTS = "inlineQueryResults"
        INLINE_QUERY_RESULTS_BUTTON = "inlineQueryResultsButton"
        INLINE_QUERY_RESULTS_BUTTON_TYPE = "inlineQueryResultsButtonType"
        INLINE_QUERY_RESULTS_BUTTON_TYPE_START_BOT = "inlineQueryResultsButtonTypeStartBot"
        INLINE_QUERY_RESULTS_BUTTON_TYPE_WEB_APP = "inlineQueryResultsButtonTypeWebApp"
        INPUT_BACKGROUND = "inputBackground"
        INPUT_BACKGROUND_LOCAL = "inputBackgroundLocal"
        INPUT_BACKGROUND_PREVIOUS = "inputBackgroundPrevious"
        INPUT_BACKGROUND_REMOTE = "inputBackgroundRemote"
        INPUT_CHAT_PHOTO = "inputChatPhoto"
        INPUT_CHAT_PHOTO_ANIMATION = "inputChatPhotoAnimation"
        INPUT_CHAT_PHOTO_PREVIOUS = "inputChatPhotoPrevious"
        INPUT_CHAT_PHOTO_STATIC = "inputChatPhotoStatic"
        INPUT_CHAT_PHOTO_STICKER = "inputChatPhotoSticker"
        INPUT_CREDENTIALS = "inputCredentials"
        INPUT_CREDENTIALS_APPLE_PAY = "inputCredentialsApplePay"
        INPUT_CREDENTIALS_GOOGLE_PAY = "inputCredentialsGooglePay"
        INPUT_CREDENTIALS_NEW = "inputCredentialsNew"
        INPUT_CREDENTIALS_SAVED = "inputCredentialsSaved"
        INPUT_FILE = "inputFile"
        INPUT_FILE_GENERATED = "inputFileGenerated"
        INPUT_FILE_ID = "inputFileId"
        INPUT_FILE_LOCAL = "inputFileLocal"
        INPUT_FILE_REMOTE = "inputFileRemote"
        INPUT_IDENTITY_DOCUMENT = "inputIdentityDocument"
        INPUT_INLINE_QUERY_RESULT = "inputInlineQueryResult"
        INPUT_INLINE_QUERY_RESULT_ANIMATION = "inputInlineQueryResultAnimation"
        INPUT_INLINE_QUERY_RESULT_ARTICLE = "inputInlineQueryResultArticle"
        INPUT_INLINE_QUERY_RESULT_AUDIO = "inputInlineQueryResultAudio"
        INPUT_INLINE_QUERY_RESULT_CONTACT = "inputInlineQueryResultContact"
        INPUT_INLINE_QUERY_RESULT_DOCUMENT = "inputInlineQueryResultDocument"
        INPUT_INLINE_QUERY_RESULT_GAME = "inputInlineQueryResultGame"
        INPUT_INLINE_QUERY_RESULT_LOCATION = "inputInlineQueryResultLocation"
        INPUT_INLINE_QUERY_RESULT_PHOTO = "inputInlineQueryResultPhoto"
        INPUT_INLINE_QUERY_RESULT_STICKER = "inputInlineQueryResultSticker"
        INPUT_INLINE_QUERY_RESULT_VENUE = "inputInlineQueryResultVenue"
        INPUT_INLINE_QUERY_RESULT_VIDEO = "inputInlineQueryResultVideo"
        INPUT_INLINE_QUERY_RESULT_VOICE_NOTE = "inputInlineQueryResultVoiceNote"
        INPUT_INVOICE = "inputInvoice"
        INPUT_INVOICE_MESSAGE = "inputInvoiceMessage"
        INPUT_INVOICE_NAME = "inputInvoiceName"
        INPUT_MESSAGE_CONTENT = "inputMessageContent"
        INPUT_MESSAGE_ANIMATION = "inputMessageAnimation"
        INPUT_MESSAGE_AUDIO = "inputMessageAudio"
        INPUT_MESSAGE_CONTACT = "inputMessageContact"
        INPUT_MESSAGE_DICE = "inputMessageDice"
        INPUT_MESSAGE_DOCUMENT = "inputMessageDocument"
        INPUT_MESSAGE_FORWARDED = "inputMessageForwarded"
        INPUT_MESSAGE_GAME = "inputMessageGame"
        INPUT_MESSAGE_INVOICE = "inputMessageInvoice"
        INPUT_MESSAGE_LOCATION = "inputMessageLocation"
        INPUT_MESSAGE_PHOTO = "inputMessagePhoto"
        INPUT_MESSAGE_POLL = "inputMessagePoll"
        INPUT_MESSAGE_STICKER = "inputMessageSticker"
        INPUT_MESSAGE_STORY = "inputMessageStory"
        INPUT_MESSAGE_TEXT = "inputMessageText"
        INPUT_MESSAGE_VENUE = "inputMessageVenue"
        INPUT_MESSAGE_VIDEO = "inputMessageVideo"
        INPUT_MESSAGE_VIDEO_NOTE = "inputMessageVideoNote"
        INPUT_MESSAGE_VOICE_NOTE = "inputMessageVoiceNote"
        INPUT_PASSPORT_ELEMENT = "inputPassportElement"
        INPUT_PASSPORT_ELEMENT_ADDRESS = "inputPassportElementAddress"
        INPUT_PASSPORT_ELEMENT_BANK_STATEMENT = "inputPassportElementBankStatement"
        INPUT_PASSPORT_ELEMENT_DRIVER_LICENSE = "inputPassportElementDriverLicense"
        INPUT_PASSPORT_ELEMENT_EMAIL_ADDRESS = "inputPassportElementEmailAddress"
        INPUT_PASSPORT_ELEMENT_IDENTITY_CARD = "inputPassportElementIdentityCard"
        INPUT_PASSPORT_ELEMENT_INTERNAL_PASSPORT = "inputPassportElementInternalPassport"
        INPUT_PASSPORT_ELEMENT_PASSPORT = "inputPassportElementPassport"
        INPUT_PASSPORT_ELEMENT_PASSPORT_REGISTRATION = "inputPassportElementPassportRegistration"
        INPUT_PASSPORT_ELEMENT_PERSONAL_DETAILS = "inputPassportElementPersonalDetails"
        INPUT_PASSPORT_ELEMENT_PHONE_NUMBER = "inputPassportElementPhoneNumber"
        INPUT_PASSPORT_ELEMENT_RENTAL_AGREEMENT = "inputPassportElementRentalAgreement"
        INPUT_PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = "inputPassportElementTemporaryRegistration"
        INPUT_PASSPORT_ELEMENT_UTILITY_BILL = "inputPassportElementUtilityBill"
        INPUT_PASSPORT_ELEMENT_ERROR = "inputPassportElementError"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE = "inputPassportElementErrorSource"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = "inputPassportElementErrorSourceDataField"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILE = "inputPassportElementErrorSourceFile"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILES = "inputPassportElementErrorSourceFiles"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = "inputPassportElementErrorSourceFrontSide"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = "inputPassportElementErrorSourceReverseSide"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = "inputPassportElementErrorSourceSelfie"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = "inputPassportElementErrorSourceTranslationFile"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = "inputPassportElementErrorSourceTranslationFiles"
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = "inputPassportElementErrorSourceUnspecified"
        INPUT_PERSONAL_DOCUMENT = "inputPersonalDocument"
        INPUT_STICKER = "inputSticker"
        INPUT_STORY_AREA = "inputStoryArea"
        INPUT_STORY_AREA_TYPE = "inputStoryAreaType"
        INPUT_STORY_AREA_TYPE_FOUND_VENUE = "inputStoryAreaTypeFoundVenue"
        INPUT_STORY_AREA_TYPE_LOCATION = "inputStoryAreaTypeLocation"
        INPUT_STORY_AREA_TYPE_PREVIOUS_VENUE = "inputStoryAreaTypePreviousVenue"
        INPUT_STORY_AREAS = "inputStoryAreas"
        INPUT_STORY_CONTENT = "inputStoryContent"
        INPUT_STORY_CONTENT_PHOTO = "inputStoryContentPhoto"
        INPUT_STORY_CONTENT_VIDEO = "inputStoryContentVideo"
        INPUT_THUMBNAIL = "inputThumbnail"
        INTERNAL_LINK_TYPE = "internalLinkType"
        INTERNAL_LINK_TYPE_ACTIVE_SESSIONS = "internalLinkTypeActiveSessions"
        INTERNAL_LINK_TYPE_ATTACHMENT_MENU_BOT = "internalLinkTypeAttachmentMenuBot"
        INTERNAL_LINK_TYPE_AUTHENTICATION_CODE = "internalLinkTypeAuthenticationCode"
        INTERNAL_LINK_TYPE_BACKGROUND = "internalLinkTypeBackground"
        INTERNAL_LINK_TYPE_BOT_ADD_TO_CHANNEL = "internalLinkTypeBotAddToChannel"
        INTERNAL_LINK_TYPE_BOT_START = "internalLinkTypeBotStart"
        INTERNAL_LINK_TYPE_BOT_START_IN_GROUP = "internalLinkTypeBotStartInGroup"
        INTERNAL_LINK_TYPE_CHANGE_PHONE_NUMBER = "internalLinkTypeChangePhoneNumber"
        INTERNAL_LINK_TYPE_CHAT_FOLDER_INVITE = "internalLinkTypeChatFolderInvite"
        INTERNAL_LINK_TYPE_CHAT_FOLDER_SETTINGS = "internalLinkTypeChatFolderSettings"
        INTERNAL_LINK_TYPE_CHAT_INVITE = "internalLinkTypeChatInvite"
        INTERNAL_LINK_TYPE_DEFAULT_MESSAGE_AUTO_DELETE_TIMER_SETTINGS = (
            "internalLinkTypeDefaultMessageAutoDeleteTimerSettings"
        )
        INTERNAL_LINK_TYPE_EDIT_PROFILE_SETTINGS = "internalLinkTypeEditProfileSettings"
        INTERNAL_LINK_TYPE_GAME = "internalLinkTypeGame"
        INTERNAL_LINK_TYPE_INSTANT_VIEW = "internalLinkTypeInstantView"
        INTERNAL_LINK_TYPE_INVOICE = "internalLinkTypeInvoice"
        INTERNAL_LINK_TYPE_LANGUAGE_PACK = "internalLinkTypeLanguagePack"
        INTERNAL_LINK_TYPE_LANGUAGE_SETTINGS = "internalLinkTypeLanguageSettings"
        INTERNAL_LINK_TYPE_MESSAGE = "internalLinkTypeMessage"
        INTERNAL_LINK_TYPE_MESSAGE_DRAFT = "internalLinkTypeMessageDraft"
        INTERNAL_LINK_TYPE_PASSPORT_DATA_REQUEST = "internalLinkTypePassportDataRequest"
        INTERNAL_LINK_TYPE_PHONE_NUMBER_CONFIRMATION = "internalLinkTypePhoneNumberConfirmation"
        INTERNAL_LINK_TYPE_PREMIUM_FEATURES = "internalLinkTypePremiumFeatures"
        INTERNAL_LINK_TYPE_PRIVACY_AND_SECURITY_SETTINGS = "internalLinkTypePrivacyAndSecuritySettings"
        INTERNAL_LINK_TYPE_PROXY = "internalLinkTypeProxy"
        INTERNAL_LINK_TYPE_PUBLIC_CHAT = "internalLinkTypePublicChat"
        INTERNAL_LINK_TYPE_QR_CODE_AUTHENTICATION = "internalLinkTypeQrCodeAuthentication"
        INTERNAL_LINK_TYPE_RESTORE_PURCHASES = "internalLinkTypeRestorePurchases"
        INTERNAL_LINK_TYPE_SETTINGS = "internalLinkTypeSettings"
        INTERNAL_LINK_TYPE_SIDE_MENU_BOT = "internalLinkTypeSideMenuBot"
        INTERNAL_LINK_TYPE_STICKER_SET = "internalLinkTypeStickerSet"
        INTERNAL_LINK_TYPE_STORY = "internalLinkTypeStory"
        INTERNAL_LINK_TYPE_THEME = "internalLinkTypeTheme"
        INTERNAL_LINK_TYPE_THEME_SETTINGS = "internalLinkTypeThemeSettings"
        INTERNAL_LINK_TYPE_UNKNOWN_DEEP_LINK = "internalLinkTypeUnknownDeepLink"
        INTERNAL_LINK_TYPE_UNSUPPORTED_PROXY = "internalLinkTypeUnsupportedProxy"
        INTERNAL_LINK_TYPE_USER_PHONE_NUMBER = "internalLinkTypeUserPhoneNumber"
        INTERNAL_LINK_TYPE_USER_TOKEN = "internalLinkTypeUserToken"
        INTERNAL_LINK_TYPE_VIDEO_CHAT = "internalLinkTypeVideoChat"
        INTERNAL_LINK_TYPE_WEB_APP = "internalLinkTypeWebApp"
        INVITE_GROUP_CALL_PARTICIPANTS = "inviteGroupCallParticipants"
        INVITE_LINK_CHAT_TYPE = "inviteLinkChatType"
        INVITE_LINK_CHAT_TYPE_BASIC_GROUP = "inviteLinkChatTypeBasicGroup"
        INVITE_LINK_CHAT_TYPE_CHANNEL = "inviteLinkChatTypeChannel"
        INVITE_LINK_CHAT_TYPE_SUPERGROUP = "inviteLinkChatTypeSupergroup"
        INVOICE = "invoice"
        JOIN_CHAT = "joinChat"
        JOIN_CHAT_BY_INVITE_LINK = "joinChatByInviteLink"
        JOIN_GROUP_CALL = "joinGroupCall"
        JSON_VALUE = "jsonValue"
        JSON_VALUE_ARRAY = "jsonValueArray"
        JSON_VALUE_BOOLEAN = "jsonValueBoolean"
        JSON_VALUE_NULL = "jsonValueNull"
        JSON_VALUE_NUMBER = "jsonValueNumber"
        JSON_VALUE_OBJECT = "jsonValueObject"
        JSON_VALUE_STRING = "jsonValueString"
        KEYBOARD_BUTTON = "keyboardButton"
        KEYBOARD_BUTTON_TYPE = "keyboardButtonType"
        KEYBOARD_BUTTON_TYPE_REQUEST_CHAT = "keyboardButtonTypeRequestChat"
        KEYBOARD_BUTTON_TYPE_REQUEST_LOCATION = "keyboardButtonTypeRequestLocation"
        KEYBOARD_BUTTON_TYPE_REQUEST_PHONE_NUMBER = "keyboardButtonTypeRequestPhoneNumber"
        KEYBOARD_BUTTON_TYPE_REQUEST_POLL = "keyboardButtonTypeRequestPoll"
        KEYBOARD_BUTTON_TYPE_REQUEST_USER = "keyboardButtonTypeRequestUser"
        KEYBOARD_BUTTON_TYPE_TEXT = "keyboardButtonTypeText"
        KEYBOARD_BUTTON_TYPE_WEB_APP = "keyboardButtonTypeWebApp"
        LABELED_PRICE_PART = "labeledPricePart"
        LANGUAGE_PACK_INFO = "languagePackInfo"
        LANGUAGE_PACK_STRING = "languagePackString"
        LANGUAGE_PACK_STRING_VALUE = "languagePackStringValue"
        LANGUAGE_PACK_STRING_VALUE_DELETED = "languagePackStringValueDeleted"
        LANGUAGE_PACK_STRING_VALUE_ORDINARY = "languagePackStringValueOrdinary"
        LANGUAGE_PACK_STRING_VALUE_PLURALIZED = "languagePackStringValuePluralized"
        LANGUAGE_PACK_STRINGS = "languagePackStrings"
        LEAVE_CHAT = "leaveChat"
        LEAVE_GROUP_CALL = "leaveGroupCall"
        LOAD_ACTIVE_STORIES = "loadActiveStories"
        LOAD_CHATS = "loadChats"
        LOAD_GROUP_CALL_PARTICIPANTS = "loadGroupCallParticipants"
        LOCAL_FILE = "localFile"
        LOCALIZATION_TARGET_INFO = "localizationTargetInfo"
        LOCATION = "location"
        LOG_OUT = "logOut"
        LOG_STREAM = "logStream"
        LOG_STREAM_DEFAULT = "logStreamDefault"
        LOG_STREAM_EMPTY = "logStreamEmpty"
        LOG_STREAM_FILE = "logStreamFile"
        LOG_TAGS = "logTags"
        LOG_VERBOSITY_LEVEL = "logVerbosityLevel"
        LOGIN_URL_INFO = "loginUrlInfo"
        LOGIN_URL_INFO_OPEN = "loginUrlInfoOpen"
        LOGIN_URL_INFO_REQUEST_CONFIRMATION = "loginUrlInfoRequestConfirmation"
        MASK_POINT = "maskPoint"
        MASK_POINT_CHIN = "maskPointChin"
        MASK_POINT_EYES = "maskPointEyes"
        MASK_POINT_FOREHEAD = "maskPointForehead"
        MASK_POINT_MOUTH = "maskPointMouth"
        MASK_POSITION = "maskPosition"
        MESSAGE = "message"
        MESSAGE_AUTO_DELETE_TIME = "messageAutoDeleteTime"
        MESSAGE_CALENDAR = "messageCalendar"
        MESSAGE_CALENDAR_DAY = "messageCalendarDay"
        MESSAGE_CONTENT = "messageContent"
        MESSAGE_ANIMATED_EMOJI = "messageAnimatedEmoji"
        MESSAGE_ANIMATION = "messageAnimation"
        MESSAGE_AUDIO = "messageAudio"
        MESSAGE_BASIC_GROUP_CHAT_CREATE = "messageBasicGroupChatCreate"
        MESSAGE_BOT_WRITE_ACCESS_ALLOWED = "messageBotWriteAccessAllowed"
        MESSAGE_CALL = "messageCall"
        MESSAGE_CHAT_ADD_MEMBERS = "messageChatAddMembers"
        MESSAGE_CHAT_CHANGE_PHOTO = "messageChatChangePhoto"
        MESSAGE_CHAT_CHANGE_TITLE = "messageChatChangeTitle"
        MESSAGE_CHAT_DELETE_MEMBER = "messageChatDeleteMember"
        MESSAGE_CHAT_DELETE_PHOTO = "messageChatDeletePhoto"
        MESSAGE_CHAT_JOIN_BY_LINK = "messageChatJoinByLink"
        MESSAGE_CHAT_JOIN_BY_REQUEST = "messageChatJoinByRequest"
        MESSAGE_CHAT_SET_BACKGROUND = "messageChatSetBackground"
        MESSAGE_CHAT_SET_MESSAGE_AUTO_DELETE_TIME = "messageChatSetMessageAutoDeleteTime"
        MESSAGE_CHAT_SET_THEME = "messageChatSetTheme"
        MESSAGE_CHAT_SHARED = "messageChatShared"
        MESSAGE_CHAT_UPGRADE_FROM = "messageChatUpgradeFrom"
        MESSAGE_CHAT_UPGRADE_TO = "messageChatUpgradeTo"
        MESSAGE_CONTACT = "messageContact"
        MESSAGE_CONTACT_REGISTERED = "messageContactRegistered"
        MESSAGE_CUSTOM_SERVICE_ACTION = "messageCustomServiceAction"
        MESSAGE_DICE = "messageDice"
        MESSAGE_DOCUMENT = "messageDocument"
        MESSAGE_EXPIRED_PHOTO = "messageExpiredPhoto"
        MESSAGE_EXPIRED_VIDEO = "messageExpiredVideo"
        MESSAGE_FORUM_TOPIC_CREATED = "messageForumTopicCreated"
        MESSAGE_FORUM_TOPIC_EDITED = "messageForumTopicEdited"
        MESSAGE_FORUM_TOPIC_IS_CLOSED_TOGGLED = "messageForumTopicIsClosedToggled"
        MESSAGE_FORUM_TOPIC_IS_HIDDEN_TOGGLED = "messageForumTopicIsHiddenToggled"
        MESSAGE_GAME = "messageGame"
        MESSAGE_GAME_SCORE = "messageGameScore"
        MESSAGE_GIFTED_PREMIUM = "messageGiftedPremium"
        MESSAGE_INVITE_VIDEO_CHAT_PARTICIPANTS = "messageInviteVideoChatParticipants"
        MESSAGE_INVOICE = "messageInvoice"
        MESSAGE_LOCATION = "messageLocation"
        MESSAGE_PASSPORT_DATA_RECEIVED = "messagePassportDataReceived"
        MESSAGE_PASSPORT_DATA_SENT = "messagePassportDataSent"
        MESSAGE_PAYMENT_SUCCESSFUL = "messagePaymentSuccessful"
        MESSAGE_PAYMENT_SUCCESSFUL_BOT = "messagePaymentSuccessfulBot"
        MESSAGE_PHOTO = "messagePhoto"
        MESSAGE_PIN_MESSAGE = "messagePinMessage"
        MESSAGE_POLL = "messagePoll"
        MESSAGE_PROXIMITY_ALERT_TRIGGERED = "messageProximityAlertTriggered"
        MESSAGE_SCREENSHOT_TAKEN = "messageScreenshotTaken"
        MESSAGE_STICKER = "messageSticker"
        MESSAGE_STORY = "messageStory"
        MESSAGE_SUGGEST_PROFILE_PHOTO = "messageSuggestProfilePhoto"
        MESSAGE_SUPERGROUP_CHAT_CREATE = "messageSupergroupChatCreate"
        MESSAGE_TEXT = "messageText"
        MESSAGE_UNSUPPORTED = "messageUnsupported"
        MESSAGE_USER_SHARED = "messageUserShared"
        MESSAGE_VENUE = "messageVenue"
        MESSAGE_VIDEO = "messageVideo"
        MESSAGE_VIDEO_CHAT_ENDED = "messageVideoChatEnded"
        MESSAGE_VIDEO_CHAT_SCHEDULED = "messageVideoChatScheduled"
        MESSAGE_VIDEO_CHAT_STARTED = "messageVideoChatStarted"
        MESSAGE_VIDEO_NOTE = "messageVideoNote"
        MESSAGE_VOICE_NOTE = "messageVoiceNote"
        MESSAGE_WEB_APP_DATA_RECEIVED = "messageWebAppDataReceived"
        MESSAGE_WEB_APP_DATA_SENT = "messageWebAppDataSent"
        MESSAGE_WEBSITE_CONNECTED = "messageWebsiteConnected"
        MESSAGE_COPY_OPTIONS = "messageCopyOptions"
        MESSAGE_EXTENDED_MEDIA = "messageExtendedMedia"
        MESSAGE_EXTENDED_MEDIA_PHOTO = "messageExtendedMediaPhoto"
        MESSAGE_EXTENDED_MEDIA_PREVIEW = "messageExtendedMediaPreview"
        MESSAGE_EXTENDED_MEDIA_UNSUPPORTED = "messageExtendedMediaUnsupported"
        MESSAGE_EXTENDED_MEDIA_VIDEO = "messageExtendedMediaVideo"
        MESSAGE_FILE_TYPE = "messageFileType"
        MESSAGE_FILE_TYPE_GROUP = "messageFileTypeGroup"
        MESSAGE_FILE_TYPE_PRIVATE = "messageFileTypePrivate"
        MESSAGE_FILE_TYPE_UNKNOWN = "messageFileTypeUnknown"
        MESSAGE_FORWARD_INFO = "messageForwardInfo"
        MESSAGE_FORWARD_ORIGIN = "messageForwardOrigin"
        MESSAGE_FORWARD_ORIGIN_CHANNEL = "messageForwardOriginChannel"
        MESSAGE_FORWARD_ORIGIN_CHAT = "messageForwardOriginChat"
        MESSAGE_FORWARD_ORIGIN_HIDDEN_USER = "messageForwardOriginHiddenUser"
        MESSAGE_FORWARD_ORIGIN_MESSAGE_IMPORT = "messageForwardOriginMessageImport"
        MESSAGE_FORWARD_ORIGIN_USER = "messageForwardOriginUser"
        MESSAGE_INTERACTION_INFO = "messageInteractionInfo"
        MESSAGE_LINK = "messageLink"
        MESSAGE_LINK_INFO = "messageLinkInfo"
        MESSAGE_POSITION = "messagePosition"
        MESSAGE_POSITIONS = "messagePositions"
        MESSAGE_REACTION = "messageReaction"
        MESSAGE_REPLY_INFO = "messageReplyInfo"
        MESSAGE_REPLY_TO = "messageReplyTo"
        MESSAGE_REPLY_TO_MESSAGE = "messageReplyToMessage"
        MESSAGE_REPLY_TO_STORY = "messageReplyToStory"
        MESSAGE_SCHEDULING_STATE = "messageSchedulingState"
        MESSAGE_SCHEDULING_STATE_SEND_AT_DATE = "messageSchedulingStateSendAtDate"
        MESSAGE_SCHEDULING_STATE_SEND_WHEN_ONLINE = "messageSchedulingStateSendWhenOnline"
        MESSAGE_SELF_DESTRUCT_TYPE = "messageSelfDestructType"
        MESSAGE_SELF_DESTRUCT_TYPE_IMMEDIATELY = "messageSelfDestructTypeImmediately"
        MESSAGE_SELF_DESTRUCT_TYPE_TIMER = "messageSelfDestructTypeTimer"
        MESSAGE_SEND_OPTIONS = "messageSendOptions"
        MESSAGE_SENDER = "messageSender"
        MESSAGE_SENDER_CHAT = "messageSenderChat"
        MESSAGE_SENDER_USER = "messageSenderUser"
        MESSAGE_SENDERS = "messageSenders"
        MESSAGE_SENDING_STATE = "messageSendingState"
        MESSAGE_SENDING_STATE_FAILED = "messageSendingStateFailed"
        MESSAGE_SENDING_STATE_PENDING = "messageSendingStatePending"
        MESSAGE_SOURCE = "messageSource"
        MESSAGE_SOURCE_CHAT_EVENT_LOG = "messageSourceChatEventLog"
        MESSAGE_SOURCE_CHAT_HISTORY = "messageSourceChatHistory"
        MESSAGE_SOURCE_CHAT_LIST = "messageSourceChatList"
        MESSAGE_SOURCE_FORUM_TOPIC_HISTORY = "messageSourceForumTopicHistory"
        MESSAGE_SOURCE_HISTORY_PREVIEW = "messageSourceHistoryPreview"
        MESSAGE_SOURCE_MESSAGE_THREAD_HISTORY = "messageSourceMessageThreadHistory"
        MESSAGE_SOURCE_NOTIFICATION = "messageSourceNotification"
        MESSAGE_SOURCE_OTHER = "messageSourceOther"
        MESSAGE_SOURCE_SCREENSHOT = "messageSourceScreenshot"
        MESSAGE_SOURCE_SEARCH = "messageSourceSearch"
        MESSAGE_SPONSOR = "messageSponsor"
        MESSAGE_SPONSOR_TYPE = "messageSponsorType"
        MESSAGE_SPONSOR_TYPE_BOT = "messageSponsorTypeBot"
        MESSAGE_SPONSOR_TYPE_PRIVATE_CHANNEL = "messageSponsorTypePrivateChannel"
        MESSAGE_SPONSOR_TYPE_PUBLIC_CHANNEL = "messageSponsorTypePublicChannel"
        MESSAGE_SPONSOR_TYPE_WEBSITE = "messageSponsorTypeWebsite"
        MESSAGE_STATISTICS = "messageStatistics"
        MESSAGE_THREAD_INFO = "messageThreadInfo"
        MESSAGE_VIEWER = "messageViewer"
        MESSAGE_VIEWERS = "messageViewers"
        MESSAGES = "messages"
        MINITHUMBNAIL = "minithumbnail"
        NETWORK_STATISTICS = "networkStatistics"
        NETWORK_STATISTICS_ENTRY = "networkStatisticsEntry"
        NETWORK_STATISTICS_ENTRY_CALL = "networkStatisticsEntryCall"
        NETWORK_STATISTICS_ENTRY_FILE = "networkStatisticsEntryFile"
        NETWORK_TYPE = "networkType"
        NETWORK_TYPE_MOBILE = "networkTypeMobile"
        NETWORK_TYPE_MOBILE_ROAMING = "networkTypeMobileRoaming"
        NETWORK_TYPE_NONE = "networkTypeNone"
        NETWORK_TYPE_OTHER = "networkTypeOther"
        NETWORK_TYPE_WI_FI = "networkTypeWiFi"
        NOTIFICATION = "notification"
        NOTIFICATION_GROUP = "notificationGroup"
        NOTIFICATION_GROUP_TYPE = "notificationGroupType"
        NOTIFICATION_GROUP_TYPE_CALLS = "notificationGroupTypeCalls"
        NOTIFICATION_GROUP_TYPE_MENTIONS = "notificationGroupTypeMentions"
        NOTIFICATION_GROUP_TYPE_MESSAGES = "notificationGroupTypeMessages"
        NOTIFICATION_GROUP_TYPE_SECRET_CHAT = "notificationGroupTypeSecretChat"
        NOTIFICATION_SETTINGS_SCOPE = "notificationSettingsScope"
        NOTIFICATION_SETTINGS_SCOPE_CHANNEL_CHATS = "notificationSettingsScopeChannelChats"
        NOTIFICATION_SETTINGS_SCOPE_GROUP_CHATS = "notificationSettingsScopeGroupChats"
        NOTIFICATION_SETTINGS_SCOPE_PRIVATE_CHATS = "notificationSettingsScopePrivateChats"
        NOTIFICATION_SOUND = "notificationSound"
        NOTIFICATION_SOUNDS = "notificationSounds"
        NOTIFICATION_TYPE = "notificationType"
        NOTIFICATION_TYPE_NEW_CALL = "notificationTypeNewCall"
        NOTIFICATION_TYPE_NEW_MESSAGE = "notificationTypeNewMessage"
        NOTIFICATION_TYPE_NEW_PUSH_MESSAGE = "notificationTypeNewPushMessage"
        NOTIFICATION_TYPE_NEW_SECRET_CHAT = "notificationTypeNewSecretChat"
        OK = "ok"
        OPEN_CHAT = "openChat"
        OPEN_MESSAGE_CONTENT = "openMessageContent"
        OPEN_STORY = "openStory"
        OPEN_WEB_APP = "openWebApp"
        OPTIMIZE_STORAGE = "optimizeStorage"
        OPTION_VALUE = "optionValue"
        OPTION_VALUE_BOOLEAN = "optionValueBoolean"
        OPTION_VALUE_EMPTY = "optionValueEmpty"
        OPTION_VALUE_INTEGER = "optionValueInteger"
        OPTION_VALUE_STRING = "optionValueString"
        ORDER_INFO = "orderInfo"
        PAGE_BLOCK = "pageBlock"
        PAGE_BLOCK_ANCHOR = "pageBlockAnchor"
        PAGE_BLOCK_ANIMATION = "pageBlockAnimation"
        PAGE_BLOCK_AUDIO = "pageBlockAudio"
        PAGE_BLOCK_AUTHOR_DATE = "pageBlockAuthorDate"
        PAGE_BLOCK_BLOCK_QUOTE = "pageBlockBlockQuote"
        PAGE_BLOCK_CHAT_LINK = "pageBlockChatLink"
        PAGE_BLOCK_COLLAGE = "pageBlockCollage"
        PAGE_BLOCK_COVER = "pageBlockCover"
        PAGE_BLOCK_DETAILS = "pageBlockDetails"
        PAGE_BLOCK_DIVIDER = "pageBlockDivider"
        PAGE_BLOCK_EMBEDDED = "pageBlockEmbedded"
        PAGE_BLOCK_EMBEDDED_POST = "pageBlockEmbeddedPost"
        PAGE_BLOCK_FOOTER = "pageBlockFooter"
        PAGE_BLOCK_HEADER = "pageBlockHeader"
        PAGE_BLOCK_KICKER = "pageBlockKicker"
        PAGE_BLOCK_LIST = "pageBlockList"
        PAGE_BLOCK_MAP = "pageBlockMap"
        PAGE_BLOCK_PARAGRAPH = "pageBlockParagraph"
        PAGE_BLOCK_PHOTO = "pageBlockPhoto"
        PAGE_BLOCK_PREFORMATTED = "pageBlockPreformatted"
        PAGE_BLOCK_PULL_QUOTE = "pageBlockPullQuote"
        PAGE_BLOCK_RELATED_ARTICLES = "pageBlockRelatedArticles"
        PAGE_BLOCK_SLIDESHOW = "pageBlockSlideshow"
        PAGE_BLOCK_SUBHEADER = "pageBlockSubheader"
        PAGE_BLOCK_SUBTITLE = "pageBlockSubtitle"
        PAGE_BLOCK_TABLE = "pageBlockTable"
        PAGE_BLOCK_TITLE = "pageBlockTitle"
        PAGE_BLOCK_VIDEO = "pageBlockVideo"
        PAGE_BLOCK_VOICE_NOTE = "pageBlockVoiceNote"
        PAGE_BLOCK_CAPTION = "pageBlockCaption"
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT = "pageBlockHorizontalAlignment"
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_CENTER = "pageBlockHorizontalAlignmentCenter"
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_LEFT = "pageBlockHorizontalAlignmentLeft"
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_RIGHT = "pageBlockHorizontalAlignmentRight"
        PAGE_BLOCK_RELATED_ARTICLE = "pageBlockRelatedArticle"
        PAGE_BLOCK_TABLE_CELL = "pageBlockTableCell"
        PAGE_BLOCK_VERTICAL_ALIGNMENT = "pageBlockVerticalAlignment"
        PAGE_BLOCK_VERTICAL_ALIGNMENT_BOTTOM = "pageBlockVerticalAlignmentBottom"
        PAGE_BLOCK_VERTICAL_ALIGNMENT_MIDDLE = "pageBlockVerticalAlignmentMiddle"
        PAGE_BLOCK_VERTICAL_ALIGNMENT_TOP = "pageBlockVerticalAlignmentTop"
        PARSE_MARKDOWN = "parseMarkdown"
        PARSE_TEXT_ENTITIES = "parseTextEntities"
        PASSPORT_AUTHORIZATION_FORM = "passportAuthorizationForm"
        PASSPORT_ELEMENT = "passportElement"
        PASSPORT_ELEMENT_ADDRESS = "passportElementAddress"
        PASSPORT_ELEMENT_BANK_STATEMENT = "passportElementBankStatement"
        PASSPORT_ELEMENT_DRIVER_LICENSE = "passportElementDriverLicense"
        PASSPORT_ELEMENT_EMAIL_ADDRESS = "passportElementEmailAddress"
        PASSPORT_ELEMENT_IDENTITY_CARD = "passportElementIdentityCard"
        PASSPORT_ELEMENT_INTERNAL_PASSPORT = "passportElementInternalPassport"
        PASSPORT_ELEMENT_PASSPORT = "passportElementPassport"
        PASSPORT_ELEMENT_PASSPORT_REGISTRATION = "passportElementPassportRegistration"
        PASSPORT_ELEMENT_PERSONAL_DETAILS = "passportElementPersonalDetails"
        PASSPORT_ELEMENT_PHONE_NUMBER = "passportElementPhoneNumber"
        PASSPORT_ELEMENT_RENTAL_AGREEMENT = "passportElementRentalAgreement"
        PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = "passportElementTemporaryRegistration"
        PASSPORT_ELEMENT_UTILITY_BILL = "passportElementUtilityBill"
        PASSPORT_ELEMENT_ERROR = "passportElementError"
        PASSPORT_ELEMENT_ERROR_SOURCE = "passportElementErrorSource"
        PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = "passportElementErrorSourceDataField"
        PASSPORT_ELEMENT_ERROR_SOURCE_FILE = "passportElementErrorSourceFile"
        PASSPORT_ELEMENT_ERROR_SOURCE_FILES = "passportElementErrorSourceFiles"
        PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = "passportElementErrorSourceFrontSide"
        PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = "passportElementErrorSourceReverseSide"
        PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = "passportElementErrorSourceSelfie"
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = "passportElementErrorSourceTranslationFile"
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = "passportElementErrorSourceTranslationFiles"
        PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = "passportElementErrorSourceUnspecified"
        PASSPORT_ELEMENT_TYPE = "passportElementType"
        PASSPORT_ELEMENT_TYPE_ADDRESS = "passportElementTypeAddress"
        PASSPORT_ELEMENT_TYPE_BANK_STATEMENT = "passportElementTypeBankStatement"
        PASSPORT_ELEMENT_TYPE_DRIVER_LICENSE = "passportElementTypeDriverLicense"
        PASSPORT_ELEMENT_TYPE_EMAIL_ADDRESS = "passportElementTypeEmailAddress"
        PASSPORT_ELEMENT_TYPE_IDENTITY_CARD = "passportElementTypeIdentityCard"
        PASSPORT_ELEMENT_TYPE_INTERNAL_PASSPORT = "passportElementTypeInternalPassport"
        PASSPORT_ELEMENT_TYPE_PASSPORT = "passportElementTypePassport"
        PASSPORT_ELEMENT_TYPE_PASSPORT_REGISTRATION = "passportElementTypePassportRegistration"
        PASSPORT_ELEMENT_TYPE_PERSONAL_DETAILS = "passportElementTypePersonalDetails"
        PASSPORT_ELEMENT_TYPE_PHONE_NUMBER = "passportElementTypePhoneNumber"
        PASSPORT_ELEMENT_TYPE_RENTAL_AGREEMENT = "passportElementTypeRentalAgreement"
        PASSPORT_ELEMENT_TYPE_TEMPORARY_REGISTRATION = "passportElementTypeTemporaryRegistration"
        PASSPORT_ELEMENT_TYPE_UTILITY_BILL = "passportElementTypeUtilityBill"
        PASSPORT_ELEMENTS = "passportElements"
        PASSPORT_ELEMENTS_WITH_ERRORS = "passportElementsWithErrors"
        PASSPORT_REQUIRED_ELEMENT = "passportRequiredElement"
        PASSPORT_SUITABLE_ELEMENT = "passportSuitableElement"
        PASSWORD_STATE = "passwordState"
        PAYMENT_FORM = "paymentForm"
        PAYMENT_OPTION = "paymentOption"
        PAYMENT_PROVIDER = "paymentProvider"
        PAYMENT_PROVIDER_OTHER = "paymentProviderOther"
        PAYMENT_PROVIDER_SMART_GLOCAL = "paymentProviderSmartGlocal"
        PAYMENT_PROVIDER_STRIPE = "paymentProviderStripe"
        PAYMENT_RECEIPT = "paymentReceipt"
        PAYMENT_RESULT = "paymentResult"
        PERSONAL_DETAILS = "personalDetails"
        PERSONAL_DOCUMENT = "personalDocument"
        PHONE_NUMBER_AUTHENTICATION_SETTINGS = "phoneNumberAuthenticationSettings"
        PHONE_NUMBER_INFO = "phoneNumberInfo"
        PHOTO = "photo"
        PHOTO_SIZE = "photoSize"
        PIN_CHAT_MESSAGE = "pinChatMessage"
        PING_PROXY = "pingProxy"
        POINT = "point"
        POLL = "poll"
        POLL_OPTION = "pollOption"
        POLL_TYPE = "pollType"
        POLL_TYPE_QUIZ = "pollTypeQuiz"
        POLL_TYPE_REGULAR = "pollTypeRegular"
        PRELIMINARY_UPLOAD_FILE = "preliminaryUploadFile"
        PREMIUM_FEATURE = "premiumFeature"
        PREMIUM_FEATURE_ADVANCED_CHAT_MANAGEMENT = "premiumFeatureAdvancedChatManagement"
        PREMIUM_FEATURE_ANIMATED_PROFILE_PHOTO = "premiumFeatureAnimatedProfilePhoto"
        PREMIUM_FEATURE_APP_ICONS = "premiumFeatureAppIcons"
        PREMIUM_FEATURE_CUSTOM_EMOJI = "premiumFeatureCustomEmoji"
        PREMIUM_FEATURE_DISABLED_ADS = "premiumFeatureDisabledAds"
        PREMIUM_FEATURE_EMOJI_STATUS = "premiumFeatureEmojiStatus"
        PREMIUM_FEATURE_FORUM_TOPIC_ICON = "premiumFeatureForumTopicIcon"
        PREMIUM_FEATURE_IMPROVED_DOWNLOAD_SPEED = "premiumFeatureImprovedDownloadSpeed"
        PREMIUM_FEATURE_INCREASED_LIMITS = "premiumFeatureIncreasedLimits"
        PREMIUM_FEATURE_INCREASED_UPLOAD_FILE_SIZE = "premiumFeatureIncreasedUploadFileSize"
        PREMIUM_FEATURE_PROFILE_BADGE = "premiumFeatureProfileBadge"
        PREMIUM_FEATURE_REAL_TIME_CHAT_TRANSLATION = "premiumFeatureRealTimeChatTranslation"
        PREMIUM_FEATURE_UNIQUE_REACTIONS = "premiumFeatureUniqueReactions"
        PREMIUM_FEATURE_UNIQUE_STICKERS = "premiumFeatureUniqueStickers"
        PREMIUM_FEATURE_UPGRADED_STORIES = "premiumFeatureUpgradedStories"
        PREMIUM_FEATURE_VOICE_RECOGNITION = "premiumFeatureVoiceRecognition"
        PREMIUM_FEATURE_PROMOTION_ANIMATION = "premiumFeaturePromotionAnimation"
        PREMIUM_FEATURES = "premiumFeatures"
        PREMIUM_LIMIT = "premiumLimit"
        PREMIUM_LIMIT_TYPE = "premiumLimitType"
        PREMIUM_LIMIT_TYPE_ACTIVE_STORY_COUNT = "premiumLimitTypeActiveStoryCount"
        PREMIUM_LIMIT_TYPE_BIO_LENGTH = "premiumLimitTypeBioLength"
        PREMIUM_LIMIT_TYPE_CAPTION_LENGTH = "premiumLimitTypeCaptionLength"
        PREMIUM_LIMIT_TYPE_CHAT_FOLDER_CHOSEN_CHAT_COUNT = "premiumLimitTypeChatFolderChosenChatCount"
        PREMIUM_LIMIT_TYPE_CHAT_FOLDER_COUNT = "premiumLimitTypeChatFolderCount"
        PREMIUM_LIMIT_TYPE_CHAT_FOLDER_INVITE_LINK_COUNT = "premiumLimitTypeChatFolderInviteLinkCount"
        PREMIUM_LIMIT_TYPE_CREATED_PUBLIC_CHAT_COUNT = "premiumLimitTypeCreatedPublicChatCount"
        PREMIUM_LIMIT_TYPE_FAVORITE_STICKER_COUNT = "premiumLimitTypeFavoriteStickerCount"
        PREMIUM_LIMIT_TYPE_MONTHLY_SENT_STORY_COUNT = "premiumLimitTypeMonthlySentStoryCount"
        PREMIUM_LIMIT_TYPE_PINNED_ARCHIVED_CHAT_COUNT = "premiumLimitTypePinnedArchivedChatCount"
        PREMIUM_LIMIT_TYPE_PINNED_CHAT_COUNT = "premiumLimitTypePinnedChatCount"
        PREMIUM_LIMIT_TYPE_SAVED_ANIMATION_COUNT = "premiumLimitTypeSavedAnimationCount"
        PREMIUM_LIMIT_TYPE_SHAREABLE_CHAT_FOLDER_COUNT = "premiumLimitTypeShareableChatFolderCount"
        PREMIUM_LIMIT_TYPE_STORY_CAPTION_LENGTH = "premiumLimitTypeStoryCaptionLength"
        PREMIUM_LIMIT_TYPE_SUPERGROUP_COUNT = "premiumLimitTypeSupergroupCount"
        PREMIUM_LIMIT_TYPE_WEEKLY_SENT_STORY_COUNT = "premiumLimitTypeWeeklySentStoryCount"
        PREMIUM_PAYMENT_OPTION = "premiumPaymentOption"
        PREMIUM_SOURCE = "premiumSource"
        PREMIUM_SOURCE_FEATURE = "premiumSourceFeature"
        PREMIUM_SOURCE_LIMIT_EXCEEDED = "premiumSourceLimitExceeded"
        PREMIUM_SOURCE_LINK = "premiumSourceLink"
        PREMIUM_SOURCE_SETTINGS = "premiumSourceSettings"
        PREMIUM_SOURCE_STORY_FEATURE = "premiumSourceStoryFeature"
        PREMIUM_STATE = "premiumState"
        PREMIUM_STATE_PAYMENT_OPTION = "premiumStatePaymentOption"
        PREMIUM_STORY_FEATURE = "premiumStoryFeature"
        PREMIUM_STORY_FEATURE_CUSTOM_EXPIRATION_DURATION = "premiumStoryFeatureCustomExpirationDuration"
        PREMIUM_STORY_FEATURE_LINKS_AND_FORMATTING = "premiumStoryFeatureLinksAndFormatting"
        PREMIUM_STORY_FEATURE_PERMANENT_VIEWS_HISTORY = "premiumStoryFeaturePermanentViewsHistory"
        PREMIUM_STORY_FEATURE_PRIORITY_ORDER = "premiumStoryFeaturePriorityOrder"
        PREMIUM_STORY_FEATURE_SAVE_STORIES = "premiumStoryFeatureSaveStories"
        PREMIUM_STORY_FEATURE_STEALTH_MODE = "premiumStoryFeatureStealthMode"
        PROCESS_CHAT_FOLDER_NEW_CHATS = "processChatFolderNewChats"
        PROCESS_CHAT_JOIN_REQUEST = "processChatJoinRequest"
        PROCESS_CHAT_JOIN_REQUESTS = "processChatJoinRequests"
        PROCESS_PUSH_NOTIFICATION = "processPushNotification"
        PROFILE_PHOTO = "profilePhoto"
        PROXIES = "proxies"
        PROXY = "proxy"
        PROXY_TYPE = "proxyType"
        PROXY_TYPE_HTTP = "proxyTypeHttp"
        PROXY_TYPE_MTPROTO = "proxyTypeMtproto"
        PROXY_TYPE_SOCKS5 = "proxyTypeSocks5"
        PUBLIC_CHAT_TYPE = "publicChatType"
        PUBLIC_CHAT_TYPE_HAS_USERNAME = "publicChatTypeHasUsername"
        PUBLIC_CHAT_TYPE_IS_LOCATION_BASED = "publicChatTypeIsLocationBased"
        PUSH_MESSAGE_CONTENT = "pushMessageContent"
        PUSH_MESSAGE_CONTENT_ANIMATION = "pushMessageContentAnimation"
        PUSH_MESSAGE_CONTENT_AUDIO = "pushMessageContentAudio"
        PUSH_MESSAGE_CONTENT_BASIC_GROUP_CHAT_CREATE = "pushMessageContentBasicGroupChatCreate"
        PUSH_MESSAGE_CONTENT_CHAT_ADD_MEMBERS = "pushMessageContentChatAddMembers"
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_PHOTO = "pushMessageContentChatChangePhoto"
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_TITLE = "pushMessageContentChatChangeTitle"
        PUSH_MESSAGE_CONTENT_CHAT_DELETE_MEMBER = "pushMessageContentChatDeleteMember"
        PUSH_MESSAGE_CONTENT_CHAT_JOIN_BY_LINK = "pushMessageContentChatJoinByLink"
        PUSH_MESSAGE_CONTENT_CHAT_JOIN_BY_REQUEST = "pushMessageContentChatJoinByRequest"
        PUSH_MESSAGE_CONTENT_CHAT_SET_BACKGROUND = "pushMessageContentChatSetBackground"
        PUSH_MESSAGE_CONTENT_CHAT_SET_THEME = "pushMessageContentChatSetTheme"
        PUSH_MESSAGE_CONTENT_CONTACT = "pushMessageContentContact"
        PUSH_MESSAGE_CONTENT_CONTACT_REGISTERED = "pushMessageContentContactRegistered"
        PUSH_MESSAGE_CONTENT_DOCUMENT = "pushMessageContentDocument"
        PUSH_MESSAGE_CONTENT_GAME = "pushMessageContentGame"
        PUSH_MESSAGE_CONTENT_GAME_SCORE = "pushMessageContentGameScore"
        PUSH_MESSAGE_CONTENT_HIDDEN = "pushMessageContentHidden"
        PUSH_MESSAGE_CONTENT_INVOICE = "pushMessageContentInvoice"
        PUSH_MESSAGE_CONTENT_LOCATION = "pushMessageContentLocation"
        PUSH_MESSAGE_CONTENT_MEDIA_ALBUM = "pushMessageContentMediaAlbum"
        PUSH_MESSAGE_CONTENT_MESSAGE_FORWARDS = "pushMessageContentMessageForwards"
        PUSH_MESSAGE_CONTENT_PHOTO = "pushMessageContentPhoto"
        PUSH_MESSAGE_CONTENT_POLL = "pushMessageContentPoll"
        PUSH_MESSAGE_CONTENT_RECURRING_PAYMENT = "pushMessageContentRecurringPayment"
        PUSH_MESSAGE_CONTENT_SCREENSHOT_TAKEN = "pushMessageContentScreenshotTaken"
        PUSH_MESSAGE_CONTENT_STICKER = "pushMessageContentSticker"
        PUSH_MESSAGE_CONTENT_STORY = "pushMessageContentStory"
        PUSH_MESSAGE_CONTENT_SUGGEST_PROFILE_PHOTO = "pushMessageContentSuggestProfilePhoto"
        PUSH_MESSAGE_CONTENT_TEXT = "pushMessageContentText"
        PUSH_MESSAGE_CONTENT_VIDEO = "pushMessageContentVideo"
        PUSH_MESSAGE_CONTENT_VIDEO_NOTE = "pushMessageContentVideoNote"
        PUSH_MESSAGE_CONTENT_VOICE_NOTE = "pushMessageContentVoiceNote"
        PUSH_RECEIVER_ID = "pushReceiverId"
        RATE_SPEECH_RECOGNITION = "rateSpeechRecognition"
        REACTION_TYPE = "reactionType"
        REACTION_TYPE_CUSTOM_EMOJI = "reactionTypeCustomEmoji"
        REACTION_TYPE_EMOJI = "reactionTypeEmoji"
        READ_ALL_CHAT_MENTIONS = "readAllChatMentions"
        READ_ALL_CHAT_REACTIONS = "readAllChatReactions"
        READ_ALL_MESSAGE_THREAD_MENTIONS = "readAllMessageThreadMentions"
        READ_ALL_MESSAGE_THREAD_REACTIONS = "readAllMessageThreadReactions"
        READ_CHAT_LIST = "readChatList"
        READ_FILE_PART = "readFilePart"
        RECOGNIZE_SPEECH = "recognizeSpeech"
        RECOMMENDED_CHAT_FOLDER = "recommendedChatFolder"
        RECOMMENDED_CHAT_FOLDERS = "recommendedChatFolders"
        RECOVER_AUTHENTICATION_PASSWORD = "recoverAuthenticationPassword"
        RECOVER_PASSWORD = "recoverPassword"
        RECOVERY_EMAIL_ADDRESS = "recoveryEmailAddress"
        REGISTER_DEVICE = "registerDevice"
        REGISTER_USER = "registerUser"
        REMOTE_FILE = "remoteFile"
        REMOVE_ALL_FILES_FROM_DOWNLOADS = "removeAllFilesFromDownloads"
        REMOVE_BACKGROUND = "removeBackground"
        REMOVE_CHAT_ACTION_BAR = "removeChatActionBar"
        REMOVE_CONTACTS = "removeContacts"
        REMOVE_FAVORITE_STICKER = "removeFavoriteSticker"
        REMOVE_FILE_FROM_DOWNLOADS = "removeFileFromDownloads"
        REMOVE_MESSAGE_REACTION = "removeMessageReaction"
        REMOVE_NOTIFICATION = "removeNotification"
        REMOVE_NOTIFICATION_GROUP = "removeNotificationGroup"
        REMOVE_PROXY = "removeProxy"
        REMOVE_RECENT_HASHTAG = "removeRecentHashtag"
        REMOVE_RECENT_STICKER = "removeRecentSticker"
        REMOVE_RECENTLY_FOUND_CHAT = "removeRecentlyFoundChat"
        REMOVE_SAVED_ANIMATION = "removeSavedAnimation"
        REMOVE_SAVED_NOTIFICATION_SOUND = "removeSavedNotificationSound"
        REMOVE_STICKER_FROM_SET = "removeStickerFromSet"
        REMOVE_TOP_CHAT = "removeTopChat"
        REORDER_ACTIVE_USERNAMES = "reorderActiveUsernames"
        REORDER_BOT_ACTIVE_USERNAMES = "reorderBotActiveUsernames"
        REORDER_CHAT_FOLDERS = "reorderChatFolders"
        REORDER_INSTALLED_STICKER_SETS = "reorderInstalledStickerSets"
        REORDER_SUPERGROUP_ACTIVE_USERNAMES = "reorderSupergroupActiveUsernames"
        REPLACE_PRIMARY_CHAT_INVITE_LINK = "replacePrimaryChatInviteLink"
        REPLACE_VIDEO_CHAT_RTMP_URL = "replaceVideoChatRtmpUrl"
        REPLY_MARKUP = "replyMarkup"
        REPLY_MARKUP_FORCE_REPLY = "replyMarkupForceReply"
        REPLY_MARKUP_INLINE_KEYBOARD = "replyMarkupInlineKeyboard"
        REPLY_MARKUP_REMOVE_KEYBOARD = "replyMarkupRemoveKeyboard"
        REPLY_MARKUP_SHOW_KEYBOARD = "replyMarkupShowKeyboard"
        REPORT_CHAT = "reportChat"
        REPORT_CHAT_PHOTO = "reportChatPhoto"
        REPORT_MESSAGE_REACTIONS = "reportMessageReactions"
        REPORT_REASON = "reportReason"
        REPORT_REASON_CHILD_ABUSE = "reportReasonChildAbuse"
        REPORT_REASON_COPYRIGHT = "reportReasonCopyright"
        REPORT_REASON_CUSTOM = "reportReasonCustom"
        REPORT_REASON_FAKE = "reportReasonFake"
        REPORT_REASON_ILLEGAL_DRUGS = "reportReasonIllegalDrugs"
        REPORT_REASON_PERSONAL_DETAILS = "reportReasonPersonalDetails"
        REPORT_REASON_PORNOGRAPHY = "reportReasonPornography"
        REPORT_REASON_SPAM = "reportReasonSpam"
        REPORT_REASON_UNRELATED_LOCATION = "reportReasonUnrelatedLocation"
        REPORT_REASON_VIOLENCE = "reportReasonViolence"
        REPORT_STORY = "reportStory"
        REPORT_SUPERGROUP_ANTI_SPAM_FALSE_POSITIVE = "reportSupergroupAntiSpamFalsePositive"
        REPORT_SUPERGROUP_SPAM = "reportSupergroupSpam"
        REQUEST_AUTHENTICATION_PASSWORD_RECOVERY = "requestAuthenticationPasswordRecovery"
        REQUEST_PASSWORD_RECOVERY = "requestPasswordRecovery"
        REQUEST_QR_CODE_AUTHENTICATION = "requestQrCodeAuthentication"
        RESEND_AUTHENTICATION_CODE = "resendAuthenticationCode"
        RESEND_CHANGE_PHONE_NUMBER_CODE = "resendChangePhoneNumberCode"
        RESEND_EMAIL_ADDRESS_VERIFICATION_CODE = "resendEmailAddressVerificationCode"
        RESEND_LOGIN_EMAIL_ADDRESS_CODE = "resendLoginEmailAddressCode"
        RESEND_MESSAGES = "resendMessages"
        RESEND_PHONE_NUMBER_CONFIRMATION_CODE = "resendPhoneNumberConfirmationCode"
        RESEND_PHONE_NUMBER_VERIFICATION_CODE = "resendPhoneNumberVerificationCode"
        RESEND_RECOVERY_EMAIL_ADDRESS_CODE = "resendRecoveryEmailAddressCode"
        RESET_ALL_NOTIFICATION_SETTINGS = "resetAllNotificationSettings"
        RESET_AUTHENTICATION_EMAIL_ADDRESS = "resetAuthenticationEmailAddress"
        RESET_BACKGROUNDS = "resetBackgrounds"
        RESET_NETWORK_STATISTICS = "resetNetworkStatistics"
        RESET_PASSWORD = "resetPassword"
        RESET_PASSWORD_RESULT = "resetPasswordResult"
        RESET_PASSWORD_RESULT_DECLINED = "resetPasswordResultDeclined"
        RESET_PASSWORD_RESULT_OK = "resetPasswordResultOk"
        RESET_PASSWORD_RESULT_PENDING = "resetPasswordResultPending"
        REVOKE_CHAT_INVITE_LINK = "revokeChatInviteLink"
        REVOKE_GROUP_CALL_INVITE_LINK = "revokeGroupCallInviteLink"
        RICH_TEXT = "richText"
        RICH_TEXT_ANCHOR = "richTextAnchor"
        RICH_TEXT_ANCHOR_LINK = "richTextAnchorLink"
        RICH_TEXT_BOLD = "richTextBold"
        RICH_TEXT_EMAIL_ADDRESS = "richTextEmailAddress"
        RICH_TEXT_FIXED = "richTextFixed"
        RICH_TEXT_ICON = "richTextIcon"
        RICH_TEXT_ITALIC = "richTextItalic"
        RICH_TEXT_MARKED = "richTextMarked"
        RICH_TEXT_PHONE_NUMBER = "richTextPhoneNumber"
        RICH_TEXT_PLAIN = "richTextPlain"
        RICH_TEXT_REFERENCE = "richTextReference"
        RICH_TEXT_STRIKETHROUGH = "richTextStrikethrough"
        RICH_TEXT_SUBSCRIPT = "richTextSubscript"
        RICH_TEXT_SUPERSCRIPT = "richTextSuperscript"
        RICH_TEXT_UNDERLINE = "richTextUnderline"
        RICH_TEXT_URL = "richTextUrl"
        RICH_TEXTS = "richTexts"
        RTMP_URL = "rtmpUrl"
        SAVE_APPLICATION_LOG_EVENT = "saveApplicationLogEvent"
        SAVED_CREDENTIALS = "savedCredentials"
        SCOPE_AUTOSAVE_SETTINGS = "scopeAutosaveSettings"
        SCOPE_NOTIFICATION_SETTINGS = "scopeNotificationSettings"
        SEARCH_BACKGROUND = "searchBackground"
        SEARCH_CALL_MESSAGES = "searchCallMessages"
        SEARCH_CHAT_MEMBERS = "searchChatMembers"
        SEARCH_CHAT_MESSAGES = "searchChatMessages"
        SEARCH_CHAT_RECENT_LOCATION_MESSAGES = "searchChatRecentLocationMessages"
        SEARCH_CHATS = "searchChats"
        SEARCH_CHATS_NEARBY = "searchChatsNearby"
        SEARCH_CHATS_ON_SERVER = "searchChatsOnServer"
        SEARCH_CONTACTS = "searchContacts"
        SEARCH_EMOJIS = "searchEmojis"
        SEARCH_FILE_DOWNLOADS = "searchFileDownloads"
        SEARCH_HASHTAGS = "searchHashtags"
        SEARCH_INSTALLED_STICKER_SETS = "searchInstalledStickerSets"
        SEARCH_MESSAGES = "searchMessages"
        SEARCH_MESSAGES_FILTER = "searchMessagesFilter"
        SEARCH_MESSAGES_FILTER_ANIMATION = "searchMessagesFilterAnimation"
        SEARCH_MESSAGES_FILTER_AUDIO = "searchMessagesFilterAudio"
        SEARCH_MESSAGES_FILTER_CHAT_PHOTO = "searchMessagesFilterChatPhoto"
        SEARCH_MESSAGES_FILTER_DOCUMENT = "searchMessagesFilterDocument"
        SEARCH_MESSAGES_FILTER_EMPTY = "searchMessagesFilterEmpty"
        SEARCH_MESSAGES_FILTER_FAILED_TO_SEND = "searchMessagesFilterFailedToSend"
        SEARCH_MESSAGES_FILTER_MENTION = "searchMessagesFilterMention"
        SEARCH_MESSAGES_FILTER_PHOTO = "searchMessagesFilterPhoto"
        SEARCH_MESSAGES_FILTER_PHOTO_AND_VIDEO = "searchMessagesFilterPhotoAndVideo"
        SEARCH_MESSAGES_FILTER_PINNED = "searchMessagesFilterPinned"
        SEARCH_MESSAGES_FILTER_UNREAD_MENTION = "searchMessagesFilterUnreadMention"
        SEARCH_MESSAGES_FILTER_UNREAD_REACTION = "searchMessagesFilterUnreadReaction"
        SEARCH_MESSAGES_FILTER_URL = "searchMessagesFilterUrl"
        SEARCH_MESSAGES_FILTER_VIDEO = "searchMessagesFilterVideo"
        SEARCH_MESSAGES_FILTER_VIDEO_NOTE = "searchMessagesFilterVideoNote"
        SEARCH_MESSAGES_FILTER_VOICE_AND_VIDEO_NOTE = "searchMessagesFilterVoiceAndVideoNote"
        SEARCH_MESSAGES_FILTER_VOICE_NOTE = "searchMessagesFilterVoiceNote"
        SEARCH_OUTGOING_DOCUMENT_MESSAGES = "searchOutgoingDocumentMessages"
        SEARCH_PUBLIC_CHAT = "searchPublicChat"
        SEARCH_PUBLIC_CHATS = "searchPublicChats"
        SEARCH_RECENTLY_FOUND_CHATS = "searchRecentlyFoundChats"
        SEARCH_SECRET_MESSAGES = "searchSecretMessages"
        SEARCH_STICKER_SET = "searchStickerSet"
        SEARCH_STICKER_SETS = "searchStickerSets"
        SEARCH_STICKERS = "searchStickers"
        SEARCH_STRINGS_BY_PREFIX = "searchStringsByPrefix"
        SEARCH_USER_BY_PHONE_NUMBER = "searchUserByPhoneNumber"
        SEARCH_USER_BY_TOKEN = "searchUserByToken"
        SEARCH_WEB_APP = "searchWebApp"
        SECONDS = "seconds"
        SECRET_CHAT = "secretChat"
        SECRET_CHAT_STATE = "secretChatState"
        SECRET_CHAT_STATE_CLOSED = "secretChatStateClosed"
        SECRET_CHAT_STATE_PENDING = "secretChatStatePending"
        SECRET_CHAT_STATE_READY = "secretChatStateReady"
        SEND_AUTHENTICATION_FIREBASE_SMS = "sendAuthenticationFirebaseSms"
        SEND_BOT_START_MESSAGE = "sendBotStartMessage"
        SEND_CALL_DEBUG_INFORMATION = "sendCallDebugInformation"
        SEND_CALL_LOG = "sendCallLog"
        SEND_CALL_RATING = "sendCallRating"
        SEND_CALL_SIGNALING_DATA = "sendCallSignalingData"
        SEND_CHAT_ACTION = "sendChatAction"
        SEND_CUSTOM_REQUEST = "sendCustomRequest"
        SEND_EMAIL_ADDRESS_VERIFICATION_CODE = "sendEmailAddressVerificationCode"
        SEND_INLINE_QUERY_RESULT_MESSAGE = "sendInlineQueryResultMessage"
        SEND_MESSAGE = "sendMessage"
        SEND_MESSAGE_ALBUM = "sendMessageAlbum"
        SEND_PASSPORT_AUTHORIZATION_FORM = "sendPassportAuthorizationForm"
        SEND_PAYMENT_FORM = "sendPaymentForm"
        SEND_PHONE_NUMBER_CONFIRMATION_CODE = "sendPhoneNumberConfirmationCode"
        SEND_PHONE_NUMBER_VERIFICATION_CODE = "sendPhoneNumberVerificationCode"
        SEND_STORY = "sendStory"
        SEND_WEB_APP_CUSTOM_REQUEST = "sendWebAppCustomRequest"
        SEND_WEB_APP_DATA = "sendWebAppData"
        SENT_WEB_APP_MESSAGE = "sentWebAppMessage"
        SESSION = "session"
        SESSION_TYPE = "sessionType"
        SESSION_TYPE_ANDROID = "sessionTypeAndroid"
        SESSION_TYPE_APPLE = "sessionTypeApple"
        SESSION_TYPE_BRAVE = "sessionTypeBrave"
        SESSION_TYPE_CHROME = "sessionTypeChrome"
        SESSION_TYPE_EDGE = "sessionTypeEdge"
        SESSION_TYPE_FIREFOX = "sessionTypeFirefox"
        SESSION_TYPE_IPAD = "sessionTypeIpad"
        SESSION_TYPE_IPHONE = "sessionTypeIphone"
        SESSION_TYPE_LINUX = "sessionTypeLinux"
        SESSION_TYPE_MAC = "sessionTypeMac"
        SESSION_TYPE_OPERA = "sessionTypeOpera"
        SESSION_TYPE_SAFARI = "sessionTypeSafari"
        SESSION_TYPE_UBUNTU = "sessionTypeUbuntu"
        SESSION_TYPE_UNKNOWN = "sessionTypeUnknown"
        SESSION_TYPE_VIVALDI = "sessionTypeVivaldi"
        SESSION_TYPE_WINDOWS = "sessionTypeWindows"
        SESSION_TYPE_XBOX = "sessionTypeXbox"
        SESSIONS = "sessions"
        SET_ACCOUNT_TTL = "setAccountTtl"
        SET_ALARM = "setAlarm"
        SET_ARCHIVE_CHAT_LIST_SETTINGS = "setArchiveChatListSettings"
        SET_AUTHENTICATION_EMAIL_ADDRESS = "setAuthenticationEmailAddress"
        SET_AUTHENTICATION_PHONE_NUMBER = "setAuthenticationPhoneNumber"
        SET_AUTO_DOWNLOAD_SETTINGS = "setAutoDownloadSettings"
        SET_AUTOSAVE_SETTINGS = "setAutosaveSettings"
        SET_BACKGROUND = "setBackground"
        SET_BIO = "setBio"
        SET_BOT_INFO_DESCRIPTION = "setBotInfoDescription"
        SET_BOT_INFO_SHORT_DESCRIPTION = "setBotInfoShortDescription"
        SET_BOT_NAME = "setBotName"
        SET_BOT_PROFILE_PHOTO = "setBotProfilePhoto"
        SET_BOT_UPDATES_STATUS = "setBotUpdatesStatus"
        SET_CHAT_ACTIVE_STORIES_LIST = "setChatActiveStoriesList"
        SET_CHAT_AVAILABLE_REACTIONS = "setChatAvailableReactions"
        SET_CHAT_BACKGROUND = "setChatBackground"
        SET_CHAT_CLIENT_DATA = "setChatClientData"
        SET_CHAT_DESCRIPTION = "setChatDescription"
        SET_CHAT_DISCUSSION_GROUP = "setChatDiscussionGroup"
        SET_CHAT_DRAFT_MESSAGE = "setChatDraftMessage"
        SET_CHAT_LOCATION = "setChatLocation"
        SET_CHAT_MEMBER_STATUS = "setChatMemberStatus"
        SET_CHAT_MESSAGE_AUTO_DELETE_TIME = "setChatMessageAutoDeleteTime"
        SET_CHAT_MESSAGE_SENDER = "setChatMessageSender"
        SET_CHAT_NOTIFICATION_SETTINGS = "setChatNotificationSettings"
        SET_CHAT_PERMISSIONS = "setChatPermissions"
        SET_CHAT_PHOTO = "setChatPhoto"
        SET_CHAT_SLOW_MODE_DELAY = "setChatSlowModeDelay"
        SET_CHAT_THEME = "setChatTheme"
        SET_CHAT_TITLE = "setChatTitle"
        SET_CLOSE_FRIENDS = "setCloseFriends"
        SET_COMMANDS = "setCommands"
        SET_CUSTOM_EMOJI_STICKER_SET_THUMBNAIL = "setCustomEmojiStickerSetThumbnail"
        SET_CUSTOM_LANGUAGE_PACK = "setCustomLanguagePack"
        SET_CUSTOM_LANGUAGE_PACK_STRING = "setCustomLanguagePackString"
        SET_DATABASE_ENCRYPTION_KEY = "setDatabaseEncryptionKey"
        SET_DEFAULT_CHANNEL_ADMINISTRATOR_RIGHTS = "setDefaultChannelAdministratorRights"
        SET_DEFAULT_GROUP_ADMINISTRATOR_RIGHTS = "setDefaultGroupAdministratorRights"
        SET_DEFAULT_MESSAGE_AUTO_DELETE_TIME = "setDefaultMessageAutoDeleteTime"
        SET_DEFAULT_REACTION_TYPE = "setDefaultReactionType"
        SET_EMOJI_STATUS = "setEmojiStatus"
        SET_FILE_GENERATION_PROGRESS = "setFileGenerationProgress"
        SET_FORUM_TOPIC_NOTIFICATION_SETTINGS = "setForumTopicNotificationSettings"
        SET_GAME_SCORE = "setGameScore"
        SET_GROUP_CALL_PARTICIPANT_IS_SPEAKING = "setGroupCallParticipantIsSpeaking"
        SET_GROUP_CALL_PARTICIPANT_VOLUME_LEVEL = "setGroupCallParticipantVolumeLevel"
        SET_GROUP_CALL_TITLE = "setGroupCallTitle"
        SET_INACTIVE_SESSION_TTL = "setInactiveSessionTtl"
        SET_INLINE_GAME_SCORE = "setInlineGameScore"
        SET_LOCATION = "setLocation"
        SET_LOG_STREAM = "setLogStream"
        SET_LOG_TAG_VERBOSITY_LEVEL = "setLogTagVerbosityLevel"
        SET_LOG_VERBOSITY_LEVEL = "setLogVerbosityLevel"
        SET_LOGIN_EMAIL_ADDRESS = "setLoginEmailAddress"
        SET_MENU_BUTTON = "setMenuButton"
        SET_MESSAGE_SENDER_BLOCK_LIST = "setMessageSenderBlockList"
        SET_NAME = "setName"
        SET_NETWORK_TYPE = "setNetworkType"
        SET_OPTION = "setOption"
        SET_PASSPORT_ELEMENT = "setPassportElement"
        SET_PASSPORT_ELEMENT_ERRORS = "setPassportElementErrors"
        SET_PASSWORD = "setPassword"
        SET_PINNED_CHATS = "setPinnedChats"
        SET_PINNED_FORUM_TOPICS = "setPinnedForumTopics"
        SET_POLL_ANSWER = "setPollAnswer"
        SET_PROFILE_PHOTO = "setProfilePhoto"
        SET_RECOVERY_EMAIL_ADDRESS = "setRecoveryEmailAddress"
        SET_SCOPE_NOTIFICATION_SETTINGS = "setScopeNotificationSettings"
        SET_STICKER_EMOJIS = "setStickerEmojis"
        SET_STICKER_KEYWORDS = "setStickerKeywords"
        SET_STICKER_MASK_POSITION = "setStickerMaskPosition"
        SET_STICKER_POSITION_IN_SET = "setStickerPositionInSet"
        SET_STICKER_SET_THUMBNAIL = "setStickerSetThumbnail"
        SET_STICKER_SET_TITLE = "setStickerSetTitle"
        SET_STORY_PRIVACY_SETTINGS = "setStoryPrivacySettings"
        SET_STORY_REACTION = "setStoryReaction"
        SET_SUPERGROUP_STICKER_SET = "setSupergroupStickerSet"
        SET_SUPERGROUP_USERNAME = "setSupergroupUsername"
        SET_TDLIB_PARAMETERS = "setTdlibParameters"
        SET_USER_PERSONAL_PROFILE_PHOTO = "setUserPersonalProfilePhoto"
        SET_USER_PRIVACY_SETTING_RULES = "setUserPrivacySettingRules"
        SET_USER_SUPPORT_INFO = "setUserSupportInfo"
        SET_USERNAME = "setUsername"
        SET_VIDEO_CHAT_DEFAULT_PARTICIPANT = "setVideoChatDefaultParticipant"
        SHARE_CHAT_WITH_BOT = "shareChatWithBot"
        SHARE_PHONE_NUMBER = "sharePhoneNumber"
        SHARE_USER_WITH_BOT = "shareUserWithBot"
        SHIPPING_OPTION = "shippingOption"
        SPEECH_RECOGNITION_RESULT = "speechRecognitionResult"
        SPEECH_RECOGNITION_RESULT_ERROR = "speechRecognitionResultError"
        SPEECH_RECOGNITION_RESULT_PENDING = "speechRecognitionResultPending"
        SPEECH_RECOGNITION_RESULT_TEXT = "speechRecognitionResultText"
        SPONSORED_MESSAGE = "sponsoredMessage"
        SPONSORED_MESSAGES = "sponsoredMessages"
        START_GROUP_CALL_RECORDING = "startGroupCallRecording"
        START_GROUP_CALL_SCREEN_SHARING = "startGroupCallScreenSharing"
        START_SCHEDULED_GROUP_CALL = "startScheduledGroupCall"
        STATISTICAL_GRAPH = "statisticalGraph"
        STATISTICAL_GRAPH_ASYNC = "statisticalGraphAsync"
        STATISTICAL_GRAPH_DATA = "statisticalGraphData"
        STATISTICAL_GRAPH_ERROR = "statisticalGraphError"
        STATISTICAL_VALUE = "statisticalValue"
        STICKER = "sticker"
        STICKER_FORMAT = "stickerFormat"
        STICKER_FORMAT_TGS = "stickerFormatTgs"
        STICKER_FORMAT_WEBM = "stickerFormatWebm"
        STICKER_FORMAT_WEBP = "stickerFormatWebp"
        STICKER_FULL_TYPE = "stickerFullType"
        STICKER_FULL_TYPE_CUSTOM_EMOJI = "stickerFullTypeCustomEmoji"
        STICKER_FULL_TYPE_MASK = "stickerFullTypeMask"
        STICKER_FULL_TYPE_REGULAR = "stickerFullTypeRegular"
        STICKER_SET = "stickerSet"
        STICKER_SET_INFO = "stickerSetInfo"
        STICKER_SETS = "stickerSets"
        STICKER_TYPE = "stickerType"
        STICKER_TYPE_CUSTOM_EMOJI = "stickerTypeCustomEmoji"
        STICKER_TYPE_MASK = "stickerTypeMask"
        STICKER_TYPE_REGULAR = "stickerTypeRegular"
        STICKERS = "stickers"
        STOP_POLL = "stopPoll"
        STORAGE_STATISTICS = "storageStatistics"
        STORAGE_STATISTICS_BY_CHAT = "storageStatisticsByChat"
        STORAGE_STATISTICS_BY_FILE_TYPE = "storageStatisticsByFileType"
        STORAGE_STATISTICS_FAST = "storageStatisticsFast"
        STORE_PAYMENT_PURPOSE = "storePaymentPurpose"
        STORE_PAYMENT_PURPOSE_GIFTED_PREMIUM = "storePaymentPurposeGiftedPremium"
        STORE_PAYMENT_PURPOSE_PREMIUM_SUBSCRIPTION = "storePaymentPurposePremiumSubscription"
        STORIES = "stories"
        STORY = "story"
        STORY_AREA = "storyArea"
        STORY_AREA_POSITION = "storyAreaPosition"
        STORY_AREA_TYPE = "storyAreaType"
        STORY_AREA_TYPE_LOCATION = "storyAreaTypeLocation"
        STORY_AREA_TYPE_VENUE = "storyAreaTypeVenue"
        STORY_CONTENT = "storyContent"
        STORY_CONTENT_PHOTO = "storyContentPhoto"
        STORY_CONTENT_UNSUPPORTED = "storyContentUnsupported"
        STORY_CONTENT_VIDEO = "storyContentVideo"
        STORY_INFO = "storyInfo"
        STORY_INTERACTION_INFO = "storyInteractionInfo"
        STORY_LIST = "storyList"
        STORY_LIST_ARCHIVE = "storyListArchive"
        STORY_LIST_MAIN = "storyListMain"
        STORY_PRIVACY_SETTINGS = "storyPrivacySettings"
        STORY_PRIVACY_SETTINGS_CLOSE_FRIENDS = "storyPrivacySettingsCloseFriends"
        STORY_PRIVACY_SETTINGS_CONTACTS = "storyPrivacySettingsContacts"
        STORY_PRIVACY_SETTINGS_EVERYONE = "storyPrivacySettingsEveryone"
        STORY_PRIVACY_SETTINGS_SELECTED_USERS = "storyPrivacySettingsSelectedUsers"
        STORY_VIDEO = "storyVideo"
        STORY_VIEWER = "storyViewer"
        STORY_VIEWERS = "storyViewers"
        SUGGEST_USER_PROFILE_PHOTO = "suggestUserProfilePhoto"
        SUGGESTED_ACTION = "suggestedAction"
        SUGGESTED_ACTION_CHECK_PASSWORD = "suggestedActionCheckPassword"
        SUGGESTED_ACTION_CHECK_PHONE_NUMBER = "suggestedActionCheckPhoneNumber"
        SUGGESTED_ACTION_CONVERT_TO_BROADCAST_GROUP = "suggestedActionConvertToBroadcastGroup"
        SUGGESTED_ACTION_ENABLE_ARCHIVE_AND_MUTE_NEW_CHATS = "suggestedActionEnableArchiveAndMuteNewChats"
        SUGGESTED_ACTION_RESTORE_PREMIUM = "suggestedActionRestorePremium"
        SUGGESTED_ACTION_SET_PASSWORD = "suggestedActionSetPassword"
        SUGGESTED_ACTION_SUBSCRIBE_TO_ANNUAL_PREMIUM = "suggestedActionSubscribeToAnnualPremium"
        SUGGESTED_ACTION_UPGRADE_PREMIUM = "suggestedActionUpgradePremium"
        SUGGESTED_ACTION_VIEW_CHECKS_HINT = "suggestedActionViewChecksHint"
        SUPERGROUP = "supergroup"
        SUPERGROUP_FULL_INFO = "supergroupFullInfo"
        SUPERGROUP_MEMBERS_FILTER = "supergroupMembersFilter"
        SUPERGROUP_MEMBERS_FILTER_ADMINISTRATORS = "supergroupMembersFilterAdministrators"
        SUPERGROUP_MEMBERS_FILTER_BANNED = "supergroupMembersFilterBanned"
        SUPERGROUP_MEMBERS_FILTER_BOTS = "supergroupMembersFilterBots"
        SUPERGROUP_MEMBERS_FILTER_CONTACTS = "supergroupMembersFilterContacts"
        SUPERGROUP_MEMBERS_FILTER_MENTION = "supergroupMembersFilterMention"
        SUPERGROUP_MEMBERS_FILTER_RECENT = "supergroupMembersFilterRecent"
        SUPERGROUP_MEMBERS_FILTER_RESTRICTED = "supergroupMembersFilterRestricted"
        SUPERGROUP_MEMBERS_FILTER_SEARCH = "supergroupMembersFilterSearch"
        SYNCHRONIZE_LANGUAGE_PACK = "synchronizeLanguagePack"
        T_ME_URL = "tMeUrl"
        T_ME_URL_TYPE = "tMeUrlType"
        T_ME_URL_TYPE_CHAT_INVITE = "tMeUrlTypeChatInvite"
        T_ME_URL_TYPE_STICKER_SET = "tMeUrlTypeStickerSet"
        T_ME_URL_TYPE_SUPERGROUP = "tMeUrlTypeSupergroup"
        T_ME_URL_TYPE_USER = "tMeUrlTypeUser"
        T_ME_URLS = "tMeUrls"
        TARGET_CHAT = "targetChat"
        TARGET_CHAT_CHOSEN = "targetChatChosen"
        TARGET_CHAT_CURRENT = "targetChatCurrent"
        TARGET_CHAT_INTERNAL_LINK = "targetChatInternalLink"
        TEMPORARY_PASSWORD_STATE = "temporaryPasswordState"
        TERMINATE_ALL_OTHER_SESSIONS = "terminateAllOtherSessions"
        TERMINATE_SESSION = "terminateSession"
        TERMS_OF_SERVICE = "termsOfService"
        TEST_BYTES = "testBytes"
        TEST_CALL_BYTES = "testCallBytes"
        TEST_CALL_EMPTY = "testCallEmpty"
        TEST_CALL_STRING = "testCallString"
        TEST_CALL_VECTOR_INT = "testCallVectorInt"
        TEST_CALL_VECTOR_INT_OBJECT = "testCallVectorIntObject"
        TEST_CALL_VECTOR_STRING = "testCallVectorString"
        TEST_CALL_VECTOR_STRING_OBJECT = "testCallVectorStringObject"
        TEST_GET_DIFFERENCE = "testGetDifference"
        TEST_INT = "testInt"
        TEST_NETWORK = "testNetwork"
        TEST_PROXY = "testProxy"
        TEST_RETURN_ERROR = "testReturnError"
        TEST_SQUARE_INT = "testSquareInt"
        TEST_STRING = "testString"
        TEST_USE_UPDATE = "testUseUpdate"
        TEST_VECTOR_INT = "testVectorInt"
        TEST_VECTOR_INT_OBJECT = "testVectorIntObject"
        TEST_VECTOR_STRING = "testVectorString"
        TEST_VECTOR_STRING_OBJECT = "testVectorStringObject"
        TEXT = "text"
        TEXT_ENTITIES = "textEntities"
        TEXT_ENTITY = "textEntity"
        TEXT_ENTITY_TYPE = "textEntityType"
        TEXT_ENTITY_TYPE_BANK_CARD_NUMBER = "textEntityTypeBankCardNumber"
        TEXT_ENTITY_TYPE_BOLD = "textEntityTypeBold"
        TEXT_ENTITY_TYPE_BOT_COMMAND = "textEntityTypeBotCommand"
        TEXT_ENTITY_TYPE_CASHTAG = "textEntityTypeCashtag"
        TEXT_ENTITY_TYPE_CODE = "textEntityTypeCode"
        TEXT_ENTITY_TYPE_CUSTOM_EMOJI = "textEntityTypeCustomEmoji"
        TEXT_ENTITY_TYPE_EMAIL_ADDRESS = "textEntityTypeEmailAddress"
        TEXT_ENTITY_TYPE_HASHTAG = "textEntityTypeHashtag"
        TEXT_ENTITY_TYPE_ITALIC = "textEntityTypeItalic"
        TEXT_ENTITY_TYPE_MEDIA_TIMESTAMP = "textEntityTypeMediaTimestamp"
        TEXT_ENTITY_TYPE_MENTION = "textEntityTypeMention"
        TEXT_ENTITY_TYPE_MENTION_NAME = "textEntityTypeMentionName"
        TEXT_ENTITY_TYPE_PHONE_NUMBER = "textEntityTypePhoneNumber"
        TEXT_ENTITY_TYPE_PRE = "textEntityTypePre"
        TEXT_ENTITY_TYPE_PRE_CODE = "textEntityTypePreCode"
        TEXT_ENTITY_TYPE_SPOILER = "textEntityTypeSpoiler"
        TEXT_ENTITY_TYPE_STRIKETHROUGH = "textEntityTypeStrikethrough"
        TEXT_ENTITY_TYPE_TEXT_URL = "textEntityTypeTextUrl"
        TEXT_ENTITY_TYPE_UNDERLINE = "textEntityTypeUnderline"
        TEXT_ENTITY_TYPE_URL = "textEntityTypeUrl"
        TEXT_PARSE_MODE = "textParseMode"
        TEXT_PARSE_MODE_HTML = "textParseModeHTML"
        TEXT_PARSE_MODE_MARKDOWN = "textParseModeMarkdown"
        THEME_PARAMETERS = "themeParameters"
        THEME_SETTINGS = "themeSettings"
        THUMBNAIL = "thumbnail"
        THUMBNAIL_FORMAT = "thumbnailFormat"
        THUMBNAIL_FORMAT_GIF = "thumbnailFormatGif"
        THUMBNAIL_FORMAT_JPEG = "thumbnailFormatJpeg"
        THUMBNAIL_FORMAT_MPEG4 = "thumbnailFormatMpeg4"
        THUMBNAIL_FORMAT_PNG = "thumbnailFormatPng"
        THUMBNAIL_FORMAT_TGS = "thumbnailFormatTgs"
        THUMBNAIL_FORMAT_WEBM = "thumbnailFormatWebm"
        THUMBNAIL_FORMAT_WEBP = "thumbnailFormatWebp"
        TOGGLE_ALL_DOWNLOADS_ARE_PAUSED = "toggleAllDownloadsArePaused"
        TOGGLE_BOT_IS_ADDED_TO_ATTACHMENT_MENU = "toggleBotIsAddedToAttachmentMenu"
        TOGGLE_BOT_USERNAME_IS_ACTIVE = "toggleBotUsernameIsActive"
        TOGGLE_CHAT_DEFAULT_DISABLE_NOTIFICATION = "toggleChatDefaultDisableNotification"
        TOGGLE_CHAT_HAS_PROTECTED_CONTENT = "toggleChatHasProtectedContent"
        TOGGLE_CHAT_IS_MARKED_AS_UNREAD = "toggleChatIsMarkedAsUnread"
        TOGGLE_CHAT_IS_PINNED = "toggleChatIsPinned"
        TOGGLE_CHAT_IS_TRANSLATABLE = "toggleChatIsTranslatable"
        TOGGLE_DOWNLOAD_IS_PAUSED = "toggleDownloadIsPaused"
        TOGGLE_FORUM_TOPIC_IS_CLOSED = "toggleForumTopicIsClosed"
        TOGGLE_FORUM_TOPIC_IS_PINNED = "toggleForumTopicIsPinned"
        TOGGLE_GENERAL_FORUM_TOPIC_IS_HIDDEN = "toggleGeneralForumTopicIsHidden"
        TOGGLE_GROUP_CALL_ENABLED_START_NOTIFICATION = "toggleGroupCallEnabledStartNotification"
        TOGGLE_GROUP_CALL_IS_MY_VIDEO_ENABLED = "toggleGroupCallIsMyVideoEnabled"
        TOGGLE_GROUP_CALL_IS_MY_VIDEO_PAUSED = "toggleGroupCallIsMyVideoPaused"
        TOGGLE_GROUP_CALL_MUTE_NEW_PARTICIPANTS = "toggleGroupCallMuteNewParticipants"
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_HAND_RAISED = "toggleGroupCallParticipantIsHandRaised"
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_MUTED = "toggleGroupCallParticipantIsMuted"
        TOGGLE_GROUP_CALL_SCREEN_SHARING_IS_PAUSED = "toggleGroupCallScreenSharingIsPaused"
        TOGGLE_SESSION_CAN_ACCEPT_CALLS = "toggleSessionCanAcceptCalls"
        TOGGLE_SESSION_CAN_ACCEPT_SECRET_CHATS = "toggleSessionCanAcceptSecretChats"
        TOGGLE_STORY_IS_PINNED = "toggleStoryIsPinned"
        TOGGLE_SUPERGROUP_HAS_AGGRESSIVE_ANTI_SPAM_ENABLED = "toggleSupergroupHasAggressiveAntiSpamEnabled"
        TOGGLE_SUPERGROUP_HAS_HIDDEN_MEMBERS = "toggleSupergroupHasHiddenMembers"
        TOGGLE_SUPERGROUP_IS_ALL_HISTORY_AVAILABLE = "toggleSupergroupIsAllHistoryAvailable"
        TOGGLE_SUPERGROUP_IS_BROADCAST_GROUP = "toggleSupergroupIsBroadcastGroup"
        TOGGLE_SUPERGROUP_IS_FORUM = "toggleSupergroupIsForum"
        TOGGLE_SUPERGROUP_JOIN_BY_REQUEST = "toggleSupergroupJoinByRequest"
        TOGGLE_SUPERGROUP_JOIN_TO_SEND_MESSAGES = "toggleSupergroupJoinToSendMessages"
        TOGGLE_SUPERGROUP_SIGN_MESSAGES = "toggleSupergroupSignMessages"
        TOGGLE_SUPERGROUP_USERNAME_IS_ACTIVE = "toggleSupergroupUsernameIsActive"
        TOGGLE_USERNAME_IS_ACTIVE = "toggleUsernameIsActive"
        TOP_CHAT_CATEGORY = "topChatCategory"
        TOP_CHAT_CATEGORY_BOTS = "topChatCategoryBots"
        TOP_CHAT_CATEGORY_CALLS = "topChatCategoryCalls"
        TOP_CHAT_CATEGORY_CHANNELS = "topChatCategoryChannels"
        TOP_CHAT_CATEGORY_FORWARD_CHATS = "topChatCategoryForwardChats"
        TOP_CHAT_CATEGORY_GROUPS = "topChatCategoryGroups"
        TOP_CHAT_CATEGORY_INLINE_BOTS = "topChatCategoryInlineBots"
        TOP_CHAT_CATEGORY_USERS = "topChatCategoryUsers"
        TRANSFER_CHAT_OWNERSHIP = "transferChatOwnership"
        TRANSLATE_MESSAGE_TEXT = "translateMessageText"
        TRANSLATE_TEXT = "translateText"
        TRENDING_STICKER_SETS = "trendingStickerSets"
        UNCONFIRMED_SESSION = "unconfirmedSession"
        UNPIN_ALL_CHAT_MESSAGES = "unpinAllChatMessages"
        UNPIN_ALL_MESSAGE_THREAD_MESSAGES = "unpinAllMessageThreadMessages"
        UNPIN_CHAT_MESSAGE = "unpinChatMessage"
        UNREAD_REACTION = "unreadReaction"
        UPDATE = "update"
        UPDATE_ACTIVE_EMOJI_REACTIONS = "updateActiveEmojiReactions"
        UPDATE_ACTIVE_NOTIFICATIONS = "updateActiveNotifications"
        UPDATE_ADD_CHAT_MEMBERS_PRIVACY_FORBIDDEN = "updateAddChatMembersPrivacyForbidden"
        UPDATE_ANIMATED_EMOJI_MESSAGE_CLICKED = "updateAnimatedEmojiMessageClicked"
        UPDATE_ANIMATION_SEARCH_PARAMETERS = "updateAnimationSearchParameters"
        UPDATE_ATTACHMENT_MENU_BOTS = "updateAttachmentMenuBots"
        UPDATE_AUTHORIZATION_STATE = "updateAuthorizationState"
        UPDATE_AUTOSAVE_SETTINGS = "updateAutosaveSettings"
        UPDATE_BASIC_GROUP = "updateBasicGroup"
        UPDATE_BASIC_GROUP_FULL_INFO = "updateBasicGroupFullInfo"
        UPDATE_CALL = "updateCall"
        UPDATE_CHAT_ACTION = "updateChatAction"
        UPDATE_CHAT_ACTION_BAR = "updateChatActionBar"
        UPDATE_CHAT_ACTIVE_STORIES = "updateChatActiveStories"
        UPDATE_CHAT_AVAILABLE_REACTIONS = "updateChatAvailableReactions"
        UPDATE_CHAT_BACKGROUND = "updateChatBackground"
        UPDATE_CHAT_BLOCK_LIST = "updateChatBlockList"
        UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION = "updateChatDefaultDisableNotification"
        UPDATE_CHAT_DRAFT_MESSAGE = "updateChatDraftMessage"
        UPDATE_CHAT_FOLDERS = "updateChatFolders"
        UPDATE_CHAT_HAS_PROTECTED_CONTENT = "updateChatHasProtectedContent"
        UPDATE_CHAT_HAS_SCHEDULED_MESSAGES = "updateChatHasScheduledMessages"
        UPDATE_CHAT_IS_MARKED_AS_UNREAD = "updateChatIsMarkedAsUnread"
        UPDATE_CHAT_IS_TRANSLATABLE = "updateChatIsTranslatable"
        UPDATE_CHAT_LAST_MESSAGE = "updateChatLastMessage"
        UPDATE_CHAT_MEMBER = "updateChatMember"
        UPDATE_CHAT_MESSAGE_AUTO_DELETE_TIME = "updateChatMessageAutoDeleteTime"
        UPDATE_CHAT_MESSAGE_SENDER = "updateChatMessageSender"
        UPDATE_CHAT_NOTIFICATION_SETTINGS = "updateChatNotificationSettings"
        UPDATE_CHAT_ONLINE_MEMBER_COUNT = "updateChatOnlineMemberCount"
        UPDATE_CHAT_PENDING_JOIN_REQUESTS = "updateChatPendingJoinRequests"
        UPDATE_CHAT_PERMISSIONS = "updateChatPermissions"
        UPDATE_CHAT_PHOTO = "updateChatPhoto"
        UPDATE_CHAT_POSITION = "updateChatPosition"
        UPDATE_CHAT_READ_INBOX = "updateChatReadInbox"
        UPDATE_CHAT_READ_OUTBOX = "updateChatReadOutbox"
        UPDATE_CHAT_REPLY_MARKUP = "updateChatReplyMarkup"
        UPDATE_CHAT_THEME = "updateChatTheme"
        UPDATE_CHAT_THEMES = "updateChatThemes"
        UPDATE_CHAT_TITLE = "updateChatTitle"
        UPDATE_CHAT_UNREAD_MENTION_COUNT = "updateChatUnreadMentionCount"
        UPDATE_CHAT_UNREAD_REACTION_COUNT = "updateChatUnreadReactionCount"
        UPDATE_CHAT_VIDEO_CHAT = "updateChatVideoChat"
        UPDATE_CONNECTION_STATE = "updateConnectionState"
        UPDATE_DEFAULT_REACTION_TYPE = "updateDefaultReactionType"
        UPDATE_DELETE_MESSAGES = "updateDeleteMessages"
        UPDATE_DICE_EMOJIS = "updateDiceEmojis"
        UPDATE_FAVORITE_STICKERS = "updateFavoriteStickers"
        UPDATE_FILE = "updateFile"
        UPDATE_FILE_ADDED_TO_DOWNLOADS = "updateFileAddedToDownloads"
        UPDATE_FILE_DOWNLOAD = "updateFileDownload"
        UPDATE_FILE_DOWNLOADS = "updateFileDownloads"
        UPDATE_FILE_GENERATION_START = "updateFileGenerationStart"
        UPDATE_FILE_GENERATION_STOP = "updateFileGenerationStop"
        UPDATE_FILE_REMOVED_FROM_DOWNLOADS = "updateFileRemovedFromDownloads"
        UPDATE_FORUM_TOPIC_INFO = "updateForumTopicInfo"
        UPDATE_GROUP_CALL = "updateGroupCall"
        UPDATE_GROUP_CALL_PARTICIPANT = "updateGroupCallParticipant"
        UPDATE_HAVE_PENDING_NOTIFICATIONS = "updateHavePendingNotifications"
        UPDATE_INSTALLED_STICKER_SETS = "updateInstalledStickerSets"
        UPDATE_LANGUAGE_PACK_STRINGS = "updateLanguagePackStrings"
        UPDATE_MESSAGE_CONTENT = "updateMessageContent"
        UPDATE_MESSAGE_CONTENT_OPENED = "updateMessageContentOpened"
        UPDATE_MESSAGE_EDITED = "updateMessageEdited"
        UPDATE_MESSAGE_INTERACTION_INFO = "updateMessageInteractionInfo"
        UPDATE_MESSAGE_IS_PINNED = "updateMessageIsPinned"
        UPDATE_MESSAGE_LIVE_LOCATION_VIEWED = "updateMessageLiveLocationViewed"
        UPDATE_MESSAGE_MENTION_READ = "updateMessageMentionRead"
        UPDATE_MESSAGE_SEND_ACKNOWLEDGED = "updateMessageSendAcknowledged"
        UPDATE_MESSAGE_SEND_FAILED = "updateMessageSendFailed"
        UPDATE_MESSAGE_SEND_SUCCEEDED = "updateMessageSendSucceeded"
        UPDATE_MESSAGE_UNREAD_REACTIONS = "updateMessageUnreadReactions"
        UPDATE_NEW_CALL_SIGNALING_DATA = "updateNewCallSignalingData"
        UPDATE_NEW_CALLBACK_QUERY = "updateNewCallbackQuery"
        UPDATE_NEW_CHAT = "updateNewChat"
        UPDATE_NEW_CHAT_JOIN_REQUEST = "updateNewChatJoinRequest"
        UPDATE_NEW_CHOSEN_INLINE_RESULT = "updateNewChosenInlineResult"
        UPDATE_NEW_CUSTOM_EVENT = "updateNewCustomEvent"
        UPDATE_NEW_CUSTOM_QUERY = "updateNewCustomQuery"
        UPDATE_NEW_INLINE_CALLBACK_QUERY = "updateNewInlineCallbackQuery"
        UPDATE_NEW_INLINE_QUERY = "updateNewInlineQuery"
        UPDATE_NEW_MESSAGE = "updateNewMessage"
        UPDATE_NEW_PRE_CHECKOUT_QUERY = "updateNewPreCheckoutQuery"
        UPDATE_NEW_SHIPPING_QUERY = "updateNewShippingQuery"
        UPDATE_NOTIFICATION = "updateNotification"
        UPDATE_NOTIFICATION_GROUP = "updateNotificationGroup"
        UPDATE_OPTION = "updateOption"
        UPDATE_POLL = "updatePoll"
        UPDATE_POLL_ANSWER = "updatePollAnswer"
        UPDATE_RECENT_STICKERS = "updateRecentStickers"
        UPDATE_SAVED_ANIMATIONS = "updateSavedAnimations"
        UPDATE_SAVED_NOTIFICATION_SOUNDS = "updateSavedNotificationSounds"
        UPDATE_SCOPE_NOTIFICATION_SETTINGS = "updateScopeNotificationSettings"
        UPDATE_SECRET_CHAT = "updateSecretChat"
        UPDATE_SELECTED_BACKGROUND = "updateSelectedBackground"
        UPDATE_SERVICE_NOTIFICATION = "updateServiceNotification"
        UPDATE_STICKER_SET = "updateStickerSet"
        UPDATE_STORY = "updateStory"
        UPDATE_STORY_DELETED = "updateStoryDeleted"
        UPDATE_STORY_LIST_CHAT_COUNT = "updateStoryListChatCount"
        UPDATE_STORY_SEND_FAILED = "updateStorySendFailed"
        UPDATE_STORY_SEND_SUCCEEDED = "updateStorySendSucceeded"
        UPDATE_STORY_STEALTH_MODE = "updateStoryStealthMode"
        UPDATE_SUGGESTED_ACTIONS = "updateSuggestedActions"
        UPDATE_SUPERGROUP = "updateSupergroup"
        UPDATE_SUPERGROUP_FULL_INFO = "updateSupergroupFullInfo"
        UPDATE_TERMS_OF_SERVICE = "updateTermsOfService"
        UPDATE_TRENDING_STICKER_SETS = "updateTrendingStickerSets"
        UPDATE_UNCONFIRMED_SESSION = "updateUnconfirmedSession"
        UPDATE_UNREAD_CHAT_COUNT = "updateUnreadChatCount"
        UPDATE_UNREAD_MESSAGE_COUNT = "updateUnreadMessageCount"
        UPDATE_USER = "updateUser"
        UPDATE_USER_FULL_INFO = "updateUserFullInfo"
        UPDATE_USER_PRIVACY_SETTING_RULES = "updateUserPrivacySettingRules"
        UPDATE_USER_STATUS = "updateUserStatus"
        UPDATE_USERS_NEARBY = "updateUsersNearby"
        UPDATE_WEB_APP_MESSAGE_SENT = "updateWebAppMessageSent"
        UPDATES = "updates"
        UPGRADE_BASIC_GROUP_CHAT_TO_SUPERGROUP_CHAT = "upgradeBasicGroupChatToSupergroupChat"
        UPLOAD_STICKER_FILE = "uploadStickerFile"
        USER = "user"
        USER_FULL_INFO = "userFullInfo"
        USER_LINK = "userLink"
        USER_PRIVACY_SETTING = "userPrivacySetting"
        USER_PRIVACY_SETTING_ALLOW_CALLS = "userPrivacySettingAllowCalls"
        USER_PRIVACY_SETTING_ALLOW_CHAT_INVITES = "userPrivacySettingAllowChatInvites"
        USER_PRIVACY_SETTING_ALLOW_FINDING_BY_PHONE_NUMBER = "userPrivacySettingAllowFindingByPhoneNumber"
        USER_PRIVACY_SETTING_ALLOW_PEER_TO_PEER_CALLS = "userPrivacySettingAllowPeerToPeerCalls"
        USER_PRIVACY_SETTING_ALLOW_PRIVATE_VOICE_AND_VIDEO_NOTE_MESSAGES = (
            "userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages"
        )
        USER_PRIVACY_SETTING_SHOW_BIO = "userPrivacySettingShowBio"
        USER_PRIVACY_SETTING_SHOW_LINK_IN_FORWARDED_MESSAGES = "userPrivacySettingShowLinkInForwardedMessages"
        USER_PRIVACY_SETTING_SHOW_PHONE_NUMBER = "userPrivacySettingShowPhoneNumber"
        USER_PRIVACY_SETTING_SHOW_PROFILE_PHOTO = "userPrivacySettingShowProfilePhoto"
        USER_PRIVACY_SETTING_SHOW_STATUS = "userPrivacySettingShowStatus"
        USER_PRIVACY_SETTING_RULE = "userPrivacySettingRule"
        USER_PRIVACY_SETTING_RULE_ALLOW_ALL = "userPrivacySettingRuleAllowAll"
        USER_PRIVACY_SETTING_RULE_ALLOW_CHAT_MEMBERS = "userPrivacySettingRuleAllowChatMembers"
        USER_PRIVACY_SETTING_RULE_ALLOW_CONTACTS = "userPrivacySettingRuleAllowContacts"
        USER_PRIVACY_SETTING_RULE_ALLOW_USERS = "userPrivacySettingRuleAllowUsers"
        USER_PRIVACY_SETTING_RULE_RESTRICT_ALL = "userPrivacySettingRuleRestrictAll"
        USER_PRIVACY_SETTING_RULE_RESTRICT_CHAT_MEMBERS = "userPrivacySettingRuleRestrictChatMembers"
        USER_PRIVACY_SETTING_RULE_RESTRICT_CONTACTS = "userPrivacySettingRuleRestrictContacts"
        USER_PRIVACY_SETTING_RULE_RESTRICT_USERS = "userPrivacySettingRuleRestrictUsers"
        USER_PRIVACY_SETTING_RULES = "userPrivacySettingRules"
        USER_STATUS = "userStatus"
        USER_STATUS_EMPTY = "userStatusEmpty"
        USER_STATUS_LAST_MONTH = "userStatusLastMonth"
        USER_STATUS_LAST_WEEK = "userStatusLastWeek"
        USER_STATUS_OFFLINE = "userStatusOffline"
        USER_STATUS_ONLINE = "userStatusOnline"
        USER_STATUS_RECENTLY = "userStatusRecently"
        USER_SUPPORT_INFO = "userSupportInfo"
        USER_TYPE = "userType"
        USER_TYPE_BOT = "userTypeBot"
        USER_TYPE_DELETED = "userTypeDeleted"
        USER_TYPE_REGULAR = "userTypeRegular"
        USER_TYPE_UNKNOWN = "userTypeUnknown"
        USERNAMES = "usernames"
        USERS = "users"
        VALIDATE_ORDER_INFO = "validateOrderInfo"
        VALIDATED_ORDER_INFO = "validatedOrderInfo"
        VECTOR_PATH_COMMAND = "vectorPathCommand"
        VECTOR_PATH_COMMAND_CUBIC_BEZIER_CURVE = "vectorPathCommandCubicBezierCurve"
        VECTOR_PATH_COMMAND_LINE = "vectorPathCommandLine"
        VENUE = "venue"
        VIDEO = "video"
        VIDEO_CHAT = "videoChat"
        VIDEO_NOTE = "videoNote"
        VIEW_MESSAGES = "viewMessages"
        VIEW_PREMIUM_FEATURE = "viewPremiumFeature"
        VIEW_TRENDING_STICKER_SETS = "viewTrendingStickerSets"
        VOICE_NOTE = "voiceNote"
        WEB_APP = "webApp"
        WEB_APP_INFO = "webAppInfo"
        WEB_PAGE = "webPage"
        WEB_PAGE_INSTANT_VIEW = "webPageInstantView"
        WRITE_GENERATED_FILE_PART = "writeGeneratedFilePart"

    def __init__(self, client: "Client"):
        self.client = client

    async def accept_call(
        self, call_id: Int32, protocol: CallProtocol, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Accepts an incoming call

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param protocol: The call protocols supported by the application
        :type protocol: :class:`CallProtocol`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AcceptCall(
                call_id=call_id,
                protocol=protocol,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def accept_terms_of_service(
        self, terms_of_service_id: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Accepts Telegram terms of services

        :param terms_of_service_id: Terms of service identifier
        :type terms_of_service_id: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AcceptTermsOfService(
                terms_of_service_id=terms_of_service_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def activate_story_stealth_mode(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Activates stealth mode for stories, which hides all views of stories from the current user in the last "story_stealth_mode_past_period" seconds and for the next "story_stealth_mode_future_period" seconds; for Telegram Premium users only
        """

        return await self.client.request(
            ActivateStoryStealthMode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_application_changelog(
        self, previous_application_version: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds server-provided application changelog as messages to the chat 777000 (Telegram) or as a stories; for official applications only. Returns a 404 error if nothing changed

        :param previous_application_version: The previous application version
        :type previous_application_version: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddApplicationChangelog(
                previous_application_version=previous_application_version,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_folder_by_invite_link(
        self, invite_link: String, chat_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a chat folder by an invite link

        :param invite_link: Invite link for the chat folder
        :type invite_link: :class:`String`
        :param chat_ids: Identifiers of the chats added to the chat folder. The chats are automatically joined if they aren't joined yet
        :type chat_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddChatFolderByInviteLink(
                invite_link=invite_link,
                chat_ids=chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_member(
        self,
        chat_id: Int53,
        user_id: Int53,
        forward_limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds a new member to a chat. Members can't be added to private or secret chats

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param user_id: Identifier of the user
        :type user_id: :class:`Int53`
        :param forward_limit: The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot
        :type forward_limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddChatMember(
                chat_id=chat_id,
                user_id=user_id,
                forward_limit=forward_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_members(
        self, chat_id: Int53, user_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds multiple new members to a chat. Currently, this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param user_ids: Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
        :type user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddChatMembers(
                chat_id=chat_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_chat_to_list(
        self, chat_id: Int53, chat_list: ChatList, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param chat_list: The chat list. Use getChatListsToAddChat to get suitable chat lists
        :type chat_list: :class:`ChatList`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddChatToList(
                chat_id=chat_id,
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_contact(
        self, contact: Contact, share_phone_number: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a user to the contact list or edits an existing contact by their user identifier

        :param contact: The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored
        :type contact: :class:`Contact`
        :param share_phone_number: Pass true to share the current user's phone number with the new contact. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed. Use the field userFullInfo.need_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number
        :type share_phone_number: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddContact(
                contact=contact,
                share_phone_number=share_phone_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_custom_server_language_pack(
        self, language_pack_id: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization

        :param language_pack_id: Identifier of a language pack to be added
        :type language_pack_id: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddCustomServerLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_favorite_sticker(
        self, sticker: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list. Emoji stickers can't be added to favorite stickers

        :param sticker: Sticker file to add
        :type sticker: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddFavoriteSticker(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_file_to_downloads(
        self,
        file_id: Int32,
        chat_id: Int53,
        message_id: Int53,
        priority: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates. If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file

        :param file_id: Identifier of the file to download
        :type file_id: :class:`Int32`
        :param chat_id: Chat identifier of the message with the file
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :type priority: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            AddFileToDownloads(
                file_id=file_id,
                chat_id=chat_id,
                message_id=message_id,
                priority=priority,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_local_message(
        self,
        chat_id: Int53,
        sender_id: MessageSender,
        input_message_content: InputMessageContent,
        disable_notification: Bool = False,
        reply_to: typing.Optional[MessageReplyTo] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message

        :param chat_id: Target chat
        :type chat_id: :class:`Int53`
        :param sender_id: Identifier of the sender of the message
        :type sender_id: :class:`MessageSender`
        :param input_message_content: The content of the message to be added
        :type input_message_content: :class:`InputMessageContent`
        :param disable_notification: Pass true to disable notification for the message
        :type disable_notification: :class:`Bool`
        :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
        :type reply_to: :class:`MessageReplyTo`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            AddLocalMessage(
                chat_id=chat_id,
                sender_id=sender_id,
                input_message_content=input_message_content,
                disable_notification=disable_notification,
                reply_to=reply_to,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_log_message(
        self, verbosity_level: Int32, text: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a message to TDLib internal log. Can be called synchronously

        :param verbosity_level: The minimum verbosity level needed for the message to be logged; 0-1023
        :type verbosity_level: :class:`Int32`
        :param text: Text of a message to log
        :type text: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddLogMessage(
                verbosity_level=verbosity_level,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_message_reaction(
        self,
        chat_id: Int53,
        message_id: Int53,
        reaction_type: ReactionType,
        is_big: Bool = False,
        update_recent_reactions: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds a reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param reaction_type: Type of the reaction to add
        :type reaction_type: :class:`ReactionType`
        :param is_big: Pass true if the reaction is added with a big animation
        :type is_big: :class:`Bool`
        :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
        :type update_recent_reactions: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddMessageReaction(
                chat_id=chat_id,
                message_id=message_id,
                reaction_type=reaction_type,
                is_big=is_big,
                update_recent_reactions=update_recent_reactions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_network_statistics(
        self, entry: NetworkStatisticsEntry, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds the specified data to data usage statistics. Can be called before authorization

        :param entry: The network statistics entry with the data to be added to statistics
        :type entry: :class:`NetworkStatisticsEntry`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddNetworkStatistics(
                entry=entry,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_proxy(
        self,
        server: String,
        port: Int32,
        type_: ProxyType,
        enable: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Proxy:
        """
        Adds a proxy server for network requests. Can be called before authorization

        :param server: Proxy server domain or IP address
        :type server: :class:`String`
        :param port: Proxy server port
        :type port: :class:`Int32`
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        :param enable: Pass true to immediately enable the proxy
        :type enable: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Proxy`
        """

        return await self.client.request(
            AddProxy(
                server=server,
                port=port,
                type=type_,
                enable=enable,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_recent_sticker(
        self, sticker: InputFile, is_attached: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list. Emoji stickers can't be added to recent stickers

        :param sticker: Sticker file to add
        :type sticker: :class:`InputFile`
        :param is_attached: Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
        :type is_attached: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            AddRecentSticker(
                sticker=sticker,
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_recently_found_chat(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first

        :param chat_id: Identifier of the chat to add
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddRecentlyFoundChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_saved_animation(
        self, animation: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list

        :param animation: The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list
        :type animation: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddSavedAnimation(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_saved_notification_sound(
        self, sound: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> NotificationSound:
        """
        Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed

        :param sound: Notification sound file to add
        :type sound: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NotificationSound`
        """

        return await self.client.request(
            AddSavedNotificationSound(
                sound=sound,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def add_sticker_to_set(
        self,
        user_id: Int53,
        name: String,
        sticker: InputSticker,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds a new sticker to a set; for bots only

        :param user_id: Sticker set owner
        :type user_id: :class:`Int53`
        :param name: Sticker set name
        :type name: :class:`String`
        :param sticker: Sticker to add to the set
        :type sticker: :class:`InputSticker`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AddStickerToSet(
                user_id=user_id,
                name=name,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def allow_bot_to_send_messages(
        self, bot_user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Allows the specified bot to send messages to the user

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AllowBotToSendMessages(
                bot_user_id=bot_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_callback_query(
        self,
        callback_query_id: Int64,
        text: String,
        url: String,
        cache_time: Int32,
        show_alert: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the result of a callback query; for bots only

        :param callback_query_id: Identifier of the callback query
        :type callback_query_id: :class:`Int64`
        :param text: Text of the answer
        :type text: :class:`String`
        :param url: URL to be opened
        :type url: :class:`String`
        :param cache_time: Time during which the result of the query can be cached, in seconds
        :type cache_time: :class:`Int32`
        :param show_alert: Pass true to show an alert to the user instead of a toast notification
        :type show_alert: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AnswerCallbackQuery(
                callback_query_id=callback_query_id,
                text=text,
                url=url,
                cache_time=cache_time,
                show_alert=show_alert,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_custom_query(
        self, custom_query_id: Int64, data: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Answers a custom query; for bots only

        :param custom_query_id: Identifier of a custom query
        :type custom_query_id: :class:`Int64`
        :param data: JSON-serialized answer to the query
        :type data: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AnswerCustomQuery(
                custom_query_id=custom_query_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_inline_query(
        self,
        inline_query_id: Int64,
        results: Vector[InputInlineQueryResult],
        cache_time: Int32,
        next_offset: String,
        is_personal: Bool = False,
        button: typing.Optional[InlineQueryResultsButton] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the result of an inline query; for bots only

        :param inline_query_id: Identifier of the inline query
        :type inline_query_id: :class:`Int64`
        :param results: The results of the query
        :type results: :class:`Vector[InputInlineQueryResult]`
        :param cache_time: Allowed time to cache the results of the query, in seconds
        :type cache_time: :class:`Int32`
        :param next_offset: Offset for the next inline query; pass an empty string if there are no more results
        :type next_offset: :class:`String`
        :param is_personal: Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :type is_personal: :class:`Bool`
        :param button: Button to be shown above inline query results; pass null if none, defaults to None
        :type button: :class:`InlineQueryResultsButton`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AnswerInlineQuery(
                inline_query_id=inline_query_id,
                results=results,
                cache_time=cache_time,
                next_offset=next_offset,
                is_personal=is_personal,
                button=button,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: Int64,
        error_message: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the result of a pre-checkout query; for bots only

        :param pre_checkout_query_id: Identifier of the pre-checkout query
        :type pre_checkout_query_id: :class:`Int64`
        :param error_message: An error message, empty on success
        :type error_message: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AnswerPreCheckoutQuery(
                pre_checkout_query_id=pre_checkout_query_id,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_shipping_query(
        self,
        shipping_query_id: Int64,
        shipping_options: Vector[ShippingOption],
        error_message: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the result of a shipping query; for bots only

        :param shipping_query_id: Identifier of the shipping query
        :type shipping_query_id: :class:`Int64`
        :param shipping_options: Available shipping options
        :type shipping_options: :class:`Vector[ShippingOption]`
        :param error_message: An error message, empty on success
        :type error_message: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AnswerShippingQuery(
                shipping_query_id=shipping_query_id,
                shipping_options=shipping_options,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def answer_web_app_query(
        self,
        web_app_query_id: String,
        result: InputInlineQueryResult,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> SentWebAppMessage:
        """
        Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

        :param web_app_query_id: Identifier of the Web App query
        :type web_app_query_id: :class:`String`
        :param result: The result of the query
        :type result: :class:`InputInlineQueryResult`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SentWebAppMessage`
        """

        return await self.client.request(
            AnswerWebAppQuery(
                web_app_query_id=web_app_query_id,
                result=result,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def assign_app_store_transaction(
        self, receipt: Bytes, purpose: StorePaymentPurpose, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs server about a purchase through App Store. For official applications only

        :param receipt: App Store receipt
        :type receipt: :class:`Bytes`
        :param purpose: Transaction purpose
        :type purpose: :class:`StorePaymentPurpose`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AssignAppStoreTransaction(
                receipt=receipt,
                purpose=purpose,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def assign_google_play_transaction(
        self,
        package_name: String,
        store_product_id: String,
        purchase_token: String,
        purpose: StorePaymentPurpose,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Informs server about a purchase through Google Play. For official applications only

        :param package_name: Application package name
        :type package_name: :class:`String`
        :param store_product_id: Identifier of the purchased store product
        :type store_product_id: :class:`String`
        :param purchase_token: Google Play purchase token
        :type purchase_token: :class:`String`
        :param purpose: Transaction purpose
        :type purpose: :class:`StorePaymentPurpose`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            AssignGooglePlayTransaction(
                package_name=package_name,
                store_product_id=store_product_id,
                purchase_token=purchase_token,
                purpose=purpose,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def ban_chat_member(
        self,
        chat_id: Int53,
        member_id: MessageSender,
        banned_until_date: Int32,
        revoke_messages: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param member_id: Member identifier
        :type member_id: :class:`MessageSender`
        :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned
        :type banned_until_date: :class:`Int32`
        :param revoke_messages: Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels
        :type revoke_messages: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            BanChatMember(
                chat_id=chat_id,
                member_id=member_id,
                banned_until_date=banned_until_date,
                revoke_messages=revoke_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def block_message_sender_from_replies(
        self,
        message_id: Int53,
        delete_message: Bool = False,
        delete_all_messages: Bool = False,
        report_spam: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Blocks an original sender of a message in the Replies chat

        :param message_id: The identifier of an incoming message in the Replies chat
        :type message_id: :class:`Int53`
        :param delete_message: Pass true to delete the message
        :type delete_message: :class:`Bool`
        :param delete_all_messages: Pass true to delete all messages from the same sender
        :type delete_all_messages: :class:`Bool`
        :param report_spam: Pass true to report the sender to the Telegram moderators
        :type report_spam: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            BlockMessageSenderFromReplies(
                message_id=message_id,
                delete_message=delete_message,
                delete_all_messages=delete_all_messages,
                report_spam=report_spam,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def can_bot_send_messages(
        self, bot_user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks whether the specified bot can send messages to the user. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CanBotSendMessages(
                bot_user_id=bot_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def can_purchase_premium(
        self, purpose: StorePaymentPurpose, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase

        :param purpose: Transaction purpose
        :type purpose: :class:`StorePaymentPurpose`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CanPurchasePremium(
                purpose=purpose,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def can_send_story(self, *, request_id: str = None, request_timeout: int = None) -> CanSendStoryResult:
        """
        Checks whether the current user can send a story
        """

        return await self.client.request(
            CanSendStory(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def can_transfer_ownership(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> CanTransferOwnershipResult:
        """
        Checks whether the current session can be used to transfer a chat ownership to another user
        """

        return await self.client.request(
            CanTransferOwnership(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_download_file(
        self, file_id: Int32, only_if_pending: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Stops the downloading of a file. If a file has already been downloaded, does nothing

        :param file_id: Identifier of a file to stop downloading
        :type file_id: :class:`Int32`
        :param only_if_pending: Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
        :type only_if_pending: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CancelDownloadFile(
                file_id=file_id,
                only_if_pending=only_if_pending,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_password_reset(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
        """

        return await self.client.request(
            CancelPasswordReset(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def cancel_preliminary_upload_file(
        self, file_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile. For other files the behavior is undefined

        :param file_id: Identifier of the file to stop uploading
        :type file_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CancelPreliminaryUploadFile(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_imported_contacts(
        self, contacts: Vector[Contact], *, request_id: str = None, request_timeout: int = None
    ) -> ImportedContacts:
        """
        Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time

        :param contacts: The new list of contacts, contact's vCard are ignored and are not imported
        :type contacts: :class:`Vector[Contact]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ImportedContacts`
        """

        return await self.client.request(
            ChangeImportedContacts(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_phone_number(
        self,
        phone_number: String,
        settings: typing.Optional[PhoneNumberAuthenticationSettings] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Changes the phone number of the user and sends an authentication code to the user's new phone number; for official Android and iOS applications only. On success, returns information about the sent code

        :param phone_number: The new phone number of the user in international format
        :type phone_number: :class:`String`
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
        :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """

        return await self.client.request(
            ChangePhoneNumber(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def change_sticker_set(
        self,
        set_id: Int64,
        is_installed: Bool,
        is_archived: Bool,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Installs/uninstalls or activates/archives a sticker set

        :param set_id: Identifier of the sticker set
        :type set_id: :class:`Int64`
        :param is_installed: The new value of is_installed
        :type is_installed: :class:`Bool`
        :param is_archived: The new value of is_archived. A sticker set can't be installed and archived simultaneously
        :type is_archived: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ChangeStickerSet(
                set_id=set_id,
                is_installed=is_installed,
                is_archived=is_archived,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_bot_token(
        self, token: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

        :param token: The bot token
        :type token: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckAuthenticationBotToken(
                token=token,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode

        :param code: Authentication code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckAuthenticationCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_email_code(
        self, code: EmailAddressAuthentication, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the authentication of a email address. Works only when the current authorization state is authorizationStateWaitEmailCode

        :param code: Email address authentication to check
        :type code: :class:`EmailAddressAuthentication`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckAuthenticationEmailCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_password(
        self, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword

        :param password: The 2-step verification password to check
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckAuthenticationPassword(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_authentication_password_recovery_code(
        self, recovery_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks whether a 2-step verification password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword

        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckAuthenticationPasswordRecoveryCode(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_change_phone_number_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the authentication code sent to confirm a new phone number of the user

        :param code: Authentication code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckChangePhoneNumberCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_chat_folder_invite_link(
        self, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolderInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder

        :param invite_link: Invite link to be checked
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInviteLinkInfo`
        """

        return await self.client.request(
            CheckChatFolderInviteLink(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_chat_invite_link(
        self, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> ChatInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat and returns information about the corresponding chat

        :param invite_link: Invite link to be checked
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkInfo`
        """

        return await self.client.request(
            CheckChatInviteLink(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_chat_username(
        self, chat_id: Int53, username: String, *, request_id: str = None, request_timeout: int = None
    ) -> CheckChatUsernameResult:
        """
        Checks whether a username can be set for a chat

        :param chat_id: Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created
        :type chat_id: :class:`Int53`
        :param username: Username to be checked
        :type username: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CheckChatUsernameResult`
        """

        return await self.client.request(
            CheckChatUsername(
                chat_id=chat_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_created_public_chats_limit(
        self, type_: PublicChatType, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium

        :param type_: Type of the public chats, for which to check the limit
        :type type_: :class:`PublicChatType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckCreatedPublicChatsLimit(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_email_address_verification_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the email address verification code for Telegram Passport

        :param code: Verification code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckEmailAddressVerificationCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_login_email_address_code(
        self, code: EmailAddressAuthentication, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the login email address authentication

        :param code: Email address authentication to check
        :type code: :class:`EmailAddressAuthentication`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckLoginEmailAddressCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_password_recovery_code(
        self, recovery_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks whether a 2-step verification password recovery code sent to an email address is valid

        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckPasswordRecoveryCode(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_phone_number_confirmation_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks phone number confirmation code

        :param code: Confirmation code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckPhoneNumberConfirmationCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_phone_number_verification_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Checks the phone number verification code for Telegram Passport

        :param code: Verification code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CheckPhoneNumberVerificationCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_recovery_email_address_code(
        self, code: String, *, request_id: str = None, request_timeout: int = None
    ) -> PasswordState:
        """
        Checks the 2-step verification recovery email address verification code

        :param code: Verification code to check
        :type code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """

        return await self.client.request(
            CheckRecoveryEmailAddressCode(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def check_sticker_set_name(
        self, name: String, *, request_id: str = None, request_timeout: int = None
    ) -> CheckStickerSetNameResult:
        """
        Checks whether a name can be used for a new sticker set

        :param name: Name to be checked
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CheckStickerSetNameResult`
        """

        return await self.client.request(
            CheckStickerSetName(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clean_file_name(self, file_name: String, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously

        :param file_name: File name or path to the file
        :type file_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            CleanFileName(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_all_draft_messages(
        self, exclude_secret_chats: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Clears message drafts in all chats

        :param exclude_secret_chats: Pass true to keep local message drafts in secret chats
        :type exclude_secret_chats: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ClearAllDraftMessages(
                exclude_secret_chats=exclude_secret_chats,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_autosave_settings_exceptions(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings
        """

        return await self.client.request(
            ClearAutosaveSettingsExceptions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_imported_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears all imported contacts, contact list remains unchanged
        """

        return await self.client.request(
            ClearImportedContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recent_emoji_statuses(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of recently used emoji statuses
        """

        return await self.client.request(
            ClearRecentEmojiStatuses(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recent_reactions(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of recently used reactions
        """

        return await self.client.request(
            ClearRecentReactions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recent_stickers(
        self, is_attached: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Clears the list of recently used stickers

        :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
        :type is_attached: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ClearRecentStickers(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def clear_recently_found_chats(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of recently found chats
        """

        return await self.client.request(
            ClearRecentlyFoundChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def click_animated_emoji_message(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Sticker:
        """
        Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played

        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the clicked message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Sticker`
        """

        return await self.client.request(
            ClickAnimatedEmojiMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def click_chat_sponsored_message(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that the user opened the sponsored chat via the button, the name, the photo, or a mention in the sponsored message

        :param chat_id: Chat identifier of the sponsored message
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the sponsored message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ClickChatSponsoredMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def click_premium_subscription_button(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Informs TDLib that the user clicked Premium subscription button on the Premium features screen
        """

        return await self.client.request(
            ClickPremiumSubscriptionButton(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization
        """

        return await self.client.request(
            Close(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CloseChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_secret_chat(
        self, secret_chat_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Closes a secret chat, effectively transferring its state to secretChatStateClosed

        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CloseSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_story(
        self, story_sender_chat_id: Int53, story_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that a story is closed by the user

        :param story_sender_chat_id: The identifier of the sender of the story to close
        :type story_sender_chat_id: :class:`Int53`
        :param story_id: The identifier of the story
        :type story_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CloseStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def close_web_app(
        self, web_app_launch_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that a previously opened Web App was closed

        :param web_app_launch_id: Identifier of Web App launch, received from openWebApp
        :type web_app_launch_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            CloseWebApp(
                web_app_launch_id=web_app_launch_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def confirm_qr_code_authentication(
        self, link: String, *, request_id: str = None, request_timeout: int = None
    ) -> Session:
        """
        Confirms QR code authentication on another device. Returns created session on success

        :param link: A link from a QR code. The link must be scanned by the in-app camera
        :type link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Session`
        """

        return await self.client.request(
            ConfirmQrCodeAuthentication(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def confirm_session(self, session_id: Int64, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Confirms an unconfirmed session of the current user from another device

        :param session_id: Session identifier
        :type session_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ConfirmSession(
                session_id=session_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_basic_group_chat(
        self, basic_group_id: Int53, force: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known basic group

        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`Int53`
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateBasicGroupChat(
                basic_group_id=basic_group_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_call(
        self,
        user_id: Int53,
        protocol: CallProtocol,
        is_video: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> CallId:
        """
        Creates a new call

        :param user_id: Identifier of the user to be called
        :type user_id: :class:`Int53`
        :param protocol: The call protocols supported by the application
        :type protocol: :class:`CallProtocol`
        :param is_video: Pass true to create a video call
        :type is_video: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CallId`
        """

        return await self.client.request(
            CreateCall(
                user_id=user_id,
                protocol=protocol,
                is_video=is_video,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_chat_folder(
        self, folder: ChatFolder, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolderInfo:
        """
        Creates new chat folder. Returns information about the created chat folder. There can be up to getOption("chat_folder_count_max") chat folders, but the limit can be increased with Telegram Premium

        :param folder: The new chat folder
        :type folder: :class:`ChatFolder`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInfo`
        """

        return await self.client.request(
            CreateChatFolder(
                folder=folder,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_chat_folder_invite_link(
        self,
        chat_folder_id: Int32,
        chat_ids: Vector[Int53],
        name: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatFolderInviteLink:
        """
        Creates a new invite link for a chat folder. A link can be created for a chat folder if it has only pinned and included chats

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param chat_ids: Identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link creation
        :type chat_ids: :class:`Vector[Int53]`
        :param name: Name of the link; 0-32 characters
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInviteLink`
        """

        return await self.client.request(
            CreateChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                chat_ids=chat_ids,
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_chat_invite_link(
        self,
        chat_id: Int53,
        name: String = "",
        expiration_date: Int32 = 0,
        member_limit: Int32 = 0,
        creates_join_request: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatInviteLink:
        """
        Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param name: Invite link name; 0-32 characters
        :type name: :class:`String`
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :type expiration_date: :class:`Int32`
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :type member_limit: :class:`Int32`
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :type creates_join_request: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """

        return await self.client.request(
            CreateChatInviteLink(
                chat_id=chat_id,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_forum_topic(
        self, chat_id: Int53, name: String, icon: ForumTopicIcon, *, request_id: str = None, request_timeout: int = None
    ) -> ForumTopicInfo:
        """
        Creates a topic in a forum supergroup chat; requires can_manage_topics rights in the supergroup

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param name: Name of the topic; 1-128 characters
        :type name: :class:`String`
        :param icon: Icon of the topic. Icon color must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F. Telegram Premium users can use any custom emoji as topic icon, other users can use only a custom emoji returned by getForumTopicDefaultIcons
        :type icon: :class:`ForumTopicIcon`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ForumTopicInfo`
        """

        return await self.client.request(
            CreateForumTopic(
                chat_id=chat_id,
                name=name,
                icon=icon,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_invoice_link(
        self, invoice: InputMessageContent, *, request_id: str = None, request_timeout: int = None
    ) -> HttpUrl:
        """
        Creates a link for the given invoice; for bots only

        :param invoice: Information about the invoice of the type inputMessageInvoice
        :type invoice: :class:`InputMessageContent`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            CreateInvoiceLink(
                invoice=invoice,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_basic_group_chat(
        self,
        title: String,
        user_ids: Vector[Int53] = [],
        message_auto_delete_time: Int32 = 0,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Chat:
        """
        Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat

        :param title: Title of the new basic group; 1-128 characters
        :type title: :class:`String`
        :param user_ids: Identifiers of users to be added to the basic group; may be empty to create a basic group without other members
        :type user_ids: :class:`Vector[Int53]`
        :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :type message_auto_delete_time: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateNewBasicGroupChat(
                title=title,
                user_ids=user_ids,
                message_auto_delete_time=message_auto_delete_time,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_secret_chat(
        self, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Creates a new secret chat. Returns the newly created chat

        :param user_id: Identifier of the target user
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateNewSecretChat(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_sticker_set(
        self,
        user_id: Int53,
        title: String,
        name: String,
        sticker_format: StickerFormat,
        sticker_type: StickerType,
        stickers: Vector[InputSticker],
        needs_repainting: Bool = False,
        source: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> StickerSet:
        """
        Creates a new sticker set. Returns the newly created sticker set

        :param user_id: Sticker set owner; ignored for regular users
        :type user_id: :class:`Int53`
        :param title: Sticker set title; 1-64 characters
        :type title: :class:`String`
        :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters
        :type name: :class:`String`
        :param sticker_format: Format of the stickers in the set
        :type sticker_format: :class:`StickerFormat`
        :param sticker_type: Type of the stickers in the set
        :type sticker_type: :class:`StickerType`
        :param stickers: List of stickers to be added to the set; must be non-empty. All stickers must have the same format. For TGS stickers, uploadStickerFile must be used before the sticker is shown
        :type stickers: :class:`Vector[InputSticker]`
        :param needs_repainting: Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only
        :type needs_repainting: :class:`Bool`
        :param source: Source of the sticker set; may be empty if unknown
        :type source: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """

        return await self.client.request(
            CreateNewStickerSet(
                user_id=user_id,
                title=title,
                name=name,
                sticker_format=sticker_format,
                sticker_type=sticker_type,
                stickers=stickers,
                needs_repainting=needs_repainting,
                source=source,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_new_supergroup_chat(
        self,
        title: String,
        is_forum: Bool = False,
        is_channel: Bool = False,
        description: String = "",
        message_auto_delete_time: Int32 = 0,
        for_import: Bool = False,
        location: typing.Optional[ChatLocation] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Chat:
        """
        Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat

        :param title: Title of the new chat; 1-128 characters
        :type title: :class:`String`
        :param is_forum: Pass true to create a forum supergroup chat
        :type is_forum: :class:`Bool`
        :param is_channel: Pass true to create a channel chat; ignored if a forum is created
        :type is_channel: :class:`Bool`
        :param description: Chat description; 0-255 characters
        :type description: :class:`String`
        :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :type message_auto_delete_time: :class:`Int32`
        :param for_import: Pass true to create a supergroup for importing messages using importMessage
        :type for_import: :class:`Bool`
        :param location: Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat, defaults to None
        :type location: :class:`ChatLocation`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateNewSupergroupChat(
                title=title,
                is_forum=is_forum,
                is_channel=is_channel,
                description=description,
                message_auto_delete_time=message_auto_delete_time,
                for_import=for_import,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_private_chat(
        self, user_id: Int53, force: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Returns an existing chat corresponding to a given user

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreatePrivateChat(
                user_id=user_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_secret_chat(
        self, secret_chat_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known secret chat

        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_supergroup_chat(
        self, supergroup_id: Int53, force: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known supergroup or channel

        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`Int53`
        :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
        :type force: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            CreateSupergroupChat(
                supergroup_id=supergroup_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_temporary_password(
        self, password: String, valid_for: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> TemporaryPasswordState:
        """
        Creates a new temporary password for processing payments

        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param valid_for: Time during which the temporary password will be valid, in seconds; must be between 60 and 86400
        :type valid_for: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TemporaryPasswordState`
        """

        return await self.client.request(
            CreateTemporaryPassword(
                password=password,
                valid_for=valid_for,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def create_video_chat(
        self,
        chat_id: Int53,
        title: String,
        start_date: Int32,
        is_rtmp_stream: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> GroupCallId:
        """
        Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats rights

        :param chat_id: Identifier of a chat in which the video chat will be created
        :type chat_id: :class:`Int53`
        :param title: Group call title; if empty, chat title will be used
        :type title: :class:`String`
        :param start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future
        :type start_date: :class:`Int32`
        :param is_rtmp_stream: Pass true to create an RTMP stream instead of an ordinary video chat; requires creator privileges
        :type is_rtmp_stream: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCallId`
        """

        return await self.client.request(
            CreateVideoChat(
                chat_id=chat_id,
                title=title,
                start_date=start_date,
                is_rtmp_stream=is_rtmp_stream,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_account(
        self, reason: String, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

        :param reason: The reason why the account was deleted; optional
        :type reason: :class:`String`
        :param password: The 2-step verification password of the current user. If not specified, account deletion can be canceled within one week
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteAccount(
                reason=reason,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_all_call_messages(
        self, revoke: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes all call messages

        :param revoke: Pass true to delete the messages for all users
        :type revoke: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteAllCallMessages(
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_all_revoked_chat_invite_links(
        self, chat_id: Int53, creator_user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param creator_user_id: User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
        :type creator_user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteAllRevokedChatInviteLinks(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the usernames and remove all members. Use the field chat.can_be_deleted_for_all_users to find whether the method can be applied to the chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_folder(
        self,
        chat_folder_id: Int32,
        leave_chat_ids: Vector[Int53],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Deletes existing chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param leave_chat_ids: Identifiers of the chats to leave. The chats must be pinned or always included in the folder
        :type leave_chat_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatFolder(
                chat_folder_id=chat_folder_id,
                leave_chat_ids=leave_chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_folder_invite_link(
        self, chat_folder_id: Int32, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes an invite link for a chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param invite_link: Invite link to be deleted
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_history(
        self,
        chat_id: Int53,
        remove_from_chat_list: Bool = False,
        revoke: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param remove_from_chat_list: Pass true to remove the chat from all chat lists
        :type remove_from_chat_list: :class:`Bool`
        :param revoke: Pass true to delete chat history for all users
        :type revoke: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatHistory(
                chat_id=chat_id,
                remove_from_chat_list=remove_from_chat_list,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_date(
        self,
        chat_id: Int53,
        min_date: Int32,
        max_date: Int32,
        revoke: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param min_date: The minimum date of the messages to delete
        :type min_date: :class:`Int32`
        :param max_date: The maximum date of the messages to delete
        :type max_date: :class:`Int32`
        :param revoke: Pass true to delete chat messages for all users; private chats only
        :type revoke: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatMessagesByDate(
                chat_id=chat_id,
                min_date=min_date,
                max_date=max_date,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_messages_by_sender(
        self, chat_id: Int53, sender_id: MessageSender, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param sender_id: Identifier of the sender of messages to delete
        :type sender_id: :class:`MessageSender`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatMessagesBySender(
                chat_id=chat_id,
                sender_id=sender_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_chat_reply_markup(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: The message identifier of the used keyboard
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteChatReplyMarkup(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_commands(
        self,
        language_code: String,
        scope: typing.Optional[BotCommandScope] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Deletes commands supported by the bot for the given user scope and language; for bots only

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`String`
        :param scope: The scope to which the commands are relevant; pass null to delete commands in the default bot command scope, defaults to None
        :type scope: :class:`BotCommandScope`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteCommands(
                language_code=language_code,
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_file(self, file_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes a file from the TDLib file cache

        :param file_id: Identifier of the file to delete
        :type file_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteFile(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_forum_topic(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes all messages in a forum topic; requires can_delete_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_language_pack(
        self, language_pack_id: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization

        :param language_pack_id: Identifier of the language pack to delete
        :type language_pack_id: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_messages(
        self,
        chat_id: Int53,
        message_ids: Vector[Int53],
        revoke: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Deletes messages

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_ids: Identifiers of the messages to be deleted
        :type message_ids: :class:`Vector[Int53]`
        :param revoke: Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats
        :type revoke: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteMessages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_passport_element(
        self, type_: PassportElementType, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes a Telegram Passport element

        :param type_: Element type
        :type type_: :class:`PassportElementType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeletePassportElement(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_profile_photo(
        self, profile_photo_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes a profile photo

        :param profile_photo_id: Identifier of the profile photo to delete
        :type profile_photo_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteProfilePhoto(
                profile_photo_id=profile_photo_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_revoked_chat_invite_link(
        self, chat_id: Int53, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link to revoke
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteRevokedChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_saved_credentials(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved credentials for all payment provider bots
        """

        return await self.client.request(
            DeleteSavedCredentials(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved order information
        """

        return await self.client.request(
            DeleteSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_sticker_set(self, name: String, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deleted a sticker set; for bots only

        :param name: Sticker set name
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteStickerSet(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def delete_story(self, story_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes a previously sent story

        :param story_id: Identifier of the story to delete
        :type story_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DeleteStory(
                story_id=story_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def destroy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent. Can be called before authorization
        """

        return await self.client.request(
            Destroy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disable_all_supergroup_usernames(
        self, supergroup_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DisableAllSupergroupUsernames(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disable_proxy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disables the currently enabled proxy. Can be called before authorization
        """

        return await self.client.request(
            DisableProxy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def discard_call(
        self,
        call_id: Int32,
        duration: Int32,
        connection_id: Int64,
        is_disconnected: Bool = False,
        is_video: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Discards a call

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param duration: The call duration, in seconds
        :type duration: :class:`Int32`
        :param connection_id: Identifier of the connection used during the call
        :type connection_id: :class:`Int64`
        :param is_disconnected: Pass true if the user was disconnected
        :type is_disconnected: :class:`Bool`
        :param is_video: Pass true if the call was a video call
        :type is_video: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DiscardCall(
                call_id=call_id,
                duration=duration,
                connection_id=connection_id,
                is_disconnected=is_disconnected,
                is_video=is_video,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disconnect_all_websites(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disconnects all websites from the current user's Telegram account
        """

        return await self.client.request(
            DisconnectAllWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def disconnect_website(self, website_id: Int64, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disconnects website from the current user's Telegram account

        :param website_id: Website identifier
        :type website_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            DisconnectWebsite(
                website_id=website_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def download_file(
        self,
        file_id: Int32,
        priority: Int32,
        offset: Int53,
        limit: Int53,
        synchronous: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates

        :param file_id: Identifier of the file to download
        :type file_id: :class:`Int32`
        :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
        :type priority: :class:`Int32`
        :param offset: The starting position from which the file needs to be downloaded
        :type offset: :class:`Int53`
        :param limit: Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit
        :type limit: :class:`Int53`
        :param synchronous: Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started
        :type synchronous: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            DownloadFile(
                file_id=file_id,
                priority=priority,
                offset=offset,
                limit=limit,
                synchronous=synchronous,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_chat_folder(
        self, chat_folder_id: Int32, folder: ChatFolder, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolderInfo:
        """
        Edits existing chat folder. Returns information about the edited chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param folder: The edited chat folder
        :type folder: :class:`ChatFolder`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInfo`
        """

        return await self.client.request(
            EditChatFolder(
                chat_folder_id=chat_folder_id,
                folder=folder,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_chat_folder_invite_link(
        self,
        chat_folder_id: Int32,
        invite_link: String,
        chat_ids: Vector[Int53],
        name: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatFolderInviteLink:
        """
        Edits an invite link for a chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param invite_link: Invite link to be edited
        :type invite_link: :class:`String`
        :param chat_ids: New identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link editing
        :type chat_ids: :class:`Vector[Int53]`
        :param name: New name of the link; 0-32 characters
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInviteLink`
        """

        return await self.client.request(
            EditChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
                invite_link=invite_link,
                chat_ids=chat_ids,
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_chat_invite_link(
        self,
        chat_id: Int53,
        invite_link: String,
        name: String = "",
        expiration_date: Int32 = 0,
        member_limit: Int32 = 0,
        creates_join_request: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatInviteLink:
        """
        Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link to be edited
        :type invite_link: :class:`String`
        :param name: Invite link name; 0-32 characters
        :type name: :class:`String`
        :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
        :type expiration_date: :class:`Int32`
        :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
        :type member_limit: :class:`Int32`
        :param creates_join_request: Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0
        :type creates_join_request: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """

        return await self.client.request(
            EditChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
                name=name,
                expiration_date=expiration_date,
                member_limit=member_limit,
                creates_join_request=creates_join_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_custom_language_pack_info(
        self, info: LanguagePackInfo, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Edits information about a custom local language pack in the current localization target. Can be called before authorization

        :param info: New information about the custom local language pack
        :type info: :class:`LanguagePackInfo`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditCustomLanguagePackInfo(
                info=info,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_forum_topic(
        self,
        chat_id: Int53,
        message_thread_id: Int53,
        icon_custom_emoji_id: Int64,
        name: String = "",
        edit_icon_custom_emoji: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits title and icon of a topic in a forum supergroup chat; requires can_manage_topics administrator right in the supergroup unless the user is creator of the topic

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param icon_custom_emoji_id: Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji. Ignored if edit_icon_custom_emoji is false. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons
        :type icon_custom_emoji_id: :class:`Int64`
        :param name: New name of the topic; 0-128 characters. If empty, the previous topic name is kept
        :type name: :class:`String`
        :param edit_icon_custom_emoji: Pass true to edit the icon of the topic. Icon of the General topic can't be edited
        :type edit_icon_custom_emoji: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                icon_custom_emoji_id=icon_custom_emoji_id,
                name=name,
                edit_icon_custom_emoji=edit_icon_custom_emoji,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_caption(
        self,
        inline_message_id: String,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        caption: typing.Optional[FormattedText] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the caption of an inline message sent via a bot; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param reply_markup: The new message reply markup; pass null if none, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param caption: New message content caption; pass null to remove caption; 0-getOption("message_caption_length_max") characters, defaults to None
        :type caption: :class:`FormattedText`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditInlineMessageCaption(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_live_location(
        self,
        inline_message_id: String,
        heading: Int32 = 0,
        proximity_alert_radius: Int32 = 0,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        location: typing.Optional[Location] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the content of a live location in an inline message sent via a bot; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :type heading: :class:`Int32`
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :type proximity_alert_radius: :class:`Int32`
        :param reply_markup: The new message reply markup; pass null if none, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param location: New location content of the message; pass null to stop sharing the live location, defaults to None
        :type location: :class:`Location`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditInlineMessageLiveLocation(
                inline_message_id=inline_message_id,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_media(
        self,
        inline_message_id: String,
        input_message_content: InputMessageContent,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :type input_message_content: :class:`InputMessageContent`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditInlineMessageMedia(
                inline_message_id=inline_message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_reply_markup(
        self,
        inline_message_id: String,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the reply markup of an inline message sent via a bot; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param reply_markup: The new message reply markup; pass null if none, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditInlineMessageReplyMarkup(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_inline_message_text(
        self,
        inline_message_id: String,
        input_message_content: InputMessageContent,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the text of an inline text or game message sent via a bot; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :type input_message_content: :class:`InputMessageContent`
        :param reply_markup: The new message reply markup; pass null if none, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditInlineMessageText(
                inline_message_id=inline_message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_caption(
        self,
        chat_id: Int53,
        message_id: Int53,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        caption: typing.Optional[FormattedText] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Edits the message content caption. Returns the edited message after the edit is completed on the server side

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param caption: New message content caption; 0-getOption("message_caption_length_max") characters; pass null to remove caption, defaults to None
        :type caption: :class:`FormattedText`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            EditMessageCaption(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_live_location(
        self,
        chat_id: Int53,
        message_id: Int53,
        heading: Int32 = 0,
        proximity_alert_radius: Int32 = 0,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        location: typing.Optional[Location] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        :type heading: :class:`Int32`
        :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        :type proximity_alert_radius: :class:`Int32`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param location: New location content of the message; pass null to stop sharing the live location, defaults to None
        :type location: :class:`Location`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            EditMessageLiveLocation(
                chat_id=chat_id,
                message_id=message_id,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_media(
        self,
        chat_id: Int53,
        message_id: Int53,
        input_message_content: InputMessageContent,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption. If only the caption needs to be edited, use editMessageCaption instead. The media can't be edited if the message was set to self-destruct or to a self-destructing media. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa. Returns the edited message after the edit is completed on the server side

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        :type input_message_content: :class:`InputMessageContent`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            EditMessageMedia(
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_reply_markup(
        self,
        chat_id: Int53,
        message_id: Int53,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param reply_markup: The new message reply markup; pass null if none, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            EditMessageReplyMarkup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_scheduling_state(
        self,
        chat_id: Int53,
        message_id: Int53,
        scheduling_state: typing.Optional[MessageSchedulingState] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param scheduling_state: The new message scheduling state; pass null to send the message immediately, defaults to None
        :type scheduling_state: :class:`MessageSchedulingState`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditMessageSchedulingState(
                chat_id=chat_id,
                message_id=message_id,
                scheduling_state=scheduling_state,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_message_text(
        self,
        chat_id: Int53,
        message_id: Int53,
        input_message_content: InputMessageContent,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side

        :param chat_id: The chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param input_message_content: New text content of the message. Must be of type inputMessageText
        :type input_message_content: :class:`InputMessageContent`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            EditMessageText(
                chat_id=chat_id,
                message_id=message_id,
                input_message_content=input_message_content,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_proxy(
        self,
        proxy_id: Int32,
        server: String,
        port: Int32,
        type_: ProxyType,
        enable: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Proxy:
        """
        Edits an existing proxy server for network requests. Can be called before authorization

        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`Int32`
        :param server: Proxy server domain or IP address
        :type server: :class:`String`
        :param port: Proxy server port
        :type port: :class:`Int32`
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        :param enable: Pass true to immediately enable the proxy
        :type enable: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Proxy`
        """

        return await self.client.request(
            EditProxy(
                proxy_id=proxy_id,
                server=server,
                port=port,
                type=type_,
                enable=enable,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def edit_story(
        self,
        story_id: Int32,
        content: typing.Optional[InputStoryContent] = None,
        areas: typing.Optional[InputStoryAreas] = None,
        caption: typing.Optional[FormattedText] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes content and caption of a previously sent story

        :param story_id: Identifier of the story to edit
        :type story_id: :class:`Int32`
        :param content: New content of the story; pass null to keep the current content, defaults to None
        :type content: :class:`InputStoryContent`, optional
        :param areas: New clickable rectangle areas to be shown on the story media; pass null to keep the current areas. Areas can't be edited if story content isn't changed, defaults to None
        :type areas: :class:`InputStoryAreas`, optional
        :param caption: New story caption; pass null to keep the current caption, defaults to None
        :type caption: :class:`FormattedText`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EditStory(
                story_id=story_id,
                content=content,
                areas=areas,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def enable_proxy(self, proxy_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization

        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EnableProxy(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call(self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Ends a group call. Requires groupCall.can_be_managed

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EndGroupCall(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call_recording(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Ends recording of an active group call. Requires groupCall.can_be_managed group call flag

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EndGroupCallRecording(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def end_group_call_screen_sharing(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Ends screen sharing in a joined group call

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            EndGroupCallScreenSharing(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def finish_file_generation(
        self,
        generation_id: Int64,
        error: typing.Optional[Error] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Finishes the file generation

        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`Int64`
        :param error: If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded, defaults to None
        :type error: :class:`Error`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            FinishFileGeneration(
                generation_id=generation_id,
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def forward_messages(
        self,
        chat_id: Int53,
        from_chat_id: Int53,
        message_ids: Vector[Int53],
        message_thread_id: Int53 = 0,
        send_copy: Bool = False,
        remove_caption: Bool = False,
        only_preview: Bool = False,
        options: typing.Optional[MessageSendOptions] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Messages:
        """
        Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message

        :param chat_id: Identifier of the chat to which to forward messages
        :type chat_id: :class:`Int53`
        :param from_chat_id: Identifier of the chat from which to forward messages
        :type from_chat_id: :class:`Int53`
        :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
        :type message_ids: :class:`Vector[Int53]`
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent; for forum threads only
        :type message_thread_id: :class:`Int53`
        :param send_copy: Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
        :type send_copy: :class:`Bool`
        :param remove_caption: Pass true to remove media captions of message copies. Ignored if send_copy is false
        :type remove_caption: :class:`Bool`
        :param only_preview: Pass true to get fake messages instead of actually forwarding them
        :type only_preview: :class:`Bool`
        :param options: Options to be used to send the messages; pass null to use default options, defaults to None
        :type options: :class:`MessageSendOptions`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            ForwardMessages(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_ids=message_ids,
                message_thread_id=message_thread_id,
                send_copy=send_copy,
                remove_caption=remove_caption,
                only_preview=only_preview,
                options=options,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_account_ttl(self, *, request_id: str = None, request_timeout: int = None) -> AccountTtl:
        """
        Returns the period of inactivity after which the account of the current user will automatically be deleted
        """

        return await self.client.request(
            GetAccountTtl(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_active_live_location_messages(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Messages:
        """
        Returns all active live locations that need to be updated by the application. The list is persistent across application restarts only if the message database is used
        """

        return await self.client.request(
            GetActiveLiveLocationMessages(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_active_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Sessions:
        """
        Returns all active sessions of the current user
        """

        return await self.client.request(
            GetActiveSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_all_passport_elements(
        self, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> PassportElements:
        """
        Returns all available Telegram Passport elements

        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElements`
        """

        return await self.client.request(
            GetAllPassportElements(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_all_sticker_emojis(
        self,
        sticker_type: StickerType,
        query: String,
        chat_id: Int53,
        return_only_main_emoji: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Emojis:
        """
        Returns unique emoji that correspond to stickers to be found by the getStickers(sticker_type, query, 1000000, chat_id)

        :param sticker_type: Type of the stickers to search for
        :type sticker_type: :class:`StickerType`
        :param query: Search query
        :type query: :class:`String`
        :param chat_id: Chat identifier for which to find stickers
        :type chat_id: :class:`Int53`
        :param return_only_main_emoji: Pass true if only main emoji for each found sticker must be included in the result
        :type return_only_main_emoji: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Emojis`
        """

        return await self.client.request(
            GetAllStickerEmojis(
                sticker_type=sticker_type,
                query=query,
                chat_id=chat_id,
                return_only_main_emoji=return_only_main_emoji,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_animated_emoji(
        self, emoji: String, *, request_id: str = None, request_timeout: int = None
    ) -> AnimatedEmoji:
        """
        Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji

        :param emoji: The emoji
        :type emoji: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AnimatedEmoji`
        """

        return await self.client.request(
            GetAnimatedEmoji(
                emoji=emoji,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_application_config(self, *, request_id: str = None, request_timeout: int = None) -> JsonValue:
        """
        Returns application config, provided by the server. Can be called before authorization
        """

        return await self.client.request(
            GetApplicationConfig(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_application_download_link(self, *, request_id: str = None, request_timeout: int = None) -> HttpUrl:
        """
        Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram
        """

        return await self.client.request(
            GetApplicationDownloadLink(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_archive_chat_list_settings(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> ArchiveChatListSettings:
        """
        Returns settings for automatic moving of chats to and from the Archive chat lists
        """

        return await self.client.request(
            GetArchiveChatListSettings(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_archived_sticker_sets(
        self,
        sticker_type: StickerType,
        offset_sticker_set_id: Int64,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> StickerSets:
        """
        Returns a list of archived sticker sets

        :param sticker_type: Type of the sticker sets to return
        :type sticker_type: :class:`StickerType`
        :param offset_sticker_set_id: Identifier of the sticker set from which to return the result
        :type offset_sticker_set_id: :class:`Int64`
        :param limit: The maximum number of sticker sets to return; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """

        return await self.client.request(
            GetArchivedStickerSets(
                sticker_type=sticker_type,
                offset_sticker_set_id=offset_sticker_set_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_archived_stories(
        self, from_story_id: Int32, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Stories:
        """
        Returns the list of all stories of the current user. The stories are returned in a reverse chronological order (i.e., in order of decreasing story_id). For optimal performance, the number of returned stories is chosen by TDLib

        :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from the last story
        :type from_story_id: :class:`Int32`
        :param limit: The maximum number of stories to be returned For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stories`
        """

        return await self.client.request(
            GetArchivedStories(
                from_story_id=from_story_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_attached_sticker_sets(
        self, file_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> StickerSets:
        """
        Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets. Currently, only animations, photos, and videos can have attached sticker sets

        :param file_id: File identifier
        :type file_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """

        return await self.client.request(
            GetAttachedStickerSets(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_attachment_menu_bot(
        self, bot_user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> AttachmentMenuBot:
        """
        Returns information about a bot that can be added to attachment or side menu

        :param bot_user_id: Bot's user identifier
        :type bot_user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AttachmentMenuBot`
        """

        return await self.client.request(
            GetAttachmentMenuBot(
                bot_user_id=bot_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_authorization_state(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> AuthorizationState:
        """
        Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
        """

        return await self.client.request(
            GetAuthorizationState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_auto_download_settings_presets(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> AutoDownloadSettingsPresets:
        """
        Returns auto-download settings presets for the current user
        """

        return await self.client.request(
            GetAutoDownloadSettingsPresets(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_autosave_settings(self, *, request_id: str = None, request_timeout: int = None) -> AutosaveSettings:
        """
        Returns autosave settings for the current user
        """

        return await self.client.request(
            GetAutosaveSettings(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_background_url(
        self, name: String, type_: BackgroundType, *, request_id: str = None, request_timeout: int = None
    ) -> HttpUrl:
        """
        Constructs a persistent HTTP URL for a background

        :param name: Background name
        :type name: :class:`String`
        :param type_: Background type
        :type type_: :class:`BackgroundType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetBackgroundUrl(
                name=name,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_backgrounds(
        self, for_dark_theme: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Backgrounds:
        """
        Returns backgrounds installed by the user

        :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
        :type for_dark_theme: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Backgrounds`
        """

        return await self.client.request(
            GetBackgrounds(
                for_dark_theme=for_dark_theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_bank_card_info(
        self, bank_card_number: String, *, request_id: str = None, request_timeout: int = None
    ) -> BankCardInfo:
        """
        Returns information about a bank card

        :param bank_card_number: The bank card number
        :type bank_card_number: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BankCardInfo`
        """

        return await self.client.request(
            GetBankCardInfo(
                bank_card_number=bank_card_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_basic_group(
        self, basic_group_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> BasicGroup:
        """
        Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot

        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BasicGroup`
        """

        return await self.client.request(
            GetBasicGroup(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_basic_group_full_info(
        self, basic_group_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> BasicGroupFullInfo:
        """
        Returns full information about a basic group by its identifier

        :param basic_group_id: Basic group identifier
        :type basic_group_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BasicGroupFullInfo`
        """

        return await self.client.request(
            GetBasicGroupFullInfo(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_blocked_message_senders(
        self, block_list: BlockList, offset: Int32, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> MessageSenders:
        """
        Returns users and chats that were blocked by the current user

        :param block_list: Block list from which to return users
        :type block_list: :class:`BlockList`
        :param offset: Number of users and chats to skip in the result; must be non-negative
        :type offset: :class:`Int32`
        :param limit: The maximum number of users and chats to return; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """

        return await self.client.request(
            GetBlockedMessageSenders(
                block_list=block_list,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_bot_info_description(
        self, bot_user_id: Int53, language_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns the text shown in the chat with a bot if the chat is empty in the given language. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetBotInfoDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_bot_info_short_description(
        self, bot_user_id: Int53, language_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns the text shown on a bot's profile page and sent together with the link when users share the bot in the given language. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetBotInfoShortDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_bot_name(
        self, bot_user_id: Int53, language_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns the name of a bot in the given language. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetBotName(
                bot_user_id=bot_user_id,
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_callback_query_answer(
        self,
        chat_id: Int53,
        message_id: Int53,
        payload: CallbackQueryPayload,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> CallbackQueryAnswer:
        """
        Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        :param chat_id: Identifier of the chat with the message
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message from which the query originated
        :type message_id: :class:`Int53`
        :param payload: Query payload
        :type payload: :class:`CallbackQueryPayload`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CallbackQueryAnswer`
        """

        return await self.client.request(
            GetCallbackQueryAnswer(
                chat_id=chat_id,
                message_id=message_id,
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_callback_query_message(
        self,
        chat_id: Int53,
        message_id: Int53,
        callback_query_id: Int64,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Returns information about a message with the callback button that originated a callback query; for bots only

        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param callback_query_id: Identifier of the callback query
        :type callback_query_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetCallbackQueryMessage(
                chat_id=chat_id,
                message_id=message_id,
                callback_query_id=callback_query_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Chat:
        """
        Returns information about a chat by its identifier; this is an offline request if the current user is not a bot

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            GetChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_active_stories(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatActiveStories:
        """
        Returns the list of active stories posted by the given chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatActiveStories`
        """

        return await self.client.request(
            GetChatActiveStories(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_administrators(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatAdministrators:
        """
        Returns a list of administrators of the chat with their custom titles

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatAdministrators`
        """

        return await self.client.request(
            GetChatAdministrators(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_available_message_senders(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatMessageSenders:
        """
        Returns list of message sender identifiers, which can be used to send messages in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMessageSenders`
        """

        return await self.client.request(
            GetChatAvailableMessageSenders(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_event_log(
        self,
        chat_id: Int53,
        query: String,
        from_event_id: Int64,
        limit: Int32,
        user_ids: Vector[Int53],
        filters: typing.Optional[ChatEventLogFilters] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatEvents:
        """
        Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i.e., in order of decreasing event_id)

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param query: Search query by which to filter events
        :type query: :class:`String`
        :param from_event_id: Identifier of an event from which to return results. Use 0 to get results from the latest events
        :type from_event_id: :class:`Int64`
        :param limit: The maximum number of events to return; up to 100
        :type limit: :class:`Int32`
        :param user_ids: User identifiers by which to filter events. By default, events relating to all users will be returned
        :type user_ids: :class:`Vector[Int53]`
        :param filters: The types of events to return; pass null to get chat events of all types, defaults to None
        :type filters: :class:`ChatEventLogFilters`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatEvents`
        """

        return await self.client.request(
            GetChatEventLog(
                chat_id=chat_id,
                query=query,
                from_event_id=from_event_id,
                limit=limit,
                user_ids=user_ids,
                filters=filters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder(
        self, chat_folder_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolder:
        """
        Returns information about a chat folder by its identifier

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolder`
        """

        return await self.client.request(
            GetChatFolder(
                chat_folder_id=chat_folder_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder_chat_count(
        self, folder: ChatFolder, *, request_id: str = None, request_timeout: int = None
    ) -> Count:
        """
        Returns approximate number of chats in a being created chat folder. Main and archive chat lists must be fully preloaded for this function to work correctly

        :param folder: The new chat folder
        :type folder: :class:`ChatFolder`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Count`
        """

        return await self.client.request(
            GetChatFolderChatCount(
                folder=folder,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder_chats_to_leave(
        self, chat_folder_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetChatFolderChatsToLeave(
                chat_folder_id=chat_folder_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder_default_icon_name(
        self, folder: ChatFolder, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolderIcon:
        """
        Returns default icon name for a folder. Can be called synchronously

        :param folder: Chat folder
        :type folder: :class:`ChatFolder`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderIcon`
        """

        return await self.client.request(
            GetChatFolderDefaultIconName(
                folder=folder,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder_invite_links(
        self, chat_folder_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> ChatFolderInviteLinks:
        """
        Returns invite links created by the current user for a shareable chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatFolderInviteLinks`
        """

        return await self.client.request(
            GetChatFolderInviteLinks(
                chat_folder_id=chat_folder_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_folder_new_chats(
        self, chat_folder_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns new chats added to a shareable chat folder by its owner. The method must be called at most once in getOption("chat_folder_new_chats_update_period") for the given chat folder

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetChatFolderNewChats(
                chat_folder_id=chat_folder_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_history(
        self,
        chat_id: Int53,
        from_message_id: Int53,
        offset: Int32,
        limit: Int32,
        only_local: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Messages:
        """
        Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib. This is an offline request if only_local is true

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`Int53`
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        :type offset: :class:`Int32`
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param only_local: Pass true to get only messages that are available without sending network requests
        :type only_local: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            GetChatHistory(
                chat_id=chat_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link(
        self, chat_id: Int53, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> ChatInviteLink:
        """
        Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link to get
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """

        return await self.client.request(
            GetChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_counts(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatInviteLinkCounts:
        """
        Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkCounts`
        """

        return await self.client.request(
            GetChatInviteLinkCounts(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_link_members(
        self,
        chat_id: Int53,
        invite_link: String,
        limit: Int32,
        offset_member: typing.Optional[ChatInviteLinkMember] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatInviteLinkMembers:
        """
        Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link for which to return chat members
        :type invite_link: :class:`String`
        :param limit: The maximum number of chat members to return; up to 100
        :type limit: :class:`Int32`
        :param offset_member: A chat member from which to return next chat members; pass null to get results from the beginning, defaults to None
        :type offset_member: :class:`ChatInviteLinkMember`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinkMembers`
        """

        return await self.client.request(
            GetChatInviteLinkMembers(
                chat_id=chat_id,
                invite_link=invite_link,
                limit=limit,
                offset_member=offset_member,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_invite_links(
        self,
        chat_id: Int53,
        creator_user_id: Int53,
        offset_date: Int32,
        offset_invite_link: String,
        limit: Int32,
        is_revoked: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatInviteLinks:
        """
        Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param creator_user_id: User identifier of a chat administrator. Must be an identifier of the current user for non-owner
        :type creator_user_id: :class:`Int53`
        :param offset_date: Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
        :type offset_date: :class:`Int32`
        :param offset_invite_link: Invite link starting after which to return invite links; use empty string to get results from the beginning
        :type offset_invite_link: :class:`String`
        :param limit: The maximum number of invite links to return; up to 100
        :type limit: :class:`Int32`
        :param is_revoked: Pass true if revoked links needs to be returned instead of active or expired
        :type is_revoked: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinks`
        """

        return await self.client.request(
            GetChatInviteLinks(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
                offset_date=offset_date,
                offset_invite_link=offset_invite_link,
                limit=limit,
                is_revoked=is_revoked,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_join_requests(
        self,
        chat_id: Int53,
        invite_link: String,
        query: String,
        limit: Int32,
        offset_request: typing.Optional[ChatJoinRequest] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatJoinRequests:
        """
        Returns pending join requests in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :type invite_link: :class:`String`
        :param query: A query to search for in the first names, last names and usernames of the users to return
        :type query: :class:`String`
        :param limit: The maximum number of requests to join the chat to return
        :type limit: :class:`Int32`
        :param offset_request: A chat join request from which to return next requests; pass null to get results from the beginning, defaults to None
        :type offset_request: :class:`ChatJoinRequest`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatJoinRequests`
        """

        return await self.client.request(
            GetChatJoinRequests(
                chat_id=chat_id,
                invite_link=invite_link,
                query=query,
                limit=limit,
                offset_request=offset_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_lists_to_add_chat(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatLists:
        """
        Returns chat lists to which the chat can be added. This is an offline request

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatLists`
        """

        return await self.client.request(
            GetChatListsToAddChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_member(
        self, chat_id: Int53, member_id: MessageSender, *, request_id: str = None, request_timeout: int = None
    ) -> ChatMember:
        """
        Returns information about a single member of a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param member_id: Member identifier
        :type member_id: :class:`MessageSender`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMember`
        """

        return await self.client.request(
            GetChatMember(
                chat_id=chat_id,
                member_id=member_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_by_date(
        self, chat_id: Int53, date: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Message:
        """
        Returns the last message sent in a chat no later than the specified date

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param date: Point in time (Unix timestamp) relative to which to search for messages
        :type date: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetChatMessageByDate(
                chat_id=chat_id,
                date=date,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_calendar(
        self,
        chat_id: Int53,
        filter_: SearchMessagesFilter,
        from_message_id: Int53,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> MessageCalendar:
        """
        Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"

        :param chat_id: Identifier of the chat in which to return information about messages
        :type chat_id: :class:`Int53`
        :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        :param from_message_id: The message identifier from which to return information about messages; use 0 to get results from the last message
        :type from_message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageCalendar`
        """

        return await self.client.request(
            GetChatMessageCalendar(
                chat_id=chat_id,
                filter=filter_,
                from_message_id=from_message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_count(
        self,
        chat_id: Int53,
        filter_: SearchMessagesFilter,
        return_local: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Count:
        """
        Returns approximate number of messages of the specified type in the chat

        :param chat_id: Identifier of the chat in which to count messages
        :type chat_id: :class:`Int53`
        :param filter_: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
        :type return_local: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Count`
        """

        return await self.client.request(
            GetChatMessageCount(
                chat_id=chat_id,
                filter=filter_,
                return_local=return_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_message_position(
        self,
        chat_id: Int53,
        message_id: Int53,
        filter_: SearchMessagesFilter,
        message_thread_id: Int53 = 0,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Count:
        """
        Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats

        :param chat_id: Identifier of the chat in which to find message position
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param filter_: Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        :param message_thread_id: If not 0, only messages in the specified thread will be considered; supergroups only
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Count`
        """

        return await self.client.request(
            GetChatMessagePosition(
                chat_id=chat_id,
                message_id=message_id,
                filter=filter_,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_notification_settings_exceptions(
        self,
        compare_sound: Bool = False,
        scope: typing.Optional[NotificationSettingsScope] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Chats:
        """
        Returns list of chats with non-default notification settings for new messages

        :param compare_sound: Pass true to include in the response chats with only non-default sound
        :type compare_sound: :class:`Bool`
        :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes, defaults to None
        :type scope: :class:`NotificationSettingsScope`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetChatNotificationSettingsExceptions(
                compare_sound=compare_sound,
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_pinned_message(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Message:
        """
        Returns information about a newest pinned message in the chat

        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetChatPinnedMessage(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_pinned_stories(
        self, chat_id: Int53, from_story_id: Int32, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Stories:
        """
        Returns the list of pinned stories posted by the given chat. The stories are returned in a reverse chronological order (i.e., in order of decreasing story_id). For optimal performance, the number of returned stories is chosen by TDLib

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from the last story
        :type from_story_id: :class:`Int32`
        :param limit: The maximum number of stories to be returned For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stories`
        """

        return await self.client.request(
            GetChatPinnedStories(
                chat_id=chat_id,
                from_story_id=from_story_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_scheduled_messages(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Messages:
        """
        Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            GetChatScheduledMessages(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_sparse_message_positions(
        self,
        chat_id: Int53,
        filter_: SearchMessagesFilter,
        from_message_id: Int53,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> MessagePositions:
        """
        Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

        :param chat_id: Identifier of the chat in which to return information about message positions
        :type chat_id: :class:`Int53`
        :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
        :type filter_: :class:`SearchMessagesFilter`
        :param from_message_id: The message identifier from which to return information about message positions
        :type from_message_id: :class:`Int53`
        :param limit: The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessagePositions`
        """

        return await self.client.request(
            GetChatSparseMessagePositions(
                chat_id=chat_id,
                filter=filter_,
                from_message_id=from_message_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_sponsored_messages(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> SponsoredMessages:
        """
        Returns sponsored messages to be shown in a chat; for channel chats only

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SponsoredMessages`
        """

        return await self.client.request(
            GetChatSponsoredMessages(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chat_statistics(
        self, chat_id: Int53, is_dark: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> ChatStatistics:
        """
        Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param is_dark: Pass true if a dark theme is used by the application
        :type is_dark: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatStatistics`
        """

        return await self.client.request(
            GetChatStatistics(
                chat_id=chat_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chats(
        self,
        limit: Int32,
        chat_list: typing.Optional[ChatList] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Chats:
        """
        Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state

        :param limit: The maximum number of chats to be returned
        :type limit: :class:`Int32`
        :param chat_list: The chat list in which to return chats; pass null to get chats from the main chat list, defaults to None
        :type chat_list: :class:`ChatList`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetChats(
                limit=limit,
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_chats_for_chat_folder_invite_link(
        self, chat_folder_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetChatsForChatFolderInviteLink(
                chat_folder_id=chat_folder_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_close_friends(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns all close friends of the current user
        """

        return await self.client.request(
            GetCloseFriends(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_commands(
        self,
        language_code: String,
        scope: typing.Optional[BotCommandScope] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> BotCommands:
        """
        Returns list of commands supported by the bot for the given user scope and language; for bots only

        :param language_code: A two-letter ISO 639-1 language code or an empty string
        :type language_code: :class:`String`
        :param scope: The scope to which the commands are relevant; pass null to get commands in the default bot command scope, defaults to None
        :type scope: :class:`BotCommandScope`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BotCommands`
        """

        return await self.client.request(
            GetCommands(
                language_code=language_code,
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_connected_websites(self, *, request_id: str = None, request_timeout: int = None) -> ConnectedWebsites:
        """
        Returns all website where the current user used Telegram to log in
        """

        return await self.client.request(
            GetConnectedWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns all contacts of the user
        """

        return await self.client.request(
            GetContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_countries(self, *, request_id: str = None, request_timeout: int = None) -> Countries:
        """
        Returns information about existing countries. Can be called before authorization
        """

        return await self.client.request(
            GetCountries(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_country_code(self, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
        """

        return await self.client.request(
            GetCountryCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_created_public_chats(
        self, type_: PublicChatType, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns a list of public chats of the specified type, owned by the user

        :param type_: Type of the public chats to return
        :type type_: :class:`PublicChatType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetCreatedPublicChats(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_current_state(self, *, request_id: str = None, request_timeout: int = None) -> Updates:
        """
        Returns all updates needed to restore current TDLib state, i.e. all actual updateAuthorizationState/updateUser/updateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
        """

        return await self.client.request(
            GetCurrentState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_custom_emoji_reaction_animations(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns TGS stickers with generic animations for custom emoji reactions
        """

        return await self.client.request(
            GetCustomEmojiReactionAnimations(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_custom_emoji_stickers(
        self, custom_emoji_ids: Vector[Int64], *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned

        :param custom_emoji_ids: Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously
        :type custom_emoji_ids: :class:`Vector[Int64]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            GetCustomEmojiStickers(
                custom_emoji_ids=custom_emoji_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_database_statistics(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> DatabaseStatistics:
        """
        Returns database statistics
        """

        return await self.client.request(
            GetDatabaseStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_deep_link_info(
        self, link: String, *, request_id: str = None, request_timeout: int = None
    ) -> DeepLinkInfo:
        """
        Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization

        :param link: The link
        :type link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.DeepLinkInfo`
        """

        return await self.client.request(
            GetDeepLinkInfo(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_default_chat_photo_custom_emoji_stickers(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns default list of custom emoji stickers for placing on a chat photo
        """

        return await self.client.request(
            GetDefaultChatPhotoCustomEmojiStickers(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_default_emoji_statuses(self, *, request_id: str = None, request_timeout: int = None) -> EmojiStatuses:
        """
        Returns default emoji statuses
        """

        return await self.client.request(
            GetDefaultEmojiStatuses(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_default_message_auto_delete_time(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> MessageAutoDeleteTime:
        """
        Returns default message auto-delete time setting for new chats
        """

        return await self.client.request(
            GetDefaultMessageAutoDeleteTime(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_default_profile_photo_custom_emoji_stickers(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns default list of custom emoji stickers for placing on a profile photo
        """

        return await self.client.request(
            GetDefaultProfilePhotoCustomEmojiStickers(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_emoji_categories(
        self, type_: typing.Optional[EmojiCategoryType] = None, *, request_id: str = None, request_timeout: int = None
    ) -> EmojiCategories:
        """
        Returns available emojis categories

        :param type_: Type of emoji categories to return; pass null to get default emoji categories, defaults to None
        :type type_: :class:`EmojiCategoryType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.EmojiCategories`
        """

        return await self.client.request(
            GetEmojiCategories(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_emoji_reaction(
        self, emoji: String, *, request_id: str = None, request_timeout: int = None
    ) -> EmojiReaction:
        """
        Returns information about a emoji reaction. Returns a 404 error if the reaction is not found

        :param emoji: Text representation of the reaction
        :type emoji: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.EmojiReaction`
        """

        return await self.client.request(
            GetEmojiReaction(
                emoji=emoji,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_emoji_suggestions_url(
        self, language_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

        :param language_code: Language code for which the emoji replacements will be suggested
        :type language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetEmojiSuggestionsUrl(
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_external_link(
        self, link: String, allow_write_access: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

        :param link: The HTTP link
        :type link: :class:`String`
        :param allow_write_access: Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
        :type allow_write_access: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetExternalLink(
                link=link,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_external_link_info(
        self, link: String, *, request_id: str = None, request_timeout: int = None
    ) -> LoginUrlInfo:
        """
        Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if web page preview is disabled in secret chats

        :param link: The link
        :type link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LoginUrlInfo`
        """

        return await self.client.request(
            GetExternalLinkInfo(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_favorite_stickers(self, *, request_id: str = None, request_timeout: int = None) -> Stickers:
        """
        Returns favorite stickers
        """

        return await self.client.request(
            GetFavoriteStickers(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file(self, file_id: Int32, *, request_id: str = None, request_timeout: int = None) -> File:
        """
        Returns information about a file; this is an offline request

        :param file_id: Identifier of the file to get
        :type file_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            GetFile(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_downloaded_prefix_size(
        self, file_id: Int32, offset: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> FileDownloadedPrefixSize:
        """
        Returns file downloaded prefix size from a given offset, in bytes

        :param file_id: Identifier of the file
        :type file_id: :class:`Int32`
        :param offset: Offset from which downloaded prefix size needs to be calculated
        :type offset: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FileDownloadedPrefixSize`
        """

        return await self.client.request(
            GetFileDownloadedPrefixSize(
                file_id=file_id,
                offset=offset,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_extension(
        self, mime_type: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously

        :param mime_type: The MIME type of the file
        :type mime_type: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetFileExtension(
                mime_type=mime_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_file_mime_type(
        self, file_name: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously

        :param file_name: The name of the file or path to the file
        :type file_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetFileMimeType(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_forum_topic(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ForumTopic:
        """
        Returns information about a forum topic

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ForumTopic`
        """

        return await self.client.request(
            GetForumTopic(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_forum_topic_default_icons(self, *, request_id: str = None, request_timeout: int = None) -> Stickers:
        """
        Returns list of custom emojis, which can be used as forum topic icon by all users
        """

        return await self.client.request(
            GetForumTopicDefaultIcons(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_forum_topic_link(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> MessageLink:
        """
        Returns an HTTPS link to a topic in a forum chat. This is an offline request

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageLink`
        """

        return await self.client.request(
            GetForumTopicLink(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_forum_topics(
        self,
        chat_id: Int53,
        query: String,
        offset_date: Int32,
        offset_message_id: Int53,
        offset_message_thread_id: Int53,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ForumTopics:
        """
        Returns found forum topics in a forum chat. This is a temporary method for getting information about topic list from the server

        :param chat_id: Identifier of the forum chat
        :type chat_id: :class:`Int53`
        :param query: Query to search for in the forum topic's name
        :type query: :class:`String`
        :param offset_date: The date starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last topic
        :type offset_date: :class:`Int32`
        :param offset_message_id: The message identifier of the last message in the last found topic, or 0 for the first request
        :type offset_message_id: :class:`Int53`
        :param offset_message_thread_id: The message thread identifier of the last found topic, or 0 for the first request
        :type offset_message_thread_id: :class:`Int53`
        :param limit: The maximum number of forum topics to be returned; up to 100. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ForumTopics`
        """

        return await self.client.request(
            GetForumTopics(
                chat_id=chat_id,
                query=query,
                offset_date=offset_date,
                offset_message_id=offset_message_id,
                offset_message_thread_id=offset_message_thread_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_game_high_scores(
        self, chat_id: Int53, message_id: Int53, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> GameHighScores:
        """
        Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only

        :param chat_id: The chat that contains the message with the game
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GameHighScores`
        """

        return await self.client.request(
            GetGameHighScores(
                chat_id=chat_id,
                message_id=message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> GroupCall:
        """
        Returns information about a group call

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCall`
        """

        return await self.client.request(
            GetGroupCall(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_invite_link(
        self,
        group_call_id: Int32,
        can_self_unmute: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns invite link to a video chat in a public chat

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param can_self_unmute: Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
        :type can_self_unmute: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetGroupCallInviteLink(
                group_call_id=group_call_id,
                can_self_unmute=can_self_unmute,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_stream_segment(
        self,
        group_call_id: Int32,
        time_offset: Int53,
        scale: Int32,
        channel_id: Int32,
        video_quality: typing.Optional[GroupCallVideoQuality] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FilePart:
        """
        Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param time_offset: Point in time when the stream segment begins; Unix timestamp in milliseconds
        :type time_offset: :class:`Int53`
        :param scale: Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
        :type scale: :class:`Int32`
        :param channel_id: Identifier of an audio/video channel to get as received from tgcalls
        :type channel_id: :class:`Int32`
        :param video_quality: Video quality as received from tgcalls; pass null to get the worst available quality, defaults to None
        :type video_quality: :class:`GroupCallVideoQuality`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FilePart`
        """

        return await self.client.request(
            GetGroupCallStreamSegment(
                group_call_id=group_call_id,
                time_offset=time_offset,
                scale=scale,
                channel_id=channel_id,
                video_quality=video_quality,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_group_call_streams(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> GroupCallStreams:
        """
        Returns information about available group call streams

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GroupCallStreams`
        """

        return await self.client.request(
            GetGroupCallStreams(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_groups_in_common(
        self,
        user_id: Int53,
        offset_chat_id: Int53,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Chats:
        """
        Returns a list of common group chats with a given user. Chats are sorted by their type and creation date

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param offset_chat_id: Chat identifier starting from which to return chats; use 0 for the first request
        :type offset_chat_id: :class:`Int53`
        :param limit: The maximum number of chats to be returned; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetGroupsInCommon(
                user_id=user_id,
                offset_chat_id=offset_chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_imported_contact_count(self, *, request_id: str = None, request_timeout: int = None) -> Count:
        """
        Returns the total number of imported contacts
        """

        return await self.client.request(
            GetImportedContactCount(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inactive_supergroup_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error. Also, the limit can be increased with Telegram Premium
        """

        return await self.client.request(
            GetInactiveSupergroupChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inline_game_high_scores(
        self, inline_message_id: String, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> GameHighScores:
        """
        Returns game high scores and some part of the high score table in the range of the specified user; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.GameHighScores`
        """

        return await self.client.request(
            GetInlineGameHighScores(
                inline_message_id=inline_message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_inline_query_results(
        self,
        bot_user_id: Int53,
        chat_id: Int53,
        query: String,
        offset: String,
        user_location: typing.Optional[Location] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> InlineQueryResults:
        """
        Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param chat_id: Identifier of the chat where the query was sent
        :type chat_id: :class:`Int53`
        :param query: Text of the query
        :type query: :class:`String`
        :param offset: Offset of the first entry to return; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param user_location: Location of the user; pass null if unknown or the bot doesn't need user's location, defaults to None
        :type user_location: :class:`Location`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.InlineQueryResults`
        """

        return await self.client.request(
            GetInlineQueryResults(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                query=query,
                offset=offset,
                user_location=user_location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_installed_sticker_sets(
        self, sticker_type: StickerType, *, request_id: str = None, request_timeout: int = None
    ) -> StickerSets:
        """
        Returns a list of installed sticker sets

        :param sticker_type: Type of the sticker sets to return
        :type sticker_type: :class:`StickerType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """

        return await self.client.request(
            GetInstalledStickerSets(
                sticker_type=sticker_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_internal_link(
        self, type_: InternalLinkType, is_http: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTPS or a tg: link with the given type. Can be called before authorization

        :param type_: Expected type of the link
        :type type_: :class:`InternalLinkType`
        :param is_http: Pass true to create an HTTPS link (only available for some link types); pass false to create a tg: link
        :type is_http: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetInternalLink(
                type=type_,
                is_http=is_http,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_internal_link_type(
        self, link: String, *, request_id: str = None, request_timeout: int = None
    ) -> InternalLinkType:
        """
        Returns information about the type of an internal link. Returns a 404 error if the link is not internal. Can be called before authorization

        :param link: The link
        :type link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.InternalLinkType`
        """

        return await self.client.request(
            GetInternalLinkType(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_json_string(
        self, json_value: JsonValue, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously

        :param json_value: The JsonValue object
        :type json_value: :class:`JsonValue`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetJsonString(
                json_value=json_value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_json_value(self, json_: String, *, request_id: str = None, request_timeout: int = None) -> JsonValue:
        """
        Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously

        :param json_: The JSON-serialized string
        :type json_: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.JsonValue`
        """

        return await self.client.request(
            GetJsonValue(
                json=json_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_info(
        self, language_pack_id: String, *, request_id: str = None, request_timeout: int = None
    ) -> LanguagePackInfo:
        """
        Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization

        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackInfo`
        """

        return await self.client.request(
            GetLanguagePackInfo(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_string(
        self,
        language_pack_database_path: String,
        localization_target: String,
        language_pack_id: String,
        key: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> LanguagePackStringValue:
        """
        Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously

        :param language_pack_database_path: Path to the language pack database in which strings are stored
        :type language_pack_database_path: :class:`String`
        :param localization_target: Localization target to which the language pack belongs
        :type localization_target: :class:`String`
        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`String`
        :param key: Language pack key of the string to be returned
        :type key: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackStringValue`
        """

        return await self.client.request(
            GetLanguagePackString(
                language_pack_database_path=language_pack_database_path,
                localization_target=localization_target,
                language_pack_id=language_pack_id,
                key=key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_language_pack_strings(
        self, language_pack_id: String, keys: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> LanguagePackStrings:
        """
        Returns strings from a language pack in the current localization target by their keys. Can be called before authorization

        :param language_pack_id: Language pack identifier of the strings to be returned
        :type language_pack_id: :class:`String`
        :param keys: Language pack keys of the strings to be returned; leave empty to request all available strings
        :type keys: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LanguagePackStrings`
        """

        return await self.client.request(
            GetLanguagePackStrings(
                language_pack_id=language_pack_id,
                keys=keys,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_localization_target_info(
        self, only_local: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> LocalizationTargetInfo:
        """
        Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization

        :param only_local: Pass true to get only locally available information without sending network requests
        :type only_local: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LocalizationTargetInfo`
        """

        return await self.client.request(
            GetLocalizationTargetInfo(
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_stream(self, *, request_id: str = None, request_timeout: int = None) -> LogStream:
        """
        Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
        """

        return await self.client.request(
            GetLogStream(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_tag_verbosity_level(
        self, tag: String, *, request_id: str = None, request_timeout: int = None
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously

        :param tag: Logging tag to change verbosity level
        :type tag: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LogVerbosityLevel`
        """

        return await self.client.request(
            GetLogTagVerbosityLevel(
                tag=tag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_tags(self, *, request_id: str = None, request_timeout: int = None) -> LogTags:
        """
        Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. Can be called synchronously
        """

        return await self.client.request(
            GetLogTags(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_log_verbosity_level(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
        """

        return await self.client.request(
            GetLogVerbosityLevel(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_login_url(
        self,
        chat_id: Int53,
        message_id: Int53,
        button_id: Int53,
        allow_write_access: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button

        :param chat_id: Chat identifier of the message with the button
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier of the message with the button
        :type message_id: :class:`Int53`
        :param button_id: Button identifier
        :type button_id: :class:`Int53`
        :param allow_write_access: Pass true to allow the bot to send messages to the current user
        :type allow_write_access: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetLoginUrl(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_login_url_info(
        self,
        chat_id: Int53,
        message_id: Int53,
        button_id: Int53,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> LoginUrlInfo:
        """
        Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button

        :param chat_id: Chat identifier of the message with the button
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier of the message with the button
        :type message_id: :class:`Int53`
        :param button_id: Button identifier
        :type button_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.LoginUrlInfo`
        """

        return await self.client.request(
            GetLoginUrlInfo(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_map_thumbnail_file(
        self,
        location: Location,
        zoom: Int32,
        width: Int32,
        height: Int32,
        scale: Int32,
        chat_id: Int53,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded

        :param location: Location of the map center
        :type location: :class:`Location`
        :param zoom: Map zoom level; 13-20
        :type zoom: :class:`Int32`
        :param width: Map width in pixels before applying scale; 16-1024
        :type width: :class:`Int32`
        :param height: Map height in pixels before applying scale; 16-1024
        :type height: :class:`Int32`
        :param scale: Map scale; 1-3
        :type scale: :class:`Int32`
        :param chat_id: Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            GetMapThumbnailFile(
                location=location,
                zoom=zoom,
                width=width,
                height=height,
                scale=scale,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_markdown_text(
        self, text: FormattedText, *, request_id: str = None, request_timeout: int = None
    ) -> FormattedText:
        """
        Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously

        :param text: The text
        :type text: :class:`FormattedText`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """

        return await self.client.request(
            GetMarkdownText(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_me(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns the current user
        """

        return await self.client.request(
            GetMe(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_menu_button(
        self, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> BotMenuButton:
        """
        Returns menu button set by the bot for the given user; for bots only

        :param user_id: Identifier of the user or 0 to get the default menu button
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.BotMenuButton`
        """

        return await self.client.request(
            GetMenuButton(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Message:
        """
        Returns information about a message

        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message to get
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_added_reactions(
        self,
        chat_id: Int53,
        message_id: Int53,
        offset: String,
        limit: Int32,
        reaction_type: typing.Optional[ReactionType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> AddedReactions:
        """
        Returns reactions added for a message, along with their sender

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of reactions to be returned; must be positive and can't be greater than 100
        :type limit: :class:`Int32`
        :param reaction_type: Type of the reactions to return; pass null to return all added reactions, defaults to None
        :type reaction_type: :class:`ReactionType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AddedReactions`
        """

        return await self.client.request(
            GetMessageAddedReactions(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
                reaction_type=reaction_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_available_reactions(
        self, chat_id: Int53, message_id: Int53, row_size: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> AvailableReactions:
        """
        Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param row_size: Number of reaction per row, 5-25
        :type row_size: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AvailableReactions`
        """

        return await self.client.request(
            GetMessageAvailableReactions(
                chat_id=chat_id,
                message_id=message_id,
                row_size=row_size,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_embedding_code(
        self,
        chat_id: Int53,
        message_id: Int53,
        for_album: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Text:
        """
        Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param for_album: Pass true to return an HTML code for embedding of the whole media album
        :type for_album: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetMessageEmbeddingCode(
                chat_id=chat_id,
                message_id=message_id,
                for_album=for_album,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_file_type(
        self, message_file_head: String, *, request_id: str = None, request_timeout: int = None
    ) -> MessageFileType:
        """
        Returns information about a file with messages exported from another application

        :param message_file_head: Beginning of the message file; up to 100 first lines
        :type message_file_head: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageFileType`
        """

        return await self.client.request(
            GetMessageFileType(
                message_file_head=message_file_head,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_import_confirmation_text(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns a confirmation text to be shown to the user before starting message import

        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetMessageImportConfirmationText(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_link(
        self,
        chat_id: Int53,
        message_id: Int53,
        media_timestamp: Int32 = 0,
        for_album: Bool = False,
        in_message_thread: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> MessageLink:
        """
        Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param media_timestamp: If not 0, timestamp from which the video/audio/video note/voice note playing must start, in seconds. The media can be in the message content or in its web page preview
        :type media_timestamp: :class:`Int32`
        :param for_album: Pass true to create a link for the whole media album
        :type for_album: :class:`Bool`
        :param in_message_thread: Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic
        :type in_message_thread: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageLink`
        """

        return await self.client.request(
            GetMessageLink(
                chat_id=chat_id,
                message_id=message_id,
                media_timestamp=media_timestamp,
                for_album=for_album,
                in_message_thread=in_message_thread,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_link_info(
        self, url: String, *, request_id: str = None, request_timeout: int = None
    ) -> MessageLinkInfo:
        """
        Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage

        :param url: The message link
        :type url: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageLinkInfo`
        """

        return await self.client.request(
            GetMessageLinkInfo(
                url=url,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_locally(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Message:
        """
        Returns information about a message, if it is available without sending network request. This is an offline request

        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message to get
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetMessageLocally(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_public_forwards(
        self,
        chat_id: Int53,
        message_id: Int53,
        offset: String,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundMessages:
        """
        Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib

        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """

        return await self.client.request(
            GetMessagePublicForwards(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_statistics(
        self,
        chat_id: Int53,
        message_id: Int53,
        is_dark: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> MessageStatistics:
        """
        Returns detailed statistics about a message. Can be used only if message.can_get_statistics == true

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param is_dark: Pass true if a dark theme is used by the application
        :type is_dark: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageStatistics`
        """

        return await self.client.request(
            GetMessageStatistics(
                chat_id=chat_id,
                message_id=message_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_thread(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> MessageThreadInfo:
        """
        Returns information about a message thread. Can be used only if message.can_get_message_thread == true

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageThreadInfo`
        """

        return await self.client.request(
            GetMessageThread(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_thread_history(
        self,
        chat_id: Int53,
        message_id: Int53,
        from_message_id: Int53,
        offset: Int32,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Messages:
        """
        Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier, which thread history needs to be returned
        :type message_id: :class:`Int53`
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`Int53`
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        :type offset: :class:`Int32`
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            GetMessageThreadHistory(
                chat_id=chat_id,
                message_id=message_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_message_viewers(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> MessageViewers:
        """
        Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if message.can_get_viewers == true

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageViewers`
        """

        return await self.client.request(
            GetMessageViewers(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_messages(
        self, chat_id: Int53, message_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Messages:
        """
        Returns information about messages. If a message is not found, returns null on the corresponding position of the result

        :param chat_id: Identifier of the chat the messages belong to
        :type chat_id: :class:`Int53`
        :param message_ids: Identifiers of the messages to get
        :type message_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            GetMessages(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_network_statistics(
        self, only_current: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> NetworkStatistics:
        """
        Returns network data usage statistics. Can be called before authorization

        :param only_current: Pass true to get statistics only for the current library launch
        :type only_current: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NetworkStatistics`
        """

        return await self.client.request(
            GetNetworkStatistics(
                only_current=only_current,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_option(self, name: String, *, request_id: str = None, request_timeout: int = None) -> OptionValue:
        """
        Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization. Can be called synchronously for options "version" and "commit_hash"

        :param name: The name of the option
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.OptionValue`
        """

        return await self.client.request(
            GetOption(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form(
        self,
        bot_user_id: Int53,
        scope: String,
        public_key: String,
        nonce: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PassportAuthorizationForm:
        """
        Returns a Telegram Passport authorization form for sharing data with a service

        :param bot_user_id: User identifier of the service's bot
        :type bot_user_id: :class:`Int53`
        :param scope: Telegram Passport element types requested by the service
        :type scope: :class:`String`
        :param public_key: Service's public key
        :type public_key: :class:`String`
        :param nonce: Unique request identifier provided by the service
        :type nonce: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportAuthorizationForm`
        """

        return await self.client.request(
            GetPassportAuthorizationForm(
                bot_user_id=bot_user_id,
                scope=scope,
                public_key=public_key,
                nonce=nonce,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_authorization_form_available_elements(
        self, authorization_form_id: Int32, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> PassportElementsWithErrors:
        """
        Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form

        :param authorization_form_id: Authorization form identifier
        :type authorization_form_id: :class:`Int32`
        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElementsWithErrors`
        """

        return await self.client.request(
            GetPassportAuthorizationFormAvailableElements(
                authorization_form_id=authorization_form_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_passport_element(
        self, type_: PassportElementType, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> PassportElement:
        """
        Returns one of the available Telegram Passport elements

        :param type_: Telegram Passport element type
        :type type_: :class:`PassportElementType`
        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElement`
        """

        return await self.client.request(
            GetPassportElement(
                type=type_,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_password_state(self, *, request_id: str = None, request_timeout: int = None) -> PasswordState:
        """
        Returns the current state of 2-step verification
        """

        return await self.client.request(
            GetPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_payment_form(
        self,
        input_invoice: InputInvoice,
        theme: typing.Optional[ThemeParameters] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PaymentForm:
        """
        Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy

        :param input_invoice: The invoice
        :type input_invoice: :class:`InputInvoice`
        :param theme: Preferred payment form theme; pass null to use the default theme, defaults to None
        :type theme: :class:`ThemeParameters`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentForm`
        """

        return await self.client.request(
            GetPaymentForm(
                input_invoice=input_invoice,
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_payment_receipt(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> PaymentReceipt:
        """
        Returns information about a successful payment

        :param chat_id: Chat identifier of the messagePaymentSuccessful message
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentReceipt`
        """

        return await self.client.request(
            GetPaymentReceipt(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_phone_number_info(
        self, phone_number_prefix: String, *, request_id: str = None, request_timeout: int = None
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix. Can be called before authorization

        :param phone_number_prefix: The phone number prefix
        :type phone_number_prefix: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PhoneNumberInfo`
        """

        return await self.client.request(
            GetPhoneNumberInfo(
                phone_number_prefix=phone_number_prefix,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_phone_number_info_sync(
        self, language_code: String, phone_number_prefix: String, *, request_id: str = None, request_timeout: int = None
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously

        :param language_code: A two-letter ISO 639-1 language code for country information localization
        :type language_code: :class:`String`
        :param phone_number_prefix: The phone number prefix
        :type phone_number_prefix: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PhoneNumberInfo`
        """

        return await self.client.request(
            GetPhoneNumberInfoSync(
                language_code=language_code,
                phone_number_prefix=phone_number_prefix,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_poll_voters(
        self,
        chat_id: Int53,
        message_id: Int53,
        option_id: Int32,
        offset: Int32,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> MessageSenders:
        """
        Returns message senders voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib

        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`Int53`
        :param option_id: 0-based identifier of the answer option
        :type option_id: :class:`Int32`
        :param offset: Number of voters to skip in the result; must be non-negative
        :type offset: :class:`Int32`
        :param limit: The maximum number of voters to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """

        return await self.client.request(
            GetPollVoters(
                chat_id=chat_id,
                message_id=message_id,
                option_id=option_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_preferred_country_language(
        self, country_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown

        :param country_code: A two-letter ISO 3166-1 alpha-2 country code
        :type country_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetPreferredCountryLanguage(
                country_code=country_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_premium_features(
        self, source: typing.Optional[PremiumSource] = None, *, request_id: str = None, request_timeout: int = None
    ) -> PremiumFeatures:
        """
        Returns information about features, available to Premium users

        :param source: Source of the request; pass null if the method is called from some non-standard source, defaults to None
        :type source: :class:`PremiumSource`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PremiumFeatures`
        """

        return await self.client.request(
            GetPremiumFeatures(
                source=source,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_premium_limit(
        self, limit_type: PremiumLimitType, *, request_id: str = None, request_timeout: int = None
    ) -> PremiumLimit:
        """
        Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown

        :param limit_type: Type of the limit
        :type limit_type: :class:`PremiumLimitType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PremiumLimit`
        """

        return await self.client.request(
            GetPremiumLimit(
                limit_type=limit_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_premium_state(self, *, request_id: str = None, request_timeout: int = None) -> PremiumState:
        """
        Returns state of Telegram Premium subscription and promotion videos for Premium features
        """

        return await self.client.request(
            GetPremiumState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_premium_sticker_examples(self, *, request_id: str = None, request_timeout: int = None) -> Stickers:
        """
        Returns examples of premium stickers for demonstration purposes
        """

        return await self.client.request(
            GetPremiumStickerExamples(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_premium_stickers(
        self, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns premium stickers from regular sticker sets

        :param limit: The maximum number of stickers to be returned; 0-100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            GetPremiumStickers(
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_proxies(self, *, request_id: str = None, request_timeout: int = None) -> Proxies:
        """
        Returns list of proxies that are currently set up. Can be called before authorization
        """

        return await self.client.request(
            GetProxies(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_proxy_link(self, proxy_id: Int32, *, request_id: str = None, request_timeout: int = None) -> HttpUrl:
        """
        Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization

        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetProxyLink(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_push_receiver_id(
        self, payload: String, *, request_id: str = None, request_timeout: int = None
    ) -> PushReceiverId:
        """
        Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously

        :param payload: JSON-encoded push notification payload
        :type payload: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PushReceiverId`
        """

        return await self.client.request(
            GetPushReceiverId(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recent_emoji_statuses(self, *, request_id: str = None, request_timeout: int = None) -> EmojiStatuses:
        """
        Returns recent emoji statuses
        """

        return await self.client.request(
            GetRecentEmojiStatuses(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recent_inline_bots(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns up to 20 recently used inline bots in the order of their last usage
        """

        return await self.client.request(
            GetRecentInlineBots(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recent_stickers(
        self, is_attached: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Stickers:
        """
        Returns a list of recently used stickers

        :param is_attached: Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
        :type is_attached: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            GetRecentStickers(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recently_opened_chats(
        self, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns recently opened chats; this is an offline request. Returns chats in the order of last opening

        :param limit: The maximum number of chats to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetRecentlyOpenedChats(
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recently_visited_t_me_urls(
        self, referrer: String, *, request_id: str = None, request_timeout: int = None
    ) -> TMeUrls:
        """
        Returns t.me URLs recently visited by a newly registered user

        :param referrer: Google Play referrer to identify the user
        :type referrer: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TMeUrls`
        """

        return await self.client.request(
            GetRecentlyVisitedTMeUrls(
                referrer=referrer,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recommended_chat_folders(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> RecommendedChatFolders:
        """
        Returns recommended chat folders for the current user
        """

        return await self.client.request(
            GetRecommendedChatFolders(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_recovery_email_address(
        self, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> RecoveryEmailAddress:
        """
        Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user

        :param password: The 2-step verification password for the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RecoveryEmailAddress`
        """

        return await self.client.request(
            GetRecoveryEmailAddress(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_remote_file(
        self,
        remote_file_id: String,
        file_type: typing.Optional[FileType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Returns information about a file by its remote identifier; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

        :param remote_file_id: Remote identifier of the file to get
        :type remote_file_id: :class:`String`
        :param file_type: File type; pass null if unknown, defaults to None
        :type file_type: :class:`FileType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            GetRemoteFile(
                remote_file_id=remote_file_id,
                file_type=file_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_replied_message(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Message:
        """
        Returns information about a message that is replied by a given message. Also, returns the pinned message, the game message, the invoice message, and the topic creation message for messages of the types messagePinMessage, messageGameScore, messagePaymentSuccessful, messageChatSetBackground and topic messages without replied message respectively

        :param chat_id: Identifier of the chat the message belongs to
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the reply message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            GetRepliedMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_animations(self, *, request_id: str = None, request_timeout: int = None) -> Animations:
        """
        Returns saved animations
        """

        return await self.client.request(
            GetSavedAnimations(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sound(
        self, notification_sound_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> NotificationSounds:
        """
        Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier

        :param notification_sound_id: Identifier of the notification sound
        :type notification_sound_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.NotificationSounds`
        """

        return await self.client.request(
            GetSavedNotificationSound(
                notification_sound_id=notification_sound_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_notification_sounds(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> NotificationSounds:
        """
        Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
        """

        return await self.client.request(
            GetSavedNotificationSounds(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> OrderInfo:
        """
        Returns saved order information. Returns a 404 error if there is no saved order information
        """

        return await self.client.request(
            GetSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_scope_notification_settings(
        self, scope: NotificationSettingsScope, *, request_id: str = None, request_timeout: int = None
    ) -> ScopeNotificationSettings:
        """
        Returns the notification settings for chats of a given type

        :param scope: Types of chats for which to return the notification settings information
        :type scope: :class:`NotificationSettingsScope`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ScopeNotificationSettings`
        """

        return await self.client.request(
            GetScopeNotificationSettings(
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_secret_chat(
        self, secret_chat_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> SecretChat:
        """
        Returns information about a secret chat by its identifier. This is an offline request

        :param secret_chat_id: Secret chat identifier
        :type secret_chat_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SecretChat`
        """

        return await self.client.request(
            GetSecretChat(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_statistical_graph(
        self, chat_id: Int53, token: String, x: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> StatisticalGraph:
        """
        Loads an asynchronous or a zoomed in statistical graph

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param token: The token for graph loading
        :type token: :class:`String`
        :param x: X-value for zoomed in graph or 0 otherwise
        :type x: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StatisticalGraph`
        """

        return await self.client.request(
            GetStatisticalGraph(
                chat_id=chat_id,
                token=token,
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_sticker_emojis(
        self, sticker: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Emojis:
        """
        Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

        :param sticker: Sticker file identifier
        :type sticker: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Emojis`
        """

        return await self.client.request(
            GetStickerEmojis(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_sticker_set(
        self, set_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> StickerSet:
        """
        Returns information about a sticker set by its identifier

        :param set_id: Identifier of the sticker set
        :type set_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """

        return await self.client.request(
            GetStickerSet(
                set_id=set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_stickers(
        self,
        sticker_type: StickerType,
        query: String,
        limit: Int32,
        chat_id: Int53,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Stickers:
        """
        Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned

        :param sticker_type: Type of the stickers to return
        :type sticker_type: :class:`StickerType`
        :param query: Search query; a space-separated list of emoji or a keyword prefix. If empty, returns all known installed stickers
        :type query: :class:`String`
        :param limit: The maximum number of stickers to be returned
        :type limit: :class:`Int32`
        :param chat_id: Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            GetStickers(
                sticker_type=sticker_type,
                query=query,
                limit=limit,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_storage_statistics(
        self, chat_limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> StorageStatistics:
        """
        Returns storage usage statistics. Can be called before authorization

        :param chat_limit: The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
        :type chat_limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StorageStatistics`
        """

        return await self.client.request(
            GetStorageStatistics(
                chat_limit=chat_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_storage_statistics_fast(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> StorageStatisticsFast:
        """
        Quickly returns approximate storage usage statistics. Can be called before authorization
        """

        return await self.client.request(
            GetStorageStatisticsFast(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_story(
        self,
        story_sender_chat_id: Int53,
        story_id: Int32,
        only_local: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Story:
        """
        Returns a story

        :param story_sender_chat_id: Identifier of the chat that posted the story
        :type story_sender_chat_id: :class:`Int53`
        :param story_id: Story identifier
        :type story_id: :class:`Int32`
        :param only_local: Pass true to get only locally available information without sending network requests
        :type only_local: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Story`
        """

        return await self.client.request(
            GetStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_story_available_reactions(
        self, row_size: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> AvailableReactions:
        """
        Returns reactions, which can be chosen for a story

        :param row_size: Number of reaction per row, 5-25
        :type row_size: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AvailableReactions`
        """

        return await self.client.request(
            GetStoryAvailableReactions(
                row_size=row_size,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_story_notification_settings_exceptions(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns list of chats with non-default notification settings for stories
        """

        return await self.client.request(
            GetStoryNotificationSettingsExceptions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_story_viewers(
        self,
        story_id: Int32,
        offset: String,
        limit: Int32,
        query: String = "",
        only_contacts: Bool = False,
        prefer_with_reaction: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> StoryViewers:
        """
        Returns viewers of a story. The method can be called if story.can_get_viewers == true

        :param story_id: Story identifier
        :type story_id: :class:`Int32`
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of story viewers to return
        :type limit: :class:`Int32`
        :param query: Query to search for in names and usernames of the viewers; may be empty to get all relevant viewers
        :type query: :class:`String`
        :param only_contacts: Pass true to get only contacts; pass false to get all relevant viewers
        :type only_contacts: :class:`Bool`
        :param prefer_with_reaction: Pass true to get viewers with reaction first; pass false to get viewers sorted just by view_date
        :type prefer_with_reaction: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StoryViewers`
        """

        return await self.client.request(
            GetStoryViewers(
                story_id=story_id,
                offset=offset,
                limit=limit,
                query=query,
                only_contacts=only_contacts,
                prefer_with_reaction=prefer_with_reaction,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suggested_file_name(
        self, file_id: Int32, directory: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns suggested name for saving a file in a given directory

        :param file_id: Identifier of the file
        :type file_id: :class:`Int32`
        :param directory: Directory in which the file is supposed to be saved
        :type directory: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetSuggestedFileName(
                file_id=file_id,
                directory=directory,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suggested_sticker_set_name(
        self, title: String, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Returns a suggested name for a new sticker set with a given title

        :param title: Sticker set title; 1-64 characters
        :type title: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetSuggestedStickerSetName(
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_suitable_discussion_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first
        """

        return await self.client.request(
            GetSuitableDiscussionChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup(
        self, supergroup_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Supergroup:
        """
        Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot

        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Supergroup`
        """

        return await self.client.request(
            GetSupergroup(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup_full_info(
        self, supergroup_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> SupergroupFullInfo:
        """
        Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

        :param supergroup_id: Supergroup or channel identifier
        :type supergroup_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.SupergroupFullInfo`
        """

        return await self.client.request(
            GetSupergroupFullInfo(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_supergroup_members(
        self,
        supergroup_id: Int53,
        offset: Int32,
        limit: Int32,
        filter_: typing.Optional[SupergroupMembersFilter] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatMembers:
        """
        Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters

        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`Int53`
        :param offset: Number of users to skip
        :type offset: :class:`Int32`
        :param limit: The maximum number of users be returned; up to 200
        :type limit: :class:`Int32`
        :param filter_: The type of users to return; pass null to use supergroupMembersFilterRecent, defaults to None
        :type filter_: :class:`SupergroupMembersFilter`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMembers`
        """

        return await self.client.request(
            GetSupergroupMembers(
                supergroup_id=supergroup_id,
                offset=offset,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_support_name(self, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Returns localized name of the Telegram support user; for Telegram support only
        """

        return await self.client.request(
            GetSupportName(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_support_user(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns a user that can be contacted to get support
        """

        return await self.client.request(
            GetSupportUser(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_temporary_password_state(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> TemporaryPasswordState:
        """
        Returns information about the current temporary password
        """

        return await self.client.request(
            GetTemporaryPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_text_entities(
        self, text: String, *, request_id: str = None, request_timeout: int = None
    ) -> TextEntities:
        """
        Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) found in the text. Can be called synchronously

        :param text: The text in which to look for entities
        :type text: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TextEntities`
        """

        return await self.client.request(
            GetTextEntities(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_theme_parameters_json_string(
        self, theme: ThemeParameters, *, request_id: str = None, request_timeout: int = None
    ) -> Text:
        """
        Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously

        :param theme: Theme parameters to convert to JSON
        :type theme: :class:`ThemeParameters`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            GetThemeParametersJsonString(
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_themed_emoji_statuses(self, *, request_id: str = None, request_timeout: int = None) -> EmojiStatuses:
        """
        Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list
        """

        return await self.client.request(
            GetThemedEmojiStatuses(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_top_chats(
        self, category: TopChatCategory, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Returns a list of frequently used chats

        :param category: Category of chats to be returned
        :type category: :class:`TopChatCategory`
        :param limit: The maximum number of chats to be returned; up to 30
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            GetTopChats(
                category=category,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_trending_sticker_sets(
        self,
        sticker_type: StickerType,
        offset: Int32,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> TrendingStickerSets:
        """
        Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib

        :param sticker_type: Type of the sticker sets to return
        :type sticker_type: :class:`StickerType`
        :param offset: The offset from which to return the sticker sets; must be non-negative
        :type offset: :class:`Int32`
        :param limit: The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TrendingStickerSets`
        """

        return await self.client.request(
            GetTrendingStickerSets(
                sticker_type=sticker_type,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user(self, user_id: Int53, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns information about a user by their identifier. This is an offline request if the current user is not a bot

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.User`
        """

        return await self.client.request(
            GetUser(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_full_info(
        self, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> UserFullInfo:
        """
        Returns full information about a user by their identifier

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserFullInfo`
        """

        return await self.client.request(
            GetUserFullInfo(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_link(self, *, request_id: str = None, request_timeout: int = None) -> UserLink:
        """
        Returns an HTTPS link, which can be used to get information about the current user
        """

        return await self.client.request(
            GetUserLink(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_privacy_setting_rules(
        self, setting: UserPrivacySetting, *, request_id: str = None, request_timeout: int = None
    ) -> UserPrivacySettingRules:
        """
        Returns the current privacy settings

        :param setting: The privacy setting
        :type setting: :class:`UserPrivacySetting`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserPrivacySettingRules`
        """

        return await self.client.request(
            GetUserPrivacySettingRules(
                setting=setting,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_profile_photos(
        self, user_id: Int53, offset: Int32, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> ChatPhotos:
        """
        Returns the profile photos of a user. Personal and public photo aren't returned

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param offset: The number of photos to skip; must be non-negative
        :type offset: :class:`Int32`
        :param limit: The maximum number of photos to be returned; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatPhotos`
        """

        return await self.client.request(
            GetUserProfilePhotos(
                user_id=user_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_user_support_info(
        self, user_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> UserSupportInfo:
        """
        Returns support information for the given user; for Telegram support only

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserSupportInfo`
        """

        return await self.client.request(
            GetUserSupportInfo(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_video_chat_available_participants(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> MessageSenders:
        """
        Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.MessageSenders`
        """

        return await self.client.request(
            GetVideoChatAvailableParticipants(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_video_chat_rtmp_url(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> RtmpUrl:
        """
        Returns RTMP URL for streaming to the chat; requires creator privileges

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RtmpUrl`
        """

        return await self.client.request(
            GetVideoChatRtmpUrl(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_app_link_url(
        self,
        bot_user_id: Int53,
        web_app_short_name: String,
        start_parameter: String,
        application_name: String,
        chat_id: Int53 = 0,
        allow_write_access: Bool = False,
        theme: typing.Optional[ThemeParameters] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param web_app_short_name: Short name of the Web App
        :type web_app_short_name: :class:`String`
        :param start_parameter: Start parameter from internalLinkTypeWebApp
        :type start_parameter: :class:`String`
        :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
        :type application_name: :class:`String`
        :param chat_id: Identifier of the chat in which the link was clicked; pass 0 if none
        :type chat_id: :class:`Int53`
        :param allow_write_access: Pass true if the current user allowed the bot to send them messages
        :type allow_write_access: :class:`Bool`
        :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
        :type theme: :class:`ThemeParameters`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetWebAppLinkUrl(
                bot_user_id=bot_user_id,
                web_app_short_name=web_app_short_name,
                start_parameter=start_parameter,
                application_name=application_name,
                chat_id=chat_id,
                allow_write_access=allow_write_access,
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_app_url(
        self,
        bot_user_id: Int53,
        url: String,
        application_name: String,
        theme: typing.Optional[ThemeParameters] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> HttpUrl:
        """
        Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, an inlineQueryResultsButtonTypeWebApp button, or an internalLinkTypeSideMenuBot link

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param url: The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, an internalLinkTypeSideMenuBot link, or an empty when the bot is opened from the side menu
        :type url: :class:`String`
        :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
        :type application_name: :class:`String`
        :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
        :type theme: :class:`ThemeParameters`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.HttpUrl`
        """

        return await self.client.request(
            GetWebAppUrl(
                bot_user_id=bot_user_id,
                url=url,
                application_name=application_name,
                theme=theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_page_instant_view(
        self, url: String, force_full: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> WebPageInstantView:
        """
        Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page

        :param url: The web page URL
        :type url: :class:`String`
        :param force_full: Pass true to get full instant view for the web page
        :type force_full: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebPageInstantView`
        """

        return await self.client.request(
            GetWebPageInstantView(
                url=url,
                force_full=force_full,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def get_web_page_preview(
        self, text: FormattedText, *, request_id: str = None, request_timeout: int = None
    ) -> WebPage:
        """
        Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview

        :param text: Message text with formatting
        :type text: :class:`FormattedText`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebPage`
        """

        return await self.client.request(
            GetWebPagePreview(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def hide_suggested_action(
        self, action: SuggestedAction, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Hides a suggested action

        :param action: Suggested action to hide
        :type action: :class:`SuggestedAction`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            HideSuggestedAction(
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def import_contacts(
        self, contacts: Vector[Contact], *, request_id: str = None, request_timeout: int = None
    ) -> ImportedContacts:
        """
        Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

        :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
        :type contacts: :class:`Vector[Contact]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ImportedContacts`
        """

        return await self.client.request(
            ImportContacts(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def import_messages(
        self,
        chat_id: Int53,
        message_file: InputFile,
        attached_files: Vector[InputFile],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Imports messages exported from another app

        :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        :type chat_id: :class:`Int53`
        :param message_file: File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded
        :type message_file: :class:`InputFile`
        :param attached_files: Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded
        :type attached_files: :class:`Vector[InputFile]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ImportMessages(
                chat_id=chat_id,
                message_file=message_file,
                attached_files=attached_files,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def invite_group_call_participants(
        self, group_call_id: Int32, user_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Invites users to an active group call. Sends a service message of type messageInviteToGroupCall for video chats

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param user_ids: User identifiers. At most 10 users can be invited simultaneously
        :type user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            InviteGroupCallParticipants(
                group_call_id=group_call_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            JoinChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_chat_by_invite_link(
        self, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Uses an invite link to add the current user to the chat if possible. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created

        :param invite_link: Invite link to use
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            JoinChatByInviteLink(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def join_group_call(
        self,
        group_call_id: Int32,
        audio_source_id: Int32,
        payload: String,
        invite_hash: String,
        is_muted: Bool = False,
        is_my_video_enabled: Bool = False,
        participant_id: typing.Optional[MessageSender] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Text:
        """
        Joins an active group call. Returns join response payload for tgcalls

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param audio_source_id: Caller audio channel synchronization source identifier; received from tgcalls
        :type audio_source_id: :class:`Int32`
        :param payload: Group call join payload; received from tgcalls
        :type payload: :class:`String`
        :param invite_hash: If non-empty, invite hash to be used to join the group call without being muted by administrators
        :type invite_hash: :class:`String`
        :param is_muted: Pass true to join the call with muted microphone
        :type is_muted: :class:`Bool`
        :param is_my_video_enabled: Pass true if the user's video is enabled
        :type is_my_video_enabled: :class:`Bool`
        :param participant_id: Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only, defaults to None
        :type participant_id: :class:`MessageSender`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            JoinGroupCall(
                group_call_id=group_call_id,
                audio_source_id=audio_source_id,
                payload=payload,
                invite_hash=invite_hash,
                is_muted=is_muted,
                is_my_video_enabled=is_my_video_enabled,
                participant_id=participant_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def leave_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Removes the current user from chat members. Private and secret chats can't be left using this method

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            LeaveChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def leave_group_call(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Leaves a group call

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            LeaveGroupCall(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def load_active_stories(
        self, story_list: StoryList, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Loads more active stories from a story list. The loaded stories will be sent through updates. Active stories are sorted by the pair (active_stories.order, active_stories.story_sender_chat_id) in descending order. Returns a 404 error if all active stories have been loaded

        :param story_list: The story list in which to load active stories
        :type story_list: :class:`StoryList`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            LoadActiveStories(
                story_list=story_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def load_chats(
        self,
        limit: Int32,
        chat_list: typing.Optional[ChatList] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded

        :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
        :type limit: :class:`Int32`
        :param chat_list: The chat list in which to load chats; pass null to load chats from the main chat list, defaults to None
        :type chat_list: :class:`ChatList`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            LoadChats(
                limit=limit,
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def load_group_call_participants(
        self, group_call_id: Int32, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded

        :param group_call_id: Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
        :type group_call_id: :class:`Int32`
        :param limit: The maximum number of participants to load; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            LoadGroupCallParticipants(
                group_call_id=group_call_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def log_out(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent
        """

        return await self.client.request(
            LogOut(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_chat(self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            OpenChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_message_content(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed

        :param chat_id: Chat identifier of the message
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message with the opened content
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            OpenMessageContent(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_story(
        self, story_sender_chat_id: Int53, story_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that a story is opened and is being viewed by the user

        :param story_sender_chat_id: The identifier of the sender of the opened story
        :type story_sender_chat_id: :class:`Int53`
        :param story_id: The identifier of the story
        :type story_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            OpenStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def open_web_app(
        self,
        chat_id: Int53,
        bot_user_id: Int53,
        url: String,
        application_name: String,
        message_thread_id: Int53 = 0,
        theme: typing.Optional[ThemeParameters] = None,
        reply_to: typing.Optional[MessageReplyTo] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> WebAppInfo:
        """
        Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once

        :param chat_id: Identifier of the chat in which the Web App is opened. The Web App can't be opened in secret chats
        :type chat_id: :class:`Int53`
        :param bot_user_id: Identifier of the bot, providing the Web App
        :type bot_user_id: :class:`Int53`
        :param url: The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise
        :type url: :class:`String`
        :param application_name: Short name of the application; 0-64 English letters, digits, and underscores
        :type application_name: :class:`String`
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
        :type message_thread_id: :class:`Int53`
        :param theme: Preferred Web App theme; pass null to use the default theme, defaults to None
        :type theme: :class:`ThemeParameters`, optional
        :param reply_to: Identifier of the replied message or story for the message sent by the Web App; pass null if none, defaults to None
        :type reply_to: :class:`MessageReplyTo`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.WebAppInfo`
        """

        return await self.client.request(
            OpenWebApp(
                chat_id=chat_id,
                bot_user_id=bot_user_id,
                url=url,
                application_name=application_name,
                message_thread_id=message_thread_id,
                theme=theme,
                reply_to=reply_to,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def optimize_storage(
        self,
        size: Int53,
        ttl: Int32,
        count: Int32,
        immunity_delay: Int32,
        file_types: Vector[FileType],
        chat_ids: Vector[Int53],
        exclude_chat_ids: Vector[Int53],
        chat_limit: Int32,
        return_deleted_file_statistics: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> StorageStatistics:
        """
        Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted

        :param size: Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit
        :type size: :class:`Int53`
        :param ttl: Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
        :type ttl: :class:`Int32`
        :param count: Limit on the total number of files after deletion. Pass -1 to use the default limit
        :type count: :class:`Int32`
        :param immunity_delay: The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
        :type immunity_delay: :class:`Int32`
        :param file_types: If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
        :type file_types: :class:`Vector[FileType]`
        :param chat_ids: If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
        :type chat_ids: :class:`Vector[Int53]`
        :param exclude_chat_ids: If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
        :type exclude_chat_ids: :class:`Vector[Int53]`
        :param chat_limit: Same as in getStorageStatistics. Affects only returned statistics
        :type chat_limit: :class:`Int32`
        :param return_deleted_file_statistics: Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
        :type return_deleted_file_statistics: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StorageStatistics`
        """

        return await self.client.request(
            OptimizeStorage(
                size=size,
                ttl=ttl,
                count=count,
                immunity_delay=immunity_delay,
                file_types=file_types,
                chat_ids=chat_ids,
                exclude_chat_ids=exclude_chat_ids,
                chat_limit=chat_limit,
                return_deleted_file_statistics=return_deleted_file_statistics,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def parse_markdown(
        self, text: FormattedText, *, request_id: str = None, request_timeout: int = None
    ) -> FormattedText:
        """
        Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously

        :param text: The text to parse. For example, "__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"
        :type text: :class:`FormattedText`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """

        return await self.client.request(
            ParseMarkdown(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def parse_text_entities(
        self, text: String, parse_mode: TextParseMode, *, request_id: str = None, request_timeout: int = None
    ) -> FormattedText:
        """
        Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Code, Pre, PreCode, TextUrl and MentionName entities from a marked-up text. Can be called synchronously

        :param text: The text to parse
        :type text: :class:`String`
        :param parse_mode: Text parse mode
        :type parse_mode: :class:`TextParseMode`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """

        return await self.client.request(
            ParseTextEntities(
                text=text,
                parse_mode=parse_mode,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def pin_chat_message(
        self,
        chat_id: Int53,
        message_id: Int53,
        disable_notification: Bool = False,
        only_for_self: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the new pinned message
        :type message_id: :class:`Int53`
        :param disable_notification: Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats
        :type disable_notification: :class:`Bool`
        :param only_for_self: Pass true to pin the message only for self; private chats only
        :type only_for_self: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            PinChatMessage(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
                only_for_self=only_for_self,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def ping_proxy(self, proxy_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Seconds:
        """
        Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization

        :param proxy_id: Proxy identifier. Use 0 to ping a Telegram server without a proxy
        :type proxy_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Seconds`
        """

        return await self.client.request(
            PingProxy(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def preliminary_upload_file(
        self,
        file: InputFile,
        priority: Int32,
        file_type: typing.Optional[FileType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes. Updates updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message

        :param file: File to upload
        :type file: :class:`InputFile`
        :param priority: Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first
        :type priority: :class:`Int32`
        :param file_type: File type; pass null if unknown, defaults to None
        :type file_type: :class:`FileType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            PreliminaryUploadFile(
                file=file,
                priority=priority,
                file_type=file_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_chat_folder_new_chats(
        self,
        chat_folder_id: Int32,
        added_chat_ids: Vector[Int53],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Process new chats added to a shareable chat folder by its owner

        :param chat_folder_id: Chat folder identifier
        :type chat_folder_id: :class:`Int32`
        :param added_chat_ids: Identifiers of the new chats, which are added to the chat folder. The chats are automatically joined if they aren't joined yet
        :type added_chat_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ProcessChatFolderNewChats(
                chat_folder_id=chat_folder_id,
                added_chat_ids=added_chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_chat_join_request(
        self,
        chat_id: Int53,
        user_id: Int53,
        approve: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Handles a pending join request in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param user_id: Identifier of the user that sent the request
        :type user_id: :class:`Int53`
        :param approve: Pass true to approve the request; pass false to decline it
        :type approve: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ProcessChatJoinRequest(
                chat_id=chat_id,
                user_id=user_id,
                approve=approve,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_chat_join_requests(
        self,
        chat_id: Int53,
        invite_link: String,
        approve: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Handles all pending join requests for a given link in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        :type invite_link: :class:`String`
        :param approve: Pass true to approve all requests; pass false to decline them
        :type approve: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ProcessChatJoinRequests(
                chat_id=chat_id,
                invite_link=invite_link,
                approve=approve,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def process_push_notification(
        self, payload: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization

        :param payload: JSON-encoded push notification payload with all fields sent by the server, and "google.sent_time" and "google.notification.sound" fields added
        :type payload: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ProcessPushNotification(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def rate_speech_recognition(
        self,
        chat_id: Int53,
        message_id: Int53,
        is_good: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Rates recognized speech in a video note or a voice note message

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param is_good: Pass true if the speech recognition is good
        :type is_good: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RateSpeechRecognition(
                chat_id=chat_id,
                message_id=message_id,
                is_good=is_good,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_chat_mentions(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Marks all mentions in a chat as read

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReadAllChatMentions(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_chat_reactions(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Marks all reactions in a chat or a forum topic as read

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReadAllChatReactions(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_message_thread_mentions(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Marks all mentions in a forum topic as read

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier in which mentions are marked as read
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReadAllMessageThreadMentions(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_all_message_thread_reactions(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Marks all reactions in a forum topic as read

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier in which reactions are marked as read
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReadAllMessageThreadReactions(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_chat_list(self, chat_list: ChatList, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Traverse all chats in a chat list and marks all messages in the chats as read

        :param chat_list: Chat list in which to mark all chats as read
        :type chat_list: :class:`ChatList`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReadChatList(
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def read_file_part(
        self, file_id: Int32, offset: Int53, count: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> FilePart:
        """
        Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

        :param file_id: Identifier of the file. The file must be located in the TDLib file cache
        :type file_id: :class:`Int32`
        :param offset: The offset from which to read the file
        :type offset: :class:`Int53`
        :param count: Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
        :type count: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FilePart`
        """

        return await self.client.request(
            ReadFilePart(
                file_id=file_id,
                offset=offset,
                count=count,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def recognize_speech(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Recognizes speech in a video note or a voice note message. The message must be successfully sent and must not be scheduled. May return an error with a message "MSG_VOICE_TOO_LONG" if media duration is too big to be recognized

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RecognizeSpeech(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def recover_authentication_password(
        self,
        recovery_code: String,
        new_password: String = "",
        new_hint: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword

        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`String`
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :type new_password: :class:`String`
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RecoverAuthenticationPassword(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def recover_password(
        self,
        recovery_code: String,
        new_password: String = "",
        new_hint: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PasswordState:
        """
        Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up

        :param recovery_code: Recovery code to check
        :type recovery_code: :class:`String`
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :type new_password: :class:`String`
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """

        return await self.client.request(
            RecoverPassword(
                recovery_code=recovery_code,
                new_password=new_password,
                new_hint=new_hint,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def register_device(
        self,
        device_token: DeviceToken,
        other_user_ids: Vector[Int53],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PushReceiverId:
        """
        Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription

        :param device_token: Device token
        :type device_token: :class:`DeviceToken`
        :param other_user_ids: List of user identifiers of other users currently using the application
        :type other_user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PushReceiverId`
        """

        return await self.client.request(
            RegisterDevice(
                device_token=device_token,
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def register_user(
        self, first_name: String, last_name: String = "", *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration

        :param first_name: The first name of the user; 1-64 characters
        :type first_name: :class:`String`
        :param last_name: The last name of the user; 0-64 characters
        :type last_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RegisterUser(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_all_files_from_downloads(
        self,
        only_active: Bool = False,
        only_completed: Bool = False,
        delete_from_cache: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Removes all files from the file download list

        :param only_active: Pass true to remove only active downloads, including paused
        :type only_active: :class:`Bool`
        :param only_completed: Pass true to remove only completed downloads
        :type only_completed: :class:`Bool`
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :type delete_from_cache: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveAllFilesFromDownloads(
                only_active=only_active,
                only_completed=only_completed,
                delete_from_cache=delete_from_cache,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_background(
        self, background_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes background from the list of installed backgrounds

        :param background_id: The background identifier
        :type background_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveBackground(
                background_id=background_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_chat_action_bar(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a chat action bar without any other action

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveChatActionBar(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_contacts(
        self, user_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes users from the contact list

        :param user_ids: Identifiers of users to be deleted
        :type user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveContacts(
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_favorite_sticker(
        self, sticker: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a sticker from the list of favorite stickers

        :param sticker: Sticker file to delete from the list
        :type sticker: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveFavoriteSticker(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_file_from_downloads(
        self, file_id: Int32, delete_from_cache: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a file from the file download list

        :param file_id: Identifier of the downloaded file
        :type file_id: :class:`Int32`
        :param delete_from_cache: Pass true to delete the file from the TDLib file cache
        :type delete_from_cache: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveFileFromDownloads(
                file_id=file_id,
                delete_from_cache=delete_from_cache,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_message_reaction(
        self,
        chat_id: Int53,
        message_id: Int53,
        reaction_type: ReactionType,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Removes a reaction from a message. A chosen reaction can always be removed

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param reaction_type: Type of the reaction to remove
        :type reaction_type: :class:`ReactionType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveMessageReaction(
                chat_id=chat_id,
                message_id=message_id,
                reaction_type=reaction_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_notification(
        self,
        notification_group_id: Int32,
        notification_id: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user

        :param notification_group_id: Identifier of notification group to which the notification belongs
        :type notification_group_id: :class:`Int32`
        :param notification_id: Identifier of removed notification
        :type notification_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveNotification(
                notification_group_id=notification_group_id,
                notification_id=notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_notification_group(
        self,
        notification_group_id: Int32,
        max_notification_id: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user

        :param notification_group_id: Notification group identifier
        :type notification_group_id: :class:`Int32`
        :param max_notification_id: The maximum identifier of removed notifications
        :type max_notification_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveNotificationGroup(
                notification_group_id=notification_group_id,
                max_notification_id=max_notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_proxy(self, proxy_id: Int32, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Removes a proxy server. Can be called before authorization

        :param proxy_id: Proxy identifier
        :type proxy_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveProxy(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recent_hashtag(
        self, hashtag: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a hashtag from the list of recently used hashtags

        :param hashtag: Hashtag to delete
        :type hashtag: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveRecentHashtag(
                hashtag=hashtag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recent_sticker(
        self, sticker: InputFile, is_attached: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a sticker from the list of recently used stickers

        :param sticker: Sticker file to delete
        :type sticker: :class:`InputFile`
        :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
        :type is_attached: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveRecentSticker(
                sticker=sticker,
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_recently_found_chat(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a chat from the list of recently found chats

        :param chat_id: Identifier of the chat to be removed
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveRecentlyFoundChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_saved_animation(
        self, animation: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes an animation from the list of saved animations

        :param animation: Animation file to be removed
        :type animation: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveSavedAnimation(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_saved_notification_sound(
        self, notification_sound_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a notification sound from the list of saved notification sounds

        :param notification_sound_id: Identifier of the notification sound
        :type notification_sound_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveSavedNotificationSound(
                notification_sound_id=notification_sound_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_sticker_from_set(
        self, sticker: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot

        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveStickerFromSet(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def remove_top_chat(
        self, category: TopChatCategory, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled

        :param category: Category of frequently used chats
        :type category: :class:`TopChatCategory`
        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RemoveTopChat(
                category=category,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_active_usernames(
        self, usernames: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes order of active usernames of the current user

        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :type usernames: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReorderActiveUsernames(
                usernames=usernames,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_bot_active_usernames(
        self, bot_user_id: Int53, usernames: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes order of active usernames of a bot. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :type usernames: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReorderBotActiveUsernames(
                bot_user_id=bot_user_id,
                usernames=usernames,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_chat_folders(
        self,
        chat_folder_ids: Vector[Int32],
        main_chat_list_position: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the order of chat folders

        :param chat_folder_ids: Identifiers of chat folders in the new correct order
        :type chat_folder_ids: :class:`Vector[Int32]`
        :param main_chat_list_position: Position of the main chat list among chat folders, 0-based. Can be non-zero only for Premium users
        :type main_chat_list_position: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReorderChatFolders(
                chat_folder_ids=chat_folder_ids,
                main_chat_list_position=main_chat_list_position,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_installed_sticker_sets(
        self,
        sticker_type: StickerType,
        sticker_set_ids: Vector[Int64],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the order of installed sticker sets

        :param sticker_type: Type of the sticker sets to reorder
        :type sticker_type: :class:`StickerType`
        :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
        :type sticker_set_ids: :class:`Vector[Int64]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReorderInstalledStickerSets(
                sticker_type=sticker_type,
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reorder_supergroup_active_usernames(
        self, supergroup_id: Int53, usernames: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`Int53`
        :param usernames: The new order of active usernames. All currently active usernames must be specified
        :type usernames: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReorderSupergroupActiveUsernames(
                supergroup_id=supergroup_id,
                usernames=usernames,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def replace_primary_chat_invite_link(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> ChatInviteLink:
        """
        Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLink`
        """

        return await self.client.request(
            ReplacePrimaryChatInviteLink(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def replace_video_chat_rtmp_url(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> RtmpUrl:
        """
        Replaces the current RTMP URL for streaming to the chat; requires creator privileges

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.RtmpUrl`
        """

        return await self.client.request(
            ReplaceVideoChatRtmpUrl(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_chat(
        self,
        chat_id: Int53,
        reason: ReportReason,
        message_ids: Vector[Int53] = [],
        text: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param reason: The reason for reporting the chat
        :type reason: :class:`ReportReason`
        :param message_ids: Identifiers of reported messages; may be empty to report the whole chat
        :type message_ids: :class:`Vector[Int53]`
        :param text: Additional report details; 0-1024 characters
        :type text: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportChat(
                chat_id=chat_id,
                reason=reason,
                message_ids=message_ids,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_chat_photo(
        self,
        chat_id: Int53,
        file_id: Int32,
        reason: ReportReason,
        text: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param file_id: Identifier of the photo to report. Only full photos from chatPhoto can be reported
        :type file_id: :class:`Int32`
        :param reason: The reason for reporting the chat photo
        :type reason: :class:`ReportReason`
        :param text: Additional report details; 0-1024 characters
        :type text: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportChatPhoto(
                chat_id=chat_id,
                file_id=file_id,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_message_reactions(
        self,
        chat_id: Int53,
        message_id: Int53,
        sender_id: MessageSender,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if message.can_report_reactions

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_id: Message identifier
        :type message_id: :class:`Int53`
        :param sender_id: Identifier of the sender, which added the reaction
        :type sender_id: :class:`MessageSender`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportMessageReactions(
                chat_id=chat_id,
                message_id=message_id,
                sender_id=sender_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_story(
        self,
        story_sender_chat_id: Int53,
        story_id: Int32,
        reason: ReportReason,
        text: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Reports a story to the Telegram moderators

        :param story_sender_chat_id: The identifier of the sender of the story to report
        :type story_sender_chat_id: :class:`Int53`
        :param story_id: The identifier of the story to report
        :type story_id: :class:`Int32`
        :param reason: The reason for reporting the story
        :type reason: :class:`ReportReason`
        :param text: Additional report details; 0-1024 characters
        :type text: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportStory(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_supergroup_anti_spam_false_positive(
        self, supergroup_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Reports a false deletion of a message by aggressive anti-spam checks; requires administrator rights in the supergroup. Can be called only for messages from chatEventMessageDeleted with can_report_anti_spam_false_positive == true

        :param supergroup_id: Supergroup identifier
        :type supergroup_id: :class:`Int53`
        :param message_id: Identifier of the erroneously deleted message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportSupergroupAntiSpamFalsePositive(
                supergroup_id=supergroup_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def report_supergroup_spam(
        self, supergroup_id: Int53, message_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Reports messages in a supergroup as spam; requires administrator rights in the supergroup

        :param supergroup_id: Supergroup identifier
        :type supergroup_id: :class:`Int53`
        :param message_ids: Identifiers of messages to report
        :type message_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ReportSupergroupSpam(
                supergroup_id=supergroup_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_authentication_password_recovery(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Requests to send a 2-step verification password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        """

        return await self.client.request(
            RequestAuthenticationPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_password_recovery(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Requests to send a 2-step verification password recovery code to an email address that was previously set up
        """

        return await self.client.request(
            RequestPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def request_qr_code_authentication(
        self, other_user_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        :param other_user_ids: List of user identifiers of other users currently using the application
        :type other_user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RequestQrCodeAuthentication(
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_authentication_code(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null and the server-specified timeout has passed, or when the current authorization state is authorizationStateWaitEmailCode
        """

        return await self.client.request(
            ResendAuthenticationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_change_phone_number_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Resends the authentication code sent to confirm a new phone number for the current user. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed
        """

        return await self.client.request(
            ResendChangePhoneNumberCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_email_address_verification_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Resends the code to verify an email address to be added to a user's Telegram Passport
        """

        return await self.client.request(
            ResendEmailAddressVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_login_email_address_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Resends the login email address verification code
        """

        return await self.client.request(
            ResendLoginEmailAddressCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_messages(
        self, chat_id: Int53, message_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Messages:
        """
        Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message

        :param chat_id: Identifier of the chat to send messages
        :type chat_id: :class:`Int53`
        :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
        :type message_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            ResendMessages(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_phone_number_confirmation_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Resends phone number confirmation code
        """

        return await self.client.request(
            ResendPhoneNumberConfirmationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_phone_number_verification_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Resends the code to verify a phone number to be added to a user's Telegram Passport
        """

        return await self.client.request(
            ResendPhoneNumberVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def resend_recovery_email_address_code(
        self, *, request_id: str = None, request_timeout: int = None
    ) -> PasswordState:
        """
        Resends the 2-step verification recovery email address verification code
        """

        return await self.client.request(
            ResendRecoveryEmailAddressCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_all_notification_settings(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all notification settings to their default values. By default, all chats are unmuted and message previews are shown
        """

        return await self.client.request(
            ResetAllNotificationSettings(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_authentication_email_address(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets the login email address. May return an error with a message "TASK_ALREADY_EXISTS" if reset is still pending. Works only when the current authorization state is authorizationStateWaitEmailCode and authorization_state.can_reset_email_address == true
        """

        return await self.client.request(
            ResetAuthenticationEmailAddress(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_backgrounds(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets list of installed backgrounds to its default value
        """

        return await self.client.request(
            ResetBackgrounds(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_network_statistics(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all network data usage statistics to zero. Can be called before authorization
        """

        return await self.client.request(
            ResetNetworkStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def reset_password(self, *, request_id: str = None, request_timeout: int = None) -> ResetPasswordResult:
        """
        Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time
        """

        return await self.client.request(
            ResetPassword(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def revoke_chat_invite_link(
        self, chat_id: Int53, invite_link: String, *, request_id: str = None, request_timeout: int = None
    ) -> ChatInviteLinks:
        """
        Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param invite_link: Invite link to be revoked
        :type invite_link: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatInviteLinks`
        """

        return await self.client.request(
            RevokeChatInviteLink(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def revoke_group_call_invite_link(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            RevokeGroupCallInviteLink(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def save_application_log_event(
        self, type_: String, chat_id: Int53, data: JsonValue, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Saves application log event on the server. Can be called before authorization

        :param type_: Event type
        :type type_: :class:`String`
        :param chat_id: Optional chat identifier, associated with the event
        :type chat_id: :class:`Int53`
        :param data: The log event data
        :type data: :class:`JsonValue`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SaveApplicationLogEvent(
                type=type_,
                chat_id=chat_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_background(
        self, name: String, *, request_id: str = None, request_timeout: int = None
    ) -> Background:
        """
        Searches for a background by its name

        :param name: The name of the background
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Background`
        """

        return await self.client.request(
            SearchBackground(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_call_messages(
        self,
        offset: String,
        limit: Int32,
        only_missed: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundMessages:
        """
        Searches for call messages. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param only_missed: Pass true to search only for messages with missed/declined calls
        :type only_missed: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """

        return await self.client.request(
            SearchCallMessages(
                offset=offset,
                limit=limit,
                only_missed=only_missed,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_members(
        self,
        chat_id: Int53,
        query: String,
        limit: Int32,
        filter_: typing.Optional[ChatMembersFilter] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ChatMembers:
        """
        Searches for a specified query in the first name, last name and usernames of the members of a specified chat. Requires administrator rights in channels

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param query: Query to search for
        :type query: :class:`String`
        :param limit: The maximum number of users to be returned; up to 200
        :type limit: :class:`Int32`
        :param filter_: The type of users to search for; pass null to search among all chat members, defaults to None
        :type filter_: :class:`ChatMembersFilter`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatMembers`
        """

        return await self.client.request(
            SearchChatMembers(
                chat_id=chat_id,
                query=query,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_messages(
        self,
        chat_id: Int53,
        query: String,
        from_message_id: Int53,
        offset: Int32,
        limit: Int32,
        message_thread_id: Int53 = 0,
        sender_id: typing.Optional[MessageSender] = None,
        filter_: typing.Optional[SearchMessagesFilter] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundChatMessages:
        """
        Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages must be used instead), or without an enabled message database. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit. A combination of query, sender_id, filter and message_thread_id search criteria is expected to be supported, only if it is required for Telegram official application implementation

        :param chat_id: Identifier of the chat in which to search messages
        :type chat_id: :class:`Int53`
        :param query: Query to search for
        :type query: :class:`String`
        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: :class:`Int53`
        :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
        :type offset: :class:`Int32`
        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param message_thread_id: If not 0, only messages in the specified thread will be returned; supergroups only
        :type message_thread_id: :class:`Int53`
        :param sender_id: Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats, defaults to None
        :type sender_id: :class:`MessageSender`, optional
        :param filter_: Additional filter for messages to search; pass null to search for all messages, defaults to None
        :type filter_: :class:`SearchMessagesFilter`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundChatMessages`
        """

        return await self.client.request(
            SearchChatMessages(
                chat_id=chat_id,
                query=query,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                message_thread_id=message_thread_id,
                sender_id=sender_id,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chat_recent_location_messages(
        self, chat_id: Int53, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Messages:
        """
        Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param limit: The maximum number of messages to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            SearchChatRecentLocationMessages(
                chat_id=chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats(
        self, query: String, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats; this is an offline request. Returns chats in the order seen in the main chat list

        :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
        :type query: :class:`String`
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            SearchChats(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats_nearby(
        self, location: Location, *, request_id: str = None, request_timeout: int = None
    ) -> ChatsNearby:
        """
        Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request must be sent again every 25 seconds with adjusted location to not miss new chats

        :param location: Current user location
        :type location: :class:`Location`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ChatsNearby`
        """

        return await self.client.request(
            SearchChatsNearby(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_chats_on_server(
        self, query: String, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list

        :param query: Query to search for
        :type query: :class:`String`
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            SearchChatsOnServer(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_contacts(
        self, limit: Int32, query: String = "", *, request_id: str = None, request_timeout: int = None
    ) -> Users:
        """
        Searches for the specified query in the first names, last names and usernames of the known user contacts

        :param limit: The maximum number of users to be returned
        :type limit: :class:`Int32`
        :param query: Query to search for; may be empty to return all contacts
        :type query: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Users`
        """

        return await self.client.request(
            SearchContacts(
                limit=limit,
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_emojis(
        self,
        text: String,
        exact_match: Bool = False,
        input_language_codes: Vector[String] = [],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Emojis:
        """
        Searches for emojis by keywords. Supported only if the file database is enabled

        :param text: Text to search for
        :type text: :class:`String`
        :param exact_match: Pass true if only emojis, which exactly match the text, needs to be returned
        :type exact_match: :class:`Bool`
        :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
        :type input_language_codes: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Emojis`
        """

        return await self.client.request(
            SearchEmojis(
                text=text,
                exact_match=exact_match,
                input_language_codes=input_language_codes,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_file_downloads(
        self,
        offset: String,
        limit: Int32,
        query: String = "",
        only_active: Bool = False,
        only_completed: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundFileDownloads:
        """
        Searches for files in the file download list or recently downloaded files from the list

        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of files to be returned
        :type limit: :class:`Int32`
        :param query: Query to search for; may be empty to return all downloaded files
        :type query: :class:`String`
        :param only_active: Pass true to search only for active downloads, including paused
        :type only_active: :class:`Bool`
        :param only_completed: Pass true to search only for completed downloads
        :type only_completed: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundFileDownloads`
        """

        return await self.client.request(
            SearchFileDownloads(
                offset=offset,
                limit=limit,
                query=query,
                only_active=only_active,
                only_completed=only_completed,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_hashtags(
        self, prefix: String, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Hashtags:
        """
        Searches for recently used hashtags by their prefix

        :param prefix: Hashtag prefix to search for
        :type prefix: :class:`String`
        :param limit: The maximum number of hashtags to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Hashtags`
        """

        return await self.client.request(
            SearchHashtags(
                prefix=prefix,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_installed_sticker_sets(
        self,
        sticker_type: StickerType,
        query: String,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> StickerSets:
        """
        Searches for installed sticker sets by looking for specified query in their title and name

        :param sticker_type: Type of the sticker sets to search for
        :type sticker_type: :class:`StickerType`
        :param query: Query to search for
        :type query: :class:`String`
        :param limit: The maximum number of sticker sets to return
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """

        return await self.client.request(
            SearchInstalledStickerSets(
                sticker_type=sticker_type,
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_messages(
        self,
        query: String,
        offset: String,
        limit: Int32,
        min_date: Int32 = 0,
        max_date: Int32 = 0,
        chat_list: typing.Optional[ChatList] = None,
        filter_: typing.Optional[SearchMessagesFilter] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundMessages:
        """
        Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        :param query: Query to search for
        :type query: :class:`String`
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param min_date: If not 0, the minimum date of the messages to return
        :type min_date: :class:`Int32`
        :param max_date: If not 0, the maximum date of the messages to return
        :type max_date: :class:`Int32`
        :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported, defaults to None
        :type chat_list: :class:`ChatList`, optional
        :param filter_: Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function, defaults to None
        :type filter_: :class:`SearchMessagesFilter`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """

        return await self.client.request(
            SearchMessages(
                query=query,
                offset=offset,
                limit=limit,
                min_date=min_date,
                max_date=max_date,
                chat_list=chat_list,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_outgoing_document_messages(
        self, query: String, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> FoundMessages:
        """
        Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order

        :param query: Query to search for in document file name and message caption
        :type query: :class:`String`
        :param limit: The maximum number of messages to be returned; up to 100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """

        return await self.client.request(
            SearchOutgoingDocumentMessages(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_public_chat(
        self, username: String, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise, an error is returned

        :param username: Username to be resolved
        :type username: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            SearchPublicChat(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_public_chats(self, query: String, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results. Excludes private chats with contacts and chats from the chat list from the results

        :param query: Query to search for
        :type query: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            SearchPublicChats(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_recently_found_chats(
        self, query: String, limit: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Chats:
        """
        Searches for the specified query in the title and username of up to 50 recently found chats; this is an offline request

        :param query: Query to search for
        :type query: :class:`String`
        :param limit: The maximum number of chats to be returned
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chats`
        """

        return await self.client.request(
            SearchRecentlyFoundChats(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_secret_messages(
        self,
        chat_id: Int53,
        query: String,
        offset: String,
        limit: Int32,
        filter_: typing.Optional[SearchMessagesFilter] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundMessages:
        """
        Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib

        :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
        :type chat_id: :class:`Int53`
        :param query: Query to search for. If empty, searchChatMessages must be used instead
        :type query: :class:`String`
        :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
        :type offset: :class:`String`
        :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: :class:`Int32`
        :param filter_: Additional filter for messages to search; pass null to search for all messages, defaults to None
        :type filter_: :class:`SearchMessagesFilter`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundMessages`
        """

        return await self.client.request(
            SearchSecretMessages(
                chat_id=chat_id,
                query=query,
                offset=offset,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_sticker_set(
        self, name: String, *, request_id: str = None, request_timeout: int = None
    ) -> StickerSet:
        """
        Searches for a sticker set by its name

        :param name: Name of the sticker set
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSet`
        """

        return await self.client.request(
            SearchStickerSet(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_sticker_sets(
        self, query: String, *, request_id: str = None, request_timeout: int = None
    ) -> StickerSets:
        """
        Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results

        :param query: Query to search for
        :type query: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.StickerSets`
        """

        return await self.client.request(
            SearchStickerSets(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_stickers(
        self,
        sticker_type: StickerType,
        emojis: String,
        limit: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Stickers:
        """
        Searches for stickers from public sticker sets that correspond to any of the given emoji

        :param sticker_type: Type of the stickers to return
        :type sticker_type: :class:`StickerType`
        :param emojis: Space-separated list of emoji to search for; must be non-empty
        :type emojis: :class:`String`
        :param limit: The maximum number of stickers to be returned; 0-100
        :type limit: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Stickers`
        """

        return await self.client.request(
            SearchStickers(
                sticker_type=sticker_type,
                emojis=emojis,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_strings_by_prefix(
        self,
        strings: Vector[String],
        query: String,
        limit: Int32,
        return_none_for_empty_query: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FoundPositions:
        """
        Searches specified query by word prefixes in the provided strings. Returns 0-based positions of strings that matched. Can be called synchronously

        :param strings: The strings to search in for the query
        :type strings: :class:`Vector[String]`
        :param query: Query to search for
        :type query: :class:`String`
        :param limit: The maximum number of objects to return
        :type limit: :class:`Int32`
        :param return_none_for_empty_query: Pass true to receive no results for an empty query
        :type return_none_for_empty_query: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundPositions`
        """

        return await self.client.request(
            SearchStringsByPrefix(
                strings=strings,
                query=query,
                limit=limit,
                return_none_for_empty_query=return_none_for_empty_query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_user_by_phone_number(
        self, phone_number: String, *, request_id: str = None, request_timeout: int = None
    ) -> User:
        """
        Searches a user by their phone number. Returns a 404 error if the user can't be found

        :param phone_number: Phone number to search for
        :type phone_number: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.User`
        """

        return await self.client.request(
            SearchUserByPhoneNumber(
                phone_number=phone_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_user_by_token(self, token: String, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Searches a user by a token from the user's link

        :param token: Token to search for
        :type token: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.User`
        """

        return await self.client.request(
            SearchUserByToken(
                token=token,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def search_web_app(
        self, bot_user_id: Int53, web_app_short_name: String, *, request_id: str = None, request_timeout: int = None
    ) -> FoundWebApp:
        """
        Returns information about a Web App by its short name. Returns a 404 error if the Web App is not found

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param web_app_short_name: Short name of the Web App
        :type web_app_short_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FoundWebApp`
        """

        return await self.client.request(
            SearchWebApp(
                bot_user_id=bot_user_id,
                web_app_short_name=web_app_short_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_authentication_firebase_sms(
        self, token: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sends Firebase Authentication SMS to the phone number of the user. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

        :param token: SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
        :type token: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendAuthenticationFirebaseSms(
                token=token,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_bot_start_message(
        self,
        bot_user_id: Int53,
        chat_id: Int53,
        parameter: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message

        :param bot_user_id: Identifier of the bot
        :type bot_user_id: :class:`Int53`
        :param chat_id: Identifier of the target chat
        :type chat_id: :class:`Int53`
        :param parameter: A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
        :type parameter: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            SendBotStartMessage(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                parameter=parameter,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_debug_information(
        self, call_id: Int32, debug_information: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sends debug information for a call to Telegram servers

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param debug_information: Debug information in application-specific format
        :type debug_information: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendCallDebugInformation(
                call_id=call_id,
                debug_information=debug_information,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_log(
        self, call_id: Int32, log_file: InputFile, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sends log file for a call to Telegram servers

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param log_file: Call log file. Only inputFileLocal and inputFileGenerated are supported
        :type log_file: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendCallLog(
                call_id=call_id,
                log_file=log_file,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_rating(
        self,
        call_id: Int32,
        rating: Int32,
        comment: String,
        problems: Vector[CallProblem],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sends a call rating

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param rating: Call rating; 1-5
        :type rating: :class:`Int32`
        :param comment: An optional user comment if the rating is less than 5
        :type comment: :class:`String`
        :param problems: List of the exact types of problems with the call, specified by the user
        :type problems: :class:`Vector[CallProblem]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendCallRating(
                call_id=call_id,
                rating=rating,
                comment=comment,
                problems=problems,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_call_signaling_data(
        self, call_id: Int32, data: Bytes, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sends call signaling data

        :param call_id: Call identifier
        :type call_id: :class:`Int32`
        :param data: The data
        :type data: :class:`Bytes`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendCallSignalingData(
                call_id=call_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_chat_action(
        self,
        chat_id: Int53,
        message_thread_id: Int53 = 0,
        action: typing.Optional[ChatAction] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sends a notification about user activity in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: If not 0, a message thread identifier in which the action was performed
        :type message_thread_id: :class:`Int53`
        :param action: The action description; pass null to cancel the currently active action, defaults to None
        :type action: :class:`ChatAction`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendChatAction(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_custom_request(
        self, method: String, parameters: String, *, request_id: str = None, request_timeout: int = None
    ) -> CustomRequestResult:
        """
        Sends a custom request; for bots only

        :param method: The method name
        :type method: :class:`String`
        :param parameters: JSON-serialized method parameters
        :type parameters: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CustomRequestResult`
        """

        return await self.client.request(
            SendCustomRequest(
                method=method,
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_email_address_verification_code(
        self, email_address: String, *, request_id: str = None, request_timeout: int = None
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Sends a code to verify an email address to be added to a user's Telegram Passport

        :param email_address: Email address
        :type email_address: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.client.request(
            SendEmailAddressVerificationCode(
                email_address=email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_inline_query_result_message(
        self,
        chat_id: Int53,
        query_id: Int64,
        result_id: String,
        message_thread_id: Int53 = 0,
        hide_via_bot: Bool = False,
        reply_to: typing.Optional[MessageReplyTo] = None,
        options: typing.Optional[MessageSendOptions] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message

        :param chat_id: Target chat
        :type chat_id: :class:`Int53`
        :param query_id: Identifier of the inline query
        :type query_id: :class:`Int64`
        :param result_id: Identifier of the inline query result
        :type result_id: :class:`String`
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
        :type message_thread_id: :class:`Int53`
        :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption("animation_search_bot_username"), getOption("photo_search_bot_username"), and getOption("venue_search_bot_username")
        :type hide_via_bot: :class:`Bool`
        :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
        :type reply_to: :class:`MessageReplyTo`, optional
        :param options: Options to be used to send the message; pass null to use default options, defaults to None
        :type options: :class:`MessageSendOptions`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            SendInlineQueryResultMessage(
                chat_id=chat_id,
                query_id=query_id,
                result_id=result_id,
                message_thread_id=message_thread_id,
                hide_via_bot=hide_via_bot,
                reply_to=reply_to,
                options=options,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_message(
        self,
        chat_id: Int53,
        input_message_content: InputMessageContent,
        message_thread_id: Int53 = 0,
        reply_to: typing.Optional[MessageReplyTo] = None,
        options: typing.Optional[MessageSendOptions] = None,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Sends a message. Returns the sent message

        :param chat_id: Target chat
        :type chat_id: :class:`Int53`
        :param input_message_content: The content of the message to be sent
        :type input_message_content: :class:`InputMessageContent`
        :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
        :type message_thread_id: :class:`Int53`
        :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
        :type reply_to: :class:`MessageReplyTo`, optional
        :param options: Options to be used to send the message; pass null to use default options, defaults to None
        :type options: :class:`MessageSendOptions`, optional
        :param reply_markup: Markup for replying to the message; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            SendMessage(
                chat_id=chat_id,
                input_message_content=input_message_content,
                message_thread_id=message_thread_id,
                reply_to=reply_to,
                options=options,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_message_album(
        self,
        chat_id: Int53,
        input_message_contents: Vector[InputMessageContent],
        message_thread_id: Int53 = 0,
        only_preview: Bool = False,
        reply_to: typing.Optional[MessageReplyTo] = None,
        options: typing.Optional[MessageSendOptions] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Messages:
        """
        Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

        :param chat_id: Target chat
        :type chat_id: :class:`Int53`
        :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album
        :type input_message_contents: :class:`Vector[InputMessageContent]`
        :param message_thread_id: If not 0, a message thread identifier in which the messages will be sent
        :type message_thread_id: :class:`Int53`
        :param only_preview: Pass true to get fake messages instead of actually sending them
        :type only_preview: :class:`Bool`
        :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
        :type reply_to: :class:`MessageReplyTo`, optional
        :param options: Options to be used to send the messages; pass null to use default options, defaults to None
        :type options: :class:`MessageSendOptions`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Messages`
        """

        return await self.client.request(
            SendMessageAlbum(
                chat_id=chat_id,
                input_message_contents=input_message_contents,
                message_thread_id=message_thread_id,
                only_preview=only_preview,
                reply_to=reply_to,
                options=options,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_passport_authorization_form(
        self,
        authorization_form_id: Int32,
        types: Vector[PassportElementType],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused

        :param authorization_form_id: Authorization form identifier
        :type authorization_form_id: :class:`Int32`
        :param types: Types of Telegram Passport elements chosen by user to complete the authorization form
        :type types: :class:`Vector[PassportElementType]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendPassportAuthorizationForm(
                authorization_form_id=authorization_form_id,
                types=types,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_payment_form(
        self,
        input_invoice: InputInvoice,
        payment_form_id: Int64,
        order_info_id: String,
        shipping_option_id: String,
        credentials: InputCredentials,
        tip_amount: Int53,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PaymentResult:
        """
        Sends a filled-out payment form to the bot for final verification

        :param input_invoice: The invoice
        :type input_invoice: :class:`InputInvoice`
        :param payment_form_id: Payment form identifier returned by getPaymentForm
        :type payment_form_id: :class:`Int64`
        :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
        :type order_info_id: :class:`String`
        :param shipping_option_id: Identifier of a chosen shipping option, if applicable
        :type shipping_option_id: :class:`String`
        :param credentials: The credentials chosen by user for payment
        :type credentials: :class:`InputCredentials`
        :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
        :type tip_amount: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PaymentResult`
        """

        return await self.client.request(
            SendPaymentForm(
                input_invoice=input_invoice,
                payment_form_id=payment_form_id,
                order_info_id=order_info_id,
                shipping_option_id=shipping_option_id,
                credentials=credentials,
                tip_amount=tip_amount,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_phone_number_confirmation_code(
        self,
        hash_: String,
        phone_number: String,
        settings: typing.Optional[PhoneNumberAuthenticationSettings] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation

        :param hash_: Hash value from the link
        :type hash_: :class:`String`
        :param phone_number: Phone number value from the link
        :type phone_number: :class:`String`
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
        :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """

        return await self.client.request(
            SendPhoneNumberConfirmationCode(
                hash=hash_,
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_phone_number_verification_code(
        self,
        phone_number: String,
        settings: typing.Optional[PhoneNumberAuthenticationSettings] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> AuthenticationCodeInfo:
        """
        Sends a code to verify a phone number to be added to a user's Telegram Passport

        :param phone_number: The phone number of the user, in international format
        :type phone_number: :class:`String`
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
        :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.AuthenticationCodeInfo`
        """

        return await self.client.request(
            SendPhoneNumberVerificationCode(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_story(
        self,
        content: InputStoryContent,
        privacy_settings: StoryPrivacySettings,
        active_period: Int32,
        is_pinned: Bool = False,
        protect_content: Bool = False,
        areas: typing.Optional[InputStoryAreas] = None,
        caption: typing.Optional[FormattedText] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Story:
        """
        Sends a new story. Returns a temporary story

        :param content: Content of the story
        :type content: :class:`InputStoryContent`
        :param privacy_settings: The privacy settings for the story
        :type privacy_settings: :class:`StoryPrivacySettings`
        :param active_period: Period after which the story is moved to archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise
        :type active_period: :class:`Int32`
        :param is_pinned: Pass true to keep the story accessible after expiration
        :type is_pinned: :class:`Bool`
        :param protect_content: Pass true if the content of the story must be protected from forwarding and screenshotting
        :type protect_content: :class:`Bool`
        :param areas: Clickable rectangle areas to be shown on the story media; pass null if none, defaults to None
        :type areas: :class:`InputStoryAreas`, optional
        :param caption: Story caption; pass null to use an empty caption; 0-getOption("story_caption_length_max") characters, defaults to None
        :type caption: :class:`FormattedText`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Story`
        """

        return await self.client.request(
            SendStory(
                content=content,
                privacy_settings=privacy_settings,
                active_period=active_period,
                is_pinned=is_pinned,
                protect_content=protect_content,
                areas=areas,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_web_app_custom_request(
        self,
        bot_user_id: Int53,
        method: String,
        parameters: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> CustomRequestResult:
        """
        Sends a custom request from a Web App

        :param bot_user_id: Identifier of the bot
        :type bot_user_id: :class:`Int53`
        :param method: The method name
        :type method: :class:`String`
        :param parameters: JSON-serialized method parameters
        :type parameters: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.CustomRequestResult`
        """

        return await self.client.request(
            SendWebAppCustomRequest(
                bot_user_id=bot_user_id,
                method=method,
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def send_web_app_data(
        self,
        bot_user_id: Int53,
        button_text: String,
        data: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sends data received from a keyboardButtonTypeWebApp Web App to a bot

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
        :type button_text: :class:`String`
        :param data: The data
        :type data: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SendWebAppData(
                bot_user_id=bot_user_id,
                button_text=button_text,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_account_ttl(self, ttl: AccountTtl, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Changes the period of inactivity after which the account of the current user will automatically be deleted

        :param ttl: New account TTL
        :type ttl: :class:`AccountTtl`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAccountTtl(
                ttl=ttl,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_alarm(self, seconds: Double, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Succeeds after a specified amount of time has passed. Can be called before initialization

        :param seconds: Number of seconds before the function returns
        :type seconds: :class:`Double`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAlarm(
                seconds=seconds,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_archive_chat_list_settings(
        self, settings: ArchiveChatListSettings, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes settings for automatic moving of chats to and from the Archive chat lists

        :param settings: New settings
        :type settings: :class:`ArchiveChatListSettings`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetArchiveChatListSettings(
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_authentication_email_address(
        self, email_address: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress

        :param email_address: The email address of the user
        :type email_address: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAuthenticationEmailAddress(
                email_address=email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_authentication_phone_number(
        self,
        phone_number: String,
        settings: typing.Optional[PhoneNumberAuthenticationSettings] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        :param phone_number: The phone number of the user, in international format
        :type phone_number: :class:`String`
        :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
        :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAuthenticationPhoneNumber(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_auto_download_settings(
        self, settings: AutoDownloadSettings, type_: NetworkType, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets auto-download settings

        :param settings: New user auto-download settings
        :type settings: :class:`AutoDownloadSettings`
        :param type_: Type of the network for which the new settings are relevant
        :type type_: :class:`NetworkType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAutoDownloadSettings(
                settings=settings,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_autosave_settings(
        self,
        scope: AutosaveSettingsScope,
        settings: typing.Optional[ScopeAutosaveSettings] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets autosave settings for the given scope. The method is guaranteed to work only after at least one call to getAutosaveSettings

        :param scope: Autosave settings scope
        :type scope: :class:`AutosaveSettingsScope`
        :param settings: New autosave settings for the scope; pass null to set autosave settings to default, defaults to None
        :type settings: :class:`ScopeAutosaveSettings`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetAutosaveSettings(
                scope=scope,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_background(
        self,
        for_dark_theme: Bool = False,
        background: typing.Optional[InputBackground] = None,
        type_: typing.Optional[BackgroundType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Background:
        """
        Changes the background selected by the user; adds background to the list of installed backgrounds

        :param for_dark_theme: Pass true if the background is changed for a dark theme
        :type for_dark_theme: :class:`Bool`
        :param background: The input background to use; pass null to create a new filled background or to remove the current background, defaults to None
        :type background: :class:`InputBackground`, optional
        :param type_: Background type; pass null to use the default type of the remote background or to remove the current background, defaults to None
        :type type_: :class:`BackgroundType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Background`
        """

        return await self.client.request(
            SetBackground(
                for_dark_theme=for_dark_theme,
                background=background,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bio(self, bio: String, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Changes the bio of the current user

        :param bio: The new value of the user bio; 0-getOption("bio_length_max") characters without line feeds
        :type bio: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBio(
                bio=bio,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_info_description(
        self,
        bot_user_id: Int53,
        language_code: String,
        description: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the text shown in the chat with a bot if the chat is empty. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code. If empty, the description will be shown to all users for whose languages there is no dedicated description
        :type language_code: :class:`String`
        :param description: New bot's description on the specified language
        :type description: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBotInfoDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
                description=description,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_info_short_description(
        self,
        bot_user_id: Int53,
        language_code: String,
        short_description: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the text shown on a bot's profile page and sent together with the link when users share the bot. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code. If empty, the short description will be shown to all users for whose languages there is no dedicated description
        :type language_code: :class:`String`
        :param short_description: New bot's short description on the specified language
        :type short_description: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBotInfoShortDescription(
                bot_user_id=bot_user_id,
                language_code=language_code,
                short_description=short_description,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_name(
        self,
        bot_user_id: Int53,
        language_code: String,
        name: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the name of a bot. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param language_code: A two-letter ISO 639-1 language code. If empty, the name will be shown to all users for whose languages there is no dedicated name
        :type language_code: :class:`String`
        :param name: New bot's name on the specified language; 0-64 characters; must be non-empty if language code is empty
        :type name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBotName(
                bot_user_id=bot_user_id,
                language_code=language_code,
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_profile_photo(
        self,
        bot_user_id: Int53,
        photo: typing.Optional[InputChatPhoto] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes a profile photo for a bot

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param photo: Profile photo to set; pass null to delete the chat photo, defaults to None
        :type photo: :class:`InputChatPhoto`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBotProfilePhoto(
                bot_user_id=bot_user_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_bot_updates_status(
        self, pending_update_count: Int32, error_message: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only

        :param pending_update_count: The number of pending updates
        :type pending_update_count: :class:`Int32`
        :param error_message: The last error message
        :type error_message: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetBotUpdatesStatus(
                pending_update_count=pending_update_count,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_active_stories_list(
        self, chat_id: Int53, story_list: StoryList, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes story list in which stories from the chat are shown

        :param chat_id: Identifier of the chat that posted stories
        :type chat_id: :class:`Int53`
        :param story_list: New list for active stories posted by the chat
        :type story_list: :class:`StoryList`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatActiveStoriesList(
                chat_id=chat_id,
                story_list=story_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_available_reactions(
        self,
        chat_id: Int53,
        available_reactions: ChatAvailableReactions,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param available_reactions: Reactions available in the chat. All emoji reactions must be active
        :type available_reactions: :class:`ChatAvailableReactions`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatAvailableReactions(
                chat_id=chat_id,
                available_reactions=available_reactions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_background(
        self,
        chat_id: Int53,
        dark_theme_dimming: Int32,
        background: typing.Optional[InputBackground] = None,
        type_: typing.Optional[BackgroundType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the background in a specific chat. Supported only in private and secret chats with non-deleted users

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
        :type dark_theme_dimming: :class:`Int32`
        :param background: The input background to use; pass null to create a new filled background or to remove the current background, defaults to None
        :type background: :class:`InputBackground`, optional
        :param type_: Background type; pass null to remove the current background, defaults to None
        :type type_: :class:`BackgroundType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatBackground(
                chat_id=chat_id,
                dark_theme_dimming=dark_theme_dimming,
                background=background,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_client_data(
        self, chat_id: Int53, client_data: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes application-specific data associated with a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param client_data: New value of client_data
        :type client_data: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatClientData(
                chat_id=chat_id,
                client_data=client_data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_description(
        self, chat_id: Int53, description: String = "", *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param description: New chat description; 0-255 characters
        :type description: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatDescription(
                chat_id=chat_id,
                description=description,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_discussion_group(
        self, chat_id: Int53, discussion_chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified

        :param chat_id: Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup)
        :type chat_id: :class:`Int53`
        :param discussion_chat_id: Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups. Basic group chats must be first upgraded to supergroup chats. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that
        :type discussion_chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatDiscussionGroup(
                chat_id=chat_id,
                discussion_chat_id=discussion_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_draft_message(
        self,
        chat_id: Int53,
        message_thread_id: Int53 = 0,
        draft_message: typing.Optional[DraftMessage] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the draft message in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: If not 0, a message thread identifier in which the draft was changed
        :type message_thread_id: :class:`Int53`
        :param draft_message: New draft message; pass null to remove the draft, defaults to None
        :type draft_message: :class:`DraftMessage`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatDraftMessage(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                draft_message=draft_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_location(
        self, chat_id: Int53, location: ChatLocation, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param location: New location for the chat; must be valid and not null
        :type location: :class:`ChatLocation`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatLocation(
                chat_id=chat_id,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_member_status(
        self,
        chat_id: Int53,
        member_id: MessageSender,
        status: ChatMemberStatus,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead. Use addChatMember or banChatMember if some additional parameters needs to be passed

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param member_id: Member identifier. Chats can be only banned and unbanned in supergroups and channels
        :type member_id: :class:`MessageSender`
        :param status: The new status of the member in the chat
        :type status: :class:`ChatMemberStatus`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatMemberStatus(
                chat_id=chat_id,
                member_id=member_id,
                status=status,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_message_auto_delete_time(
        self,
        chat_id: Int53,
        message_auto_delete_time: Int32 = 0,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the message auto-delete or self-destruct (for secret chats) time in a chat. Requires change_info administrator right in basic groups, supergroups and channels Message auto-delete time can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_auto_delete_time: New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :type message_auto_delete_time: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatMessageAutoDeleteTime(
                chat_id=chat_id,
                message_auto_delete_time=message_auto_delete_time,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_message_sender(
        self, chat_id: Int53, message_sender_id: MessageSender, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Selects a message sender to send messages in a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_sender_id: New message sender for the chat
        :type message_sender_id: :class:`MessageSender`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatMessageSender(
                chat_id=chat_id,
                message_sender_id=message_sender_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_notification_settings(
        self,
        chat_id: Int53,
        notification_settings: ChatNotificationSettings,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param notification_settings: New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever
        :type notification_settings: :class:`ChatNotificationSettings`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatNotificationSettings(
                chat_id=chat_id,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_permissions(
        self, chat_id: Int53, permissions: ChatPermissions, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param permissions: New non-administrator members permissions in the chat
        :type permissions: :class:`ChatPermissions`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatPermissions(
                chat_id=chat_id,
                permissions=permissions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_photo(
        self,
        chat_id: Int53,
        photo: typing.Optional[InputChatPhoto] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param photo: New chat photo; pass null to delete the chat photo, defaults to None
        :type photo: :class:`InputChatPhoto`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatPhoto(
                chat_id=chat_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_slow_mode_delay(
        self, chat_id: Int53, slow_mode_delay: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param slow_mode_delay: New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600
        :type slow_mode_delay: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatSlowModeDelay(
                chat_id=chat_id,
                slow_mode_delay=slow_mode_delay,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_theme(
        self, chat_id: Int53, theme_name: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the chat theme. Supported only in private and secret chats

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param theme_name: Name of the new chat theme; pass an empty string to return the default theme
        :type theme_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatTheme(
                chat_id=chat_id,
                theme_name=theme_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_chat_title(
        self, chat_id: Int53, title: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param title: New title of the chat; 1-128 characters
        :type title: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetChatTitle(
                chat_id=chat_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_close_friends(
        self, user_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the list of close friends of the current user

        :param user_ids: User identifiers of close friends; the users must be contacts of the current user
        :type user_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetCloseFriends(
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_commands(
        self,
        language_code: String,
        commands: Vector[BotCommand],
        scope: typing.Optional[BotCommandScope] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the list of commands supported by the bot for the given user scope and language; for bots only

        :param language_code: A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands
        :type language_code: :class:`String`
        :param commands: List of the bot's commands
        :type commands: :class:`Vector[BotCommand]`
        :param scope: The scope to which the commands are relevant; pass null to change commands in the default bot command scope, defaults to None
        :type scope: :class:`BotCommandScope`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetCommands(
                language_code=language_code,
                commands=commands,
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_custom_emoji_sticker_set_thumbnail(
        self, name: String, custom_emoji_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets a custom emoji sticker set thumbnail; for bots only

        :param name: Sticker set name
        :type name: :class:`String`
        :param custom_emoji_id: Identifier of the custom emoji from the sticker set, which will be set as sticker set thumbnail; pass 0 to remove the sticker set thumbnail
        :type custom_emoji_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetCustomEmojiStickerSetThumbnail(
                name=name,
                custom_emoji_id=custom_emoji_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack(
        self,
        info: LanguagePackInfo,
        strings: Vector[LanguagePackString],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds or changes a custom local language pack to the current localization target

        :param info: Information about the language pack. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
        :type info: :class:`LanguagePackInfo`
        :param strings: Strings of the new language pack
        :type strings: :class:`Vector[LanguagePackString]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetCustomLanguagePack(
                info=info,
                strings=strings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_custom_language_pack_string(
        self,
        language_pack_id: String,
        new_string: LanguagePackString,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds, edits or deletes a string in a custom local language pack. Can be called before authorization

        :param language_pack_id: Identifier of a previously added custom local language pack in the current localization target
        :type language_pack_id: :class:`String`
        :param new_string: New language pack string
        :type new_string: :class:`LanguagePackString`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetCustomLanguagePackString(
                language_pack_id=language_pack_id,
                new_string=new_string,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_database_encryption_key(
        self, new_encryption_key: Bytes, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain

        :param new_encryption_key: New encryption key
        :type new_encryption_key: :class:`Bytes`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetDatabaseEncryptionKey(
                new_encryption_key=new_encryption_key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_channel_administrator_rights(
        self,
        default_channel_administrator_rights: typing.Optional[ChatAdministratorRights] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to channel chats; for bots only

        :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; pass null to remove default rights, defaults to None
        :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetDefaultChannelAdministratorRights(
                default_channel_administrator_rights=default_channel_administrator_rights,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_group_administrator_rights(
        self,
        default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

        :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights, defaults to None
        :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetDefaultGroupAdministratorRights(
                default_group_administrator_rights=default_group_administrator_rights,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_message_auto_delete_time(
        self,
        message_auto_delete_time: MessageAutoDeleteTime = 0,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the default message auto-delete time for new chats

        :param message_auto_delete_time: New default message auto-delete time; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
        :type message_auto_delete_time: :class:`MessageAutoDeleteTime`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetDefaultMessageAutoDeleteTime(
                message_auto_delete_time=message_auto_delete_time,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_default_reaction_type(
        self, reaction_type: ReactionType, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes type of default reaction for the current user

        :param reaction_type: New type of the default reaction
        :type reaction_type: :class:`ReactionType`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetDefaultReactionType(
                reaction_type=reaction_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_emoji_status(
        self, emoji_status: typing.Optional[EmojiStatus] = None, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the emoji status of the current user; for Telegram Premium users only

        :param emoji_status: New emoji status; pass null to switch to the default badge, defaults to None
        :type emoji_status: :class:`EmojiStatus`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetEmojiStatus(
                emoji_status=emoji_status,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_file_generation_progress(
        self,
        generation_id: Int64,
        local_prefix_size: Int53,
        expected_size: typing.Optional[Int53] = 0,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib on a file generation progress

        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`Int64`
        :param local_prefix_size: The number of bytes already generated
        :type local_prefix_size: :class:`Int53`
        :param expected_size: Expected size of the generated file, in bytes; 0 if unknown, defaults to None
        :type expected_size: :class:`Int53`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetFileGenerationProgress(
                generation_id=generation_id,
                local_prefix_size=local_prefix_size,
                expected_size=expected_size,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_forum_topic_notification_settings(
        self,
        chat_id: Int53,
        message_thread_id: Int53,
        notification_settings: ChatNotificationSettings,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the notification settings of a forum topic

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param notification_settings: New notification settings for the forum topic. If the topic is muted for more than 366 days, it is considered to be muted forever
        :type notification_settings: :class:`ChatNotificationSettings`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetForumTopicNotificationSettings(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_game_score(
        self,
        chat_id: Int53,
        message_id: Int53,
        user_id: Int53,
        score: Int32,
        edit_message: Bool = False,
        force: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Message:
        """
        Updates the game score of the specified user in the game; for bots only

        :param chat_id: The chat to which the message with the game belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param score: The new score
        :type score: :class:`Int32`
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :type edit_message: :class:`Bool`
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :type force: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Message`
        """

        return await self.client.request(
            SetGameScore(
                chat_id=chat_id,
                message_id=message_id,
                user_id=user_id,
                score=score,
                edit_message=edit_message,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_is_speaking(
        self,
        group_call_id: Int32,
        audio_source: Int32,
        is_speaking: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that speaking state of a participant of an active group has changed

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param audio_source: Group call participant's synchronization audio source identifier, or 0 for the current user
        :type audio_source: :class:`Int32`
        :param is_speaking: Pass true if the user is speaking
        :type is_speaking: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetGroupCallParticipantIsSpeaking(
                group_call_id=group_call_id,
                audio_source=audio_source,
                is_speaking=is_speaking,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_participant_volume_level(
        self,
        group_call_id: Int32,
        participant_id: MessageSender,
        volume_level: Int32,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        :param volume_level: New participant's volume level; 1-20000 in hundreds of percents
        :type volume_level: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetGroupCallParticipantVolumeLevel(
                group_call_id=group_call_id,
                participant_id=participant_id,
                volume_level=volume_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_group_call_title(
        self, group_call_id: Int32, title: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets group call title. Requires groupCall.can_be_managed group call flag

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param title: New group call title; 1-64 characters
        :type title: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetGroupCallTitle(
                group_call_id=group_call_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_inactive_session_ttl(
        self, inactive_session_ttl_days: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the period of inactivity after which sessions will automatically be terminated

        :param inactive_session_ttl_days: New number of days of inactivity before sessions will be automatically terminated; 1-366 days
        :type inactive_session_ttl_days: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetInactiveSessionTtl(
                inactive_session_ttl_days=inactive_session_ttl_days,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_inline_game_score(
        self,
        inline_message_id: String,
        user_id: Int53,
        score: Int32,
        edit_message: Bool = False,
        force: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Updates the game score of the specified user in a game; for bots only

        :param inline_message_id: Inline message identifier
        :type inline_message_id: :class:`String`
        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param score: The new score
        :type score: :class:`Int32`
        :param edit_message: Pass true to edit the game message to include the current scoreboard
        :type edit_message: :class:`Bool`
        :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        :type force: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetInlineGameScore(
                inline_message_id=inline_message_id,
                user_id=user_id,
                score=score,
                edit_message=edit_message,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_location(self, location: Location, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Changes the location of the current user. Needs to be called if getOption("is_location_visible") is true and location changes for more than 1 kilometer

        :param location: The new location of the user
        :type location: :class:`Location`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetLocation(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_stream(self, log_stream: LogStream, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Sets new log stream for internal logging of TDLib. Can be called synchronously

        :param log_stream: New log stream
        :type log_stream: :class:`LogStream`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetLogStream(
                log_stream=log_stream,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_tag_verbosity_level(
        self, tag: String, new_verbosity_level: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously

        :param tag: Logging tag to change verbosity level
        :type tag: :class:`String`
        :param new_verbosity_level: New verbosity level; 1-1024
        :type new_verbosity_level: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetLogTagVerbosityLevel(
                tag=tag,
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_log_verbosity_level(
        self, new_verbosity_level: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets the verbosity level of the internal logging of TDLib. Can be called synchronously

        :param new_verbosity_level: New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging
        :type new_verbosity_level: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetLogVerbosityLevel(
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_login_email_address(
        self, new_login_email_address: String, *, request_id: str = None, request_timeout: int = None
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Changes the login email address of the user. The email address can be changed only if the current user already has login email and passwordState.login_email_address_pattern is non-empty. The change will not be applied until the new login email address is confirmed with checkLoginEmailAddressCode. To use Apple ID/Google ID instead of a email address, call checkLoginEmailAddressCode directly

        :param new_login_email_address: New login email address
        :type new_login_email_address: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.client.request(
            SetLoginEmailAddress(
                new_login_email_address=new_login_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_menu_button(
        self, user_id: Int53, menu_button: BotMenuButton, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets menu button for the given user or for all users; for bots only

        :param user_id: Identifier of the user or 0 to set menu button for all users
        :type user_id: :class:`Int53`
        :param menu_button: New menu button
        :type menu_button: :class:`BotMenuButton`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetMenuButton(
                user_id=user_id,
                menu_button=menu_button,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_message_sender_block_list(
        self,
        sender_id: MessageSender,
        block_list: typing.Optional[BlockList] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the block list of a message sender. Currently, only users and supergroup chats can be blocked

        :param sender_id: Identifier of a message sender to block/unblock
        :type sender_id: :class:`MessageSender`
        :param block_list: New block list for the message sender; pass null to unblock the message sender, defaults to None
        :type block_list: :class:`BlockList`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetMessageSenderBlockList(
                sender_id=sender_id,
                block_list=block_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_name(
        self, first_name: String, last_name: String = "", *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the first and last name of the current user

        :param first_name: The new value of the first name for the current user; 1-64 characters
        :type first_name: :class:`String`
        :param last_name: The new value of the optional last name for the current user; 0-64 characters
        :type last_name: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetName(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_network_type(
        self, type_: typing.Optional[NetworkType] = None, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics

        :param type_: The new network type; pass null to set network type to networkTypeOther, defaults to None
        :type type_: :class:`NetworkType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetNetworkType(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_option(
        self,
        name: String,
        value: typing.Optional[OptionValue] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization

        :param name: The name of the option
        :type name: :class:`String`
        :param value: The new value of the option; pass null to reset option value to a default value, defaults to None
        :type value: :class:`OptionValue`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetOption(
                name=name,
                value=value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_passport_element(
        self, element: InputPassportElement, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> PassportElement:
        """
        Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first

        :param element: Input Telegram Passport element
        :type element: :class:`InputPassportElement`
        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PassportElement`
        """

        return await self.client.request(
            SetPassportElement(
                element=element,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_passport_element_errors(
        self,
        user_id: Int53,
        errors: Vector[InputPassportElementError],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param errors: The errors
        :type errors: :class:`Vector[InputPassportElementError]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetPassportElementErrors(
                user_id=user_id,
                errors=errors,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_password(
        self,
        old_password: String,
        new_password: String = "",
        new_hint: String = "",
        set_recovery_email_address: Bool = False,
        new_recovery_email_address: String = "",
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PasswordState:
        """
        Changes the 2-step verification password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

        :param old_password: Previous 2-step verification password of the user
        :type old_password: :class:`String`
        :param new_password: New 2-step verification password of the user; may be empty to remove the password
        :type new_password: :class:`String`
        :param new_hint: New password hint; may be empty
        :type new_hint: :class:`String`
        :param set_recovery_email_address: Pass true to change also the recovery email address
        :type set_recovery_email_address: :class:`Bool`
        :param new_recovery_email_address: New recovery email address; may be empty
        :type new_recovery_email_address: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """

        return await self.client.request(
            SetPassword(
                old_password=old_password,
                new_password=new_password,
                new_hint=new_hint,
                set_recovery_email_address=set_recovery_email_address,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_pinned_chats(
        self, chat_list: ChatList, chat_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the order of pinned chats

        :param chat_list: Chat list in which to change the order of pinned chats
        :type chat_list: :class:`ChatList`
        :param chat_ids: The new list of pinned chats
        :type chat_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetPinnedChats(
                chat_list=chat_list,
                chat_ids=chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_pinned_forum_topics(
        self, chat_id: Int53, message_thread_ids: Vector[Int53], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the order of pinned forum topics

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_ids: The new list of pinned forum topics
        :type message_thread_ids: :class:`Vector[Int53]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetPinnedForumTopics(
                chat_id=chat_id,
                message_thread_ids=message_thread_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_poll_answer(
        self,
        chat_id: Int53,
        message_id: Int53,
        option_ids: Vector[Int32],
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the user answer to a poll. A poll in quiz mode can be answered only once

        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`Int53`
        :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
        :type option_ids: :class:`Vector[Int32]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetPollAnswer(
                chat_id=chat_id,
                message_id=message_id,
                option_ids=option_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_profile_photo(
        self, photo: InputChatPhoto, is_public: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes a profile photo for the current user

        :param photo: Profile photo to set
        :type photo: :class:`InputChatPhoto`
        :param is_public: Pass true to set a public photo, which will be visible even the main photo is hidden by privacy settings
        :type is_public: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetProfilePhoto(
                photo=photo,
                is_public=is_public,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_recovery_email_address(
        self,
        password: String,
        new_recovery_email_address: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> PasswordState:
        """
        Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation

        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param new_recovery_email_address: New recovery email address
        :type new_recovery_email_address: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.PasswordState`
        """

        return await self.client.request(
            SetRecoveryEmailAddress(
                password=password,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_scope_notification_settings(
        self,
        scope: NotificationSettingsScope,
        notification_settings: ScopeNotificationSettings,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes notification settings for chats of a given type

        :param scope: Types of chats for which to change the notification settings
        :type scope: :class:`NotificationSettingsScope`
        :param notification_settings: The new notification settings for the given scope
        :type notification_settings: :class:`ScopeNotificationSettings`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetScopeNotificationSettings(
                scope=scope,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_emojis(
        self, sticker: InputFile, emojis: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the list of emoji corresponding to a sticker; for bots only. The sticker must belong to a regular or custom emoji sticker set created by the bot

        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        :param emojis: New string with 1-20 emoji corresponding to the sticker
        :type emojis: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerEmojis(
                sticker=sticker,
                emojis=emojis,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_keywords(
        self, sticker: InputFile, keywords: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the list of keywords of a sticker; for bots only. The sticker must belong to a regular or custom emoji sticker set created by the bot

        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        :param keywords: List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker
        :type keywords: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerKeywords(
                sticker=sticker,
                keywords=keywords,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_mask_position(
        self,
        sticker: InputFile,
        mask_position: typing.Optional[MaskPosition] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the mask position of a mask sticker; for bots only. The sticker must belong to a mask sticker set created by the bot

        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        :param mask_position: Position where the mask is placed; pass null to remove mask position, defaults to None
        :type mask_position: :class:`MaskPosition`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerMaskPosition(
                sticker=sticker,
                mask_position=mask_position,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_position_in_set(
        self, sticker: InputFile, position: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

        :param sticker: Sticker
        :type sticker: :class:`InputFile`
        :param position: New position of the sticker in the set, 0-based
        :type position: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerPositionInSet(
                sticker=sticker,
                position=position,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_set_thumbnail(
        self,
        user_id: Int53,
        name: String,
        thumbnail: typing.Optional[InputFile] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets a sticker set thumbnail; for bots only

        :param user_id: Sticker set owner
        :type user_id: :class:`Int53`
        :param name: Sticker set name
        :type name: :class:`String`
        :param thumbnail: Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail. Thumbnail format must match the format of stickers in the set, defaults to None
        :type thumbnail: :class:`InputFile`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerSetThumbnail(
                user_id=user_id,
                name=name,
                thumbnail=thumbnail,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_sticker_set_title(
        self, name: String, title: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Sets a sticker set title; for bots only

        :param name: Sticker set name
        :type name: :class:`String`
        :param title: New sticker set title
        :type title: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStickerSetTitle(
                name=name,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_story_privacy_settings(
        self,
        story_id: Int32,
        privacy_settings: StoryPrivacySettings,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes privacy settings of a previously sent story

        :param story_id: Identifier of the story
        :type story_id: :class:`Int32`
        :param privacy_settings: The new privacy settigs for the story
        :type privacy_settings: :class:`StoryPrivacySettings`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStoryPrivacySettings(
                story_id=story_id,
                privacy_settings=privacy_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_story_reaction(
        self,
        story_sender_chat_id: Int53,
        story_id: Int32,
        update_recent_reactions: Bool = False,
        reaction_type: typing.Optional[ReactionType] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes chosen reaction on a story

        :param story_sender_chat_id: The identifier of the sender of the story
        :type story_sender_chat_id: :class:`Int53`
        :param story_id: The identifier of the story
        :type story_id: :class:`Int32`
        :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
        :type update_recent_reactions: :class:`Bool`
        :param reaction_type: Type of the reaction to set; pass null to remove the reaction. `reactionTypeCustomEmoji` reactions can be used only by Telegram Premium users, defaults to None
        :type reaction_type: :class:`ReactionType`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetStoryReaction(
                story_sender_chat_id=story_sender_chat_id,
                story_id=story_id,
                update_recent_reactions=update_recent_reactions,
                reaction_type=reaction_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_supergroup_sticker_set(
        self, supergroup_id: Int53, sticker_set_id: Int64, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the sticker set of a supergroup; requires can_change_info administrator right

        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param sticker_set_id: New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
        :type sticker_set_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetSupergroupStickerSet(
                supergroup_id=supergroup_id,
                sticker_set_id=sticker_set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_supergroup_username(
        self, supergroup_id: Int53, username: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel

        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`Int53`
        :param username: New value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
        :type username: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetSupergroupUsername(
                supergroup_id=supergroup_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_tdlib_parameters(
        self,
        database_directory: String,
        files_directory: String,
        database_encryption_key: Bytes,
        api_id: Int32,
        api_hash: String,
        system_language_code: String,
        device_model: String,
        system_version: String,
        application_version: String,
        use_test_dc: Bool = False,
        use_file_database: Bool = False,
        use_chat_info_database: Bool = False,
        use_message_database: Bool = False,
        use_secret_chats: Bool = False,
        enable_storage_optimizer: Bool = True,
        ignore_file_names: Bool = True,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters

        :param database_directory: The path to the directory for the persistent database; if empty, the current working directory will be used
        :type database_directory: :class:`String`
        :param files_directory: The path to the directory for storing files; if empty, database_directory will be used
        :type files_directory: :class:`String`
        :param database_encryption_key: Encryption key for the database. If the encryption key is invalid, then an error with code 401 will be returned
        :type database_encryption_key: :class:`Bytes`
        :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
        :type api_id: :class:`Int32`
        :param api_hash: Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
        :type api_hash: :class:`String`
        :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
        :type system_language_code: :class:`String`
        :param device_model: Model of the device the application is being run on; must be non-empty
        :type device_model: :class:`String`
        :param system_version: Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
        :type system_version: :class:`String`
        :param application_version: Application version; must be non-empty
        :type application_version: :class:`String`
        :param use_test_dc: Pass true to use Telegram test environment instead of the production environment
        :type use_test_dc: :class:`Bool`
        :param use_file_database: Pass true to keep information about downloaded and uploaded files between application restarts
        :type use_file_database: :class:`Bool`
        :param use_chat_info_database: Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts. Implies use_file_database
        :type use_chat_info_database: :class:`Bool`
        :param use_message_database: Pass true to keep cache of chats and messages between restarts. Implies use_chat_info_database
        :type use_message_database: :class:`Bool`
        :param use_secret_chats: Pass true to enable support for secret chats
        :type use_secret_chats: :class:`Bool`
        :param enable_storage_optimizer: Pass true to automatically delete old files in background
        :type enable_storage_optimizer: :class:`Bool`
        :param ignore_file_names: Pass true to ignore original file names for downloaded files. Otherwise, downloaded files are saved under names as close as possible to the original name
        :type ignore_file_names: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetTdlibParameters(
                database_directory=database_directory,
                files_directory=files_directory,
                database_encryption_key=database_encryption_key,
                api_id=api_id,
                api_hash=api_hash,
                system_language_code=system_language_code,
                device_model=device_model,
                system_version=system_version,
                application_version=application_version,
                use_test_dc=use_test_dc,
                use_file_database=use_file_database,
                use_chat_info_database=use_chat_info_database,
                use_message_database=use_message_database,
                use_secret_chats=use_secret_chats,
                enable_storage_optimizer=enable_storage_optimizer,
                ignore_file_names=ignore_file_names,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_user_personal_profile_photo(
        self,
        user_id: Int53,
        photo: typing.Optional[InputChatPhoto] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes a personal profile photo of a contact user

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param photo: Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function, defaults to None
        :type photo: :class:`InputChatPhoto`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetUserPersonalProfilePhoto(
                user_id=user_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_user_privacy_setting_rules(
        self,
        setting: UserPrivacySetting,
        rules: UserPrivacySettingRules,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes user privacy settings

        :param setting: The privacy setting
        :type setting: :class:`UserPrivacySetting`
        :param rules: The new privacy rules
        :type rules: :class:`UserPrivacySettingRules`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetUserPrivacySettingRules(
                setting=setting,
                rules=rules,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_user_support_info(
        self, user_id: Int53, message: FormattedText, *, request_id: str = None, request_timeout: int = None
    ) -> UserSupportInfo:
        """
        Sets support information for the given user; for Telegram support only

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param message: New information message
        :type message: :class:`FormattedText`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.UserSupportInfo`
        """

        return await self.client.request(
            SetUserSupportInfo(
                user_id=user_id,
                message=message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_username(self, username: String, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Changes the editable username of the current user

        :param username: The new value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
        :type username: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetUsername(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def set_video_chat_default_participant(
        self,
        chat_id: Int53,
        default_participant_id: MessageSender,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes default participant identifier, on whose behalf a video chat in the chat will be joined

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param default_participant_id: Default group call participant identifier to join the video chats
        :type default_participant_id: :class:`MessageSender`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SetVideoChatDefaultParticipant(
                chat_id=chat_id,
                default_participant_id=default_participant_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def share_chat_with_bot(
        self,
        chat_id: Int53,
        message_id: Int53,
        button_id: Int32,
        shared_chat_id: Int53,
        only_check: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot

        :param chat_id: Identifier of the chat with the bot
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message with the button
        :type message_id: :class:`Int53`
        :param button_id: Identifier of the button
        :type button_id: :class:`Int32`
        :param shared_chat_id: Identifier of the shared chat
        :type shared_chat_id: :class:`Int53`
        :param only_check: Pass true to check that the chat can be shared by the button instead of actually sharing it. Doesn't check bot_is_member and bot_administrator_rights restrictions. If the bot must be a member, then all chats from getGroupsInCommon and all chats, where the user can add the bot, are suitable. In the latter case the bot will be automatically added to the chat. If the bot must be an administrator, then all chats, where the bot already has requested rights or can be added to administrators by the user, are suitable. In the latter case the bot will be automatically granted requested rights
        :type only_check: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ShareChatWithBot(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                shared_chat_id=shared_chat_id,
                only_check=only_check,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def share_phone_number(self, user_id: Int53, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber

        :param user_id: Identifier of the user with whom to share the phone number. The user must be a mutual contact
        :type user_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SharePhoneNumber(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def share_user_with_bot(
        self,
        chat_id: Int53,
        message_id: Int53,
        button_id: Int32,
        shared_user_id: Int53,
        only_check: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Shares a user after pressing a keyboardButtonTypeRequestUser button with the bot

        :param chat_id: Identifier of the chat with the bot
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message with the button
        :type message_id: :class:`Int53`
        :param button_id: Identifier of the button
        :type button_id: :class:`Int32`
        :param shared_user_id: Identifier of the shared user
        :type shared_user_id: :class:`Int53`
        :param only_check: Pass true to check that the user can be shared by the button instead of actually sharing them
        :type only_check: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ShareUserWithBot(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                shared_user_id=shared_user_id,
                only_check=only_check,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_group_call_recording(
        self,
        group_call_id: Int32,
        title: String = "",
        record_video: Bool = False,
        use_portrait_orientation: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Starts recording of an active group call. Requires groupCall.can_be_managed group call flag

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param title: Group call recording title; 0-64 characters
        :type title: :class:`String`
        :param record_video: Pass true to record a video file instead of an audio file
        :type record_video: :class:`Bool`
        :param use_portrait_orientation: Pass true to use portrait orientation for video instead of landscape one
        :type use_portrait_orientation: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            StartGroupCallRecording(
                group_call_id=group_call_id,
                title=title,
                record_video=record_video,
                use_portrait_orientation=use_portrait_orientation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_group_call_screen_sharing(
        self,
        group_call_id: Int32,
        audio_source_id: Int32,
        payload: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Text:
        """
        Starts screen sharing in a joined group call. Returns join response payload for tgcalls

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param audio_source_id: Screen sharing audio channel synchronization source identifier; received from tgcalls
        :type audio_source_id: :class:`Int32`
        :param payload: Group call join payload; received from tgcalls
        :type payload: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Text`
        """

        return await self.client.request(
            StartGroupCallScreenSharing(
                group_call_id=group_call_id,
                audio_source_id=audio_source_id,
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def start_scheduled_group_call(
        self, group_call_id: Int32, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Starts a scheduled group call

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            StartScheduledGroupCall(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def stop_poll(
        self,
        chat_id: Int53,
        message_id: Int53,
        reply_markup: typing.Optional[ReplyMarkup] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set

        :param chat_id: Identifier of the chat to which the poll belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message containing the poll
        :type message_id: :class:`Int53`
        :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
        :type reply_markup: :class:`ReplyMarkup`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            StopPoll(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def suggest_user_profile_photo(
        self, user_id: Int53, photo: InputChatPhoto, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Suggests a profile photo to another regular user with common messages

        :param user_id: User identifier
        :type user_id: :class:`Int53`
        :param photo: Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function
        :type photo: :class:`InputChatPhoto`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SuggestUserProfilePhoto(
                user_id=user_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def synchronize_language_pack(
        self, language_pack_id: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method doesn't need to be called explicitly for the current used/base language packs. Can be called before authorization

        :param language_pack_id: Language pack identifier
        :type language_pack_id: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            SynchronizeLanguagePack(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def terminate_all_other_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Terminates all other sessions of the current user
        """

        return await self.client.request(
            TerminateAllOtherSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def terminate_session(self, session_id: Int64, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Terminates a session of the current user

        :param session_id: Session identifier
        :type session_id: :class:`Int64`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            TerminateSession(
                session_id=session_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_bytes(self, x: Bytes, *, request_id: str = None, request_timeout: int = None) -> TestBytes:
        """
        Returns the received bytes; for testing only. This is an offline method. Can be called before authorization

        :param x: Bytes to return
        :type x: :class:`Bytes`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestBytes`
        """

        return await self.client.request(
            TestCallBytes(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_empty(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Does nothing; for testing only. This is an offline method. Can be called before authorization
        """

        return await self.client.request(
            TestCallEmpty(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_string(self, x: String, *, request_id: str = None, request_timeout: int = None) -> TestString:
        """
        Returns the received string; for testing only. This is an offline method. Can be called before authorization

        :param x: String to return
        :type x: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestString`
        """

        return await self.client.request(
            TestCallString(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_int(
        self, x: Vector[Int32], *, request_id: str = None, request_timeout: int = None
    ) -> TestVectorInt:
        """
        Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization

        :param x: Vector of numbers to return
        :type x: :class:`Vector[Int32]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorInt`
        """

        return await self.client.request(
            TestCallVectorInt(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_int_object(
        self, x: Vector[TestInt], *, request_id: str = None, request_timeout: int = None
    ) -> TestVectorIntObject:
        """
        Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization

        :param x: Vector of objects to return
        :type x: :class:`Vector[TestInt]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorIntObject`
        """

        return await self.client.request(
            TestCallVectorIntObject(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_string(
        self, x: Vector[String], *, request_id: str = None, request_timeout: int = None
    ) -> TestVectorString:
        """
        Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization

        :param x: Vector of strings to return
        :type x: :class:`Vector[String]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorString`
        """

        return await self.client.request(
            TestCallVectorString(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_call_vector_string_object(
        self, x: Vector[TestString], *, request_id: str = None, request_timeout: int = None
    ) -> TestVectorStringObject:
        """
        Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization

        :param x: Vector of objects to return
        :type x: :class:`Vector[TestString]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestVectorStringObject`
        """

        return await self.client.request(
            TestCallVectorStringObject(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_get_difference(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Forces an updates.getDifference call to the Telegram servers; for testing only
        """

        return await self.client.request(
            TestGetDifference(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_network(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
        """

        return await self.client.request(
            TestNetwork(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_proxy(
        self,
        server: String,
        port: Int32,
        type_: ProxyType,
        dc_id: Int32,
        timeout: Double,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization

        :param server: Proxy server domain or IP address
        :type server: :class:`String`
        :param port: Proxy server port
        :type port: :class:`Int32`
        :param type_: Proxy type
        :type type_: :class:`ProxyType`
        :param dc_id: Identifier of a datacenter with which to test connection
        :type dc_id: :class:`Int32`
        :param timeout: The maximum overall timeout for the request
        :type timeout: :class:`Double`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            TestProxy(
                server=server,
                port=port,
                type=type_,
                dc_id=dc_id,
                timeout=timeout,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_return_error(self, error: Error, *, request_id: str = None, request_timeout: int = None) -> Error:
        """
        Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously

        :param error: The error to be returned
        :type error: :class:`Error`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Error`
        """

        return await self.client.request(
            TestReturnError(
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_square_int(self, x: Int32, *, request_id: str = None, request_timeout: int = None) -> TestInt:
        """
        Returns the squared received number; for testing only. This is an offline method. Can be called before authorization

        :param x: Number to square
        :type x: :class:`Int32`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.TestInt`
        """

        return await self.client.request(
            TestSquareInt(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def test_use_update(self, *, request_id: str = None, request_timeout: int = None) -> Update:
        """
        Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
        """

        return await self.client.request(
            TestUseUpdate(),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_all_downloads_are_paused(
        self, are_paused: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes pause state of all files in the file download list

        :param are_paused: Pass true to pause all downloads; pass false to unpause them
        :type are_paused: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleAllDownloadsArePaused(
                are_paused=are_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_bot_is_added_to_attachment_menu(
        self,
        bot_user_id: Int53,
        is_added: Bool = False,
        allow_write_access: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Adds or removes a bot to attachment and side menu. Bot can be added to the menu, only if userTypeBot.can_be_added_to_attachment_menu == true

        :param bot_user_id: Bot's user identifier
        :type bot_user_id: :class:`Int53`
        :param is_added: Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu
        :type is_added: :class:`Bool`
        :param allow_write_access: Pass true if the current user allowed the bot to send them messages. Ignored if is_added is false
        :type allow_write_access: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleBotIsAddedToAttachmentMenu(
                bot_user_id=bot_user_id,
                is_added=is_added,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_bot_username_is_active(
        self,
        bot_user_id: Int53,
        username: String,
        is_active: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes active state for a username of a bot. The editable username can't be disabled. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached. Can be called only if userTypeBot.can_be_edited == true

        :param bot_user_id: Identifier of the target bot
        :type bot_user_id: :class:`Int53`
        :param username: The username to change
        :type username: :class:`String`
        :param is_active: Pass true to activate the username; pass false to disable it
        :type is_active: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleBotUsernameIsActive(
                bot_user_id=bot_user_id,
                username=username,
                is_active=is_active,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_default_disable_notification(
        self, chat_id: Int53, default_disable_notification: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the value of the default disable_notification parameter, used when a message is sent to a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param default_disable_notification: New value of default_disable_notification
        :type default_disable_notification: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleChatDefaultDisableNotification(
                chat_id=chat_id,
                default_disable_notification=default_disable_notification,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_has_protected_content(
        self, chat_id: Int53, has_protected_content: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param has_protected_content: New value of has_protected_content
        :type has_protected_content: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleChatHasProtectedContent(
                chat_id=chat_id,
                has_protected_content=has_protected_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_marked_as_unread(
        self, chat_id: Int53, is_marked_as_unread: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the marked as unread state of a chat

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param is_marked_as_unread: New value of is_marked_as_unread
        :type is_marked_as_unread: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleChatIsMarkedAsUnread(
                chat_id=chat_id,
                is_marked_as_unread=is_marked_as_unread,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_pinned(
        self,
        chat_list: ChatList,
        chat_id: Int53,
        is_pinned: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the pinned state of a chat. There can be up to getOption("pinned_chat_count_max")/getOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium

        :param chat_list: Chat list in which to change the pinned state of the chat
        :type chat_list: :class:`ChatList`
        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param is_pinned: Pass true to pin the chat; pass false to unpin it
        :type is_pinned: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleChatIsPinned(
                chat_list=chat_list,
                chat_id=chat_id,
                is_pinned=is_pinned,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_chat_is_translatable(
        self, chat_id: Int53, is_translatable: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the translatable state of a chat; for Telegram Premium users only

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param is_translatable: New value of is_translatable
        :type is_translatable: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleChatIsTranslatable(
                chat_id=chat_id,
                is_translatable=is_translatable,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_download_is_paused(
        self, file_id: Int32, is_paused: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes pause state of a file in the file download list

        :param file_id: Identifier of the downloaded file
        :type file_id: :class:`Int32`
        :param is_paused: Pass true if the download is paused
        :type is_paused: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleDownloadIsPaused(
                file_id=file_id,
                is_paused=is_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_forum_topic_is_closed(
        self,
        chat_id: Int53,
        message_thread_id: Int53,
        is_closed: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics administrator right in the supergroup unless the user is creator of the topic

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param is_closed: Pass true to close the topic; pass false to reopen it
        :type is_closed: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleForumTopicIsClosed(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                is_closed=is_closed,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_forum_topic_is_pinned(
        self,
        chat_id: Int53,
        message_thread_id: Int53,
        is_pinned: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes the pinned state of a forum topic; requires can_manage_topics administrator right in the supergroup. There can be up to getOption("pinned_forum_topic_count_max") pinned forum topics

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier of the forum topic
        :type message_thread_id: :class:`Int53`
        :param is_pinned: Pass true to pin the topic; pass false to unpin it
        :type is_pinned: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleForumTopicIsPinned(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                is_pinned=is_pinned,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_general_forum_topic_is_hidden(
        self, chat_id: Int53, is_hidden: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a General topic is hidden in a forum supergroup chat; requires can_manage_topics administrator right in the supergroup

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param is_hidden: Pass true to hide and close the General topic; pass false to unhide it
        :type is_hidden: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGeneralForumTopicIsHidden(
                chat_id=chat_id,
                is_hidden=is_hidden,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_enabled_start_notification(
        self,
        group_call_id: Int32,
        enabled_start_notification: Bool,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param enabled_start_notification: New value of the enabled_start_notification setting
        :type enabled_start_notification: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallEnabledStartNotification(
                group_call_id=group_call_id,
                enabled_start_notification=enabled_start_notification,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_enabled(
        self,
        group_call_id: Int32,
        is_my_video_enabled: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether current user's video is enabled

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param is_my_video_enabled: Pass true if the current user's video is enabled
        :type is_my_video_enabled: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallIsMyVideoEnabled(
                group_call_id=group_call_id,
                is_my_video_enabled=is_my_video_enabled,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_is_my_video_paused(
        self,
        group_call_id: Int32,
        is_my_video_paused: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether current user's video is paused

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param is_my_video_paused: Pass true if the current user's video is paused
        :type is_my_video_paused: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallIsMyVideoPaused(
                group_call_id=group_call_id,
                is_my_video_paused=is_my_video_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_mute_new_participants(
        self, group_call_id: Int32, mute_new_participants: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param mute_new_participants: New value of the mute_new_participants setting
        :type mute_new_participants: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallMuteNewParticipants(
                group_call_id=group_call_id,
                mute_new_participants=mute_new_participants,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_hand_raised(
        self,
        group_call_id: Int32,
        participant_id: MessageSender,
        is_hand_raised: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a group call participant hand is rased

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        :param is_hand_raised: Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
        :type is_hand_raised: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallParticipantIsHandRaised(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_hand_raised=is_hand_raised,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_participant_is_muted(
        self,
        group_call_id: Int32,
        participant_id: MessageSender,
        is_muted: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param participant_id: Participant identifier
        :type participant_id: :class:`MessageSender`
        :param is_muted: Pass true to mute the user; pass false to unmute them
        :type is_muted: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallParticipantIsMuted(
                group_call_id=group_call_id,
                participant_id=participant_id,
                is_muted=is_muted,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_group_call_screen_sharing_is_paused(
        self, group_call_id: Int32, is_paused: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Pauses or unpauses screen sharing in a joined group call

        :param group_call_id: Group call identifier
        :type group_call_id: :class:`Int32`
        :param is_paused: Pass true to pause screen sharing; pass false to unpause it
        :type is_paused: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleGroupCallScreenSharingIsPaused(
                group_call_id=group_call_id,
                is_paused=is_paused,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_calls(
        self, session_id: Int64, can_accept_calls: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a session can accept incoming calls

        :param session_id: Session identifier
        :type session_id: :class:`Int64`
        :param can_accept_calls: Pass true to allow accepting incoming calls by the session; pass false otherwise
        :type can_accept_calls: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSessionCanAcceptCalls(
                session_id=session_id,
                can_accept_calls=can_accept_calls,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_session_can_accept_secret_chats(
        self,
        session_id: Int64,
        can_accept_secret_chats: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a session can accept incoming secret chats

        :param session_id: Session identifier
        :type session_id: :class:`Int64`
        :param can_accept_secret_chats: Pass true to allow accepting secret chats by the session; pass false otherwise
        :type can_accept_secret_chats: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSessionCanAcceptSecretChats(
                session_id=session_id,
                can_accept_secret_chats=can_accept_secret_chats,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_story_is_pinned(
        self, story_id: Int32, is_pinned: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether a story is accessible after expiration

        :param story_id: Identifier of the story
        :type story_id: :class:`Int32`
        :param is_pinned: Pass true to make the story accessible after expiration; pass false to make it private
        :type is_pinned: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleStoryIsPinned(
                story_id=story_id,
                is_pinned=is_pinned,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_has_aggressive_anti_spam_enabled(
        self,
        supergroup_id: Int53,
        has_aggressive_anti_spam_enabled: Bool,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether aggressive anti-spam checks are enabled in the supergroup. Can be called only if supergroupFullInfo.can_toggle_aggressive_anti_spam == true

        :param supergroup_id: The identifier of the supergroup, which isn't a broadcast group
        :type supergroup_id: :class:`Int53`
        :param has_aggressive_anti_spam_enabled: The new value of has_aggressive_anti_spam_enabled
        :type has_aggressive_anti_spam_enabled: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupHasAggressiveAntiSpamEnabled(
                supergroup_id=supergroup_id,
                has_aggressive_anti_spam_enabled=has_aggressive_anti_spam_enabled,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_has_hidden_members(
        self, supergroup_id: Int53, has_hidden_members: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers. Can be called only if supergroupFullInfo.can_hide_members == true

        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param has_hidden_members: New value of has_hidden_members
        :type has_hidden_members: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupHasHiddenMembers(
                supergroup_id=supergroup_id,
                has_hidden_members=has_hidden_members,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_all_history_available(
        self,
        supergroup_id: Int53,
        is_all_history_available: Bool,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right

        :param supergroup_id: The identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param is_all_history_available: The new value of is_all_history_available
        :type is_all_history_available: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupIsAllHistoryAvailable(
                supergroup_id=supergroup_id,
                is_all_history_available=is_all_history_available,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_broadcast_group(
        self, supergroup_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupIsBroadcastGroup(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_is_forum(
        self, supergroup_id: Int53, is_forum: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether the supergroup is a forum; requires owner privileges in the supergroup. Discussion supergroups can't be converted to forums

        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param is_forum: New value of is_forum
        :type is_forum: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupIsForum(
                supergroup_id=supergroup_id,
                is_forum=is_forum,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_join_by_request(
        self, supergroup_id: Int53, join_by_request: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right

        :param supergroup_id: Identifier of the channel
        :type supergroup_id: :class:`Int53`
        :param join_by_request: New value of join_by_request
        :type join_by_request: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupJoinByRequest(
                supergroup_id=supergroup_id,
                join_by_request=join_by_request,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_join_to_send_messages(
        self, supergroup_id: Int53, join_to_send_messages: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right

        :param supergroup_id: Identifier of the supergroup
        :type supergroup_id: :class:`Int53`
        :param join_to_send_messages: New value of join_to_send_messages
        :type join_to_send_messages: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupJoinToSendMessages(
                supergroup_id=supergroup_id,
                join_to_send_messages=join_to_send_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_sign_messages(
        self, supergroup_id: Int53, sign_messages: Bool, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Toggles whether sender signature is added to sent messages in a channel; requires can_change_info administrator right

        :param supergroup_id: Identifier of the channel
        :type supergroup_id: :class:`Int53`
        :param sign_messages: New value of sign_messages
        :type sign_messages: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupSignMessages(
                supergroup_id=supergroup_id,
                sign_messages=sign_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_supergroup_username_is_active(
        self,
        supergroup_id: Int53,
        username: String,
        is_active: Bool = False,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel. The editable username can't be disabled. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached

        :param supergroup_id: Identifier of the supergroup or channel
        :type supergroup_id: :class:`Int53`
        :param username: The username to change
        :type username: :class:`String`
        :param is_active: Pass true to activate the username; pass false to disable it
        :type is_active: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleSupergroupUsernameIsActive(
                supergroup_id=supergroup_id,
                username=username,
                is_active=is_active,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def toggle_username_is_active(
        self, username: String, is_active: Bool = False, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes active state for a username of the current user. The editable username can't be disabled. May return an error with a message "USERNAMES_ACTIVE_TOO_MUCH" if the maximum number of active usernames has been reached

        :param username: The username to change
        :type username: :class:`String`
        :param is_active: Pass true to activate the username; pass false to disable it
        :type is_active: :class:`Bool`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ToggleUsernameIsActive(
                username=username,
                is_active=is_active,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def transfer_chat_ownership(
        self, chat_id: Int53, user_id: Int53, password: String, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param user_id: Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
        :type user_id: :class:`Int53`
        :param password: The 2-step verification password of the current user
        :type password: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            TransferChatOwnership(
                chat_id=chat_id,
                user_id=user_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def translate_message_text(
        self,
        chat_id: Int53,
        message_id: Int53,
        to_language_code: String,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> FormattedText:
        """
        Extracts text or caption of the given message and translates it to the given language. If the current user is a Telegram Premium user, then text formatting is preserved

        :param chat_id: Identifier of the chat to which the message belongs
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the message
        :type message_id: :class:`Int53`
        :param to_language_code: Language code of the language to which the message is translated. Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"
        :type to_language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """

        return await self.client.request(
            TranslateMessageText(
                chat_id=chat_id,
                message_id=message_id,
                to_language_code=to_language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def translate_text(
        self, text: FormattedText, to_language_code: String, *, request_id: str = None, request_timeout: int = None
    ) -> FormattedText:
        """
        Translates a text to the given language. If the current user is a Telegram Premium user, then text formatting is preserved

        :param text: Text to translate
        :type text: :class:`FormattedText`
        :param to_language_code: Language code of the language to which the message is translated. Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh", "zh-Hans", "zh-TW", "zh-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"
        :type to_language_code: :class:`String`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.FormattedText`
        """

        return await self.client.request(
            TranslateText(
                text=text,
                to_language_code=to_language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def unpin_all_chat_messages(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            UnpinAllChatMessages(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def unpin_all_message_thread_messages(
        self, chat_id: Int53, message_thread_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes all pinned messages from a forum topic; requires can_pin_messages rights in the supergroup

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_thread_id: Message thread identifier in which messages will be unpinned
        :type message_thread_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            UnpinAllMessageThreadMessages(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def unpin_chat_message(
        self, chat_id: Int53, message_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel

        :param chat_id: Identifier of the chat
        :type chat_id: :class:`Int53`
        :param message_id: Identifier of the removed pinned message
        :type message_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            UnpinChatMessage(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def upgrade_basic_group_chat_to_supergroup_chat(
        self, chat_id: Int53, *, request_id: str = None, request_timeout: int = None
    ) -> Chat:
        """
        Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group

        :param chat_id: Identifier of the chat to upgrade
        :type chat_id: :class:`Int53`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Chat`
        """

        return await self.client.request(
            UpgradeBasicGroupChatToSupergroupChat(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def upload_sticker_file(
        self,
        user_id: Int53,
        sticker_format: StickerFormat,
        sticker: InputFile,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> File:
        """
        Uploads a file with a sticker; returns the uploaded file

        :param user_id: Sticker file owner; ignored for regular users
        :type user_id: :class:`Int53`
        :param sticker_format: Sticker format
        :type sticker_format: :class:`StickerFormat`
        :param sticker: File file to upload; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
        :type sticker: :class:`InputFile`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.File`
        """

        return await self.client.request(
            UploadStickerFile(
                user_id=user_id,
                sticker_format=sticker_format,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def validate_order_info(
        self,
        input_invoice: InputInvoice,
        allow_save: Bool = False,
        order_info: typing.Optional[OrderInfo] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> ValidatedOrderInfo:
        """
        Validates the order information provided by a user and returns the available shipping options for a flexible invoice

        :param input_invoice: The invoice
        :type input_invoice: :class:`InputInvoice`
        :param allow_save: Pass true to save the order information
        :type allow_save: :class:`Bool`
        :param order_info: The order information, provided by the user; pass null if empty, defaults to None
        :type order_info: :class:`OrderInfo`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.ValidatedOrderInfo`
        """

        return await self.client.request(
            ValidateOrderInfo(
                input_invoice=input_invoice,
                allow_save=allow_save,
                order_info=order_info,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def view_messages(
        self,
        chat_id: Int53,
        message_ids: Vector[Int53],
        force_read: Bool = False,
        source: typing.Optional[MessageSource] = None,
        *,
        request_id: str = None,
        request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button). Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)

        :param chat_id: Chat identifier
        :type chat_id: :class:`Int53`
        :param message_ids: The identifiers of the messages being viewed
        :type message_ids: :class:`Vector[Int53]`
        :param force_read: Pass true to mark as read the specified messages even the chat is closed
        :type force_read: :class:`Bool`
        :param source: Source of the message view; pass null to guess the source based on chat open state, defaults to None
        :type source: :class:`MessageSource`, optional
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ViewMessages(
                chat_id=chat_id,
                message_ids=message_ids,
                force_read=force_read,
                source=source,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def view_premium_feature(
        self, feature: PremiumFeature, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

        :param feature: The viewed premium feature
        :type feature: :class:`PremiumFeature`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ViewPremiumFeature(
                feature=feature,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def view_trending_sticker_sets(
        self, sticker_set_ids: Vector[Int64], *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Informs the server that some trending sticker sets have been viewed by the user

        :param sticker_set_ids: Identifiers of viewed trending sticker sets
        :type sticker_set_ids: :class:`Vector[Int64]`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            ViewTrendingStickerSets(
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )

    async def write_generated_file_part(
        self, generation_id: Int64, offset: Int53, data: Bytes, *, request_id: str = None, request_timeout: int = None
    ) -> Ok:
        """
        Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

        :param generation_id: The identifier of the generation process
        :type generation_id: :class:`Int64`
        :param offset: The offset from which to write the data to the file
        :type offset: :class:`Int53`
        :param data: The data to write
        :type data: :class:`Bytes`
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.Ok`
        """

        return await self.client.request(
            WriteGeneratedFilePart(
                generation_id=generation_id,
                offset=offset,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
