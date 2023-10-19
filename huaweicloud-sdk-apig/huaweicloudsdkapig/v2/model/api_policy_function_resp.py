# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyFunctionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'invocation_type': 'str',
        'network_type': 'str',
        'version': 'str',
        'alias_urn': 'str',
        'timeout': 'int',
        'id': 'str',
        'effect_mode': 'str',
        'name': 'str',
        'backend_params': 'list[BackendParam]',
        'conditions': 'list[CoditionResp]',
        'authorizer_id': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'invocation_type': 'invocation_type',
        'network_type': 'network_type',
        'version': 'version',
        'alias_urn': 'alias_urn',
        'timeout': 'timeout',
        'id': 'id',
        'effect_mode': 'effect_mode',
        'name': 'name',
        'backend_params': 'backend_params',
        'conditions': 'conditions',
        'authorizer_id': 'authorizer_id'
    }

    def __init__(self, function_urn=None, invocation_type=None, network_type=None, version=None, alias_urn=None, timeout=None, id=None, effect_mode=None, name=None, backend_params=None, conditions=None, authorizer_id=None):
        """ApiPolicyFunctionResp

        The model defined in huaweicloud sdk

        :param function_urn: 函数URN
        :type function_urn: str
        :param invocation_type: 调用类型 - async： 异步 - sync：同步
        :type invocation_type: str
        :param network_type: 对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构
        :type network_type: str
        :param version: 函数版本  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN
        :type version: str
        :param alias_urn: 函数别名URN  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN
        :type alias_urn: str
        :param timeout: API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。
        :type timeout: int
        :param id: 编号
        :type id: str
        :param effect_mode: 关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件
        :type effect_mode: str
        :param name: 策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。
        :type name: str
        :param backend_params: 后端参数列表
        :type backend_params: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        :param conditions: 策略条件列表
        :type conditions: list[:class:`huaweicloudsdkapig.v2.CoditionResp`]
        :param authorizer_id: 后端自定义认证对象的ID
        :type authorizer_id: str
        """
        
        

        self._function_urn = None
        self._invocation_type = None
        self._network_type = None
        self._version = None
        self._alias_urn = None
        self._timeout = None
        self._id = None
        self._effect_mode = None
        self._name = None
        self._backend_params = None
        self._conditions = None
        self._authorizer_id = None
        self.discriminator = None

        self.function_urn = function_urn
        self.invocation_type = invocation_type
        self.network_type = network_type
        if version is not None:
            self.version = version
        if alias_urn is not None:
            self.alias_urn = alias_urn
        if timeout is not None:
            self.timeout = timeout
        if id is not None:
            self.id = id
        self.effect_mode = effect_mode
        self.name = name
        if backend_params is not None:
            self.backend_params = backend_params
        self.conditions = conditions
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id

    @property
    def function_urn(self):
        """Gets the function_urn of this ApiPolicyFunctionResp.

        函数URN

        :return: The function_urn of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ApiPolicyFunctionResp.

        函数URN

        :param function_urn: The function_urn of this ApiPolicyFunctionResp.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def invocation_type(self):
        """Gets the invocation_type of this ApiPolicyFunctionResp.

        调用类型 - async： 异步 - sync：同步

        :return: The invocation_type of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        """Sets the invocation_type of this ApiPolicyFunctionResp.

        调用类型 - async： 异步 - sync：同步

        :param invocation_type: The invocation_type of this ApiPolicyFunctionResp.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def network_type(self):
        """Gets the network_type of this ApiPolicyFunctionResp.

        对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构

        :return: The network_type of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this ApiPolicyFunctionResp.

        对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构

        :param network_type: The network_type of this ApiPolicyFunctionResp.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def version(self):
        """Gets the version of this ApiPolicyFunctionResp.

        函数版本  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :return: The version of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiPolicyFunctionResp.

        函数版本  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :param version: The version of this ApiPolicyFunctionResp.
        :type version: str
        """
        self._version = version

    @property
    def alias_urn(self):
        """Gets the alias_urn of this ApiPolicyFunctionResp.

        函数别名URN  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :return: The alias_urn of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._alias_urn

    @alias_urn.setter
    def alias_urn(self, alias_urn):
        """Sets the alias_urn of this ApiPolicyFunctionResp.

        函数别名URN  当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :param alias_urn: The alias_urn of this ApiPolicyFunctionResp.
        :type alias_urn: str
        """
        self._alias_urn = alias_urn

    @property
    def timeout(self):
        """Gets the timeout of this ApiPolicyFunctionResp.

        API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this ApiPolicyFunctionResp.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiPolicyFunctionResp.

        API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyFunctionResp.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def id(self):
        """Gets the id of this ApiPolicyFunctionResp.

        编号

        :return: The id of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiPolicyFunctionResp.

        编号

        :param id: The id of this ApiPolicyFunctionResp.
        :type id: str
        """
        self._id = id

    @property
    def effect_mode(self):
        """Gets the effect_mode of this ApiPolicyFunctionResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        """Sets the effect_mode of this ApiPolicyFunctionResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyFunctionResp.
        :type effect_mode: str
        """
        self._effect_mode = effect_mode

    @property
    def name(self):
        """Gets the name of this ApiPolicyFunctionResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPolicyFunctionResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyFunctionResp.
        :type name: str
        """
        self._name = name

    @property
    def backend_params(self):
        """Gets the backend_params of this ApiPolicyFunctionResp.

        后端参数列表

        :return: The backend_params of this ApiPolicyFunctionResp.
        :rtype: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ApiPolicyFunctionResp.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyFunctionResp.
        :type backend_params: list[:class:`huaweicloudsdkapig.v2.BackendParam`]
        """
        self._backend_params = backend_params

    @property
    def conditions(self):
        """Gets the conditions of this ApiPolicyFunctionResp.

        策略条件列表

        :return: The conditions of this ApiPolicyFunctionResp.
        :rtype: list[:class:`huaweicloudsdkapig.v2.CoditionResp`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiPolicyFunctionResp.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyFunctionResp.
        :type conditions: list[:class:`huaweicloudsdkapig.v2.CoditionResp`]
        """
        self._conditions = conditions

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiPolicyFunctionResp.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyFunctionResp.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiPolicyFunctionResp.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyFunctionResp.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

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
        if not isinstance(other, ApiPolicyFunctionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
