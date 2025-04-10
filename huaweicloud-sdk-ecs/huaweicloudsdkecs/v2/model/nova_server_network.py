# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerNetwork:

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
        'uuid': 'str',
        'fixed_ip': 'str'
    }

    attribute_map = {
        'port': 'port',
        'uuid': 'uuid',
        'fixed_ip': 'fixed_ip'
    }

    def __init__(self, port=None, uuid=None, fixed_ip=None):
        r"""NovaServerNetwork

        The model defined in huaweicloud sdk

        :param port: 网络port uuid。  没有指定网络uuid时必须指定。
        :type port: str
        :param uuid: 网络uuid。  没有指定网络port时必须指定。
        :type uuid: str
        :param fixed_ip: 指定的IP地址。网络的三个参数（port、uuid和fixed_ip）中，port优先级最高；指定fixed_ip时必须指明uuid。
        :type fixed_ip: str
        """
        
        

        self._port = None
        self._uuid = None
        self._fixed_ip = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if uuid is not None:
            self.uuid = uuid
        if fixed_ip is not None:
            self.fixed_ip = fixed_ip

    @property
    def port(self):
        r"""Gets the port of this NovaServerNetwork.

        网络port uuid。  没有指定网络uuid时必须指定。

        :return: The port of this NovaServerNetwork.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this NovaServerNetwork.

        网络port uuid。  没有指定网络uuid时必须指定。

        :param port: The port of this NovaServerNetwork.
        :type port: str
        """
        self._port = port

    @property
    def uuid(self):
        r"""Gets the uuid of this NovaServerNetwork.

        网络uuid。  没有指定网络port时必须指定。

        :return: The uuid of this NovaServerNetwork.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this NovaServerNetwork.

        网络uuid。  没有指定网络port时必须指定。

        :param uuid: The uuid of this NovaServerNetwork.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def fixed_ip(self):
        r"""Gets the fixed_ip of this NovaServerNetwork.

        指定的IP地址。网络的三个参数（port、uuid和fixed_ip）中，port优先级最高；指定fixed_ip时必须指明uuid。

        :return: The fixed_ip of this NovaServerNetwork.
        :rtype: str
        """
        return self._fixed_ip

    @fixed_ip.setter
    def fixed_ip(self, fixed_ip):
        r"""Sets the fixed_ip of this NovaServerNetwork.

        指定的IP地址。网络的三个参数（port、uuid和fixed_ip）中，port优先级最高；指定fixed_ip时必须指明uuid。

        :param fixed_ip: The fixed_ip of this NovaServerNetwork.
        :type fixed_ip: str
        """
        self._fixed_ip = fixed_ip

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
        if not isinstance(other, NovaServerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
