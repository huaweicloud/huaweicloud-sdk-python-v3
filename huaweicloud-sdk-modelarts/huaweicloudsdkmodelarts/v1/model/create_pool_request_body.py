# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoolRequestBody:

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
        'metadata': 'PoolMetadataCreation',
        'spec': 'PoolSpecCreation'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None):
        r"""CreatePoolRequestBody

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**：API版本。 **约束限制**：不涉及。 **取值范围**：可选值如下： - v2 **默认取值**：不涉及。
        :type api_version: str
        :param kind: **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Pool：资源池 **默认取值**：不涉及。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.PoolMetadataCreation`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreation`
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        if spec is not None:
            self.spec = spec

    @property
    def api_version(self):
        r"""Gets the api_version of this CreatePoolRequestBody.

        **参数解释**：API版本。 **约束限制**：不涉及。 **取值范围**：可选值如下： - v2 **默认取值**：不涉及。

        :return: The api_version of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreatePoolRequestBody.

        **参数解释**：API版本。 **约束限制**：不涉及。 **取值范围**：可选值如下： - v2 **默认取值**：不涉及。

        :param api_version: The api_version of this CreatePoolRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreatePoolRequestBody.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Pool：资源池 **默认取值**：不涉及。

        :return: The kind of this CreatePoolRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreatePoolRequestBody.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Pool：资源池 **默认取值**：不涉及。

        :param kind: The kind of this CreatePoolRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this CreatePoolRequestBody.

        :return: The metadata of this CreatePoolRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolMetadataCreation`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreatePoolRequestBody.

        :param metadata: The metadata of this CreatePoolRequestBody.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.PoolMetadataCreation`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this CreatePoolRequestBody.

        :return: The spec of this CreatePoolRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreation`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreatePoolRequestBody.

        :param spec: The spec of this CreatePoolRequestBody.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.PoolSpecCreation`
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
        if not isinstance(other, CreatePoolRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
