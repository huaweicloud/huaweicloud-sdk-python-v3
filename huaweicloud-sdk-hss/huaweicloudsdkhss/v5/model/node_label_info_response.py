# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeLabelInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'children': 'list[str]'
    }

    attribute_map = {
        'label': 'label',
        'children': 'children'
    }

    def __init__(self, label=None, children=None):
        r"""NodeLabelInfoResponse

        The model defined in huaweicloud sdk

        :param label: **参数解释**: 节点标签名称。 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 
        :type label: str
        :param children: **参数解释**: 节点名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type children: list[str]
        """
        
        

        self._label = None
        self._children = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if children is not None:
            self.children = children

    @property
    def label(self):
        r"""Gets the label of this NodeLabelInfoResponse.

        **参数解释**: 节点标签名称。 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :return: The label of this NodeLabelInfoResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this NodeLabelInfoResponse.

        **参数解释**: 节点标签名称。 **约束限制**: 不涉及 **取值范围**: 字符长度0-512位 **默认取值**: 不涉及 

        :param label: The label of this NodeLabelInfoResponse.
        :type label: str
        """
        self._label = label

    @property
    def children(self):
        r"""Gets the children of this NodeLabelInfoResponse.

        **参数解释**: 节点名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The children of this NodeLabelInfoResponse.
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this NodeLabelInfoResponse.

        **参数解释**: 节点名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param children: The children of this NodeLabelInfoResponse.
        :type children: list[str]
        """
        self._children = children

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
        if not isinstance(other, NodeLabelInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
