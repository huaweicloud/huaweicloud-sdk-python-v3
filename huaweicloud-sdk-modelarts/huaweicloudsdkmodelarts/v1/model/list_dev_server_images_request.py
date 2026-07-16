# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevServerImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_type': 'str',
        'flavor_name': 'str'
    }

    attribute_map = {
        'server_type': 'server_type',
        'flavor_name': 'flavor_name'
    }

    def __init__(self, server_type=None, flavor_name=None):
        r"""ListDevServerImagesRequest

        The model defined in huaweicloud sdk

        :param server_type: **参数解释**：server_type。 **约束限制**：不涉及。 **取值范围**：  - BMS  - ECS  - HPS **默认取值**：不涉及。
        :type server_type: str
        :param flavor_name: **参数解释**：规格名称。 **约束限制**：^.{1,128}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor_name: str
        """
        
        

        self._server_type = None
        self._flavor_name = None
        self.discriminator = None

        if server_type is not None:
            self.server_type = server_type
        if flavor_name is not None:
            self.flavor_name = flavor_name

    @property
    def server_type(self):
        r"""Gets the server_type of this ListDevServerImagesRequest.

        **参数解释**：server_type。 **约束限制**：不涉及。 **取值范围**：  - BMS  - ECS  - HPS **默认取值**：不涉及。

        :return: The server_type of this ListDevServerImagesRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ListDevServerImagesRequest.

        **参数解释**：server_type。 **约束限制**：不涉及。 **取值范围**：  - BMS  - ECS  - HPS **默认取值**：不涉及。

        :param server_type: The server_type of this ListDevServerImagesRequest.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this ListDevServerImagesRequest.

        **参数解释**：规格名称。 **约束限制**：^.{1,128}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor_name of this ListDevServerImagesRequest.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this ListDevServerImagesRequest.

        **参数解释**：规格名称。 **约束限制**：^.{1,128}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor_name: The flavor_name of this ListDevServerImagesRequest.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

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
        if not isinstance(other, ListDevServerImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
