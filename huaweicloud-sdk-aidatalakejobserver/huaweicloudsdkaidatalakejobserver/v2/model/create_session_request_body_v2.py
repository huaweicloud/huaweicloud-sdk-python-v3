# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSessionRequestBodyV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_name': 'str',
        'catalog_context': 'CatalogContext',
        'wait_timeout': 'int'
    }

    attribute_map = {
        'endpoint_name': 'endpoint_name',
        'catalog_context': 'catalog_context',
        'wait_timeout': 'wait_timeout'
    }

    def __init__(self, endpoint_name=None, catalog_context=None, wait_timeout=None):
        r"""CreateSessionRequestBodyV2

        The model defined in huaweicloud sdk

        :param endpoint_name: **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param catalog_context: 
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.CatalogContext`
        :param wait_timeout: **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~7200。 **默认取值**：不涉及。
        :type wait_timeout: int
        """
        
        

        self._endpoint_name = None
        self._catalog_context = None
        self._wait_timeout = None
        self.discriminator = None

        self.endpoint_name = endpoint_name
        self.catalog_context = catalog_context
        if wait_timeout is not None:
            self.wait_timeout = wait_timeout

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this CreateSessionRequestBodyV2.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this CreateSessionRequestBodyV2.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this CreateSessionRequestBodyV2.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this CreateSessionRequestBodyV2.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def catalog_context(self):
        r"""Gets the catalog_context of this CreateSessionRequestBodyV2.

        :return: The catalog_context of this CreateSessionRequestBodyV2.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CatalogContext`
        """
        return self._catalog_context

    @catalog_context.setter
    def catalog_context(self, catalog_context):
        r"""Sets the catalog_context of this CreateSessionRequestBodyV2.

        :param catalog_context: The catalog_context of this CreateSessionRequestBodyV2.
        :type catalog_context: :class:`huaweicloudsdkaidatalakejobserver.v2.CatalogContext`
        """
        self._catalog_context = catalog_context

    @property
    def wait_timeout(self):
        r"""Gets the wait_timeout of this CreateSessionRequestBodyV2.

        **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~7200。 **默认取值**：不涉及。

        :return: The wait_timeout of this CreateSessionRequestBodyV2.
        :rtype: int
        """
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, wait_timeout):
        r"""Sets the wait_timeout of this CreateSessionRequestBodyV2.

        **参数解释**：创建session排队等待时间，单位：秒。 **约束限制**：不涉及。 **取值范围**：300~7200。 **默认取值**：不涉及。

        :param wait_timeout: The wait_timeout of this CreateSessionRequestBodyV2.
        :type wait_timeout: int
        """
        self._wait_timeout = wait_timeout

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
        if not isinstance(other, CreateSessionRequestBodyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
