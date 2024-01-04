# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterUpgradeInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'Metadata',
        'spec': 'UpgradeInfoSpec',
        'status': 'UpgradeInfoStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        """ShowClusterUpgradeInfoResponse

        The model defined in huaweicloud sdk

        :param kind: 类型
        :type kind: str
        :param api_version: API版本
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.UpgradeInfoSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
        """
        
        super(ShowClusterUpgradeInfoResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def kind(self):
        """Gets the kind of this ShowClusterUpgradeInfoResponse.

        类型

        :return: The kind of this ShowClusterUpgradeInfoResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ShowClusterUpgradeInfoResponse.

        类型

        :param kind: The kind of this ShowClusterUpgradeInfoResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this ShowClusterUpgradeInfoResponse.

        API版本

        :return: The api_version of this ShowClusterUpgradeInfoResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ShowClusterUpgradeInfoResponse.

        API版本

        :param api_version: The api_version of this ShowClusterUpgradeInfoResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """Gets the metadata of this ShowClusterUpgradeInfoResponse.

        :return: The metadata of this ShowClusterUpgradeInfoResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowClusterUpgradeInfoResponse.

        :param metadata: The metadata of this ShowClusterUpgradeInfoResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this ShowClusterUpgradeInfoResponse.

        :return: The spec of this ShowClusterUpgradeInfoResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeInfoSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ShowClusterUpgradeInfoResponse.

        :param spec: The spec of this ShowClusterUpgradeInfoResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.UpgradeInfoSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this ShowClusterUpgradeInfoResponse.

        :return: The status of this ShowClusterUpgradeInfoResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowClusterUpgradeInfoResponse.

        :param status: The status of this ShowClusterUpgradeInfoResponse.
        :type status: :class:`huaweicloudsdkcce.v3.UpgradeInfoStatus`
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
        if not isinstance(other, ShowClusterUpgradeInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
