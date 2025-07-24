# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerPowerStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'on': 'int',
        'off': 'int',
        'unknown': 'int'
    }

    attribute_map = {
        'on': 'on',
        'off': 'off',
        'unknown': 'unknown'
    }

    def __init__(self, on=None, off=None, unknown=None):
        r"""ServerPowerStatus

        The model defined in huaweicloud sdk

        :param on: 开机状态的数量
        :type on: int
        :param off: 关机状态的数量
        :type off: int
        :param unknown: 未知状态的数量
        :type unknown: int
        """
        
        

        self._on = None
        self._off = None
        self._unknown = None
        self.discriminator = None

        self.on = on
        self.off = off
        if unknown is not None:
            self.unknown = unknown

    @property
    def on(self):
        r"""Gets the on of this ServerPowerStatus.

        开机状态的数量

        :return: The on of this ServerPowerStatus.
        :rtype: int
        """
        return self._on

    @on.setter
    def on(self, on):
        r"""Sets the on of this ServerPowerStatus.

        开机状态的数量

        :param on: The on of this ServerPowerStatus.
        :type on: int
        """
        self._on = on

    @property
    def off(self):
        r"""Gets the off of this ServerPowerStatus.

        关机状态的数量

        :return: The off of this ServerPowerStatus.
        :rtype: int
        """
        return self._off

    @off.setter
    def off(self, off):
        r"""Sets the off of this ServerPowerStatus.

        关机状态的数量

        :param off: The off of this ServerPowerStatus.
        :type off: int
        """
        self._off = off

    @property
    def unknown(self):
        r"""Gets the unknown of this ServerPowerStatus.

        未知状态的数量

        :return: The unknown of this ServerPowerStatus.
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        r"""Sets the unknown of this ServerPowerStatus.

        未知状态的数量

        :param unknown: The unknown of this ServerPowerStatus.
        :type unknown: int
        """
        self._unknown = unknown

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
        if not isinstance(other, ServerPowerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
