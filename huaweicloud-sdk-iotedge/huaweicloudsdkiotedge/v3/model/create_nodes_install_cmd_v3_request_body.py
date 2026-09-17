# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodesInstallCmdV3RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_info': 'list[NodeConfig]'
    }

    attribute_map = {
        'node_info': 'node_info'
    }

    def __init__(self, node_info=None):
        r"""CreateNodesInstallCmdV3RequestBody

        The model defined in huaweicloud sdk

        :param node_info: 集群节点名称列表
        :type node_info: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        
        

        self._node_info = None
        self.discriminator = None

        if node_info is not None:
            self.node_info = node_info

    @property
    def node_info(self):
        r"""Gets the node_info of this CreateNodesInstallCmdV3RequestBody.

        集群节点名称列表

        :return: The node_info of this CreateNodesInstallCmdV3RequestBody.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        r"""Sets the node_info of this CreateNodesInstallCmdV3RequestBody.

        集群节点名称列表

        :param node_info: The node_info of this CreateNodesInstallCmdV3RequestBody.
        :type node_info: list[:class:`huaweicloudsdkiotedge.v3.NodeConfig`]
        """
        self._node_info = node_info

    def to_dict(self):
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
        if not isinstance(other, CreateNodesInstallCmdV3RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
