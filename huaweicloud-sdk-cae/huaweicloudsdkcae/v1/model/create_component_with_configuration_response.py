# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentWithConfigurationResponse(SdkResponse):

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
        'metadata': 'MetadataResponse',
        'spec': 'CreateComponentSpec',
        'configurations': 'list[ConfigurationItem]',
        'status': 'CreateComponentWithConfigurationResponseBodyStatus'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'configurations': 'configurations',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, configurations=None, status=None):
        r"""CreateComponentWithConfigurationResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本，固定值“v1”，该值不可修改。
        :type api_version: str
        :param kind: API类型，固定值“Component”，该值不可修改。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        :param configurations: 配置项列表。
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        :param status: 
        :type status: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        
        super().__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._configurations = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if configurations is not None:
            self.configurations = configurations
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        r"""Gets the api_version of this CreateComponentWithConfigurationResponse.

        API版本，固定值“v1”，该值不可修改。

        :return: The api_version of this CreateComponentWithConfigurationResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this CreateComponentWithConfigurationResponse.

        API版本，固定值“v1”，该值不可修改。

        :param api_version: The api_version of this CreateComponentWithConfigurationResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this CreateComponentWithConfigurationResponse.

        API类型，固定值“Component”，该值不可修改。

        :return: The kind of this CreateComponentWithConfigurationResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this CreateComponentWithConfigurationResponse.

        API类型，固定值“Component”，该值不可修改。

        :param kind: The kind of this CreateComponentWithConfigurationResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateComponentWithConfigurationResponse.

        :return: The metadata of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateComponentWithConfigurationResponse.

        :param metadata: The metadata of this CreateComponentWithConfigurationResponse.
        :type metadata: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this CreateComponentWithConfigurationResponse.

        :return: The spec of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateComponentWithConfigurationResponse.

        :param spec: The spec of this CreateComponentWithConfigurationResponse.
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        """
        self._spec = spec

    @property
    def configurations(self):
        r"""Gets the configurations of this CreateComponentWithConfigurationResponse.

        配置项列表。

        :return: The configurations of this CreateComponentWithConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        r"""Sets the configurations of this CreateComponentWithConfigurationResponse.

        配置项列表。

        :param configurations: The configurations of this CreateComponentWithConfigurationResponse.
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        self._configurations = configurations

    @property
    def status(self):
        r"""Gets the status of this CreateComponentWithConfigurationResponse.

        :return: The status of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateComponentWithConfigurationResponse.

        :param status: The status of this CreateComponentWithConfigurationResponse.
        :type status: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("CreateComponentWithConfigurationResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateComponentWithConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
