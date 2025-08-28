# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionDrain:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'timeout': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'timeout': 'timeout'
    }

    def __init__(self, enable=None, timeout=None):
        r"""ConnectionDrain

        The model defined in huaweicloud sdk

        :param enable: **参数解释**：延迟注销功能开关。  **约束限制**：不涉及  **取值范围**：true 开启，false 关闭。  **默认取值**：不涉及
        :type enable: bool
        :param timeout: **参数解释**：延迟注销时间。  **约束限制**：不涉及  **取值范围**：10~4000，单位：秒。  **默认取值**：不涉及
        :type timeout: int
        """
        
        

        self._enable = None
        self._timeout = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if timeout is not None:
            self.timeout = timeout

    @property
    def enable(self):
        r"""Gets the enable of this ConnectionDrain.

        **参数解释**：延迟注销功能开关。  **约束限制**：不涉及  **取值范围**：true 开启，false 关闭。  **默认取值**：不涉及

        :return: The enable of this ConnectionDrain.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ConnectionDrain.

        **参数解释**：延迟注销功能开关。  **约束限制**：不涉及  **取值范围**：true 开启，false 关闭。  **默认取值**：不涉及

        :param enable: The enable of this ConnectionDrain.
        :type enable: bool
        """
        self._enable = enable

    @property
    def timeout(self):
        r"""Gets the timeout of this ConnectionDrain.

        **参数解释**：延迟注销时间。  **约束限制**：不涉及  **取值范围**：10~4000，单位：秒。  **默认取值**：不涉及

        :return: The timeout of this ConnectionDrain.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ConnectionDrain.

        **参数解释**：延迟注销时间。  **约束限制**：不涉及  **取值范围**：10~4000，单位：秒。  **默认取值**：不涉及

        :param timeout: The timeout of this ConnectionDrain.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, ConnectionDrain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
