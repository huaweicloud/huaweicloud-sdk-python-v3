# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_port': 'int',
        'end_port': 'int'
    }

    attribute_map = {
        'start_port': 'start_port',
        'end_port': 'end_port'
    }

    def __init__(self, start_port=None, end_port=None):
        r"""PortRange

        The model defined in huaweicloud sdk

        :param start_port: **参数解释**：起始端口。  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及
        :type start_port: int
        :param end_port: **参数解释**：结束端口，需大于等于起始端口  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及
        :type end_port: int
        """
        
        

        self._start_port = None
        self._end_port = None
        self.discriminator = None

        if start_port is not None:
            self.start_port = start_port
        if end_port is not None:
            self.end_port = end_port

    @property
    def start_port(self):
        r"""Gets the start_port of this PortRange.

        **参数解释**：起始端口。  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及

        :return: The start_port of this PortRange.
        :rtype: int
        """
        return self._start_port

    @start_port.setter
    def start_port(self, start_port):
        r"""Sets the start_port of this PortRange.

        **参数解释**：起始端口。  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及

        :param start_port: The start_port of this PortRange.
        :type start_port: int
        """
        self._start_port = start_port

    @property
    def end_port(self):
        r"""Gets the end_port of this PortRange.

        **参数解释**：结束端口，需大于等于起始端口  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及

        :return: The end_port of this PortRange.
        :rtype: int
        """
        return self._end_port

    @end_port.setter
    def end_port(self, end_port):
        r"""Sets the end_port of this PortRange.

        **参数解释**：结束端口，需大于等于起始端口  **约束限制**：不涉及  **取值范围**：1-65535  **默认取值：不涉及

        :param end_port: The end_port of this PortRange.
        :type end_port: int
        """
        self._end_port = end_port

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
        if not isinstance(other, PortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
