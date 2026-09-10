# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachDevServerPortRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'port_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'port_id': 'port_id'
    }

    def __init__(self, id=None, port_id=None):
        r"""DetachDevServerPortRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**：lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。
        :type id: str
        :param port_id: **参数解释**：要卸载的网卡ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。
        :type port_id: str
        """
        
        

        self._id = None
        self._port_id = None
        self.discriminator = None

        self.id = id
        self.port_id = port_id

    @property
    def id(self):
        r"""Gets the id of this DetachDevServerPortRequest.

        **参数解释**：lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :return: The id of this DetachDevServerPortRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DetachDevServerPortRequest.

        **参数解释**：lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :param id: The id of this DetachDevServerPortRequest.
        :type id: str
        """
        self._id = id

    @property
    def port_id(self):
        r"""Gets the port_id of this DetachDevServerPortRequest.

        **参数解释**：要卸载的网卡ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :return: The port_id of this DetachDevServerPortRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this DetachDevServerPortRequest.

        **参数解释**：要卸载的网卡ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :param port_id: The port_id of this DetachDevServerPortRequest.
        :type port_id: str
        """
        self._port_id = port_id

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
        if not isinstance(other, DetachDevServerPortRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
