# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReadonlyNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_distribution': 'list[NodeDistributionOption]'
    }

    attribute_map = {
        'node_distribution': 'node_distribution'
    }

    def __init__(self, node_distribution=None):
        r"""CreateReadonlyNodesRequestBody

        The model defined in huaweicloud sdk

        :param node_distribution: **参数解释**: 新创建只读节点在各可用区的分布情况。 **约束限制**: 不涉及。
        :type node_distribution: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeDistributionOption`]
        """
        
        

        self._node_distribution = None
        self.discriminator = None

        self.node_distribution = node_distribution

    @property
    def node_distribution(self):
        r"""Gets the node_distribution of this CreateReadonlyNodesRequestBody.

        **参数解释**: 新创建只读节点在各可用区的分布情况。 **约束限制**: 不涉及。

        :return: The node_distribution of this CreateReadonlyNodesRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeDistributionOption`]
        """
        return self._node_distribution

    @node_distribution.setter
    def node_distribution(self, node_distribution):
        r"""Sets the node_distribution of this CreateReadonlyNodesRequestBody.

        **参数解释**: 新创建只读节点在各可用区的分布情况。 **约束限制**: 不涉及。

        :param node_distribution: The node_distribution of this CreateReadonlyNodesRequestBody.
        :type node_distribution: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.NodeDistributionOption`]
        """
        self._node_distribution = node_distribution

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
        if not isinstance(other, CreateReadonlyNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
