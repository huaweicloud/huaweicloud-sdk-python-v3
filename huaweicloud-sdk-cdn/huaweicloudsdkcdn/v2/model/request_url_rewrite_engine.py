# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestUrlRewriteEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'redirect_status_code': 'int',
        'redirect_url': 'str',
        'redirect_host': 'str',
        'execution_mode': 'str'
    }

    attribute_map = {
        'redirect_status_code': 'redirect_status_code',
        'redirect_url': 'redirect_url',
        'redirect_host': 'redirect_host',
        'execution_mode': 'execution_mode'
    }

    def __init__(self, redirect_status_code=None, redirect_url=None, redirect_host=None, execution_mode=None):
        r"""RequestUrlRewriteEngine

        The model defined in huaweicloud sdk

        :param redirect_status_code: **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301 - 302 - 303 - 307 **默认取值：** 不涉及
        :type redirect_status_code: int
        :param redirect_url: **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\&quot;\\*\&quot;可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg **取值范围：** 不涉及 **默认取值：** 不涉及
        :type redirect_url: str
        :param redirect_host: **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头 **默认取值：** 不填时默认为当前域名
        :type redirect_host: str
        :param execution_mode: **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200 **默认取值：** 不涉及
        :type execution_mode: str
        """
        
        

        self._redirect_status_code = None
        self._redirect_url = None
        self._redirect_host = None
        self._execution_mode = None
        self.discriminator = None

        if redirect_status_code is not None:
            self.redirect_status_code = redirect_status_code
        self.redirect_url = redirect_url
        self.redirect_host = redirect_host
        self.execution_mode = execution_mode

    @property
    def redirect_status_code(self):
        r"""Gets the redirect_status_code of this RequestUrlRewriteEngine.

        **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301 - 302 - 303 - 307 **默认取值：** 不涉及

        :return: The redirect_status_code of this RequestUrlRewriteEngine.
        :rtype: int
        """
        return self._redirect_status_code

    @redirect_status_code.setter
    def redirect_status_code(self, redirect_status_code):
        r"""Sets the redirect_status_code of this RequestUrlRewriteEngine.

        **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301 - 302 - 303 - 307 **默认取值：** 不涉及

        :param redirect_status_code: The redirect_status_code of this RequestUrlRewriteEngine.
        :type redirect_status_code: int
        """
        self._redirect_status_code = redirect_status_code

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\"\\*\"可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The redirect_url of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\"\\*\"可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg **取值范围：** 不涉及 **默认取值：** 不涉及

        :param redirect_url: The redirect_url of this RequestUrlRewriteEngine.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_host(self):
        r"""Gets the redirect_host of this RequestUrlRewriteEngine.

        **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头 **默认取值：** 不填时默认为当前域名

        :return: The redirect_host of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._redirect_host

    @redirect_host.setter
    def redirect_host(self, redirect_host):
        r"""Sets the redirect_host of this RequestUrlRewriteEngine.

        **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头 **默认取值：** 不填时默认为当前域名

        :param redirect_host: The redirect_host of this RequestUrlRewriteEngine.
        :type redirect_host: str
        """
        self._redirect_host = redirect_host

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this RequestUrlRewriteEngine.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200 **默认取值：** 不涉及

        :return: The execution_mode of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this RequestUrlRewriteEngine.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200 **默认取值：** 不涉及

        :param execution_mode: The execution_mode of this RequestUrlRewriteEngine.
        :type execution_mode: str
        """
        self._execution_mode = execution_mode

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
        if not isinstance(other, RequestUrlRewriteEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
