# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandPreparationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num_node': 'int',
        'is_retry': 'bool'
    }

    attribute_map = {
        'num_node': 'num_node',
        'is_retry': 'is_retry'
    }

    def __init__(self, num_node=None, is_retry=None):
        r"""ExpandPreparationRequestBody

        The model defined in huaweicloud sdk

        :param num_node: **参数解释**： 扩容节点数。 **取值范围：** 大于等于3。
        :type num_node: int
        :param is_retry: **参数解释**： 是否是扩容准备重试。 **约束限制**： 不涉及。 **取值范围**： true：扩容准备重试； false：首次进行扩容准备； **默认取值**： false
        :type is_retry: bool
        """
        
        

        self._num_node = None
        self._is_retry = None
        self.discriminator = None

        self.num_node = num_node
        self.is_retry = is_retry

    @property
    def num_node(self):
        r"""Gets the num_node of this ExpandPreparationRequestBody.

        **参数解释**： 扩容节点数。 **取值范围：** 大于等于3。

        :return: The num_node of this ExpandPreparationRequestBody.
        :rtype: int
        """
        return self._num_node

    @num_node.setter
    def num_node(self, num_node):
        r"""Sets the num_node of this ExpandPreparationRequestBody.

        **参数解释**： 扩容节点数。 **取值范围：** 大于等于3。

        :param num_node: The num_node of this ExpandPreparationRequestBody.
        :type num_node: int
        """
        self._num_node = num_node

    @property
    def is_retry(self):
        r"""Gets the is_retry of this ExpandPreparationRequestBody.

        **参数解释**： 是否是扩容准备重试。 **约束限制**： 不涉及。 **取值范围**： true：扩容准备重试； false：首次进行扩容准备； **默认取值**： false

        :return: The is_retry of this ExpandPreparationRequestBody.
        :rtype: bool
        """
        return self._is_retry

    @is_retry.setter
    def is_retry(self, is_retry):
        r"""Sets the is_retry of this ExpandPreparationRequestBody.

        **参数解释**： 是否是扩容准备重试。 **约束限制**： 不涉及。 **取值范围**： true：扩容准备重试； false：首次进行扩容准备； **默认取值**： false

        :param is_retry: The is_retry of this ExpandPreparationRequestBody.
        :type is_retry: bool
        """
        self._is_retry = is_retry

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
        if not isinstance(other, ExpandPreparationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
