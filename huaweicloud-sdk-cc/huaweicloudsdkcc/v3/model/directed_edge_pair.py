# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectedEdgePair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_pair': 'list[DirectedEdge]'
    }

    attribute_map = {
        'edge_pair': 'edge_pair'
    }

    def __init__(self, edge_pair=None):
        r"""DirectedEdgePair

        The model defined in huaweicloud sdk

        :param edge_pair: 分支网络连接的两个端点定义，长度固定为2的数组。
        :type edge_pair: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        """
        
        

        self._edge_pair = None
        self.discriminator = None

        self.edge_pair = edge_pair

    @property
    def edge_pair(self):
        r"""Gets the edge_pair of this DirectedEdgePair.

        分支网络连接的两个端点定义，长度固定为2的数组。

        :return: The edge_pair of this DirectedEdgePair.
        :rtype: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        """
        return self._edge_pair

    @edge_pair.setter
    def edge_pair(self, edge_pair):
        r"""Sets the edge_pair of this DirectedEdgePair.

        分支网络连接的两个端点定义，长度固定为2的数组。

        :param edge_pair: The edge_pair of this DirectedEdgePair.
        :type edge_pair: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        """
        self._edge_pair = edge_pair

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
        if not isinstance(other, DirectedEdgePair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
