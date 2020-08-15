# coding: utf-8

import pprint
import re

import six





class BackendApiBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authorizer_id': 'str',
        'url_domain': 'str',
        'req_protocol': 'str',
        'remark': 'str',
        'req_method': 'str',
        'version': 'str',
        'req_uri': 'str',
        'timeout': 'int',
        'id': 'str',
        'status': 'int',
        'register_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'authorizer_id': 'authorizer_id',
        'url_domain': 'url_domain',
        'req_protocol': 'req_protocol',
        'remark': 'remark',
        'req_method': 'req_method',
        'version': 'version',
        'req_uri': 'req_uri',
        'timeout': 'timeout',
        'id': 'id',
        'status': 'status',
        'register_time': 'register_time',
        'update_time': 'update_time'
    }

    def __init__(self, authorizer_id=None, url_domain=None, req_protocol=None, remark=None, req_method=None, version=None, req_uri=None, timeout=None, id=None, status=None, register_time=None, update_time=None):
        """BackendApiBase - a model defined in huaweicloud sdk"""
        
        

        self._authorizer_id = None
        self._url_domain = None
        self._req_protocol = None
        self._remark = None
        self._req_method = None
        self._version = None
        self._req_uri = None
        self._timeout = None
        self._id = None
        self._status = None
        self._register_time = None
        self._update_time = None
        self.discriminator = None

        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if url_domain is not None:
            self.url_domain = url_domain
        self.req_protocol = req_protocol
        if remark is not None:
            self.remark = remark
        self.req_method = req_method
        if version is not None:
            self.version = version
        self.req_uri = req_uri
        self.timeout = timeout
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if register_time is not None:
            self.register_time = register_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this BackendApiBase.

        后端自定义认证对象的ID

        :return: The authorizer_id of this BackendApiBase.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this BackendApiBase.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this BackendApiBase.
        :type: str
        """
        self._authorizer_id = authorizer_id

    @property
    def url_domain(self):
        """Gets the url_domain of this BackendApiBase.

        后端服务的地址。  由主机（IP或域名）和端口号组成，总长度不超过255。格式为主机:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443，HTTP默认端口号为80。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、下划线、中划线组成，且只能以英文开头

        :return: The url_domain of this BackendApiBase.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this BackendApiBase.

        后端服务的地址。  由主机（IP或域名）和端口号组成，总长度不超过255。格式为主机:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443，HTTP默认端口号为80。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、下划线、中划线组成，且只能以英文开头

        :param url_domain: The url_domain of this BackendApiBase.
        :type: str
        """
        self._url_domain = url_domain

    @property
    def req_protocol(self):
        """Gets the req_protocol of this BackendApiBase.

        请求协议

        :return: The req_protocol of this BackendApiBase.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this BackendApiBase.

        请求协议

        :param req_protocol: The req_protocol of this BackendApiBase.
        :type: str
        """
        self._req_protocol = req_protocol

    @property
    def remark(self):
        """Gets the remark of this BackendApiBase.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this BackendApiBase.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackendApiBase.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this BackendApiBase.
        :type: str
        """
        self._remark = remark

    @property
    def req_method(self):
        """Gets the req_method of this BackendApiBase.

        请求方式

        :return: The req_method of this BackendApiBase.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this BackendApiBase.

        请求方式

        :param req_method: The req_method of this BackendApiBase.
        :type: str
        """
        self._req_method = req_method

    @property
    def version(self):
        """Gets the version of this BackendApiBase.

        web后端版本，字符长度不超过16

        :return: The version of this BackendApiBase.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BackendApiBase.

        web后端版本，字符长度不超过16

        :param version: The version of this BackendApiBase.
        :type: str
        """
        self._version = version

    @property
    def req_uri(self):
        """Gets the req_uri of this BackendApiBase.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :return: The req_uri of this BackendApiBase.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this BackendApiBase.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :param req_uri: The req_uri of this BackendApiBase.
        :type: str
        """
        self._req_uri = req_uri

    @property
    def timeout(self):
        """Gets the timeout of this BackendApiBase.

        API网关请求后端服务的超时时间。  单位：毫秒。请求参数值不在合法范围内时将使用默认值

        :return: The timeout of this BackendApiBase.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this BackendApiBase.

        API网关请求后端服务的超时时间。  单位：毫秒。请求参数值不在合法范围内时将使用默认值

        :param timeout: The timeout of this BackendApiBase.
        :type: int
        """
        self._timeout = timeout

    @property
    def id(self):
        """Gets the id of this BackendApiBase.

        编号

        :return: The id of this BackendApiBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackendApiBase.

        编号

        :param id: The id of this BackendApiBase.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this BackendApiBase.

        状态

        :return: The status of this BackendApiBase.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackendApiBase.

        状态

        :param status: The status of this BackendApiBase.
        :type: int
        """
        self._status = status

    @property
    def register_time(self):
        """Gets the register_time of this BackendApiBase.

        注册时间

        :return: The register_time of this BackendApiBase.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this BackendApiBase.

        注册时间

        :param register_time: The register_time of this BackendApiBase.
        :type: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        """Gets the update_time of this BackendApiBase.

        修改时间

        :return: The update_time of this BackendApiBase.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BackendApiBase.

        修改时间

        :param update_time: The update_time of this BackendApiBase.
        :type: datetime
        """
        self._update_time = update_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackendApiBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
