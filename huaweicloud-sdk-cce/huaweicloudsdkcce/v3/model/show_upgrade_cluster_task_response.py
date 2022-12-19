# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeClusterTaskResponse(SdkResponse):

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
        'metadata': 'UpgradeTaskMetadata',
        'spec': 'UpgradeTaskSpec',
        'status': 'UpgradeTaskStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        """ShowUpgradeClusterTaskResponse

        The model defined in huaweicloud sdk

        :param api_version: api版本，默认为v3
        :type api_version: str
        :param kind: 资源类型，默认为UpgradeTask
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.UpgradeTaskMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.UpgradeTaskSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.UpgradeTaskStatus`
        """
        
        super(ShowUpgradeClusterTaskResponse, self).__init__()

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
        """Gets the api_version of this ShowUpgradeClusterTaskResponse.

        api版本，默认为v3

        :return: The api_version of this ShowUpgradeClusterTaskResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ShowUpgradeClusterTaskResponse.

        api版本，默认为v3

        :param api_version: The api_version of this ShowUpgradeClusterTaskResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this ShowUpgradeClusterTaskResponse.

        资源类型，默认为UpgradeTask

        :return: The kind of this ShowUpgradeClusterTaskResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ShowUpgradeClusterTaskResponse.

        资源类型，默认为UpgradeTask

        :param kind: The kind of this ShowUpgradeClusterTaskResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this ShowUpgradeClusterTaskResponse.

        :return: The metadata of this ShowUpgradeClusterTaskResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeTaskMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ShowUpgradeClusterTaskResponse.

        :param metadata: The metadata of this ShowUpgradeClusterTaskResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.UpgradeTaskMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this ShowUpgradeClusterTaskResponse.

        :return: The spec of this ShowUpgradeClusterTaskResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeTaskSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ShowUpgradeClusterTaskResponse.

        :param spec: The spec of this ShowUpgradeClusterTaskResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.UpgradeTaskSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this ShowUpgradeClusterTaskResponse.

        :return: The status of this ShowUpgradeClusterTaskResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.UpgradeTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowUpgradeClusterTaskResponse.

        :param status: The status of this ShowUpgradeClusterTaskResponse.
        :type status: :class:`huaweicloudsdkcce.v3.UpgradeTaskStatus`
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
        if not isinstance(other, ShowUpgradeClusterTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
