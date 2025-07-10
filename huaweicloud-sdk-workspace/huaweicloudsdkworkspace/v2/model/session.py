# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Session:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vdi': 'Vdi',
        'self_help_console': 'bool',
        'disconnect_on_lock_flag': 'bool',
        'auto_lock_start_time': 'str',
        'auto_lock_end_time': 'str'
    }

    attribute_map = {
        'vdi': 'vdi',
        'self_help_console': 'self_help_console',
        'disconnect_on_lock_flag': 'disconnect_on_lock_flag',
        'auto_lock_start_time': 'auto_lock_start_time',
        'auto_lock_end_time': 'auto_lock_end_time'
    }

    def __init__(self, vdi=None, self_help_console=None, disconnect_on_lock_flag=None, auto_lock_start_time=None, auto_lock_end_time=None):
        r"""Session

        The model defined in huaweicloud sdk

        :param vdi: 
        :type vdi: :class:`huaweicloudsdkworkspace.v2.Vdi`
        :param self_help_console: 是否开启自助维护台抢占登录。取值为：false：表示关闭。true：表示开启。
        :type self_help_console: bool
        :param disconnect_on_lock_flag: 是否锁屏后断开。
        :type disconnect_on_lock_flag: bool
        :param auto_lock_start_time: 锁定生效开始时间，格式 hh:mm:ss
        :type auto_lock_start_time: str
        :param auto_lock_end_time: 锁定生效开始时间，格式 hh:mm:ss
        :type auto_lock_end_time: str
        """
        
        

        self._vdi = None
        self._self_help_console = None
        self._disconnect_on_lock_flag = None
        self._auto_lock_start_time = None
        self._auto_lock_end_time = None
        self.discriminator = None

        if vdi is not None:
            self.vdi = vdi
        if self_help_console is not None:
            self.self_help_console = self_help_console
        if disconnect_on_lock_flag is not None:
            self.disconnect_on_lock_flag = disconnect_on_lock_flag
        if auto_lock_start_time is not None:
            self.auto_lock_start_time = auto_lock_start_time
        if auto_lock_end_time is not None:
            self.auto_lock_end_time = auto_lock_end_time

    @property
    def vdi(self):
        r"""Gets the vdi of this Session.

        :return: The vdi of this Session.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Vdi`
        """
        return self._vdi

    @vdi.setter
    def vdi(self, vdi):
        r"""Sets the vdi of this Session.

        :param vdi: The vdi of this Session.
        :type vdi: :class:`huaweicloudsdkworkspace.v2.Vdi`
        """
        self._vdi = vdi

    @property
    def self_help_console(self):
        r"""Gets the self_help_console of this Session.

        是否开启自助维护台抢占登录。取值为：false：表示关闭。true：表示开启。

        :return: The self_help_console of this Session.
        :rtype: bool
        """
        return self._self_help_console

    @self_help_console.setter
    def self_help_console(self, self_help_console):
        r"""Sets the self_help_console of this Session.

        是否开启自助维护台抢占登录。取值为：false：表示关闭。true：表示开启。

        :param self_help_console: The self_help_console of this Session.
        :type self_help_console: bool
        """
        self._self_help_console = self_help_console

    @property
    def disconnect_on_lock_flag(self):
        r"""Gets the disconnect_on_lock_flag of this Session.

        是否锁屏后断开。

        :return: The disconnect_on_lock_flag of this Session.
        :rtype: bool
        """
        return self._disconnect_on_lock_flag

    @disconnect_on_lock_flag.setter
    def disconnect_on_lock_flag(self, disconnect_on_lock_flag):
        r"""Sets the disconnect_on_lock_flag of this Session.

        是否锁屏后断开。

        :param disconnect_on_lock_flag: The disconnect_on_lock_flag of this Session.
        :type disconnect_on_lock_flag: bool
        """
        self._disconnect_on_lock_flag = disconnect_on_lock_flag

    @property
    def auto_lock_start_time(self):
        r"""Gets the auto_lock_start_time of this Session.

        锁定生效开始时间，格式 hh:mm:ss

        :return: The auto_lock_start_time of this Session.
        :rtype: str
        """
        return self._auto_lock_start_time

    @auto_lock_start_time.setter
    def auto_lock_start_time(self, auto_lock_start_time):
        r"""Sets the auto_lock_start_time of this Session.

        锁定生效开始时间，格式 hh:mm:ss

        :param auto_lock_start_time: The auto_lock_start_time of this Session.
        :type auto_lock_start_time: str
        """
        self._auto_lock_start_time = auto_lock_start_time

    @property
    def auto_lock_end_time(self):
        r"""Gets the auto_lock_end_time of this Session.

        锁定生效开始时间，格式 hh:mm:ss

        :return: The auto_lock_end_time of this Session.
        :rtype: str
        """
        return self._auto_lock_end_time

    @auto_lock_end_time.setter
    def auto_lock_end_time(self, auto_lock_end_time):
        r"""Sets the auto_lock_end_time of this Session.

        锁定生效开始时间，格式 hh:mm:ss

        :param auto_lock_end_time: The auto_lock_end_time of this Session.
        :type auto_lock_end_time: str
        """
        self._auto_lock_end_time = auto_lock_end_time

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
        if not isinstance(other, Session):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
