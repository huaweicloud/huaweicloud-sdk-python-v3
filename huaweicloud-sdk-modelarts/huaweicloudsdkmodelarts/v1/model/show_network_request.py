# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_name': 'str'
    }

    attribute_map = {
        'network_name': 'network_name'
    }

    def __init__(self, network_name=None):
        r"""ShowNetworkRequest

        The model defined in huaweicloud sdk

        :param network_name: **参数解释**：网络的ID，取值自网络详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type network_name: str
        """
        
        

        self._network_name = None
        self.discriminator = None

        self.network_name = network_name

    @property
    def network_name(self):
        r"""Gets the network_name of this ShowNetworkRequest.

        **参数解释**：网络的ID，取值自网络详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The network_name of this ShowNetworkRequest.
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        r"""Sets the network_name of this ShowNetworkRequest.

        **参数解释**：网络的ID，取值自网络详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为[36-63]个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param network_name: The network_name of this ShowNetworkRequest.
        :type network_name: str
        """
        self._network_name = network_name

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
        if not isinstance(other, ShowNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
