# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponsesInfo:

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
        'responses': 'dict(str, ResponseInfoResp)',
        'id': 'str',
        'default': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'responses': 'responses',
        'id': 'id',
        'default': 'default',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, name=None, responses=None, id=None, default=None, create_time=None, update_time=None):
        r"""ResponsesInfo

        The model defined in huaweicloud sdk

        :param name: 响应名称
        :type name: str
        :param responses: 错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: When the token verification mode is used for OIDC authentication, the token verification fails. - OIDC_AUTH_GET_DISCOVERY_ERROR: During OIDC authentication, the IDP service is unavailable or the network is unreachable. As a result, information cannot be obtained from the configured discovery. - OIDC_AUTH_CODE_FLOW_FAIL: When a browser is used for OIDC authentication, the authorization code processing fails. - JWT_AUTH_FAILURE: The JWT authentication plug-in fails to verify the token. - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体
        :type responses: dict(str, ResponseInfoResp)
        :param id: 响应ID
        :type id: str
        :param default: 是否为分组默认响应
        :type default: bool
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 修改时间
        :type update_time: datetime
        """
        
        

        self._name = None
        self._responses = None
        self._id = None
        self._default = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if responses is not None:
            self.responses = responses
        if id is not None:
            self.id = id
        if default is not None:
            self.default = default
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def name(self):
        r"""Gets the name of this ResponsesInfo.

        响应名称

        :return: The name of this ResponsesInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResponsesInfo.

        响应名称

        :param name: The name of this ResponsesInfo.
        :type name: str
        """
        self._name = name

    @property
    def responses(self):
        r"""Gets the responses of this ResponsesInfo.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: When the token verification mode is used for OIDC authentication, the token verification fails. - OIDC_AUTH_GET_DISCOVERY_ERROR: During OIDC authentication, the IDP service is unavailable or the network is unreachable. As a result, information cannot be obtained from the configured discovery. - OIDC_AUTH_CODE_FLOW_FAIL: When a browser is used for OIDC authentication, the authorization code processing fails. - JWT_AUTH_FAILURE: The JWT authentication plug-in fails to verify the token. - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体

        :return: The responses of this ResponsesInfo.
        :rtype: dict(str, ResponseInfoResp)
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        r"""Sets the responses of this ResponsesInfo.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: When the token verification mode is used for OIDC authentication, the token verification fails. - OIDC_AUTH_GET_DISCOVERY_ERROR: During OIDC authentication, the IDP service is unavailable or the network is unreachable. As a result, information cannot be obtained from the configured discovery. - OIDC_AUTH_CODE_FLOW_FAIL: When a browser is used for OIDC authentication, the authorization code processing fails. - JWT_AUTH_FAILURE: The JWT authentication plug-in fails to verify the token. - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体

        :param responses: The responses of this ResponsesInfo.
        :type responses: dict(str, ResponseInfoResp)
        """
        self._responses = responses

    @property
    def id(self):
        r"""Gets the id of this ResponsesInfo.

        响应ID

        :return: The id of this ResponsesInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResponsesInfo.

        响应ID

        :param id: The id of this ResponsesInfo.
        :type id: str
        """
        self._id = id

    @property
    def default(self):
        r"""Gets the default of this ResponsesInfo.

        是否为分组默认响应

        :return: The default of this ResponsesInfo.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this ResponsesInfo.

        是否为分组默认响应

        :param default: The default of this ResponsesInfo.
        :type default: bool
        """
        self._default = default

    @property
    def create_time(self):
        r"""Gets the create_time of this ResponsesInfo.

        创建时间

        :return: The create_time of this ResponsesInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ResponsesInfo.

        创建时间

        :param create_time: The create_time of this ResponsesInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ResponsesInfo.

        修改时间

        :return: The update_time of this ResponsesInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ResponsesInfo.

        修改时间

        :param update_time: The update_time of this ResponsesInfo.
        :type update_time: datetime
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
        if not isinstance(other, ResponsesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
