# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProxyFlavorsByAzCodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'az_codes': 'str',
        'proxy_engine_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'az_codes': 'az_codes',
        'proxy_engine_name': 'proxy_engine_name'
    }

    def __init__(self, x_language=None, az_codes=None, proxy_engine_name=None):
        r"""ShowProxyFlavorsByAzCodeRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param az_codes: **参数解释**：  可用区。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type az_codes: str
        :param proxy_engine_name: **参数解释**：  代理引擎名称。  **约束限制**：  不涉及。  **取值范围**：  taurusproxy。  **默认取值**：  不涉及。
        :type proxy_engine_name: str
        """
        
        

        self._x_language = None
        self._az_codes = None
        self._proxy_engine_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.az_codes = az_codes
        self.proxy_engine_name = proxy_engine_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ShowProxyFlavorsByAzCodeRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowProxyFlavorsByAzCodeRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def az_codes(self):
        r"""Gets the az_codes of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：  可用区。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The az_codes of this ShowProxyFlavorsByAzCodeRequest.
        :rtype: str
        """
        return self._az_codes

    @az_codes.setter
    def az_codes(self, az_codes):
        r"""Sets the az_codes of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：  可用区。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param az_codes: The az_codes of this ShowProxyFlavorsByAzCodeRequest.
        :type az_codes: str
        """
        self._az_codes = az_codes

    @property
    def proxy_engine_name(self):
        r"""Gets the proxy_engine_name of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：  代理引擎名称。  **约束限制**：  不涉及。  **取值范围**：  taurusproxy。  **默认取值**：  不涉及。

        :return: The proxy_engine_name of this ShowProxyFlavorsByAzCodeRequest.
        :rtype: str
        """
        return self._proxy_engine_name

    @proxy_engine_name.setter
    def proxy_engine_name(self, proxy_engine_name):
        r"""Sets the proxy_engine_name of this ShowProxyFlavorsByAzCodeRequest.

        **参数解释**：  代理引擎名称。  **约束限制**：  不涉及。  **取值范围**：  taurusproxy。  **默认取值**：  不涉及。

        :param proxy_engine_name: The proxy_engine_name of this ShowProxyFlavorsByAzCodeRequest.
        :type proxy_engine_name: str
        """
        self._proxy_engine_name = proxy_engine_name

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
        if not isinstance(other, ShowProxyFlavorsByAzCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
