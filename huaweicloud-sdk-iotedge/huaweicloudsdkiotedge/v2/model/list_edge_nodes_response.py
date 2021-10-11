# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeNodesResponse(SdkResponse):


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
        'page_info': 'PageInfoDTO',
        'nodes': 'list[EdgeNodeDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'nodes': 'nodes'
    }

    def __init__(self, count=None, page_info=None, nodes=None):
        """ListEdgeNodesResponse - a model defined in huaweicloud sdk"""
        
        super(ListEdgeNodesResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._nodes = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if nodes is not None:
            self.nodes = nodes

    @property
    def count(self):
        """Gets the count of this ListEdgeNodesResponse.

        总记录数

        :return: The count of this ListEdgeNodesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListEdgeNodesResponse.

        总记录数

        :param count: The count of this ListEdgeNodesResponse.
        :type: int
        """
        self._count = count

    @property
    def page_info(self):
        """Gets the page_info of this ListEdgeNodesResponse.


        :return: The page_info of this ListEdgeNodesResponse.
        :rtype: PageInfoDTO
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListEdgeNodesResponse.


        :param page_info: The page_info of this ListEdgeNodesResponse.
        :type: PageInfoDTO
        """
        self._page_info = page_info

    @property
    def nodes(self):
        """Gets the nodes of this ListEdgeNodesResponse.

        节点列表

        :return: The nodes of this ListEdgeNodesResponse.
        :rtype: list[EdgeNodeDTO]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ListEdgeNodesResponse.

        节点列表

        :param nodes: The nodes of this ListEdgeNodesResponse.
        :type: list[EdgeNodeDTO]
        """
        self._nodes = nodes

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
        if not isinstance(other, ListEdgeNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
