# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClusterNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_list': 'list[str]',
        'operate_type': 'str'
    }

    attribute_map = {
        'node_list': 'node_list',
        'operate_type': 'operate_type'
    }

    def __init__(self, node_list=None, operate_type=None):
        r"""DeleteClusterNodesRequestBody

        The model defined in huaweicloud sdk

        :param node_list: **参数解释**： 空闲节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_list: list[str]
        :param operate_type: **参数解释**： 操作类型，一般传delete即可。 **约束限制**： 不涉及。 **取值范围**： clear：清理创建失败的空闲节点 delete：删除空闲节点 **默认取值**： 不涉及。
        :type operate_type: str
        """
        
        

        self._node_list = None
        self._operate_type = None
        self.discriminator = None

        self.node_list = node_list
        self.operate_type = operate_type

    @property
    def node_list(self):
        r"""Gets the node_list of this DeleteClusterNodesRequestBody.

        **参数解释**： 空闲节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_list of this DeleteClusterNodesRequestBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this DeleteClusterNodesRequestBody.

        **参数解释**： 空闲节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_list: The node_list of this DeleteClusterNodesRequestBody.
        :type node_list: list[str]
        """
        self._node_list = node_list

    @property
    def operate_type(self):
        r"""Gets the operate_type of this DeleteClusterNodesRequestBody.

        **参数解释**： 操作类型，一般传delete即可。 **约束限制**： 不涉及。 **取值范围**： clear：清理创建失败的空闲节点 delete：删除空闲节点 **默认取值**： 不涉及。

        :return: The operate_type of this DeleteClusterNodesRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this DeleteClusterNodesRequestBody.

        **参数解释**： 操作类型，一般传delete即可。 **约束限制**： 不涉及。 **取值范围**： clear：清理创建失败的空闲节点 delete：删除空闲节点 **默认取值**： 不涉及。

        :param operate_type: The operate_type of this DeleteClusterNodesRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, DeleteClusterNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
