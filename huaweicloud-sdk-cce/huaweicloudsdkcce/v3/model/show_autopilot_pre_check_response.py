# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutopilotPreCheckResponse(SdkResponse):

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
        'metadata': 'PrecheckTaskMetadata',
        'spec': 'PrecheckSpec',
        'status': 'PrecheckStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        r"""ShowAutopilotPreCheckResponse

        The model defined in huaweicloud sdk

        :param api_version: api版本，默认为v3
        :type api_version: str
        :param kind: 资源类型，默认为PreCheckTask
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
        """
        
        super(ShowAutopilotPreCheckResponse, self).__init__()

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
        r"""Gets the api_version of this ShowAutopilotPreCheckResponse.

        api版本，默认为v3

        :return: The api_version of this ShowAutopilotPreCheckResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ShowAutopilotPreCheckResponse.

        api版本，默认为v3

        :param api_version: The api_version of this ShowAutopilotPreCheckResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ShowAutopilotPreCheckResponse.

        资源类型，默认为PreCheckTask

        :return: The kind of this ShowAutopilotPreCheckResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ShowAutopilotPreCheckResponse.

        资源类型，默认为PreCheckTask

        :param kind: The kind of this ShowAutopilotPreCheckResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowAutopilotPreCheckResponse.

        :return: The metadata of this ShowAutopilotPreCheckResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowAutopilotPreCheckResponse.

        :param metadata: The metadata of this ShowAutopilotPreCheckResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.PrecheckTaskMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ShowAutopilotPreCheckResponse.

        :return: The spec of this ShowAutopilotPreCheckResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowAutopilotPreCheckResponse.

        :param spec: The spec of this ShowAutopilotPreCheckResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.PrecheckSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this ShowAutopilotPreCheckResponse.

        :return: The status of this ShowAutopilotPreCheckResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAutopilotPreCheckResponse.

        :param status: The status of this ShowAutopilotPreCheckResponse.
        :type status: :class:`huaweicloudsdkcce.v3.PrecheckStatus`
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
        if not isinstance(other, ShowAutopilotPreCheckResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
