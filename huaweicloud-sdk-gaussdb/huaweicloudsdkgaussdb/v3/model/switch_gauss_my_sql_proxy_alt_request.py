# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchGaussMySqlProxyAltRequest:

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
        'proxy_id': 'str',
        'x_language': 'str',
        'body': 'SwitchGaussMySqlProxyAltRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'proxy_id': 'proxy_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, instance_id=None, proxy_id=None, x_language=None, body=None):
        r"""SwitchGaussMySqlProxyAltRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param proxy_id: **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为po01，长度为36个字符。  **默认取值**：  不涉及。
        :type proxy_id: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。
        :type x_language: str
        :param body: Body of the SwitchGaussMySqlProxyAltRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyAltRequestBody`
        """
        
        

        self._instance_id = None
        self._proxy_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.proxy_id = proxy_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this SwitchGaussMySqlProxyAltRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this SwitchGaussMySqlProxyAltRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为po01，长度为36个字符。  **默认取值**：  不涉及。

        :return: The proxy_id of this SwitchGaussMySqlProxyAltRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  获取方法请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为po01，长度为36个字符。  **默认取值**：  不涉及。

        :param proxy_id: The proxy_id of this SwitchGaussMySqlProxyAltRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。

        :return: The x_language of this SwitchGaussMySqlProxyAltRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this SwitchGaussMySqlProxyAltRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认值**：  en-us。

        :param x_language: The x_language of this SwitchGaussMySqlProxyAltRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this SwitchGaussMySqlProxyAltRequest.

        :return: The body of this SwitchGaussMySqlProxyAltRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyAltRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SwitchGaussMySqlProxyAltRequest.

        :param body: The body of this SwitchGaussMySqlProxyAltRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxyAltRequestBody`
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
        if not isinstance(other, SwitchGaussMySqlProxyAltRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
