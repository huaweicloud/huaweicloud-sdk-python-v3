# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeTypesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_types': 'list[NodeTypes]',
        'count': 'int'
    }

    attribute_map = {
        'node_types': 'node_types',
        'count': 'count'
    }

    def __init__(self, node_types=None, count=None):
        r"""ListNodeTypesResponse

        The model defined in huaweicloud sdk

        :param node_types: **参数解释**： 可用的规格列表。 **取值范围**： 非空对象列表。
        :type node_types: list[:class:`huaweicloudsdkdws.v2.NodeTypes`]
        :param count: **参数解释**： 规格总数 **取值范围**： 大于等于0的正整数。
        :type count: int
        """
        
        super(ListNodeTypesResponse, self).__init__()

        self._node_types = None
        self._count = None
        self.discriminator = None

        if node_types is not None:
            self.node_types = node_types
        if count is not None:
            self.count = count

    @property
    def node_types(self):
        r"""Gets the node_types of this ListNodeTypesResponse.

        **参数解释**： 可用的规格列表。 **取值范围**： 非空对象列表。

        :return: The node_types of this ListNodeTypesResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.NodeTypes`]
        """
        return self._node_types

    @node_types.setter
    def node_types(self, node_types):
        r"""Sets the node_types of this ListNodeTypesResponse.

        **参数解释**： 可用的规格列表。 **取值范围**： 非空对象列表。

        :param node_types: The node_types of this ListNodeTypesResponse.
        :type node_types: list[:class:`huaweicloudsdkdws.v2.NodeTypes`]
        """
        self._node_types = node_types

    @property
    def count(self):
        r"""Gets the count of this ListNodeTypesResponse.

        **参数解释**： 规格总数 **取值范围**： 大于等于0的正整数。

        :return: The count of this ListNodeTypesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListNodeTypesResponse.

        **参数解释**： 规格总数 **取值范围**： 大于等于0的正整数。

        :param count: The count of this ListNodeTypesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListNodeTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
