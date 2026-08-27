# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicNetworkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_network_type': 'str'
    }

    attribute_map = {
        'public_network_type': 'public_network_type'
    }

    def __init__(self, public_network_type=None):
        r"""PublicNetworkConfig

        The model defined in huaweicloud sdk

        :param public_network_type: **参数解释**：NoteBook网络类型 **约束限制**： - SHARED：公共网络 - EXCLUSIVE：专属网络 - FORBIDDEN：禁用网络
        :type public_network_type: str
        """
        
        

        self._public_network_type = None
        self.discriminator = None

        if public_network_type is not None:
            self.public_network_type = public_network_type

    @property
    def public_network_type(self):
        r"""Gets the public_network_type of this PublicNetworkConfig.

        **参数解释**：NoteBook网络类型 **约束限制**： - SHARED：公共网络 - EXCLUSIVE：专属网络 - FORBIDDEN：禁用网络

        :return: The public_network_type of this PublicNetworkConfig.
        :rtype: str
        """
        return self._public_network_type

    @public_network_type.setter
    def public_network_type(self, public_network_type):
        r"""Sets the public_network_type of this PublicNetworkConfig.

        **参数解释**：NoteBook网络类型 **约束限制**： - SHARED：公共网络 - EXCLUSIVE：专属网络 - FORBIDDEN：禁用网络

        :param public_network_type: The public_network_type of this PublicNetworkConfig.
        :type public_network_type: str
        """
        self._public_network_type = public_network_type

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
        if not isinstance(other, PublicNetworkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
