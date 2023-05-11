# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2xEdgesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'edges': 'list[V2XEdgeListResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'edges': 'edges'
    }

    def __init__(self, count=None, edges=None):
        """ListV2xEdgesResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：总数。
        :type count: int
        :param edges: **参数说明**：数据列表。
        :type edges: list[:class:`huaweicloudsdkdris.v1.V2XEdgeListResponseDTO`]
        """
        
        super(ListV2xEdgesResponse, self).__init__()

        self._count = None
        self._edges = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if edges is not None:
            self.edges = edges

    @property
    def count(self):
        """Gets the count of this ListV2xEdgesResponse.

        **参数说明**：总数。

        :return: The count of this ListV2xEdgesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListV2xEdgesResponse.

        **参数说明**：总数。

        :param count: The count of this ListV2xEdgesResponse.
        :type count: int
        """
        self._count = count

    @property
    def edges(self):
        """Gets the edges of this ListV2xEdgesResponse.

        **参数说明**：数据列表。

        :return: The edges of this ListV2xEdgesResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.V2XEdgeListResponseDTO`]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this ListV2xEdgesResponse.

        **参数说明**：数据列表。

        :param edges: The edges of this ListV2xEdgesResponse.
        :type edges: list[:class:`huaweicloudsdkdris.v1.V2XEdgeListResponseDTO`]
        """
        self._edges = edges

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
        if not isinstance(other, ListV2xEdgesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
