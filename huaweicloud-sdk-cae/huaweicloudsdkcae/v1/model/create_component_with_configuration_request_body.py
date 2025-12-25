# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentWithConfigurationRequestBody:

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
        'metadata': 'CreateComponentWithConfigurationRequestBodyMetadata',
        'spec': 'CreateComponentWithConfigurationRequestBodySpec',
        'configurations': 'list[ConfigurationItem]'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'configurations': 'configurations'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, configurations=None):
        r"""CreateComponentWithConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v1”，该值不可修改。
        :type api_version: str
        :param kind: API类型，固定值“Component”，该值不可修改。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodyMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodySpec`
        :param configurations: 配置项列表。
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._configurations = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if configurations is not None:
            self.configurations = configurations

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateComponentWithConfigurationRequestBody.

        API版本，固定值“v1”，该值不可修改。

        :return: The api_version of this CreateComponentWithConfigurationRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateComponentWithConfigurationRequestBody.

        API版本，固定值“v1”，该值不可修改。

        :param api_version: The api_version of this CreateComponentWithConfigurationRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreateComponentWithConfigurationRequestBody.

        API类型，固定值“Component”，该值不可修改。

        :return: The kind of this CreateComponentWithConfigurationRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateComponentWithConfigurationRequestBody.

        API类型，固定值“Component”，该值不可修改。

        :param kind: The kind of this CreateComponentWithConfigurationRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateComponentWithConfigurationRequestBody.

        :return: The metadata of this CreateComponentWithConfigurationRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateComponentWithConfigurationRequestBody.

        :param metadata: The metadata of this CreateComponentWithConfigurationRequestBody.
        :type metadata: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodyMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this CreateComponentWithConfigurationRequestBody.

        :return: The spec of this CreateComponentWithConfigurationRequestBody.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodySpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateComponentWithConfigurationRequestBody.

        :param spec: The spec of this CreateComponentWithConfigurationRequestBody.
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationRequestBodySpec`
        """
        self._spec = spec

    @property
    def configurations(self):
        r"""Gets the configurations of this CreateComponentWithConfigurationRequestBody.

        配置项列表。

        :return: The configurations of this CreateComponentWithConfigurationRequestBody.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this CreateComponentWithConfigurationRequestBody.

        配置项列表。

        :param configurations: The configurations of this CreateComponentWithConfigurationRequestBody.
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        self._configurations = configurations

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
        if not isinstance(other, CreateComponentWithConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
