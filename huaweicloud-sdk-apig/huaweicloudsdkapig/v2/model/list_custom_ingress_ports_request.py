# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomIngressPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'protocol': 'str',
        'ingress_port': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'protocol': 'protocol',
        'ingress_port': 'ingress_port'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, protocol=None, ingress_port=None):
        """ListCustomIngressPortsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param protocol: 入方向端口的请求协议。 - HTTP: 入方向端口为HTTP协议。 - HTTPS: 入方向端口为HTTPS协议。 
        :type protocol: str
        :param ingress_port: 入方向端口的端口号，支持的端口范围为1024~49151。
        :type ingress_port: int
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._protocol = None
        self._ingress_port = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if protocol is not None:
            self.protocol = protocol
        if ingress_port is not None:
            self.ingress_port = ingress_port

    @property
    def instance_id(self):
        """Gets the instance_id of this ListCustomIngressPortsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListCustomIngressPortsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListCustomIngressPortsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListCustomIngressPortsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListCustomIngressPortsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListCustomIngressPortsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomIngressPortsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListCustomIngressPortsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCustomIngressPortsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListCustomIngressPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomIngressPortsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListCustomIngressPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def protocol(self):
        """Gets the protocol of this ListCustomIngressPortsRequest.

        入方向端口的请求协议。 - HTTP: 入方向端口为HTTP协议。 - HTTPS: 入方向端口为HTTPS协议。 

        :return: The protocol of this ListCustomIngressPortsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListCustomIngressPortsRequest.

        入方向端口的请求协议。 - HTTP: 入方向端口为HTTP协议。 - HTTPS: 入方向端口为HTTPS协议。 

        :param protocol: The protocol of this ListCustomIngressPortsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ingress_port(self):
        """Gets the ingress_port of this ListCustomIngressPortsRequest.

        入方向端口的端口号，支持的端口范围为1024~49151。

        :return: The ingress_port of this ListCustomIngressPortsRequest.
        :rtype: int
        """
        return self._ingress_port

    @ingress_port.setter
    def ingress_port(self, ingress_port):
        """Sets the ingress_port of this ListCustomIngressPortsRequest.

        入方向端口的端口号，支持的端口范围为1024~49151。

        :param ingress_port: The ingress_port of this ListCustomIngressPortsRequest.
        :type ingress_port: int
        """
        self._ingress_port = ingress_port

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
        if not isinstance(other, ListCustomIngressPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
