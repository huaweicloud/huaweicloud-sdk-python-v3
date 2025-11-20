# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDetailfNodesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'port': 'str',
        'ip': 'str',
        'group_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'port': 'port',
        'ip': 'ip',
        'group_id': 'group_id',
        'node_id': 'node_id'
    }

    def __init__(self, status=None, port=None, ip=None, group_id=None, node_id=None):
        r"""GetDetailfNodesInfo

        The model defined in huaweicloud sdk

        :param status: DDM实例节点状态。
        :type status: str
        :param port: DDM实例节点port。
        :type port: str
        :param ip: DDM实例节点IP。
        :type ip: str
        :param group_id: 节点所在组ID。
        :type group_id: str
        :param node_id: 节点ID。
        :type node_id: str
        """
        
        

        self._status = None
        self._port = None
        self._ip = None
        self._group_id = None
        self._node_id = None
        self.discriminator = None

        self.status = status
        self.port = port
        self.ip = ip
        self.group_id = group_id
        self.node_id = node_id

    @property
    def status(self):
        r"""Gets the status of this GetDetailfNodesInfo.

        DDM实例节点状态。

        :return: The status of this GetDetailfNodesInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetDetailfNodesInfo.

        DDM实例节点状态。

        :param status: The status of this GetDetailfNodesInfo.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this GetDetailfNodesInfo.

        DDM实例节点port。

        :return: The port of this GetDetailfNodesInfo.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this GetDetailfNodesInfo.

        DDM实例节点port。

        :param port: The port of this GetDetailfNodesInfo.
        :type port: str
        """
        self._port = port

    @property
    def ip(self):
        r"""Gets the ip of this GetDetailfNodesInfo.

        DDM实例节点IP。

        :return: The ip of this GetDetailfNodesInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this GetDetailfNodesInfo.

        DDM实例节点IP。

        :param ip: The ip of this GetDetailfNodesInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def group_id(self):
        r"""Gets the group_id of this GetDetailfNodesInfo.

        节点所在组ID。

        :return: The group_id of this GetDetailfNodesInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GetDetailfNodesInfo.

        节点所在组ID。

        :param group_id: The group_id of this GetDetailfNodesInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def node_id(self):
        r"""Gets the node_id of this GetDetailfNodesInfo.

        节点ID。

        :return: The node_id of this GetDetailfNodesInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this GetDetailfNodesInfo.

        节点ID。

        :param node_id: The node_id of this GetDetailfNodesInfo.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, GetDetailfNodesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
