# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str',
        'status': 'str',
        'node_id': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'port': 'port',
        'status': 'status',
        'node_id': 'node_id',
        'ip': 'ip'
    }

    def __init__(self, port=None, status=None, node_id=None, ip=None):
        r"""NodeList

        The model defined in huaweicloud sdk

        :param port: 端口。
        :type port: str
        :param status: 节点状态。
        :type status: str
        :param node_id: 节点id。
        :type node_id: str
        :param ip: ip
        :type ip: str
        """
        
        

        self._port = None
        self._status = None
        self._node_id = None
        self._ip = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if status is not None:
            self.status = status
        if node_id is not None:
            self.node_id = node_id
        if ip is not None:
            self.ip = ip

    @property
    def port(self):
        r"""Gets the port of this NodeList.

        端口。

        :return: The port of this NodeList.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this NodeList.

        端口。

        :param port: The port of this NodeList.
        :type port: str
        """
        self._port = port

    @property
    def status(self):
        r"""Gets the status of this NodeList.

        节点状态。

        :return: The status of this NodeList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeList.

        节点状态。

        :param status: The status of this NodeList.
        :type status: str
        """
        self._status = status

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeList.

        节点id。

        :return: The node_id of this NodeList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeList.

        节点id。

        :param node_id: The node_id of this NodeList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ip(self):
        r"""Gets the ip of this NodeList.

        ip

        :return: The ip of this NodeList.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this NodeList.

        ip

        :param ip: The ip of this NodeList.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, NodeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
