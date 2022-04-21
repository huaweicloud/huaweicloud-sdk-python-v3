# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssociateNaToNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nodes': 'list[QueryAuthorizedNodeDTO]'
    }

    attribute_map = {
        'nodes': 'nodes'
    }

    def __init__(self, nodes=None):
        """BatchAssociateNaToNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: 授权北向NA信息到边缘节点列表的返回结构体，仅返回本次授权的节点列表信息
        :type nodes: list[:class:`huaweicloudsdkiotedge.v2.QueryAuthorizedNodeDTO`]
        """
        
        super(BatchAssociateNaToNodesResponse, self).__init__()

        self._nodes = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes

    @property
    def nodes(self):
        """Gets the nodes of this BatchAssociateNaToNodesResponse.

        授权北向NA信息到边缘节点列表的返回结构体，仅返回本次授权的节点列表信息

        :return: The nodes of this BatchAssociateNaToNodesResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.QueryAuthorizedNodeDTO`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this BatchAssociateNaToNodesResponse.

        授权北向NA信息到边缘节点列表的返回结构体，仅返回本次授权的节点列表信息

        :param nodes: The nodes of this BatchAssociateNaToNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkiotedge.v2.QueryAuthorizedNodeDTO`]
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
        if not isinstance(other, BatchAssociateNaToNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
