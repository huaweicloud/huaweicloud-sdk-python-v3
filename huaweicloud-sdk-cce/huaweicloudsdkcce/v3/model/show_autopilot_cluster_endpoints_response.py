# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutopilotClusterEndpointsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'Metadata',
        'spec': 'OpenAPISpec',
        'status': 'OpenAPIResponseStatus'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, metadata=None, spec=None, status=None):
        r"""ShowAutopilotClusterEndpointsResponse

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.OpenAPISpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.OpenAPIResponseStatus`
        """
        
        super().__init__()

        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowAutopilotClusterEndpointsResponse.

        :return: The metadata of this ShowAutopilotClusterEndpointsResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowAutopilotClusterEndpointsResponse.

        :param metadata: The metadata of this ShowAutopilotClusterEndpointsResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.Metadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ShowAutopilotClusterEndpointsResponse.

        :return: The spec of this ShowAutopilotClusterEndpointsResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.OpenAPISpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowAutopilotClusterEndpointsResponse.

        :param spec: The spec of this ShowAutopilotClusterEndpointsResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.OpenAPISpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this ShowAutopilotClusterEndpointsResponse.

        :return: The status of this ShowAutopilotClusterEndpointsResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.OpenAPIResponseStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAutopilotClusterEndpointsResponse.

        :param status: The status of this ShowAutopilotClusterEndpointsResponse.
        :type status: :class:`huaweicloudsdkcce.v3.OpenAPIResponseStatus`
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("ShowAutopilotClusterEndpointsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAutopilotClusterEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
