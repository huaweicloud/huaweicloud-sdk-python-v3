# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSubNetworkInterfaceTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_network_interface_id': 'str',
        'tag_key': 'str'
    }

    attribute_map = {
        'sub_network_interface_id': 'sub_network_interface_id',
        'tag_key': 'tag_key'
    }

    def __init__(self, sub_network_interface_id=None, tag_key=None):
        r"""DeleteSubNetworkInterfaceTagRequest

        The model defined in huaweicloud sdk

        :param sub_network_interface_id: **参数解释**： 辅助弹性网卡唯一标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type sub_network_interface_id: str
        :param tag_key: **参数解释**： 标签键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type tag_key: str
        """
        
        

        self._sub_network_interface_id = None
        self._tag_key = None
        self.discriminator = None

        self.sub_network_interface_id = sub_network_interface_id
        self.tag_key = tag_key

    @property
    def sub_network_interface_id(self):
        r"""Gets the sub_network_interface_id of this DeleteSubNetworkInterfaceTagRequest.

        **参数解释**： 辅助弹性网卡唯一标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The sub_network_interface_id of this DeleteSubNetworkInterfaceTagRequest.
        :rtype: str
        """
        return self._sub_network_interface_id

    @sub_network_interface_id.setter
    def sub_network_interface_id(self, sub_network_interface_id):
        r"""Sets the sub_network_interface_id of this DeleteSubNetworkInterfaceTagRequest.

        **参数解释**： 辅助弹性网卡唯一标识。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param sub_network_interface_id: The sub_network_interface_id of this DeleteSubNetworkInterfaceTagRequest.
        :type sub_network_interface_id: str
        """
        self._sub_network_interface_id = sub_network_interface_id

    @property
    def tag_key(self):
        r"""Gets the tag_key of this DeleteSubNetworkInterfaceTagRequest.

        **参数解释**： 标签键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The tag_key of this DeleteSubNetworkInterfaceTagRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this DeleteSubNetworkInterfaceTagRequest.

        **参数解释**： 标签键。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param tag_key: The tag_key of this DeleteSubNetworkInterfaceTagRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

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
        if not isinstance(other, DeleteSubNetworkInterfaceTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
