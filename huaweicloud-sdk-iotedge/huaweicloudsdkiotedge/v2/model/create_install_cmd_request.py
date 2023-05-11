# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstallCmdRequest:

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
        'arch': 'str',
        'body': 'CreateInstallCmdRequestDTO'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'arch': 'arch',
        'body': 'body'
    }

    def __init__(self, edge_node_id=None, arch=None, body=None):
        """CreateInstallCmdRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param arch: 节点架构
        :type arch: str
        :param body: Body of the CreateInstallCmdRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.CreateInstallCmdRequestDTO`
        """
        
        

        self._edge_node_id = None
        self._arch = None
        self._body = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.arch = arch
        if body is not None:
            self.body = body

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this CreateInstallCmdRequest.

        边缘节点ID

        :return: The edge_node_id of this CreateInstallCmdRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this CreateInstallCmdRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this CreateInstallCmdRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def arch(self):
        """Gets the arch of this CreateInstallCmdRequest.

        节点架构

        :return: The arch of this CreateInstallCmdRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateInstallCmdRequest.

        节点架构

        :param arch: The arch of this CreateInstallCmdRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def body(self):
        """Gets the body of this CreateInstallCmdRequest.

        :return: The body of this CreateInstallCmdRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateInstallCmdRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateInstallCmdRequest.

        :param body: The body of this CreateInstallCmdRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.CreateInstallCmdRequestDTO`
        """
        self._body = body

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
        if not isinstance(other, CreateInstallCmdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
