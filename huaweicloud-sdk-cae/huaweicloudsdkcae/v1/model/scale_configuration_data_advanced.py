# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleConfigurationDataAdvanced:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaledown_stabilization_seconds': 'int',
        'scaledown_rate': 'int',
        'scaleup_stabilization_seconds': 'int',
        'scaleup_rate': 'int',
        'disable_scaledown': 'bool'
    }

    attribute_map = {
        'scaledown_stabilization_seconds': 'scaledown_stabilization_seconds',
        'scaledown_rate': 'scaledown_rate',
        'scaleup_stabilization_seconds': 'scaleup_stabilization_seconds',
        'scaleup_rate': 'scaleup_rate',
        'disable_scaledown': 'disable_scaledown'
    }

    def __init__(self, scaledown_stabilization_seconds=None, scaledown_rate=None, scaleup_stabilization_seconds=None, scaleup_rate=None, disable_scaledown=None):
        """ScaleConfigurationDataAdvanced

        The model defined in huaweicloud sdk

        :param scaledown_stabilization_seconds: 缩容冷却时间窗。
        :type scaledown_stabilization_seconds: int
        :param scaledown_rate: 缩容步长。
        :type scaledown_rate: int
        :param scaleup_stabilization_seconds: 扩容冷却时间窗。
        :type scaleup_stabilization_seconds: int
        :param scaleup_rate: 扩容步长。
        :type scaleup_rate: int
        :param disable_scaledown: 是否禁用自动缩容。
        :type disable_scaledown: bool
        """
        
        

        self._scaledown_stabilization_seconds = None
        self._scaledown_rate = None
        self._scaleup_stabilization_seconds = None
        self._scaleup_rate = None
        self._disable_scaledown = None
        self.discriminator = None

        if scaledown_stabilization_seconds is not None:
            self.scaledown_stabilization_seconds = scaledown_stabilization_seconds
        if scaledown_rate is not None:
            self.scaledown_rate = scaledown_rate
        if scaleup_stabilization_seconds is not None:
            self.scaleup_stabilization_seconds = scaleup_stabilization_seconds
        if scaleup_rate is not None:
            self.scaleup_rate = scaleup_rate
        if disable_scaledown is not None:
            self.disable_scaledown = disable_scaledown

    @property
    def scaledown_stabilization_seconds(self):
        """Gets the scaledown_stabilization_seconds of this ScaleConfigurationDataAdvanced.

        缩容冷却时间窗。

        :return: The scaledown_stabilization_seconds of this ScaleConfigurationDataAdvanced.
        :rtype: int
        """
        return self._scaledown_stabilization_seconds

    @scaledown_stabilization_seconds.setter
    def scaledown_stabilization_seconds(self, scaledown_stabilization_seconds):
        """Sets the scaledown_stabilization_seconds of this ScaleConfigurationDataAdvanced.

        缩容冷却时间窗。

        :param scaledown_stabilization_seconds: The scaledown_stabilization_seconds of this ScaleConfigurationDataAdvanced.
        :type scaledown_stabilization_seconds: int
        """
        self._scaledown_stabilization_seconds = scaledown_stabilization_seconds

    @property
    def scaledown_rate(self):
        """Gets the scaledown_rate of this ScaleConfigurationDataAdvanced.

        缩容步长。

        :return: The scaledown_rate of this ScaleConfigurationDataAdvanced.
        :rtype: int
        """
        return self._scaledown_rate

    @scaledown_rate.setter
    def scaledown_rate(self, scaledown_rate):
        """Sets the scaledown_rate of this ScaleConfigurationDataAdvanced.

        缩容步长。

        :param scaledown_rate: The scaledown_rate of this ScaleConfigurationDataAdvanced.
        :type scaledown_rate: int
        """
        self._scaledown_rate = scaledown_rate

    @property
    def scaleup_stabilization_seconds(self):
        """Gets the scaleup_stabilization_seconds of this ScaleConfigurationDataAdvanced.

        扩容冷却时间窗。

        :return: The scaleup_stabilization_seconds of this ScaleConfigurationDataAdvanced.
        :rtype: int
        """
        return self._scaleup_stabilization_seconds

    @scaleup_stabilization_seconds.setter
    def scaleup_stabilization_seconds(self, scaleup_stabilization_seconds):
        """Sets the scaleup_stabilization_seconds of this ScaleConfigurationDataAdvanced.

        扩容冷却时间窗。

        :param scaleup_stabilization_seconds: The scaleup_stabilization_seconds of this ScaleConfigurationDataAdvanced.
        :type scaleup_stabilization_seconds: int
        """
        self._scaleup_stabilization_seconds = scaleup_stabilization_seconds

    @property
    def scaleup_rate(self):
        """Gets the scaleup_rate of this ScaleConfigurationDataAdvanced.

        扩容步长。

        :return: The scaleup_rate of this ScaleConfigurationDataAdvanced.
        :rtype: int
        """
        return self._scaleup_rate

    @scaleup_rate.setter
    def scaleup_rate(self, scaleup_rate):
        """Sets the scaleup_rate of this ScaleConfigurationDataAdvanced.

        扩容步长。

        :param scaleup_rate: The scaleup_rate of this ScaleConfigurationDataAdvanced.
        :type scaleup_rate: int
        """
        self._scaleup_rate = scaleup_rate

    @property
    def disable_scaledown(self):
        """Gets the disable_scaledown of this ScaleConfigurationDataAdvanced.

        是否禁用自动缩容。

        :return: The disable_scaledown of this ScaleConfigurationDataAdvanced.
        :rtype: bool
        """
        return self._disable_scaledown

    @disable_scaledown.setter
    def disable_scaledown(self, disable_scaledown):
        """Sets the disable_scaledown of this ScaleConfigurationDataAdvanced.

        是否禁用自动缩容。

        :param disable_scaledown: The disable_scaledown of this ScaleConfigurationDataAdvanced.
        :type disable_scaledown: bool
        """
        self._disable_scaledown = disable_scaledown

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
        if not isinstance(other, ScaleConfigurationDataAdvanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
