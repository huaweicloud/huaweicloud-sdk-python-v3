# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendParamBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'location': 'str',
        'origin': 'str',
        'value': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'origin': 'origin',
        'value': 'value',
        'remark': 'remark'
    }

    def __init__(self, name=None, location=None, origin=None, value=None, remark=None):
        """BackendParamBase

        The model defined in huaweicloud sdk

        :param name: 参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 
        :type name: str
        :param location: 参数位置：PATH、QUERY、HEADER
        :type location: str
        :param origin: 参数类别：REQUEST、CONSTANT、SYSTEM
        :type origin: str
        :param value: 参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiName: API的名称 - $context.apiId：API的ID - $context.appName: API调用者的APP对象名称 - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成跟踪ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用 - $context.clientCertCN：开启客户端认证时，本次API调用携带的客户端证书CN  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa
        :type value: str
        :param remark: 描述。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        """
        
        

        self._name = None
        self._location = None
        self._origin = None
        self._value = None
        self._remark = None
        self.discriminator = None

        self.name = name
        self.location = location
        self.origin = origin
        self.value = value
        if remark is not None:
            self.remark = remark

    @property
    def name(self):
        """Gets the name of this BackendParamBase.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :return: The name of this BackendParamBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendParamBase.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :param name: The name of this BackendParamBase.
        :type name: str
        """
        self._name = name

    @property
    def location(self):
        """Gets the location of this BackendParamBase.

        参数位置：PATH、QUERY、HEADER

        :return: The location of this BackendParamBase.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BackendParamBase.

        参数位置：PATH、QUERY、HEADER

        :param location: The location of this BackendParamBase.
        :type location: str
        """
        self._location = location

    @property
    def origin(self):
        """Gets the origin of this BackendParamBase.

        参数类别：REQUEST、CONSTANT、SYSTEM

        :return: The origin of this BackendParamBase.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BackendParamBase.

        参数类别：REQUEST、CONSTANT、SYSTEM

        :param origin: The origin of this BackendParamBase.
        :type origin: str
        """
        self._origin = origin

    @property
    def value(self):
        """Gets the value of this BackendParamBase.

        参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiName: API的名称 - $context.apiId：API的ID - $context.appName: API调用者的APP对象名称 - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成跟踪ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用 - $context.clientCertCN：开启客户端认证时，本次API调用携带的客户端证书CN  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa

        :return: The value of this BackendParamBase.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BackendParamBase.

        参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiName: API的名称 - $context.apiId：API的ID - $context.appName: API调用者的APP对象名称 - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成跟踪ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用 - $context.clientCertCN：开启客户端认证时，本次API调用携带的客户端证书CN  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa

        :param value: The value of this BackendParamBase.
        :type value: str
        """
        self._value = value

    @property
    def remark(self):
        """Gets the remark of this BackendParamBase.

        描述。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this BackendParamBase.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackendParamBase.

        描述。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this BackendParamBase.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, BackendParamBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
