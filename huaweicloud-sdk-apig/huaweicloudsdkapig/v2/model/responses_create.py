# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponsesCreate:

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
        'responses': 'dict(str, ResponseInfo)'
    }

    attribute_map = {
        'name': 'name',
        'responses': 'responses'
    }

    def __init__(self, name=None, responses=None):
        """ResponsesCreate

        The model defined in huaweicloud sdk

        :param name: 响应名称。支持英文、数字、下划线、中划线，1-64个字符。
        :type name: str
        :param responses: 错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体
        :type responses: dict(str, ResponseInfo)
        """
        
        

        self._name = None
        self._responses = None
        self.discriminator = None

        self.name = name
        if responses is not None:
            self.responses = responses

    @property
    def name(self):
        """Gets the name of this ResponsesCreate.

        响应名称。支持英文、数字、下划线、中划线，1-64个字符。

        :return: The name of this ResponsesCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponsesCreate.

        响应名称。支持英文、数字、下划线、中划线，1-64个字符。

        :param name: The name of this ResponsesCreate.
        :type name: str
        """
        self._name = name

    @property
    def responses(self):
        """Gets the responses of this ResponsesCreate.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体

        :return: The responses of this ResponsesCreate.
        :rtype: dict(str, ResponseInfo)
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this ResponsesCreate.

        错误类型的响应定义，其中key为错误类型。key的枚举值为： - AUTH_FAILURE：认证失败 - AUTH_HEADER_MISSING：认证身份来源缺失 - AUTHORIZER_FAILURE：自定义认证失败 - AUTHORIZER_CONF_FAILURE：自定义认证配置错误 - AUTHORIZER_IDENTITIES_FAILURE：自定义认证身份来源错误 - BACKEND_UNAVAILABLE：后端不可用 - BACKEND_TIMEOUT：后端超时 - THROTTLED：调用次数超出阈值 - UNAUTHORIZED：应用未授权 - ACCESS_DENIED：拒绝访问 - NOT_FOUND：未找到匹配的API - REQUEST_PARAMETERS_FAILURE：请求参数错误 - DEFAULT_4XX：默认4XX - DEFAULT_5XX：默认5XX - THIRD_AUTH_FAILURE: 第三方认证失败 - THIRD_AUTH_IDENTITIES_FAILURE: 第三方认证身份来源错误 - THIRD_AUTH_CONF_FAILURE: 第三方认证配置错误 - ORCHESTRATION_PARAMETER_NOT_FOUND: 没有入参进行参数编排规则匹配，参数编排失败 - ORCHESTRATION_FAILURE: 有入参进行参数编排规则匹配，但是匹配不上编排规则，参数编排失败  每项错误类型均为一个JSON体

        :param responses: The responses of this ResponsesCreate.
        :type responses: dict(str, ResponseInfo)
        """
        self._responses = responses

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
        if not isinstance(other, ResponsesCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
