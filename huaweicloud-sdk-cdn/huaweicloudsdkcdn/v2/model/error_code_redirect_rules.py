# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorCodeRedirectRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'int',
        'execution_mode': 'str',
        'target_code': 'int',
        'target_link': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'execution_mode': 'execution_mode',
        'target_code': 'target_code',
        'target_link': 'target_link'
    }

    def __init__(self, error_code=None, execution_mode=None, target_code=None, target_link=None):
        r"""ErrorCodeRedirectRules

        The model defined in huaweicloud sdk

        :param error_code: **参数解释：** 重定向的错误码 **约束限制：** 不涉及 **取值范围：** - 4xx: 400, 403, 404, 405, 414, 416, 451 - 5xx: 500, 501, 502, 503, 504  **默认取值：** 不涉及
        :type error_code: int
        :param execution_mode: **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - break：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则。 - redirect：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将继续匹配剩余规则。  **默认取值：** 不涉及
        :type execution_mode: str
        :param target_code: **参数解释：** 重定向状态码 **约束限制：** 当执行规则选择redirect时，需要配置该参数 **取值范围：** - 301 - 302  **默认取值：** 不涉及
        :type target_code: int
        :param target_link: **参数解释：** 重定向的目标链接 **约束限制：** “执行规则”选择“Break”时：全路径匹配，支持输入一个目标地址，以“/”作为首字符，字符长度不超过512，如：/errorcode.html。 “执行规则”选择“Redirect”时：输入的URL须以http://或https:// 开头 ，字符长度不超过512，包含完整的域名和路径信息，如：http://example.com/errorcode.html。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type target_link: str
        """
        
        

        self._error_code = None
        self._execution_mode = None
        self._target_code = None
        self._target_link = None
        self.discriminator = None

        self.error_code = error_code
        if execution_mode is not None:
            self.execution_mode = execution_mode
        self.target_code = target_code
        self.target_link = target_link

    @property
    def error_code(self):
        r"""Gets the error_code of this ErrorCodeRedirectRules.

        **参数解释：** 重定向的错误码 **约束限制：** 不涉及 **取值范围：** - 4xx: 400, 403, 404, 405, 414, 416, 451 - 5xx: 500, 501, 502, 503, 504  **默认取值：** 不涉及

        :return: The error_code of this ErrorCodeRedirectRules.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ErrorCodeRedirectRules.

        **参数解释：** 重定向的错误码 **约束限制：** 不涉及 **取值范围：** - 4xx: 400, 403, 404, 405, 414, 416, 451 - 5xx: 500, 501, 502, 503, 504  **默认取值：** 不涉及

        :param error_code: The error_code of this ErrorCodeRedirectRules.
        :type error_code: int
        """
        self._error_code = error_code

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this ErrorCodeRedirectRules.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - break：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则。 - redirect：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将继续匹配剩余规则。  **默认取值：** 不涉及

        :return: The execution_mode of this ErrorCodeRedirectRules.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this ErrorCodeRedirectRules.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - break：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则。 - redirect：如果错误码匹配了当前配置，请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，将继续匹配剩余规则。  **默认取值：** 不涉及

        :param execution_mode: The execution_mode of this ErrorCodeRedirectRules.
        :type execution_mode: str
        """
        self._execution_mode = execution_mode

    @property
    def target_code(self):
        r"""Gets the target_code of this ErrorCodeRedirectRules.

        **参数解释：** 重定向状态码 **约束限制：** 当执行规则选择redirect时，需要配置该参数 **取值范围：** - 301 - 302  **默认取值：** 不涉及

        :return: The target_code of this ErrorCodeRedirectRules.
        :rtype: int
        """
        return self._target_code

    @target_code.setter
    def target_code(self, target_code):
        r"""Sets the target_code of this ErrorCodeRedirectRules.

        **参数解释：** 重定向状态码 **约束限制：** 当执行规则选择redirect时，需要配置该参数 **取值范围：** - 301 - 302  **默认取值：** 不涉及

        :param target_code: The target_code of this ErrorCodeRedirectRules.
        :type target_code: int
        """
        self._target_code = target_code

    @property
    def target_link(self):
        r"""Gets the target_link of this ErrorCodeRedirectRules.

        **参数解释：** 重定向的目标链接 **约束限制：** “执行规则”选择“Break”时：全路径匹配，支持输入一个目标地址，以“/”作为首字符，字符长度不超过512，如：/errorcode.html。 “执行规则”选择“Redirect”时：输入的URL须以http://或https:// 开头 ，字符长度不超过512，包含完整的域名和路径信息，如：http://example.com/errorcode.html。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The target_link of this ErrorCodeRedirectRules.
        :rtype: str
        """
        return self._target_link

    @target_link.setter
    def target_link(self, target_link):
        r"""Sets the target_link of this ErrorCodeRedirectRules.

        **参数解释：** 重定向的目标链接 **约束限制：** “执行规则”选择“Break”时：全路径匹配，支持输入一个目标地址，以“/”作为首字符，字符长度不超过512，如：/errorcode.html。 “执行规则”选择“Redirect”时：输入的URL须以http://或https:// 开头 ，字符长度不超过512，包含完整的域名和路径信息，如：http://example.com/errorcode.html。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param target_link: The target_link of this ErrorCodeRedirectRules.
        :type target_link: str
        """
        self._target_link = target_link

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorCodeRedirectRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
