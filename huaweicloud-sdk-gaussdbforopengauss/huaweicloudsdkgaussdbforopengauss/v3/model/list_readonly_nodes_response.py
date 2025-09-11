# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReadonlyNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[ListReadonlyNodesResult]',
        'max_readonly_node_num': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'max_readonly_node_num': 'max_readonly_node_num'
    }

    def __init__(self, instances=None, max_readonly_node_num=None):
        r"""ListReadonlyNodesResponse

        The model defined in huaweicloud sdk

        :param instances: **参数解释**: 只读节点列表。 **约束限制**: 不涉及。
        :type instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        :param max_readonly_node_num: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type max_readonly_node_num: int
        """
        
        super(ListReadonlyNodesResponse, self).__init__()

        self._instances = None
        self._max_readonly_node_num = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if max_readonly_node_num is not None:
            self.max_readonly_node_num = max_readonly_node_num

    @property
    def instances(self):
        r"""Gets the instances of this ListReadonlyNodesResponse.

        **参数解释**: 只读节点列表。 **约束限制**: 不涉及。

        :return: The instances of this ListReadonlyNodesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListReadonlyNodesResponse.

        **参数解释**: 只读节点列表。 **约束限制**: 不涉及。

        :param instances: The instances of this ListReadonlyNodesResponse.
        :type instances: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListReadonlyNodesResult`]
        """
        self._instances = instances

    @property
    def max_readonly_node_num(self):
        r"""Gets the max_readonly_node_num of this ListReadonlyNodesResponse.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The max_readonly_node_num of this ListReadonlyNodesResponse.
        :rtype: int
        """
        return self._max_readonly_node_num

    @max_readonly_node_num.setter
    def max_readonly_node_num(self, max_readonly_node_num):
        r"""Sets the max_readonly_node_num of this ListReadonlyNodesResponse.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param max_readonly_node_num: The max_readonly_node_num of this ListReadonlyNodesResponse.
        :type max_readonly_node_num: int
        """
        self._max_readonly_node_num = max_readonly_node_num

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
        if not isinstance(other, ListReadonlyNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
