# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePluginRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'spec': 'PluginSpec'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, spec=None):
        r"""CreatePluginRequestBody

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**：API资源类型，固定值“Plugin”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type api_version: str
        :param kind: **参数解释**：API版本，固定值“v2”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type kind: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.PluginSpec`
        """
        
        

        self._api_version = None
        self._kind = None
        self._spec = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.spec = spec

    @property
    def api_version(self):
        r"""Gets the api_version of this CreatePluginRequestBody.

        **参数解释**：API资源类型，固定值“Plugin”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The api_version of this CreatePluginRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreatePluginRequestBody.

        **参数解释**：API资源类型，固定值“Plugin”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param api_version: The api_version of this CreatePluginRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreatePluginRequestBody.

        **参数解释**：API版本，固定值“v2”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The kind of this CreatePluginRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreatePluginRequestBody.

        **参数解释**：API版本，固定值“v2”，该值不可修改。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param kind: The kind of this CreatePluginRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def spec(self):
        r"""Gets the spec of this CreatePluginRequestBody.

        :return: The spec of this CreatePluginRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PluginSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreatePluginRequestBody.

        :param spec: The spec of this CreatePluginRequestBody.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.PluginSpec`
        """
        self._spec = spec

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
        if not isinstance(other, CreatePluginRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
