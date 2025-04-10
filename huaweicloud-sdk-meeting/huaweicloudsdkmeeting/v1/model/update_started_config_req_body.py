# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStartedConfigReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_sharing': 'int',
        'call_in_restriction': 'int',
        'allow_unmute_by_oneself': 'int',
        'chat_permission': 'int',
        'audience_call_in_restriction': 'int',
        'client_rec_mode': 'int',
        'allow_open_camera': 'int',
        'allow_rename': 'int',
        'is_lock': 'int',
        'free_share': 'int'
    }

    attribute_map = {
        'lock_sharing': 'lockSharing',
        'call_in_restriction': 'callInRestriction',
        'allow_unmute_by_oneself': 'allowUnmuteByOneself',
        'chat_permission': 'chatPermission',
        'audience_call_in_restriction': 'audienceCallInRestriction',
        'client_rec_mode': 'clientRecMode',
        'allow_open_camera': 'allowOpenCamera',
        'allow_rename': 'allowRename',
        'is_lock': 'isLock',
        'free_share': 'freeShare'
    }

    def __init__(self, lock_sharing=None, call_in_restriction=None, allow_unmute_by_oneself=None, chat_permission=None, audience_call_in_restriction=None, client_rec_mode=None, allow_open_camera=None, allow_rename=None, is_lock=None, free_share=None):
        r"""UpdateStartedConfigReqBody

        The model defined in huaweicloud sdk

        :param lock_sharing: 锁定共享标志位。 * 0: 不锁定 * 1: 锁定 
        :type lock_sharing: int
        :param call_in_restriction: 允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 
        :type call_in_restriction: int
        :param allow_unmute_by_oneself: 是否允许自己解除静音，默认为允许 - 0: 不允许 - 1: 允许 
        :type allow_unmute_by_oneself: int
        :param chat_permission: 会议聊天权限 1.全员禁止 2.仅允许私聊 3.仅允许公开聊天 4.允许自由聊天
        :type chat_permission: int
        :param audience_call_in_restriction: 网络研讨会观众允许呼入的范围 0：所有用户  2：企业内用户和被邀请用户
        :type audience_call_in_restriction: int
        :param client_rec_mode: 客户端本地录制权限的范围，默认为仅主持人支持本地录制 - 0: 所有用户 - 1：全部人可录制 - 2：部分人可录制 
        :type client_rec_mode: int
        :param allow_open_camera: 与会人自行开启摄像头 0:禁止 1:允许
        :type allow_open_camera: int
        :param allow_rename: 是否允许与会人改名 0:不允许 1:允许
        :type allow_rename: int
        :param is_lock: 锁定会议 0：解锁 1：锁定
        :type is_lock: int
        :param free_share: 抢共享权限设置 0:仅主持人/联席 1:所有人可抢共享
        :type free_share: int
        """
        
        

        self._lock_sharing = None
        self._call_in_restriction = None
        self._allow_unmute_by_oneself = None
        self._chat_permission = None
        self._audience_call_in_restriction = None
        self._client_rec_mode = None
        self._allow_open_camera = None
        self._allow_rename = None
        self._is_lock = None
        self._free_share = None
        self.discriminator = None

        if lock_sharing is not None:
            self.lock_sharing = lock_sharing
        if call_in_restriction is not None:
            self.call_in_restriction = call_in_restriction
        if allow_unmute_by_oneself is not None:
            self.allow_unmute_by_oneself = allow_unmute_by_oneself
        if chat_permission is not None:
            self.chat_permission = chat_permission
        if audience_call_in_restriction is not None:
            self.audience_call_in_restriction = audience_call_in_restriction
        if client_rec_mode is not None:
            self.client_rec_mode = client_rec_mode
        if allow_open_camera is not None:
            self.allow_open_camera = allow_open_camera
        if allow_rename is not None:
            self.allow_rename = allow_rename
        if is_lock is not None:
            self.is_lock = is_lock
        if free_share is not None:
            self.free_share = free_share

    @property
    def lock_sharing(self):
        r"""Gets the lock_sharing of this UpdateStartedConfigReqBody.

        锁定共享标志位。 * 0: 不锁定 * 1: 锁定 

        :return: The lock_sharing of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._lock_sharing

    @lock_sharing.setter
    def lock_sharing(self, lock_sharing):
        r"""Sets the lock_sharing of this UpdateStartedConfigReqBody.

        锁定共享标志位。 * 0: 不锁定 * 1: 锁定 

        :param lock_sharing: The lock_sharing of this UpdateStartedConfigReqBody.
        :type lock_sharing: int
        """
        self._lock_sharing = lock_sharing

    @property
    def call_in_restriction(self):
        r"""Gets the call_in_restriction of this UpdateStartedConfigReqBody.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :return: The call_in_restriction of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._call_in_restriction

    @call_in_restriction.setter
    def call_in_restriction(self, call_in_restriction):
        r"""Sets the call_in_restriction of this UpdateStartedConfigReqBody.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :param call_in_restriction: The call_in_restriction of this UpdateStartedConfigReqBody.
        :type call_in_restriction: int
        """
        self._call_in_restriction = call_in_restriction

    @property
    def allow_unmute_by_oneself(self):
        r"""Gets the allow_unmute_by_oneself of this UpdateStartedConfigReqBody.

        是否允许自己解除静音，默认为允许 - 0: 不允许 - 1: 允许 

        :return: The allow_unmute_by_oneself of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._allow_unmute_by_oneself

    @allow_unmute_by_oneself.setter
    def allow_unmute_by_oneself(self, allow_unmute_by_oneself):
        r"""Sets the allow_unmute_by_oneself of this UpdateStartedConfigReqBody.

        是否允许自己解除静音，默认为允许 - 0: 不允许 - 1: 允许 

        :param allow_unmute_by_oneself: The allow_unmute_by_oneself of this UpdateStartedConfigReqBody.
        :type allow_unmute_by_oneself: int
        """
        self._allow_unmute_by_oneself = allow_unmute_by_oneself

    @property
    def chat_permission(self):
        r"""Gets the chat_permission of this UpdateStartedConfigReqBody.

        会议聊天权限 1.全员禁止 2.仅允许私聊 3.仅允许公开聊天 4.允许自由聊天

        :return: The chat_permission of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._chat_permission

    @chat_permission.setter
    def chat_permission(self, chat_permission):
        r"""Sets the chat_permission of this UpdateStartedConfigReqBody.

        会议聊天权限 1.全员禁止 2.仅允许私聊 3.仅允许公开聊天 4.允许自由聊天

        :param chat_permission: The chat_permission of this UpdateStartedConfigReqBody.
        :type chat_permission: int
        """
        self._chat_permission = chat_permission

    @property
    def audience_call_in_restriction(self):
        r"""Gets the audience_call_in_restriction of this UpdateStartedConfigReqBody.

        网络研讨会观众允许呼入的范围 0：所有用户  2：企业内用户和被邀请用户

        :return: The audience_call_in_restriction of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._audience_call_in_restriction

    @audience_call_in_restriction.setter
    def audience_call_in_restriction(self, audience_call_in_restriction):
        r"""Sets the audience_call_in_restriction of this UpdateStartedConfigReqBody.

        网络研讨会观众允许呼入的范围 0：所有用户  2：企业内用户和被邀请用户

        :param audience_call_in_restriction: The audience_call_in_restriction of this UpdateStartedConfigReqBody.
        :type audience_call_in_restriction: int
        """
        self._audience_call_in_restriction = audience_call_in_restriction

    @property
    def client_rec_mode(self):
        r"""Gets the client_rec_mode of this UpdateStartedConfigReqBody.

        客户端本地录制权限的范围，默认为仅主持人支持本地录制 - 0: 所有用户 - 1：全部人可录制 - 2：部分人可录制 

        :return: The client_rec_mode of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._client_rec_mode

    @client_rec_mode.setter
    def client_rec_mode(self, client_rec_mode):
        r"""Sets the client_rec_mode of this UpdateStartedConfigReqBody.

        客户端本地录制权限的范围，默认为仅主持人支持本地录制 - 0: 所有用户 - 1：全部人可录制 - 2：部分人可录制 

        :param client_rec_mode: The client_rec_mode of this UpdateStartedConfigReqBody.
        :type client_rec_mode: int
        """
        self._client_rec_mode = client_rec_mode

    @property
    def allow_open_camera(self):
        r"""Gets the allow_open_camera of this UpdateStartedConfigReqBody.

        与会人自行开启摄像头 0:禁止 1:允许

        :return: The allow_open_camera of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._allow_open_camera

    @allow_open_camera.setter
    def allow_open_camera(self, allow_open_camera):
        r"""Sets the allow_open_camera of this UpdateStartedConfigReqBody.

        与会人自行开启摄像头 0:禁止 1:允许

        :param allow_open_camera: The allow_open_camera of this UpdateStartedConfigReqBody.
        :type allow_open_camera: int
        """
        self._allow_open_camera = allow_open_camera

    @property
    def allow_rename(self):
        r"""Gets the allow_rename of this UpdateStartedConfigReqBody.

        是否允许与会人改名 0:不允许 1:允许

        :return: The allow_rename of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._allow_rename

    @allow_rename.setter
    def allow_rename(self, allow_rename):
        r"""Sets the allow_rename of this UpdateStartedConfigReqBody.

        是否允许与会人改名 0:不允许 1:允许

        :param allow_rename: The allow_rename of this UpdateStartedConfigReqBody.
        :type allow_rename: int
        """
        self._allow_rename = allow_rename

    @property
    def is_lock(self):
        r"""Gets the is_lock of this UpdateStartedConfigReqBody.

        锁定会议 0：解锁 1：锁定

        :return: The is_lock of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._is_lock

    @is_lock.setter
    def is_lock(self, is_lock):
        r"""Sets the is_lock of this UpdateStartedConfigReqBody.

        锁定会议 0：解锁 1：锁定

        :param is_lock: The is_lock of this UpdateStartedConfigReqBody.
        :type is_lock: int
        """
        self._is_lock = is_lock

    @property
    def free_share(self):
        r"""Gets the free_share of this UpdateStartedConfigReqBody.

        抢共享权限设置 0:仅主持人/联席 1:所有人可抢共享

        :return: The free_share of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._free_share

    @free_share.setter
    def free_share(self, free_share):
        r"""Sets the free_share of this UpdateStartedConfigReqBody.

        抢共享权限设置 0:仅主持人/联席 1:所有人可抢共享

        :param free_share: The free_share of this UpdateStartedConfigReqBody.
        :type free_share: int
        """
        self._free_share = free_share

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateStartedConfigReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
