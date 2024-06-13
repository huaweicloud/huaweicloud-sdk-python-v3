# coding: utf-8

import six

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
        'api_version': 'ApiVersionObj',
        'kind': 'ComponentKindObj',
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
        """CreateComponentWithConfigurationResponse

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        :param configurations: 配置项列表。
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        :param status: 
        :type status: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        
        super(CreateComponentWithConfigurationResponse, self).__init__()

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
        """Gets the api_version of this CreateComponentWithConfigurationResponse.

        :return: The api_version of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CreateComponentWithConfigurationResponse.

        :param api_version: The api_version of this CreateComponentWithConfigurationResponse.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this CreateComponentWithConfigurationResponse.

        :return: The kind of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateComponentWithConfigurationResponse.

        :param kind: The kind of this CreateComponentWithConfigurationResponse.
        :type kind: :class:`huaweicloudsdkcae.v1.ComponentKindObj`
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this CreateComponentWithConfigurationResponse.

        :return: The metadata of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateComponentWithConfigurationResponse.

        :param metadata: The metadata of this CreateComponentWithConfigurationResponse.
        :type metadata: :class:`huaweicloudsdkcae.v1.MetadataResponse`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this CreateComponentWithConfigurationResponse.

        :return: The spec of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CreateComponentWithConfigurationResponse.

        :param spec: The spec of this CreateComponentWithConfigurationResponse.
        :type spec: :class:`huaweicloudsdkcae.v1.CreateComponentSpec`
        """
        self._spec = spec

    @property
    def configurations(self):
        """Gets the configurations of this CreateComponentWithConfigurationResponse.

        配置项列表。

        :return: The configurations of this CreateComponentWithConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this CreateComponentWithConfigurationResponse.

        配置项列表。

        :param configurations: The configurations of this CreateComponentWithConfigurationResponse.
        :type configurations: list[:class:`huaweicloudsdkcae.v1.ConfigurationItem`]
        """
        self._configurations = configurations

    @property
    def status(self):
        """Gets the status of this CreateComponentWithConfigurationResponse.

        :return: The status of this CreateComponentWithConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateComponentWithConfigurationResponse.

        :param status: The status of this CreateComponentWithConfigurationResponse.
        :type status: :class:`huaweicloudsdkcae.v1.CreateComponentWithConfigurationResponseBodyStatus`
        """
        self._status = status

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
        if not isinstance(other, CreateComponentWithConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
