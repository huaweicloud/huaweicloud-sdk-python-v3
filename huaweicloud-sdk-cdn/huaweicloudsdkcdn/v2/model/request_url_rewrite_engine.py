# coding: utf-8

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
        'rewrite_type': 'str',
        'source_url': 'str',
        'redirect_status_code': 'int',
        'redirect_url': 'str',
        'redirect_host': 'str',
        'execution_mode': 'str',
        'inherit_param': 'str'
    }

    attribute_map = {
        'rewrite_type': 'rewrite_type',
        'source_url': 'source_url',
        'redirect_status_code': 'redirect_status_code',
        'redirect_url': 'redirect_url',
        'redirect_host': 'redirect_host',
        'execution_mode': 'execution_mode',
        'inherit_param': 'inherit_param'
    }

    def __init__(self, rewrite_type=None, source_url=None, redirect_status_code=None, redirect_url=None, redirect_host=None, execution_mode=None, inherit_param=None):
        r"""RequestUrlRewriteEngine

        The model defined in huaweicloud sdk

        :param rewrite_type: **参数解释：** 改写方式 **约束限制：** - regex为白名单controlled功能，非白名单用户不开放  **取值范围：** - simple: 精确改写 - regex: 正则改写  **默认取值：** simple: 精确改写
        :type rewrite_type: str
        :param source_url: **参数解释：** 需要替换的URI **约束限制：** - 当rewrite_type为wildcard或regex时必填 - 当rewrite_type为regex时必须以“^/”开始，如：^/test  **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名  **默认取值：** 不涉及
        :type source_url: str
        :param redirect_status_code: **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301: 资源被永久转移。 - 302: 由于不可预见的原因该页面暂不可用。 - 303: 用于PUT或POST请求完成之后进行页面跳转，防止由于页面刷新导致的操作的重复触发。 - 307: 由于不可预见的原因该页面暂不可用。  **默认取值：** 不涉及
        :type redirect_status_code: int
        :param redirect_url: **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\&quot;\\*\&quot;可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg  **取值范围：** 不涉及 **默认取值：** 不涉及
        :type redirect_url: str
        :param redirect_host: **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头  **默认取值：** 不填时默认为当前域名
        :type redirect_host: str
        :param execution_mode: **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200  **默认取值：** 不涉及
        :type execution_mode: str
        :param inherit_param: **参数解释：** 重定向URL是否携带请求参数 **约束限制：** 不涉及 **取值范围：** - on: 携带 - off: 不携带  **默认取值：** on: 携带
        :type inherit_param: str
        """
        
        

        self._rewrite_type = None
        self._source_url = None
        self._redirect_status_code = None
        self._redirect_url = None
        self._redirect_host = None
        self._execution_mode = None
        self._inherit_param = None
        self.discriminator = None

        if rewrite_type is not None:
            self.rewrite_type = rewrite_type
        if source_url is not None:
            self.source_url = source_url
        if redirect_status_code is not None:
            self.redirect_status_code = redirect_status_code
        self.redirect_url = redirect_url
        if redirect_host is not None:
            self.redirect_host = redirect_host
        self.execution_mode = execution_mode
        if inherit_param is not None:
            self.inherit_param = inherit_param

    @property
    def rewrite_type(self):
        r"""Gets the rewrite_type of this RequestUrlRewriteEngine.

        **参数解释：** 改写方式 **约束限制：** - regex为白名单controlled功能，非白名单用户不开放  **取值范围：** - simple: 精确改写 - regex: 正则改写  **默认取值：** simple: 精确改写

        :return: The rewrite_type of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._rewrite_type

    @rewrite_type.setter
    def rewrite_type(self, rewrite_type):
        r"""Sets the rewrite_type of this RequestUrlRewriteEngine.

        **参数解释：** 改写方式 **约束限制：** - regex为白名单controlled功能，非白名单用户不开放  **取值范围：** - simple: 精确改写 - regex: 正则改写  **默认取值：** simple: 精确改写

        :param rewrite_type: The rewrite_type of this RequestUrlRewriteEngine.
        :type rewrite_type: str
        """
        self._rewrite_type = rewrite_type

    @property
    def source_url(self):
        r"""Gets the source_url of this RequestUrlRewriteEngine.

        **参数解释：** 需要替换的URI **约束限制：** - 当rewrite_type为wildcard或regex时必填 - 当rewrite_type为regex时必须以“^/”开始，如：^/test  **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名  **默认取值：** 不涉及

        :return: The source_url of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        r"""Sets the source_url of this RequestUrlRewriteEngine.

        **参数解释：** 需要替换的URI **约束限制：** - 当rewrite_type为wildcard或regex时必填 - 当rewrite_type为regex时必须以“^/”开始，如：^/test  **取值范围：** - 1-512个字符 - 支持通配符\\*匹配，如：/test/\\*/\\*.mp4 - 以正斜线（/）开头的URI，不含http(s)://头及域名  **默认取值：** 不涉及

        :param source_url: The source_url of this RequestUrlRewriteEngine.
        :type source_url: str
        """
        self._source_url = source_url

    @property
    def redirect_status_code(self):
        r"""Gets the redirect_status_code of this RequestUrlRewriteEngine.

        **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301: 资源被永久转移。 - 302: 由于不可预见的原因该页面暂不可用。 - 303: 用于PUT或POST请求完成之后进行页面跳转，防止由于页面刷新导致的操作的重复触发。 - 307: 由于不可预见的原因该页面暂不可用。  **默认取值：** 不涉及

        :return: The redirect_status_code of this RequestUrlRewriteEngine.
        :rtype: int
        """
        return self._redirect_status_code

    @redirect_status_code.setter
    def redirect_status_code(self, redirect_status_code):
        r"""Sets the redirect_status_code of this RequestUrlRewriteEngine.

        **参数解释：** 重定向状态码 **约束限制：** 不涉及 **取值范围：** - 301: 资源被永久转移。 - 302: 由于不可预见的原因该页面暂不可用。 - 303: 用于PUT或POST请求完成之后进行页面跳转，防止由于页面刷新导致的操作的重复触发。 - 307: 由于不可预见的原因该页面暂不可用。  **默认取值：** 不涉及

        :param redirect_status_code: The redirect_status_code of this RequestUrlRewriteEngine.
        :type redirect_status_code: int
        """
        self._redirect_status_code = redirect_status_code

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\"\\*\"可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg  **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The redirect_url of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL **约束限制：** - 重定向后的URL，以正斜线（/）开头，不含http://头及域名，如：/test/index.html - 当匹配类型为全路径时，\"\\*\"可以用“$1”捕获，例如：匹配内容为/test/\\*.jpg，重定向URL配置为/newtest/$1.jpg，则用户请求/test/11.jpg时，$1捕获11，重定向后请求的URL为/newtest/11.jpg  **取值范围：** 不涉及 **默认取值：** 不涉及

        :param redirect_url: The redirect_url of this RequestUrlRewriteEngine.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_host(self):
        r"""Gets the redirect_host of this RequestUrlRewriteEngine.

        **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头  **默认取值：** 不填时默认为当前域名

        :return: The redirect_host of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._redirect_host

    @redirect_host.setter
    def redirect_host(self, redirect_host):
        r"""Sets the redirect_host of this RequestUrlRewriteEngine.

        **参数解释：** 支持将客户端请求重定向到其他域名 **约束限制：** 不涉及 **取值范围：** - 1-255个字符 - 必须以http://或https://开头  **默认取值：** 不填时默认为当前域名

        :param redirect_host: The redirect_host of this RequestUrlRewriteEngine.
        :type redirect_host: str
        """
        self._redirect_host = redirect_host

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this RequestUrlRewriteEngine.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200  **默认取值：** 不涉及

        :return: The execution_mode of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this RequestUrlRewriteEngine.

        **参数解释：** 执行规则 **约束限制：** 不涉及 **取值范围：** - redirect: 如果请求的URL匹配了当前规则，该请求将被重定向到目标Path。执行完当前规则后，当存在其他配置规则时，会继续匹配剩余规则 - break: 如果请求的URL匹配了当前规则，请求将被改写为目标Path。执行完当前规则后，当存在其他配置规则时，将不再匹配剩余规则，此时不支持配置重定向Host和重定向状态码，返回状态码200  **默认取值：** 不涉及

        :param execution_mode: The execution_mode of this RequestUrlRewriteEngine.
        :type execution_mode: str
        """
        self._execution_mode = execution_mode

    @property
    def inherit_param(self):
        r"""Gets the inherit_param of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL是否携带请求参数 **约束限制：** 不涉及 **取值范围：** - on: 携带 - off: 不携带  **默认取值：** on: 携带

        :return: The inherit_param of this RequestUrlRewriteEngine.
        :rtype: str
        """
        return self._inherit_param

    @inherit_param.setter
    def inherit_param(self, inherit_param):
        r"""Sets the inherit_param of this RequestUrlRewriteEngine.

        **参数解释：** 重定向URL是否携带请求参数 **约束限制：** 不涉及 **取值范围：** - on: 携带 - off: 不携带  **默认取值：** on: 携带

        :param inherit_param: The inherit_param of this RequestUrlRewriteEngine.
        :type inherit_param: str
        """
        self._inherit_param = inherit_param

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
        if not isinstance(other, RequestUrlRewriteEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
