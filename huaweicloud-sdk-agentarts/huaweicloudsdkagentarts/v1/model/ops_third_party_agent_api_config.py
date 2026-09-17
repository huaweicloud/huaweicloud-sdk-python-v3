# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentApiConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'headers': 'list[OpsThirdPartyAgentKeyValuePair]',
        '_query_params': 'list[OpsThirdPartyAgentKeyValuePair]',
        'body': 'OpsThirdPartyAgentRequestBodyConfig'
    }

    attribute_map = {
        'url': 'url',
        'headers': 'headers',
        '_query_params': 'query_params',
        'body': 'body'
    }

    def __init__(self, url=None, headers=None, _query_params=None, body=None):
        r"""OpsThirdPartyAgentApiConfig

        The model defined in huaweicloud sdk

        :param url: **参数解释：** 三方智能体的API访问地址。 **约束限制：** 仅支持HTTP/HTTPS协议。 **取值范围：** 由英文字母、数字、特殊字符(:/.-?&amp;&#x3D;%_)组成的字符串，长度为1~2048个字符。 **默认取值：** 不涉及。
        :type url: str
        :param headers: **参数解释：** 请求Header参数列表。 **约束限制：** 最多支持10个Header。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type headers: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        :param _query_params: **参数解释：** 请求Query参数列表。 **约束限制：** 最多支持10个Query参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type _query_params: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        :param body: 
        :type body: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentRequestBodyConfig`
        """
        
        

        self._url = None
        self._headers = None
        self.__query_params = None
        self._body = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if headers is not None:
            self.headers = headers
        if _query_params is not None:
            self._query_params = _query_params
        if body is not None:
            self.body = body

    @property
    def url(self):
        r"""Gets the url of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 三方智能体的API访问地址。 **约束限制：** 仅支持HTTP/HTTPS协议。 **取值范围：** 由英文字母、数字、特殊字符(:/.-?&=%_)组成的字符串，长度为1~2048个字符。 **默认取值：** 不涉及。

        :return: The url of this OpsThirdPartyAgentApiConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 三方智能体的API访问地址。 **约束限制：** 仅支持HTTP/HTTPS协议。 **取值范围：** 由英文字母、数字、特殊字符(:/.-?&=%_)组成的字符串，长度为1~2048个字符。 **默认取值：** 不涉及。

        :param url: The url of this OpsThirdPartyAgentApiConfig.
        :type url: str
        """
        self._url = url

    @property
    def headers(self):
        r"""Gets the headers of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 请求Header参数列表。 **约束限制：** 最多支持10个Header。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The headers of this OpsThirdPartyAgentApiConfig.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 请求Header参数列表。 **约束限制：** 最多支持10个Header。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param headers: The headers of this OpsThirdPartyAgentApiConfig.
        :type headers: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        """
        self._headers = headers

    @property
    def _query_params(self):
        r"""Gets the _query_params of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 请求Query参数列表。 **约束限制：** 最多支持10个Query参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The _query_params of this OpsThirdPartyAgentApiConfig.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        """
        return self.__query_params

    @_query_params.setter
    def _query_params(self, _query_params):
        r"""Sets the _query_params of this OpsThirdPartyAgentApiConfig.

        **参数解释：** 请求Query参数列表。 **约束限制：** 最多支持10个Query参数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param _query_params: The _query_params of this OpsThirdPartyAgentApiConfig.
        :type _query_params: list[:class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentKeyValuePair`]
        """
        self.__query_params = _query_params

    @property
    def body(self):
        r"""Gets the body of this OpsThirdPartyAgentApiConfig.

        :return: The body of this OpsThirdPartyAgentApiConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentRequestBodyConfig`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this OpsThirdPartyAgentApiConfig.

        :param body: The body of this OpsThirdPartyAgentApiConfig.
        :type body: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentRequestBodyConfig`
        """
        self._body = body

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
        if not isinstance(other, OpsThirdPartyAgentApiConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
