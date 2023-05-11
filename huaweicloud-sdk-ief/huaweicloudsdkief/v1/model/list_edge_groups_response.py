# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeGroupsResponse(SdkResponse):

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
        'edge_groups': 'list[EdgeGroupResp]'
    }

    attribute_map = {
        'count': 'count',
        'edge_groups': 'edge_groups'
    }

    def __init__(self, count=None, edge_groups=None):
        """ListEdgeGroupsResponse

        The model defined in huaweicloud sdk

        :param count: 边缘节点组数目
        :type count: int
        :param edge_groups: 边缘节点组详情
        :type edge_groups: list[:class:`huaweicloudsdkief.v1.EdgeGroupResp`]
        """
        
        super(ListEdgeGroupsResponse, self).__init__()

        self._count = None
        self._edge_groups = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if edge_groups is not None:
            self.edge_groups = edge_groups

    @property
    def count(self):
        """Gets the count of this ListEdgeGroupsResponse.

        边缘节点组数目

        :return: The count of this ListEdgeGroupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListEdgeGroupsResponse.

        边缘节点组数目

        :param count: The count of this ListEdgeGroupsResponse.
        :type count: int
        """
        self._count = count

    @property
    def edge_groups(self):
        """Gets the edge_groups of this ListEdgeGroupsResponse.

        边缘节点组详情

        :return: The edge_groups of this ListEdgeGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.EdgeGroupResp`]
        """
        return self._edge_groups

    @edge_groups.setter
    def edge_groups(self, edge_groups):
        """Sets the edge_groups of this ListEdgeGroupsResponse.

        边缘节点组详情

        :param edge_groups: The edge_groups of this ListEdgeGroupsResponse.
        :type edge_groups: list[:class:`huaweicloudsdkief.v1.EdgeGroupResp`]
        """
        self._edge_groups = edge_groups

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
        if not isinstance(other, ListEdgeGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
