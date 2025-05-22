# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecUpdateNodeNameTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name_prefix': 'str',
        'node_name_suffix': 'str'
    }

    attribute_map = {
        'node_name_prefix': 'nodeNamePrefix',
        'node_name_suffix': 'nodeNameSuffix'
    }

    def __init__(self, node_name_prefix=None, node_name_suffix=None):
        r"""NodeSpecUpdateNodeNameTemplate

        The model defined in huaweicloud sdk

        :param node_name_prefix: **参数解释**： 节点名称前缀。如果用户填写为空串或缺省，则节点名称不会增加前缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type node_name_prefix: str
        :param node_name_suffix: **参数解释**： 节点名称后缀。如果用户填写为空串或缺省，则节点名称不会增加后缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type node_name_suffix: str
        """
        
        

        self._node_name_prefix = None
        self._node_name_suffix = None
        self.discriminator = None

        if node_name_prefix is not None:
            self.node_name_prefix = node_name_prefix
        if node_name_suffix is not None:
            self.node_name_suffix = node_name_suffix

    @property
    def node_name_prefix(self):
        r"""Gets the node_name_prefix of this NodeSpecUpdateNodeNameTemplate.

        **参数解释**： 节点名称前缀。如果用户填写为空串或缺省，则节点名称不会增加前缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The node_name_prefix of this NodeSpecUpdateNodeNameTemplate.
        :rtype: str
        """
        return self._node_name_prefix

    @node_name_prefix.setter
    def node_name_prefix(self, node_name_prefix):
        r"""Sets the node_name_prefix of this NodeSpecUpdateNodeNameTemplate.

        **参数解释**： 节点名称前缀。如果用户填写为空串或缺省，则节点名称不会增加前缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param node_name_prefix: The node_name_prefix of this NodeSpecUpdateNodeNameTemplate.
        :type node_name_prefix: str
        """
        self._node_name_prefix = node_name_prefix

    @property
    def node_name_suffix(self):
        r"""Gets the node_name_suffix of this NodeSpecUpdateNodeNameTemplate.

        **参数解释**： 节点名称后缀。如果用户填写为空串或缺省，则节点名称不会增加后缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The node_name_suffix of this NodeSpecUpdateNodeNameTemplate.
        :rtype: str
        """
        return self._node_name_suffix

    @node_name_suffix.setter
    def node_name_suffix(self, node_name_suffix):
        r"""Sets the node_name_suffix of this NodeSpecUpdateNodeNameTemplate.

        **参数解释**： 节点名称后缀。如果用户填写为空串或缺省，则节点名称不会增加后缀。 **约束限制**： 仅支持小写字母、数字、连字符（-）和点（.），必须以小写字母开头。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param node_name_suffix: The node_name_suffix of this NodeSpecUpdateNodeNameTemplate.
        :type node_name_suffix: str
        """
        self._node_name_suffix = node_name_suffix

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
        if not isinstance(other, NodeSpecUpdateNodeNameTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
