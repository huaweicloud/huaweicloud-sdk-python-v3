# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataframeJobRequestBody:

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
        'description': 'str',
        'endpoint_name': 'str',
        'agency_name': 'str',
        'config': 'DataframeJobConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'endpoint_name': 'endpoint_name',
        'agency_name': 'agency_name',
        'config': 'config'
    }

    def __init__(self, name=None, description=None, endpoint_name=None, agency_name=None, config=None):
        r"""CreateDataframeJobRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：作业名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type name: str
        :param description: **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“&lt;”、“&gt;”、“&#x3D;”、“&amp;”、“\&quot;”、“&#39;”。 **默认取值**：不涉及。 
        :type description: str
        :param endpoint_name: **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param agency_name: **参数解释**：委托名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type agency_name: str
        :param config: 
        :type config: :class:`huaweicloudsdkaidatalake.v2.DataframeJobConfig`
        """
        
        

        self._name = None
        self._description = None
        self._endpoint_name = None
        self._agency_name = None
        self._config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.endpoint_name = endpoint_name
        if agency_name is not None:
            self.agency_name = agency_name
        if config is not None:
            self.config = config

    @property
    def name(self):
        r"""Gets the name of this CreateDataframeJobRequestBody.

        **参数解释**：作业名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The name of this CreateDataframeJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDataframeJobRequestBody.

        **参数解释**：作业名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param name: The name of this CreateDataframeJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateDataframeJobRequestBody.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“<”、“>”、“=”、“&”、“\"”、“'”。 **默认取值**：不涉及。 

        :return: The description of this CreateDataframeJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDataframeJobRequestBody.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“<”、“>”、“=”、“&”、“\"”、“'”。 **默认取值**：不涉及。 

        :param description: The description of this CreateDataframeJobRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this CreateDataframeJobRequestBody.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this CreateDataframeJobRequestBody.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this CreateDataframeJobRequestBody.

        **参数解释**：Endpoint名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this CreateDataframeJobRequestBody.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateDataframeJobRequestBody.

        **参数解释**：委托名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The agency_name of this CreateDataframeJobRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateDataframeJobRequestBody.

        **参数解释**：委托名称。  **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param agency_name: The agency_name of this CreateDataframeJobRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def config(self):
        r"""Gets the config of this CreateDataframeJobRequestBody.

        :return: The config of this CreateDataframeJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.DataframeJobConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this CreateDataframeJobRequestBody.

        :param config: The config of this CreateDataframeJobRequestBody.
        :type config: :class:`huaweicloudsdkaidatalake.v2.DataframeJobConfig`
        """
        self._config = config

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
        if not isinstance(other, CreateDataframeJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
