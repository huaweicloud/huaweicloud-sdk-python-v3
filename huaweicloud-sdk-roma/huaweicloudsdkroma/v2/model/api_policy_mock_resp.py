# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyMockResp:

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
        'result_content': 'str',
        'status_code': 'int',
        'header': 'list[MockApiBaseInfoHeader]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'conditions': 'conditions',
        'backend_params': 'backend_params',
        'effect_mode': 'effect_mode',
        'authorizer_id': 'authorizer_id',
        'result_content': 'result_content',
        'status_code': 'status_code',
        'header': 'header'
    }

    def __init__(self, id=None, name=None, conditions=None, backend_params=None, effect_mode=None, authorizer_id=None, result_content=None, status_code=None, header=None):
        """ApiPolicyMockResp

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
        :param result_content: 返回结果
        :type result_content: str
        :param status_code: mock后端自定义状态码： \&quot;200\&quot;: \&quot;OK\&quot;, \&quot;201\&quot;: \&quot;Created\&quot;, \&quot;202\&quot;: \&quot;Accepted\&quot;, \&quot;203\&quot;: \&quot;NonAuthoritativeInformation\&quot;, \&quot;204\&quot;: \&quot;NoContent\&quot;, \&quot;205\&quot;: \&quot;ResetContent\&quot;, \&quot;206\&quot;: \&quot;PartialContent\&quot;, \&quot;300\&quot;: \&quot;MultipleChoices\&quot;, \&quot;301\&quot;: \&quot;MovedPermanently\&quot;, \&quot;302\&quot;: \&quot;Found\&quot;, \&quot;303\&quot;: \&quot;SeeOther\&quot;, \&quot;304\&quot;: \&quot;NotModified\&quot;, \&quot;305\&quot;: \&quot;UseProxy\&quot;, \&quot;306\&quot;: \&quot;Unused\&quot;, \&quot;307\&quot;: \&quot;TemporaryRedirect\&quot;, \&quot;400\&quot;: \&quot;BadRequest\&quot;, \&quot;401\&quot;: \&quot;Unauthorized\&quot;, \&quot;402\&quot;: \&quot;PaymentRequired\&quot;, \&quot;403\&quot;: \&quot;Forbidden\&quot;, \&quot;404\&quot;: \&quot;NotFound\&quot;, \&quot;405\&quot;: \&quot;MethodNotAllowed\&quot;, \&quot;406\&quot;: \&quot;NotAcceptable\&quot;, \&quot;407\&quot;: \&quot;ProxyAuthenticationRequired\&quot;, \&quot;408\&quot;: \&quot;RequestTimeout\&quot;, \&quot;409\&quot;: \&quot;Conflict\&quot;, \&quot;410\&quot;: \&quot;Gone\&quot;, \&quot;411\&quot;: \&quot;LengthRequired\&quot;, \&quot;412\&quot;: \&quot;PreconditionFailed\&quot;, \&quot;413\&quot;: \&quot;RequestEntityTooLarge\&quot;, \&quot;414\&quot;: \&quot;RequestURITooLong\&quot;, \&quot;415\&quot;: \&quot;UnsupportedMediaType\&quot;, \&quot;416\&quot;: \&quot;RequestedRangeNotSatisfiable\&quot;, \&quot;417\&quot;: \&quot;ExpectationFailed\&quot;, \&quot;450\&quot;: \&quot;ParameterRequried\&quot;, \&quot;451\&quot;: \&quot;MethodConnectException\&quot;, \&quot;500\&quot;: \&quot;InternalServerError\&quot;, \&quot;501\&quot;: \&quot;NotImplemented\&quot;, \&quot;502\&quot;: \&quot;BadGateway\&quot;, \&quot;503\&quot;: \&quot;ServiceUnavailable\&quot;, \&quot;504\&quot;: \&quot;GatewayTimeout\&quot;, \&quot;505\&quot;: \&quot;HTTPVersionNotSupported\&quot;,
        :type status_code: int
        :param header: mock后端自定义响应头header
        :type header: list[:class:`huaweicloudsdkroma.v2.MockApiBaseInfoHeader`]
        """
        
        

        self._id = None
        self._name = None
        self._conditions = None
        self._backend_params = None
        self._effect_mode = None
        self._authorizer_id = None
        self._result_content = None
        self._status_code = None
        self._header = None
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
        if result_content is not None:
            self.result_content = result_content
        if status_code is not None:
            self.status_code = status_code
        if header is not None:
            self.header = header

    @property
    def id(self):
        """Gets the id of this ApiPolicyMockResp.

        编号

        :return: The id of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiPolicyMockResp.

        编号

        :param id: The id of this ApiPolicyMockResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiPolicyMockResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :return: The name of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPolicyMockResp.

        策略后端名称。字符串由中文、英文字母、数字、下划线组成，且只能以中文或英文开头。

        :param name: The name of this ApiPolicyMockResp.
        :type name: str
        """
        self._name = name

    @property
    def conditions(self):
        """Gets the conditions of this ApiPolicyMockResp.

        策略条件列表

        :return: The conditions of this ApiPolicyMockResp.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ConditionResp`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ApiPolicyMockResp.

        策略条件列表

        :param conditions: The conditions of this ApiPolicyMockResp.
        :type conditions: list[:class:`huaweicloudsdkroma.v2.ConditionResp`]
        """
        self._conditions = conditions

    @property
    def backend_params(self):
        """Gets the backend_params of this ApiPolicyMockResp.

        后端参数列表

        :return: The backend_params of this ApiPolicyMockResp.
        :rtype: list[:class:`huaweicloudsdkroma.v2.BackendParam`]
        """
        return self._backend_params

    @backend_params.setter
    def backend_params(self, backend_params):
        """Sets the backend_params of this ApiPolicyMockResp.

        后端参数列表

        :param backend_params: The backend_params of this ApiPolicyMockResp.
        :type backend_params: list[:class:`huaweicloudsdkroma.v2.BackendParam`]
        """
        self._backend_params = backend_params

    @property
    def effect_mode(self):
        """Gets the effect_mode of this ApiPolicyMockResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :return: The effect_mode of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._effect_mode

    @effect_mode.setter
    def effect_mode(self, effect_mode):
        """Sets the effect_mode of this ApiPolicyMockResp.

        关联的策略组合模式： - ALL：满足全部条件 - ANY：满足任一条件

        :param effect_mode: The effect_mode of this ApiPolicyMockResp.
        :type effect_mode: str
        """
        self._effect_mode = effect_mode

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiPolicyMockResp.

        后端自定义认证对象的ID

        :return: The authorizer_id of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiPolicyMockResp.

        后端自定义认证对象的ID

        :param authorizer_id: The authorizer_id of this ApiPolicyMockResp.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

    @property
    def result_content(self):
        """Gets the result_content of this ApiPolicyMockResp.

        返回结果

        :return: The result_content of this ApiPolicyMockResp.
        :rtype: str
        """
        return self._result_content

    @result_content.setter
    def result_content(self, result_content):
        """Sets the result_content of this ApiPolicyMockResp.

        返回结果

        :param result_content: The result_content of this ApiPolicyMockResp.
        :type result_content: str
        """
        self._result_content = result_content

    @property
    def status_code(self):
        """Gets the status_code of this ApiPolicyMockResp.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :return: The status_code of this ApiPolicyMockResp.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ApiPolicyMockResp.

        mock后端自定义状态码： \"200\": \"OK\", \"201\": \"Created\", \"202\": \"Accepted\", \"203\": \"NonAuthoritativeInformation\", \"204\": \"NoContent\", \"205\": \"ResetContent\", \"206\": \"PartialContent\", \"300\": \"MultipleChoices\", \"301\": \"MovedPermanently\", \"302\": \"Found\", \"303\": \"SeeOther\", \"304\": \"NotModified\", \"305\": \"UseProxy\", \"306\": \"Unused\", \"307\": \"TemporaryRedirect\", \"400\": \"BadRequest\", \"401\": \"Unauthorized\", \"402\": \"PaymentRequired\", \"403\": \"Forbidden\", \"404\": \"NotFound\", \"405\": \"MethodNotAllowed\", \"406\": \"NotAcceptable\", \"407\": \"ProxyAuthenticationRequired\", \"408\": \"RequestTimeout\", \"409\": \"Conflict\", \"410\": \"Gone\", \"411\": \"LengthRequired\", \"412\": \"PreconditionFailed\", \"413\": \"RequestEntityTooLarge\", \"414\": \"RequestURITooLong\", \"415\": \"UnsupportedMediaType\", \"416\": \"RequestedRangeNotSatisfiable\", \"417\": \"ExpectationFailed\", \"450\": \"ParameterRequried\", \"451\": \"MethodConnectException\", \"500\": \"InternalServerError\", \"501\": \"NotImplemented\", \"502\": \"BadGateway\", \"503\": \"ServiceUnavailable\", \"504\": \"GatewayTimeout\", \"505\": \"HTTPVersionNotSupported\",

        :param status_code: The status_code of this ApiPolicyMockResp.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def header(self):
        """Gets the header of this ApiPolicyMockResp.

        mock后端自定义响应头header

        :return: The header of this ApiPolicyMockResp.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MockApiBaseInfoHeader`]
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this ApiPolicyMockResp.

        mock后端自定义响应头header

        :param header: The header of this ApiPolicyMockResp.
        :type header: list[:class:`huaweicloudsdkroma.v2.MockApiBaseInfoHeader`]
        """
        self._header = header

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
        if not isinstance(other, ApiPolicyMockResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
