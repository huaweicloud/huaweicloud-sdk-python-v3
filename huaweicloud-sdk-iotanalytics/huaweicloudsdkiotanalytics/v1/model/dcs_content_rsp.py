# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DcsContentRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_service_id': 'str',
        'endpoint_service_name': 'str',
        'endpoint_ip': 'str',
        'port': 'int',
        'dcs_type': 'str',
        'password': 'str'
    }

    attribute_map = {
        'endpoint_service_id': 'endpointServiceId',
        'endpoint_service_name': 'endpointServiceName',
        'endpoint_ip': 'endpointIp',
        'port': 'port',
        'dcs_type': 'dcsType',
        'password': 'password'
    }

    def __init__(self, endpoint_service_id=None, endpoint_service_name=None, endpoint_ip=None, port=None, dcs_type=None, password=None):
        """DcsContentRsp

        The model defined in huaweicloud sdk

        :param endpoint_service_id: VPC-EP服务端id
        :type endpoint_service_id: str
        :param endpoint_service_name: VPC-EP服务端名称
        :type endpoint_service_name: str
        :param endpoint_ip: VPC-EP客户端IP
        :type endpoint_ip: str
        :param port: VPC-EP客户端Port
        :type port: int
        :param dcs_type: redis实例类型
        :type dcs_type: str
        :param password: redis访问密码
        :type password: str
        """
        
        

        self._endpoint_service_id = None
        self._endpoint_service_name = None
        self._endpoint_ip = None
        self._port = None
        self._dcs_type = None
        self._password = None
        self.discriminator = None

        if endpoint_service_id is not None:
            self.endpoint_service_id = endpoint_service_id
        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if endpoint_ip is not None:
            self.endpoint_ip = endpoint_ip
        if port is not None:
            self.port = port
        if dcs_type is not None:
            self.dcs_type = dcs_type
        if password is not None:
            self.password = password

    @property
    def endpoint_service_id(self):
        """Gets the endpoint_service_id of this DcsContentRsp.

        VPC-EP服务端id

        :return: The endpoint_service_id of this DcsContentRsp.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """Sets the endpoint_service_id of this DcsContentRsp.

        VPC-EP服务端id

        :param endpoint_service_id: The endpoint_service_id of this DcsContentRsp.
        :type endpoint_service_id: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this DcsContentRsp.

        VPC-EP服务端名称

        :return: The endpoint_service_name of this DcsContentRsp.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this DcsContentRsp.

        VPC-EP服务端名称

        :param endpoint_service_name: The endpoint_service_name of this DcsContentRsp.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def endpoint_ip(self):
        """Gets the endpoint_ip of this DcsContentRsp.

        VPC-EP客户端IP

        :return: The endpoint_ip of this DcsContentRsp.
        :rtype: str
        """
        return self._endpoint_ip

    @endpoint_ip.setter
    def endpoint_ip(self, endpoint_ip):
        """Sets the endpoint_ip of this DcsContentRsp.

        VPC-EP客户端IP

        :param endpoint_ip: The endpoint_ip of this DcsContentRsp.
        :type endpoint_ip: str
        """
        self._endpoint_ip = endpoint_ip

    @property
    def port(self):
        """Gets the port of this DcsContentRsp.

        VPC-EP客户端Port

        :return: The port of this DcsContentRsp.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DcsContentRsp.

        VPC-EP客户端Port

        :param port: The port of this DcsContentRsp.
        :type port: int
        """
        self._port = port

    @property
    def dcs_type(self):
        """Gets the dcs_type of this DcsContentRsp.

        redis实例类型

        :return: The dcs_type of this DcsContentRsp.
        :rtype: str
        """
        return self._dcs_type

    @dcs_type.setter
    def dcs_type(self, dcs_type):
        """Sets the dcs_type of this DcsContentRsp.

        redis实例类型

        :param dcs_type: The dcs_type of this DcsContentRsp.
        :type dcs_type: str
        """
        self._dcs_type = dcs_type

    @property
    def password(self):
        """Gets the password of this DcsContentRsp.

        redis访问密码

        :return: The password of this DcsContentRsp.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DcsContentRsp.

        redis访问密码

        :param password: The password of this DcsContentRsp.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, DcsContentRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
