# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyHttpResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'conditions': 'list[ConditionResp]',
        'backend_params': 'list[BackendParam]',
        'effect_mode': 'str',
        'authorizer_id': 'str',
        'url_domain': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'timeout': 'int',
        'enable_client_ssl': 'bool',
        'retry_count': 'str',
        'vpc_channel_info': 'VpcInfo',
        'vpc_channel_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'conditions': 'conditions',
        'backend_params': 'backend_params',
        'effect_mode': 'effect_mode',
        'authorizer_id': 'authorizer_id',
        'url_domain': 'url_domain',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'timeout': 'timeout',
        'enable_client_ssl': 'enable_client_ssl',
        'retry_count': 'retry_count',
        'vpc_channel_info': 'vpc_channel_info',
        'vpc_channel_status': 'vpc_channel_status'
    }

    def __init__(self, id=None, name=None, conditions=None, backend_params=None, effect_mode=None, authorizer_id=None, url_domain=None, req_protocol=None, req_method=None, req_uri=None, timeout=None, enable_client_ssl=None, retry_count=None, vpc_channel_info=None, vpc_channel_status=None):
        r"""ApiPolicyHttpResp

        The model defined in huaweicloud sdk

        :param id: 编号
        :type id: str
        :param name: 策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。
        :type name: str
        :param conditions: 策略条件列表
        :type conditions: list[:class:`huaweicloudsdkroma.v2.ConditionResp`]
        :param backend_params: 后端参数列表
        :type backend_params: list[:class:`huaweicloudsdkroma.v2.BackendParam`]
        :param effect_mode: 关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件
        :type effect_mode: str
        :param authorizer_id: 后端自定义认证对象的ID
        :type authorizer_id: str
        :param url_domain: 策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 
        :type url_domain: str
        :param req_protocol: 请求协议：HTTP、HTTPS
        :type req_protocol: str
        :param req_method: 请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  &gt; 需要服从URI规范。
        :type req_uri: str
        :param timeout: 服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。
        :type timeout: int
        :param enable_client_ssl: 是否开启双向认证
        :type enable_client_ssl: bool
        :param retry_count: 服务集成请求后端服务的重试次数，默认为-1，范围[-1,10]
        :type retry_count: str
        :param vpc_channel_info: 
        :type vpc_channel_info: :class:`huaweicloudsdkroma.v2.VpcInfo`
        :param vpc_channel_status: 是否使用VPC通道： - 1： 使用VPC通道 - 2：不使用VPC通道
        :type vpc_channel_status: int
        """
        
        

        self._id = None
        self._name = None
        self._conditions = None
        self._backend_params = None
        self._effect_mode = None
        self._authorizer_id = None
        self._url_domain = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._timeout = None
        self._enable_client_ssl = None
        self._retry_count = None
        self._vpc_channel_info = None
        self._vpc_channel_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.conditions = conditions
        if backend_params is not None:
            self.backend_params = backend_params
        self.effect_mode = effect_mode
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id
        if url_domain is not None:
            self.url_domain = url_domain
        self.req_protocol = req_protocol
        self.req_method = req_method
        self.req_uri = req_uri
        if timeout is not None:
            self.timeout = timeout
        if enable_client_ssl is not None:
            self.enable_client_ssl = enable_client_ssl
        if retry_count is not None:
            self.retry_count = retry_count
        if vpc_channel_info is not None:
            self.vpc_channel_info = vpc_channel_info
        if vpc_channel_status is not None:
            self.vpc_channel_status = vpc_channel_status

    @property
    def id(self):
        r"""Gets the id of this ApiPolicyHttpResp.

        编号

        :return: The id of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApiPolicyHttpResp.

        编号

        :param id: The id of this ApiPolicyHttpResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ApiPolicyHttpResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApiPolicyHttpResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyHttpResp.
        :type name: str
        """
        self._name = name

    @property
    def conditions(self):
        r"""Gets the conditions of this ApiPolicyHttpResp.

        策略条件列表

        :return: The conditions of this ApiPolicyHttpResp.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ConditionResp`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ApiPolicyHttpResp.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyHttpResp.
        :type conditions: list[:class:`huaweicloudsdkroma.v2.ConditionResp`]
        """
        self._conditions = conditions

    @property
    def backend_params(self):
        r"""Gets the backend_params of this ApiPolicyHttpResp.

        后端参数列表

        :return: The backend_params of this ApiPolicyHttpResp.
        :rtype: list[:class:`huaweicloudsdkroma.v2.BackendParam`]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        r"""Sets the backend_params of this ApiPolicyHttpResp.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyHttpResp.
        :type backend_params: list[:class:`huaweicloudsdkroma.v2.BackendParam`]
        """
        self._backend_params = backend_params

    @property
    def effect_mode(self):
        r"""Gets the effect_mode of this ApiPolicyHttpResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        r"""Sets the effect_mode of this ApiPolicyHttpResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyHttpResp.
        :type effect_mode: str
        """
        self._effect_mode = effect_mode

    @property
    def authorizer_id(self):
        r"""Gets the authorizer_id of this ApiPolicyHttpResp.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        r"""Sets the authorizer_id of this ApiPolicyHttpResp.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyHttpResp.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def url_domain(self):
        r"""Gets the url_domain of this ApiPolicyHttpResp.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :return: The url_domain of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        r"""Sets the url_domain of this ApiPolicyHttpResp.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :param url_domain: The url_domain of this ApiPolicyHttpResp.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this ApiPolicyHttpResp.

        请求协议：HTTP、HTTPS

        :return: The req_protocol of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this ApiPolicyHttpResp.

        请求协议：HTTP、HTTPS

        :param req_protocol: The req_protocol of this ApiPolicyHttpResp.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        r"""Gets the req_method of this ApiPolicyHttpResp.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :return: The req_method of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this ApiPolicyHttpResp.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :param req_method: The req_method of this ApiPolicyHttpResp.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        r"""Gets the req_uri of this ApiPolicyHttpResp.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :return: The req_uri of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        r"""Sets the req_uri of this ApiPolicyHttpResp.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :param req_uri: The req_uri of this ApiPolicyHttpResp.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def timeout(self):
        r"""Gets the timeout of this ApiPolicyHttpResp.

        服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。

        :return: The timeout of this ApiPolicyHttpResp.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ApiPolicyHttpResp.

        服务集成请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyHttpResp.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def enable_client_ssl(self):
        r"""Gets the enable_client_ssl of this ApiPolicyHttpResp.

        是否开启双向认证

        :return: The enable_client_ssl of this ApiPolicyHttpResp.
        :rtype: bool
        """
        return self._enable_client_ssl

    @enable_client_ssl.setter
    def enable_client_ssl(self, enable_client_ssl):
        r"""Sets the enable_client_ssl of this ApiPolicyHttpResp.

        是否开启双向认证

        :param enable_client_ssl: The enable_client_ssl of this ApiPolicyHttpResp.
        :type enable_client_ssl: bool
        """
        self._enable_client_ssl = enable_client_ssl

    @property
    def retry_count(self):
        r"""Gets the retry_count of this ApiPolicyHttpResp.

        服务集成请求后端服务的重试次数，默认为-1，范围[-1,10]

        :return: The retry_count of this ApiPolicyHttpResp.
        :rtype: str
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        r"""Sets the retry_count of this ApiPolicyHttpResp.

        服务集成请求后端服务的重试次数，默认为-1，范围[-1,10]

        :param retry_count: The retry_count of this ApiPolicyHttpResp.
        :type retry_count: str
        """
        self._retry_count = retry_count

    @property
    def vpc_channel_info(self):
        r"""Gets the vpc_channel_info of this ApiPolicyHttpResp.

        :return: The vpc_channel_info of this ApiPolicyHttpResp.
        :rtype: :class:`huaweicloudsdkroma.v2.VpcInfo`
        """
        return self._vpc_channel_info

    @vpc_channel_info.setter
    def vpc_channel_info(self, vpc_channel_info):
        r"""Sets the vpc_channel_info of this ApiPolicyHttpResp.

        :param vpc_channel_info: The vpc_channel_info of this ApiPolicyHttpResp.
        :type vpc_channel_info: :class:`huaweicloudsdkroma.v2.VpcInfo`
        """
        self._vpc_channel_info = vpc_channel_info

    @property
    def vpc_channel_status(self):
        r"""Gets the vpc_channel_status of this ApiPolicyHttpResp.

        是否使用VPC通道： - 1： 使用VPC通道 - 2：不使用VPC通道

        :return: The vpc_channel_status of this ApiPolicyHttpResp.
        :rtype: int
        """
        return self._vpc_channel_status

    @vpc_channel_status.setter
    def vpc_channel_status(self, vpc_channel_status):
        r"""Sets the vpc_channel_status of this ApiPolicyHttpResp.

        是否使用VPC通道： - 1： 使用VPC通道 - 2：不使用VPC通道

        :param vpc_channel_status: The vpc_channel_status of this ApiPolicyHttpResp.
        :type vpc_channel_status: int
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
        if not isinstance(other, ApiPolicyHttpResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
