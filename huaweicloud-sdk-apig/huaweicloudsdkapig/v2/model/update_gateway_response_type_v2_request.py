# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGatewayResponseTypeV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'group_id': 'str',
        'response_id': 'str',
        'response_type': 'str',
        'body': 'ResponseInfo'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'response_id': 'response_id',
        'response_type': 'response_type',
        'body': 'body'
    }

    def __init__(self, instance_id=None, group_id=None, response_id=None, response_type=None, body=None):
        r"""UpdateGatewayResponseTypeV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param group_id: 分组的编号
        :type group_id: str
        :param response_id: 响应编号
        :type response_id: str
        :param response_type: 错误类型 - AUTH_FAILURE: 认证失败，IAM或APP认证校验失败 - AUTH_HEADER_MISSING: 认证身份来源信息缺失 - AUTHORIZER_FAILURE: 自定义认证方返回认证失败 - AUTHORIZER_CONF_FAILURE:自定义认证方异常，通信失败、返回异常响应等错误 - AUTHORIZER_IDENTITIES_FAILURE: 前端自定义认证的身份来源信息缺失或不合法错误 - BACKEND_UNAVAILABLE: 后端不可用，网络不可达错误 - BACKEND_TIMEOUT: 后端超时，与后端的网络交互超过预配置的时间错误 - THROTTLED: API调用次数超出所配置的流量策略阈值 - UNAUTHORIZED: 使用的凭据未被授权访问该API - ACCESS_DENIED: 拒绝访问，如触发配置的访问控制策略、或异常攻击检测拦截 - NOT_FOUND: 未匹配到API错误 - REQUEST_PARAMETERS_FAILURE: 请求参数校验失败、不支持的HTTP方法 - DEFAULT_4XX: 其它4XX类错误 - DEFAULT_5XX: 其它5XX类错误 - THIRD_AUTH_FAILURE: 第三方认证方返回认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证的身份来源信息缺失或不合法错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证方异常，通信失败、返回异常响应等错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: OIDC认证中token校验失败 - OIDC_AUTH_GET_DISCOVERY_ERROR: OIDC认证中从配置的discovery处获取信息失败 - OIDC_AUTH_CODE_FLOW_FAIL: OIDC认证中授权码流程处理失败 - JWT_AUTH_FAILURE: JWT认证中token校验失败 - ORCHESTRATION_PARAMETER_NOT_FOUND: 参数编排失败，请求中没有待编排的入参 - ORCHESTRATION_FAILURE: 参数编排失败，没有编排规则匹配成功
        :type response_type: str
        :param body: Body of the UpdateGatewayResponseTypeV2Request
        :type body: :class:`huaweicloudsdkapig.v2.ResponseInfo`
        """
        
        

        self._instance_id = None
        self._group_id = None
        self._response_id = None
        self._response_type = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        self.response_id = response_id
        self.response_type = response_type
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateGatewayResponseTypeV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this UpdateGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateGatewayResponseTypeV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this UpdateGatewayResponseTypeV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateGatewayResponseTypeV2Request.

        分组的编号

        :return: The group_id of this UpdateGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateGatewayResponseTypeV2Request.

        分组的编号

        :param group_id: The group_id of this UpdateGatewayResponseTypeV2Request.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def response_id(self):
        r"""Gets the response_id of this UpdateGatewayResponseTypeV2Request.

        响应编号

        :return: The response_id of this UpdateGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        r"""Sets the response_id of this UpdateGatewayResponseTypeV2Request.

        响应编号

        :param response_id: The response_id of this UpdateGatewayResponseTypeV2Request.
        :type response_id: str
        """
        self._response_id = response_id

    @property
    def response_type(self):
        r"""Gets the response_type of this UpdateGatewayResponseTypeV2Request.

        错误类型 - AUTH_FAILURE: 认证失败，IAM或APP认证校验失败 - AUTH_HEADER_MISSING: 认证身份来源信息缺失 - AUTHORIZER_FAILURE: 自定义认证方返回认证失败 - AUTHORIZER_CONF_FAILURE:自定义认证方异常，通信失败、返回异常响应等错误 - AUTHORIZER_IDENTITIES_FAILURE: 前端自定义认证的身份来源信息缺失或不合法错误 - BACKEND_UNAVAILABLE: 后端不可用，网络不可达错误 - BACKEND_TIMEOUT: 后端超时，与后端的网络交互超过预配置的时间错误 - THROTTLED: API调用次数超出所配置的流量策略阈值 - UNAUTHORIZED: 使用的凭据未被授权访问该API - ACCESS_DENIED: 拒绝访问，如触发配置的访问控制策略、或异常攻击检测拦截 - NOT_FOUND: 未匹配到API错误 - REQUEST_PARAMETERS_FAILURE: 请求参数校验失败、不支持的HTTP方法 - DEFAULT_4XX: 其它4XX类错误 - DEFAULT_5XX: 其它5XX类错误 - THIRD_AUTH_FAILURE: 第三方认证方返回认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证的身份来源信息缺失或不合法错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证方异常，通信失败、返回异常响应等错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: OIDC认证中token校验失败 - OIDC_AUTH_GET_DISCOVERY_ERROR: OIDC认证中从配置的discovery处获取信息失败 - OIDC_AUTH_CODE_FLOW_FAIL: OIDC认证中授权码流程处理失败 - JWT_AUTH_FAILURE: JWT认证中token校验失败 - ORCHESTRATION_PARAMETER_NOT_FOUND: 参数编排失败，请求中没有待编排的入参 - ORCHESTRATION_FAILURE: 参数编排失败，没有编排规则匹配成功

        :return: The response_type of this UpdateGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        r"""Sets the response_type of this UpdateGatewayResponseTypeV2Request.

        错误类型 - AUTH_FAILURE: 认证失败，IAM或APP认证校验失败 - AUTH_HEADER_MISSING: 认证身份来源信息缺失 - AUTHORIZER_FAILURE: 自定义认证方返回认证失败 - AUTHORIZER_CONF_FAILURE:自定义认证方异常，通信失败、返回异常响应等错误 - AUTHORIZER_IDENTITIES_FAILURE: 前端自定义认证的身份来源信息缺失或不合法错误 - BACKEND_UNAVAILABLE: 后端不可用，网络不可达错误 - BACKEND_TIMEOUT: 后端超时，与后端的网络交互超过预配置的时间错误 - THROTTLED: API调用次数超出所配置的流量策略阈值 - UNAUTHORIZED: 使用的凭据未被授权访问该API - ACCESS_DENIED: 拒绝访问，如触发配置的访问控制策略、或异常攻击检测拦截 - NOT_FOUND: 未匹配到API错误 - REQUEST_PARAMETERS_FAILURE: 请求参数校验失败、不支持的HTTP方法 - DEFAULT_4XX: 其它4XX类错误 - DEFAULT_5XX: 其它5XX类错误 - THIRD_AUTH_FAILURE: 第三方认证方返回认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证的身份来源信息缺失或不合法错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证方异常，通信失败、返回异常响应等错误 - OIDC_AUTH_TOKEN_VERIFY_FAIL: OIDC认证中token校验失败 - OIDC_AUTH_GET_DISCOVERY_ERROR: OIDC认证中从配置的discovery处获取信息失败 - OIDC_AUTH_CODE_FLOW_FAIL: OIDC认证中授权码流程处理失败 - JWT_AUTH_FAILURE: JWT认证中token校验失败 - ORCHESTRATION_PARAMETER_NOT_FOUND: 参数编排失败，请求中没有待编排的入参 - ORCHESTRATION_FAILURE: 参数编排失败，没有编排规则匹配成功

        :param response_type: The response_type of this UpdateGatewayResponseTypeV2Request.
        :type response_type: str
        """
        self._response_type = response_type

    @property
    def body(self):
        r"""Gets the body of this UpdateGatewayResponseTypeV2Request.

        :return: The body of this UpdateGatewayResponseTypeV2Request.
        :rtype: :class:`huaweicloudsdkapig.v2.ResponseInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateGatewayResponseTypeV2Request.

        :param body: The body of this UpdateGatewayResponseTypeV2Request.
        :type body: :class:`huaweicloudsdkapig.v2.ResponseInfo`
        """
        self._body = body

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
        if not isinstance(other, UpdateGatewayResponseTypeV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
