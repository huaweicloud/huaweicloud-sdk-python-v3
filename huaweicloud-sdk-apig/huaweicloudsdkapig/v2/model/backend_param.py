# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin': 'str',
        'name': 'str',
        'remark': 'str',
        'location': 'str',
        'value': 'str',
        'id': 'str',
        'req_param_id': 'str'
    }

    attribute_map = {
        'origin': 'origin',
        'name': 'name',
        'remark': 'remark',
        'location': 'location',
        'value': 'value',
        'id': 'id',
        'req_param_id': 'req_param_id'
    }

    def __init__(self, origin=None, name=None, remark=None, location=None, value=None, id=None, req_param_id=None):
        """BackendParam

        The model defined in huaweicloud sdk

        :param origin: 参数类别：   - 后端服务参数：REQUEST   - 常量参数：CONSTANT   - 系统参数：SYSTEM
        :type origin: str
        :param name: 参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 
        :type name: str
        :param remark: 描述。字符长度不超过255 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param location: 参数位置：PATH、QUERY、HEADER
        :type location: str
        :param value: 参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiId：API的ID - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成请求ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa
        :type value: str
        :param id: 参数编号
        :type id: str
        :param req_param_id: 对应的请求参数编号
        :type req_param_id: str
        """
        
        

        self._origin = None
        self._name = None
        self._remark = None
        self._location = None
        self._value = None
        self._id = None
        self._req_param_id = None
        self.discriminator = None

        self.origin = origin
        self.name = name
        if remark is not None:
            self.remark = remark
        self.location = location
        self.value = value
        if id is not None:
            self.id = id
        if req_param_id is not None:
            self.req_param_id = req_param_id

    @property
    def origin(self):
        """Gets the origin of this BackendParam.

        参数类别：   - 后端服务参数：REQUEST   - 常量参数：CONSTANT   - 系统参数：SYSTEM

        :return: The origin of this BackendParam.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this BackendParam.

        参数类别：   - 后端服务参数：REQUEST   - 常量参数：CONSTANT   - 系统参数：SYSTEM

        :param origin: The origin of this BackendParam.
        :type origin: str
        """
        self._origin = origin

    @property
    def name(self):
        """Gets the name of this BackendParam.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :return: The name of this BackendParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackendParam.

        参数名称。 字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :param name: The name of this BackendParam.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this BackendParam.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this BackendParam.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackendParam.

        描述。字符长度不超过255 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this BackendParam.
        :type remark: str
        """
        self._remark = remark

    @property
    def location(self):
        """Gets the location of this BackendParam.

        参数位置：PATH、QUERY、HEADER

        :return: The location of this BackendParam.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this BackendParam.

        参数位置：PATH、QUERY、HEADER

        :param location: The location of this BackendParam.
        :type location: str
        """
        self._location = location

    @property
    def value(self):
        """Gets the value of this BackendParam.

        参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiId：API的ID - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成请求ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa

        :return: The value of this BackendParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BackendParam.

        参数值。字符长度不超过255 origin类别为REQUEST时，此字段值为req_params中的参数名称；  origin类别为CONSTANT时，此字段值为参数真正的值；  origin类别为SYSTEM时，此字段值为系统参数名称，系统参数分为网关内置参数、前端认证参数和后端认证参数，当api前端安全认证方式为自定义认证时，可以填写前端认证参数，当api开启后端认证时，可以填写后端认证参数。  网关内置参数取值及对应含义： - $context.sourceIp：API调用者的源地址 - $context.stage：API调用的部署环境 - $context.apiId：API的ID - $context.appId：API调用者的APP对象ID - $context.requestId：当次API调用生成请求ID - $context.serverAddr：网关的服务器地址 - $context.serverName：网关的服务器名称 - $context.handleTime：本次API调用的处理时间 - $context.providerAppId：API拥有者的应用对象ID，暂不支持使用  前端认证参数取值：以“$context.authorizer.frontend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.frontend.aaa  后端认证参数取值：以“$context.authorizer.backend.”为前缀，如希望自定义认证校验通过返回的参数为aaa，那么此字段填写为$context.authorizer.backend.aaa

        :param value: The value of this BackendParam.
        :type value: str
        """
        self._value = value

    @property
    def id(self):
        """Gets the id of this BackendParam.

        参数编号

        :return: The id of this BackendParam.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackendParam.

        参数编号

        :param id: The id of this BackendParam.
        :type id: str
        """
        self._id = id

    @property
    def req_param_id(self):
        """Gets the req_param_id of this BackendParam.

        对应的请求参数编号

        :return: The req_param_id of this BackendParam.
        :rtype: str
        """
        return self._req_param_id

    @req_param_id.setter
    def req_param_id(self, req_param_id):
        """Sets the req_param_id of this BackendParam.

        对应的请求参数编号

        :param req_param_id: The req_param_id of this BackendParam.
        :type req_param_id: str
        """
        self._req_param_id = req_param_id

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
        if not isinstance(other, BackendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
