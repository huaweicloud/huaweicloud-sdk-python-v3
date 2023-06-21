# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'protocol': 'str',
        'host': 'str',
        'timeout': 'int',
        'path': 'str',
        'backend_paras': 'list[BackendRequestPara]',
        'constant_paras': 'list[BackendConstant]'
    }

    attribute_map = {
        'type': 'type',
        'protocol': 'protocol',
        'host': 'host',
        'timeout': 'timeout',
        'path': 'path',
        'backend_paras': 'backend_paras',
        'constant_paras': 'constant_paras'
    }

    def __init__(self, type=None, protocol=None, host=None, timeout=None, path=None, backend_paras=None, constant_paras=None):
        """BackendConfig

        The model defined in huaweicloud sdk

        :param type: 后端请求类型
        :type type: str
        :param protocol: 后端请求协议类型
        :type protocol: str
        :param host: 后端host
        :type host: str
        :param timeout: 后端超时时间
        :type timeout: int
        :param path: 后端请求Path
        :type path: str
        :param backend_paras: API后端参数
        :type backend_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendRequestPara`]
        :param constant_paras: 后端常量参数
        :type constant_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendConstant`]
        """
        
        

        self._type = None
        self._protocol = None
        self._host = None
        self._timeout = None
        self._path = None
        self._backend_paras = None
        self._constant_paras = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if protocol is not None:
            self.protocol = protocol
        if host is not None:
            self.host = host
        if timeout is not None:
            self.timeout = timeout
        if path is not None:
            self.path = path
        if backend_paras is not None:
            self.backend_paras = backend_paras
        if constant_paras is not None:
            self.constant_paras = constant_paras

    @property
    def type(self):
        """Gets the type of this BackendConfig.

        后端请求类型

        :return: The type of this BackendConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackendConfig.

        后端请求类型

        :param type: The type of this BackendConfig.
        :type type: str
        """
        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this BackendConfig.

        后端请求协议类型

        :return: The protocol of this BackendConfig.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this BackendConfig.

        后端请求协议类型

        :param protocol: The protocol of this BackendConfig.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def host(self):
        """Gets the host of this BackendConfig.

        后端host

        :return: The host of this BackendConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this BackendConfig.

        后端host

        :param host: The host of this BackendConfig.
        :type host: str
        """
        self._host = host

    @property
    def timeout(self):
        """Gets the timeout of this BackendConfig.

        后端超时时间

        :return: The timeout of this BackendConfig.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this BackendConfig.

        后端超时时间

        :param timeout: The timeout of this BackendConfig.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def path(self):
        """Gets the path of this BackendConfig.

        后端请求Path

        :return: The path of this BackendConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BackendConfig.

        后端请求Path

        :param path: The path of this BackendConfig.
        :type path: str
        """
        self._path = path

    @property
    def backend_paras(self):
        """Gets the backend_paras of this BackendConfig.

        API后端参数

        :return: The backend_paras of this BackendConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendRequestPara`]
        """
        return self._backend_paras

    @backend_paras.setter
    def backend_paras(self, backend_paras):
        """Sets the backend_paras of this BackendConfig.

        API后端参数

        :param backend_paras: The backend_paras of this BackendConfig.
        :type backend_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendRequestPara`]
        """
        self._backend_paras = backend_paras

    @property
    def constant_paras(self):
        """Gets the constant_paras of this BackendConfig.

        后端常量参数

        :return: The constant_paras of this BackendConfig.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendConstant`]
        """
        return self._constant_paras

    @constant_paras.setter
    def constant_paras(self, constant_paras):
        """Sets the constant_paras of this BackendConfig.

        后端常量参数

        :param constant_paras: The constant_paras of this BackendConfig.
        :type constant_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.BackendConstant`]
        """
        self._constant_paras = constant_paras

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
        if not isinstance(other, BackendConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
