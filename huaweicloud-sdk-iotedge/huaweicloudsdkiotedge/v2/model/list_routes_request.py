# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRoutesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_node_id': 'str',
        'parsed': 'bool'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'parsed': 'parsed'
    }

    def __init__(self, edge_node_id=None, parsed=None):
        """ListRoutesRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param parsed: 是否解析路由
        :type parsed: bool
        """
        
        

        self._edge_node_id = None
        self._parsed = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        if parsed is not None:
            self.parsed = parsed

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this ListRoutesRequest.

        边缘节点ID

        :return: The edge_node_id of this ListRoutesRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this ListRoutesRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this ListRoutesRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def parsed(self):
        """Gets the parsed of this ListRoutesRequest.

        是否解析路由

        :return: The parsed of this ListRoutesRequest.
        :rtype: bool
        """
        return self._parsed

    @parsed.setter
    def parsed(self, parsed):
        """Sets the parsed of this ListRoutesRequest.

        是否解析路由

        :param parsed: The parsed of this ListRoutesRequest.
        :type parsed: bool
        """
        self._parsed = parsed

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
        if not isinstance(other, ListRoutesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
