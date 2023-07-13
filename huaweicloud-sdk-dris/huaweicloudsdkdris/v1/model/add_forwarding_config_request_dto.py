# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddForwardingConfigRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'forwarding_type': 'str',
        'forwarding_config': 'ForwardingConfigRequestDTO'
    }

    attribute_map = {
        'forwarding_type': 'forwarding_type',
        'forwarding_config': 'forwarding_config'
    }

    def __init__(self, forwarding_type=None, forwarding_config=None):
        """AddForwardingConfigRequestDTO

        The model defined in huaweicloud sdk

        :param forwarding_type: **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。
        :type forwarding_type: str
        :param forwarding_config: 
        :type forwarding_config: :class:`huaweicloudsdkdris.v1.ForwardingConfigRequestDTO`
        """
        
        

        self._forwarding_type = None
        self._forwarding_config = None
        self.discriminator = None

        self.forwarding_type = forwarding_type
        self.forwarding_config = forwarding_config

    @property
    def forwarding_type(self):
        """Gets the forwarding_type of this AddForwardingConfigRequestDTO.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :return: The forwarding_type of this AddForwardingConfigRequestDTO.
        :rtype: str
        """
        return self._forwarding_type

    @forwarding_type.setter
    def forwarding_type(self, forwarding_type):
        """Sets the forwarding_type of this AddForwardingConfigRequestDTO.

        **参数说明**：转发配置的类型。  **取值范围**：当前仅支持“kafka，mrskafka”。

        :param forwarding_type: The forwarding_type of this AddForwardingConfigRequestDTO.
        :type forwarding_type: str
        """
        self._forwarding_type = forwarding_type

    @property
    def forwarding_config(self):
        """Gets the forwarding_config of this AddForwardingConfigRequestDTO.

        :return: The forwarding_config of this AddForwardingConfigRequestDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ForwardingConfigRequestDTO`
        """
        return self._forwarding_config

    @forwarding_config.setter
    def forwarding_config(self, forwarding_config):
        """Sets the forwarding_config of this AddForwardingConfigRequestDTO.

        :param forwarding_config: The forwarding_config of this AddForwardingConfigRequestDTO.
        :type forwarding_config: :class:`huaweicloudsdkdris.v1.ForwardingConfigRequestDTO`
        """
        self._forwarding_config = forwarding_config

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
        if not isinstance(other, AddForwardingConfigRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
