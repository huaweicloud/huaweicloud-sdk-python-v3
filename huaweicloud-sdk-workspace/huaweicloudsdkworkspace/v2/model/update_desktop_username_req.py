# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDesktopUsernameReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_username': 'str',
        'old_user_domain': 'str',
        'new_username': 'str',
        'new_user_domain': 'str',
        'is_reboot': 'bool'
    }

    attribute_map = {
        'old_username': 'old_username',
        'old_user_domain': 'old_user_domain',
        'new_username': 'new_username',
        'new_user_domain': 'new_user_domain',
        'is_reboot': 'is_reboot'
    }

    def __init__(self, old_username=None, old_user_domain=None, new_username=None, new_user_domain=None, is_reboot=None):
        r"""UpdateDesktopUsernameReq

        The model defined in huaweicloud sdk

        :param old_username: 桌面关联原用户名，只传用户名，不带域信息。
        :type old_username: str
        :param old_user_domain: 桌面关联原用户名的域。
        :type old_user_domain: str
        :param new_username: 桌面关联新用户名，只传用户名，不带域信息。
        :type new_username: str
        :param new_user_domain: 桌面关联新用户名的域。
        :type new_user_domain: str
        :param is_reboot: 桌面关联新用户名后是否重启虚拟机，默认不重启。
        :type is_reboot: bool
        """
        
        

        self._old_username = None
        self._old_user_domain = None
        self._new_username = None
        self._new_user_domain = None
        self._is_reboot = None
        self.discriminator = None

        self.old_username = old_username
        if old_user_domain is not None:
            self.old_user_domain = old_user_domain
        self.new_username = new_username
        if new_user_domain is not None:
            self.new_user_domain = new_user_domain
        if is_reboot is not None:
            self.is_reboot = is_reboot

    @property
    def old_username(self):
        r"""Gets the old_username of this UpdateDesktopUsernameReq.

        桌面关联原用户名，只传用户名，不带域信息。

        :return: The old_username of this UpdateDesktopUsernameReq.
        :rtype: str
        """
        return self._old_username

    @old_username.setter
    def old_username(self, old_username):
        r"""Sets the old_username of this UpdateDesktopUsernameReq.

        桌面关联原用户名，只传用户名，不带域信息。

        :param old_username: The old_username of this UpdateDesktopUsernameReq.
        :type old_username: str
        """
        self._old_username = old_username

    @property
    def old_user_domain(self):
        r"""Gets the old_user_domain of this UpdateDesktopUsernameReq.

        桌面关联原用户名的域。

        :return: The old_user_domain of this UpdateDesktopUsernameReq.
        :rtype: str
        """
        return self._old_user_domain

    @old_user_domain.setter
    def old_user_domain(self, old_user_domain):
        r"""Sets the old_user_domain of this UpdateDesktopUsernameReq.

        桌面关联原用户名的域。

        :param old_user_domain: The old_user_domain of this UpdateDesktopUsernameReq.
        :type old_user_domain: str
        """
        self._old_user_domain = old_user_domain

    @property
    def new_username(self):
        r"""Gets the new_username of this UpdateDesktopUsernameReq.

        桌面关联新用户名，只传用户名，不带域信息。

        :return: The new_username of this UpdateDesktopUsernameReq.
        :rtype: str
        """
        return self._new_username

    @new_username.setter
    def new_username(self, new_username):
        r"""Sets the new_username of this UpdateDesktopUsernameReq.

        桌面关联新用户名，只传用户名，不带域信息。

        :param new_username: The new_username of this UpdateDesktopUsernameReq.
        :type new_username: str
        """
        self._new_username = new_username

    @property
    def new_user_domain(self):
        r"""Gets the new_user_domain of this UpdateDesktopUsernameReq.

        桌面关联新用户名的域。

        :return: The new_user_domain of this UpdateDesktopUsernameReq.
        :rtype: str
        """
        return self._new_user_domain

    @new_user_domain.setter
    def new_user_domain(self, new_user_domain):
        r"""Sets the new_user_domain of this UpdateDesktopUsernameReq.

        桌面关联新用户名的域。

        :param new_user_domain: The new_user_domain of this UpdateDesktopUsernameReq.
        :type new_user_domain: str
        """
        self._new_user_domain = new_user_domain

    @property
    def is_reboot(self):
        r"""Gets the is_reboot of this UpdateDesktopUsernameReq.

        桌面关联新用户名后是否重启虚拟机，默认不重启。

        :return: The is_reboot of this UpdateDesktopUsernameReq.
        :rtype: bool
        """
        return self._is_reboot

    @is_reboot.setter
    def is_reboot(self, is_reboot):
        r"""Sets the is_reboot of this UpdateDesktopUsernameReq.

        桌面关联新用户名后是否重启虚拟机，默认不重启。

        :param is_reboot: The is_reboot of this UpdateDesktopUsernameReq.
        :type is_reboot: bool
        """
        self._is_reboot = is_reboot

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDesktopUsernameReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
