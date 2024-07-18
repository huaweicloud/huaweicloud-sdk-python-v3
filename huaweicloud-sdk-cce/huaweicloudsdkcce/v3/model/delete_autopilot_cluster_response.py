# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAutopilotClusterResponse(SdkResponse):

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
        'metadata': 'AutopilotClusterMetadata',
        'spec': 'AutopilotClusterSpec',
        'status': 'AutopilotClusterStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        """DeleteAutopilotClusterResponse

        The model defined in huaweicloud sdk

        :param kind: API类型，固定值“Cluster”或“cluster”，该值不可修改。  
        :type kind: str
        :param api_version: API版本，固定值“v3”，该值不可修改。  
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.AutopilotClusterMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.AutopilotClusterSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.AutopilotClusterStatus`
        """
        
        super(DeleteAutopilotClusterResponse, self).__init__()

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
        """Gets the kind of this DeleteAutopilotClusterResponse.

        API类型，固定值“Cluster”或“cluster”，该值不可修改。  

        :return: The kind of this DeleteAutopilotClusterResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this DeleteAutopilotClusterResponse.

        API类型，固定值“Cluster”或“cluster”，该值不可修改。  

        :param kind: The kind of this DeleteAutopilotClusterResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this DeleteAutopilotClusterResponse.

        API版本，固定值“v3”，该值不可修改。  

        :return: The api_version of this DeleteAutopilotClusterResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this DeleteAutopilotClusterResponse.

        API版本，固定值“v3”，该值不可修改。  

        :param api_version: The api_version of this DeleteAutopilotClusterResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """Gets the metadata of this DeleteAutopilotClusterResponse.

        :return: The metadata of this DeleteAutopilotClusterResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotClusterMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeleteAutopilotClusterResponse.

        :param metadata: The metadata of this DeleteAutopilotClusterResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.AutopilotClusterMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this DeleteAutopilotClusterResponse.

        :return: The spec of this DeleteAutopilotClusterResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotClusterSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DeleteAutopilotClusterResponse.

        :param spec: The spec of this DeleteAutopilotClusterResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.AutopilotClusterSpec`
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this DeleteAutopilotClusterResponse.

        :return: The status of this DeleteAutopilotClusterResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.AutopilotClusterStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeleteAutopilotClusterResponse.

        :param status: The status of this DeleteAutopilotClusterResponse.
        :type status: :class:`huaweicloudsdkcce.v3.AutopilotClusterStatus`
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
        if not isinstance(other, DeleteAutopilotClusterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
