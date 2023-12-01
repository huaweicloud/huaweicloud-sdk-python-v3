# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodePoolConfigurationResponse(SdkResponse):

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
        'metadata': 'ConfigurationMetadata',
        'spec': 'ClusterConfigurationsSpec',
        'status': 'object'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        """UpdateNodePoolConfigurationResponse

        The model defined in huaweicloud sdk

        :param api_version: API版本
        :type api_version: str
        :param kind: API类型，固定值**Configuration**
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.ConfigurationMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.ClusterConfigurationsSpec`
        :param status: Configuration的状态信息
        :type status: object
        """
        
        super(UpdateNodePoolConfigurationResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
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
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        """Gets the api_version of this UpdateNodePoolConfigurationResponse.

        API版本

        :return: The api_version of this UpdateNodePoolConfigurationResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this UpdateNodePoolConfigurationResponse.

        API版本

        :param api_version: The api_version of this UpdateNodePoolConfigurationResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this UpdateNodePoolConfigurationResponse.

        API类型，固定值**Configuration**

        :return: The kind of this UpdateNodePoolConfigurationResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this UpdateNodePoolConfigurationResponse.

        API类型，固定值**Configuration**

        :param kind: The kind of this UpdateNodePoolConfigurationResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this UpdateNodePoolConfigurationResponse.

        :return: The metadata of this UpdateNodePoolConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.ConfigurationMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateNodePoolConfigurationResponse.

        :param metadata: The metadata of this UpdateNodePoolConfigurationResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.ConfigurationMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this UpdateNodePoolConfigurationResponse.

        :return: The spec of this UpdateNodePoolConfigurationResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.ClusterConfigurationsSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this UpdateNodePoolConfigurationResponse.

        :param spec: The spec of this UpdateNodePoolConfigurationResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.ClusterConfigurationsSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this UpdateNodePoolConfigurationResponse.

        Configuration的状态信息

        :return: The status of this UpdateNodePoolConfigurationResponse.
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateNodePoolConfigurationResponse.

        Configuration的状态信息

        :param status: The status of this UpdateNodePoolConfigurationResponse.
        :type status: object
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
        if not isinstance(other, UpdateNodePoolConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
