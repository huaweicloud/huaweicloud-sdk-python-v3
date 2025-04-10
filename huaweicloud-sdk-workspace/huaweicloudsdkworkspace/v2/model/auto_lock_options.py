# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoLockOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_lock_minutes': 'int',
        'auto_disconnect': 'str',
        'options': 'AutoDisconnectOrLogoutControlOptions'
    }

    attribute_map = {
        'auto_lock_minutes': 'auto_lock_minutes',
        'auto_disconnect': 'auto_disconnect',
        'options': 'options'
    }

    def __init__(self, auto_lock_minutes=None, auto_disconnect=None, options=None):
        r"""AutoLockOptions

        The model defined in huaweicloud sdk

        :param auto_lock_minutes: 锁屏等待时间（分钟）。取值范围为[3-86400]。默认：10。
        :type auto_lock_minutes: int
        :param auto_disconnect: 自动断开或注销。取值为：AUTO_DISCONNECT：自动断开。AUTO_LOGOUT：自动注销。DISABLED：已禁用。（默认）AUTO_RESTART：自动重启。AUTO_STOP：自动停止。HIBERNATE:休眠。
        :type auto_disconnect: str
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.AutoDisconnectOrLogoutControlOptions`
        """
        
        

        self._auto_lock_minutes = None
        self._auto_disconnect = None
        self._options = None
        self.discriminator = None

        if auto_lock_minutes is not None:
            self.auto_lock_minutes = auto_lock_minutes
        if auto_disconnect is not None:
            self.auto_disconnect = auto_disconnect
        if options is not None:
            self.options = options

    @property
    def auto_lock_minutes(self):
        r"""Gets the auto_lock_minutes of this AutoLockOptions.

        锁屏等待时间（分钟）。取值范围为[3-86400]。默认：10。

        :return: The auto_lock_minutes of this AutoLockOptions.
        :rtype: int
        """
        return self._auto_lock_minutes

    @auto_lock_minutes.setter
    def auto_lock_minutes(self, auto_lock_minutes):
        r"""Sets the auto_lock_minutes of this AutoLockOptions.

        锁屏等待时间（分钟）。取值范围为[3-86400]。默认：10。

        :param auto_lock_minutes: The auto_lock_minutes of this AutoLockOptions.
        :type auto_lock_minutes: int
        """
        self._auto_lock_minutes = auto_lock_minutes

    @property
    def auto_disconnect(self):
        r"""Gets the auto_disconnect of this AutoLockOptions.

        自动断开或注销。取值为：AUTO_DISCONNECT：自动断开。AUTO_LOGOUT：自动注销。DISABLED：已禁用。（默认）AUTO_RESTART：自动重启。AUTO_STOP：自动停止。HIBERNATE:休眠。

        :return: The auto_disconnect of this AutoLockOptions.
        :rtype: str
        """
        return self._auto_disconnect

    @auto_disconnect.setter
    def auto_disconnect(self, auto_disconnect):
        r"""Sets the auto_disconnect of this AutoLockOptions.

        自动断开或注销。取值为：AUTO_DISCONNECT：自动断开。AUTO_LOGOUT：自动注销。DISABLED：已禁用。（默认）AUTO_RESTART：自动重启。AUTO_STOP：自动停止。HIBERNATE:休眠。

        :param auto_disconnect: The auto_disconnect of this AutoLockOptions.
        :type auto_disconnect: str
        """
        self._auto_disconnect = auto_disconnect

    @property
    def options(self):
        r"""Gets the options of this AutoLockOptions.

        :return: The options of this AutoLockOptions.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AutoDisconnectOrLogoutControlOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this AutoLockOptions.

        :param options: The options of this AutoLockOptions.
        :type options: :class:`huaweicloudsdkworkspace.v2.AutoDisconnectOrLogoutControlOptions`
        """
        self._options = options

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
        if not isinstance(other, AutoLockOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
