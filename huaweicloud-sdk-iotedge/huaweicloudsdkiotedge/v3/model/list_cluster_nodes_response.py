# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[QueryNodeResp]'
    }

    attribute_map = {
        'nodes': 'nodes'
    }

    def __init__(self, nodes=None):
        r"""ListClusterNodesResponse

        The model defined in huaweicloud sdk

        :param nodes: 节点列表
        :type nodes: list[:class:`huaweicloudsdkiotedge.v3.QueryNodeResp`]
        """
        
        super().__init__()

        self._nodes = None
        self.discriminator = None

        if nodes is not None:
            self.nodes = nodes

    @property
    def nodes(self):
        r"""Gets the nodes of this ListClusterNodesResponse.

        节点列表

        :return: The nodes of this ListClusterNodesResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.QueryNodeResp`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ListClusterNodesResponse.

        节点列表

        :param nodes: The nodes of this ListClusterNodesResponse.
        :type nodes: list[:class:`huaweicloudsdkiotedge.v3.QueryNodeResp`]
        """
        self._nodes = nodes

    def to_dict(self):
        import warnings
        warnings.warn("ListClusterNodesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListClusterNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
