# coding: utf-8

import pprint
import re

import six





class ApiPolicyHttpCreate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url_domain': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'timeout': 'int',
        'effect_mode': 'str',
        'name': 'str',
        'backend_params': 'list[BackendParamBase]',
        'conditions': 'list[ApiConditionBase]',
        'authorizer_id': 'str',
        'vpc_channel_info': 'ApiBackendVpcReq',
        'vpc_channel_status': 'int'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'timeout': 'timeout',
        'effect_mode': 'effect_mode',
        'name': 'name',
        'backend_params': 'backend_params',
        'conditions': 'conditions',
        'authorizer_id': 'authorizer_id',
        'vpc_channel_info': 'vpc_channel_info',
        'vpc_channel_status': 'vpc_channel_status'
    }

    def __init__(self, url_domain=None, req_protocol=None, req_method=None, req_uri=None, timeout=None, effect_mode=None, name=None, backend_params=None, conditions=None, authorizer_id=None, vpc_channel_info=None, vpc_channel_status=None):
        """ApiPolicyHttpCreate - a model defined in huaweicloud sdk"""
        
        

        self._url_domain = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._timeout = None
        self._effect_mode = None
        self._name = None
        self._backend_params = None
        self._conditions = None
        self._authorizer_id = None
        self._vpc_channel_info = None
        self._vpc_channel_status = None
        self.discriminator = None

        if url_domain is not None:
            self.url_domain = url_domain
        self.req_protocol = req_protocol
        self.req_method = req_method
        self.req_uri = req_uri
        if timeout is not None:
            self.timeout = timeout
        self.effect_mode = effect_mode
        self.name = name
        if backend_params is not None:
            self.backend_params = backend_params
        self.conditions = conditions
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if vpc_channel_info is not None:
            self.vpc_channel_info = vpc_channel_info
        if vpc_channel_status is not None:
            self.vpc_channel_status = vpc_channel_status

    @property
    def url_domain(self):
        """Gets the url_domain of this ApiPolicyHttpCreate.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :return: The url_domain of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this ApiPolicyHttpCreate.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :param url_domain: The url_domain of this ApiPolicyHttpCreate.
        :type: str
        """
        self._url_domain = url_domain

    @property
    def req_protocol(self):
        """Gets the req_protocol of this ApiPolicyHttpCreate.

        请求协议：HTTP、HTTPS

        :return: The req_protocol of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this ApiPolicyHttpCreate.

        请求协议：HTTP、HTTPS

        :param req_protocol: The req_protocol of this ApiPolicyHttpCreate.
        :type: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this ApiPolicyHttpCreate.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :return: The req_method of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ApiPolicyHttpCreate.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :param req_method: The req_method of this ApiPolicyHttpCreate.
        :type: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiPolicyHttpCreate.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :return: The req_uri of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiPolicyHttpCreate.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :param req_uri: The req_uri of this ApiPolicyHttpCreate.
        :type: str
        """
        self._req_uri = req_uri

    @property
    def timeout(self):
        """Gets the timeout of this ApiPolicyHttpCreate.

        API网关请求后端服务的超时时间。  单位：毫秒。

        :return: The timeout of this ApiPolicyHttpCreate.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiPolicyHttpCreate.

        API网关请求后端服务的超时时间。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyHttpCreate.
        :type: int
        """
        self._timeout = timeout

    @property
    def effect_mode(self):
        """Gets the effect_mode of this ApiPolicyHttpCreate.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        """Sets the effect_mode of this ApiPolicyHttpCreate.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyHttpCreate.
        :type: str
        """
        self._effect_mode = effect_mode

    @property
    def name(self):
        """Gets the name of this ApiPolicyHttpCreate.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPolicyHttpCreate.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyHttpCreate.
        :type: str
        """
        self._name = name

    @property
    def backend_params(self):
        """Gets the backend_params of this ApiPolicyHttpCreate.

        后端参数列表

        :return: The backend_params of this ApiPolicyHttpCreate.
        :rtype: list[BackendParamBase]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ApiPolicyHttpCreate.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyHttpCreate.
        :type: list[BackendParamBase]
        """
        self._backend_params = backend_params

    @property
    def conditions(self):
        """Gets the conditions of this ApiPolicyHttpCreate.

        策略条件列表

        :return: The conditions of this ApiPolicyHttpCreate.
        :rtype: list[ApiConditionBase]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiPolicyHttpCreate.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyHttpCreate.
        :type: list[ApiConditionBase]
        """
        self._conditions = conditions

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiPolicyHttpCreate.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyHttpCreate.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiPolicyHttpCreate.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyHttpCreate.
        :type: str
        """
        self._authorizer_id = authorizer_id

    @property
    def vpc_channel_info(self):
        """Gets the vpc_channel_info of this ApiPolicyHttpCreate.


        :return: The vpc_channel_info of this ApiPolicyHttpCreate.
        :rtype: ApiBackendVpcReq
        """
        return self._vpc_channel_info

    @vpc_channel_info.setter
    def vpc_channel_info(self, vpc_channel_info):
        """Sets the vpc_channel_info of this ApiPolicyHttpCreate.


        :param vpc_channel_info: The vpc_channel_info of this ApiPolicyHttpCreate.
        :type: ApiBackendVpcReq
        """
        self._vpc_channel_info = vpc_channel_info

    @property
    def vpc_channel_status(self):
        """Gets the vpc_channel_status of this ApiPolicyHttpCreate.

        是否使用VPC通道 - 1 : 使用VPC通道 - 2 : 不使用VPC通道

        :return: The vpc_channel_status of this ApiPolicyHttpCreate.
        :rtype: int
        """
        return self._vpc_channel_status

    @vpc_channel_status.setter
    def vpc_channel_status(self, vpc_channel_status):
        """Sets the vpc_channel_status of this ApiPolicyHttpCreate.

        是否使用VPC通道 - 1 : 使用VPC通道 - 2 : 不使用VPC通道

        :param vpc_channel_status: The vpc_channel_status of this ApiPolicyHttpCreate.
        :type: int
        """
        self._vpc_channel_status = vpc_channel_status

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
        if not isinstance(other, ApiPolicyHttpCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
