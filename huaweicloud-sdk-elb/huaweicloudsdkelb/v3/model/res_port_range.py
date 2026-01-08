# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResPortRange:

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
        r"""ResPortRange

        The model defined in huaweicloud sdk

        :param start_port: **参数解释**：起始端口。 **取值范围**：1-65535
        :type start_port: int
        :param end_port: **参数解释**：结束端口。 **取值范围**：1-65535
        :type end_port: int
        """
        
        

        self._start_port = None
        self._end_port = None
        self.discriminator = None

        self.start_port = start_port
        self.end_port = end_port

    @property
    def start_port(self):
        r"""Gets the start_port of this ResPortRange.

        **参数解释**：起始端口。 **取值范围**：1-65535

        :return: The start_port of this ResPortRange.
        :rtype: int
        """
        return self._start_port

    @start_port.setter
    def start_port(self, start_port):
        r"""Sets the start_port of this ResPortRange.

        **参数解释**：起始端口。 **取值范围**：1-65535

        :param start_port: The start_port of this ResPortRange.
        :type start_port: int
        """
        self._start_port = start_port

    @property
    def end_port(self):
        r"""Gets the end_port of this ResPortRange.

        **参数解释**：结束端口。 **取值范围**：1-65535

        :return: The end_port of this ResPortRange.
        :rtype: int
        """
        return self._end_port

    @end_port.setter
    def end_port(self, end_port):
        r"""Sets the end_port of this ResPortRange.

        **参数解释**：结束端口。 **取值范围**：1-65535

        :param end_port: The end_port of this ResPortRange.
        :type end_port: int
        """
        self._end_port = end_port

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
        if not isinstance(other, ResPortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
