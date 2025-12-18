# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAutopilotOneJobResponse(SdkResponse):

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
        'metadata': 'V2JobTypeObject',
        'spec': 'V2JobSpec',
        'status': 'V2JobStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        r"""GetAutopilotOneJobResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释**： API类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： Job 
        :type kind: str
        :param api_version: **参数解释**： API版本 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： v2 
        :type api_version: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.V2JobTypeObject`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.V2JobSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.V2JobStatus`
        """
        
        super().__init__()

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
        r"""Gets the kind of this GetAutopilotOneJobResponse.

        **参数解释**： API类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： Job 

        :return: The kind of this GetAutopilotOneJobResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this GetAutopilotOneJobResponse.

        **参数解释**： API类型 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： Job 

        :param kind: The kind of this GetAutopilotOneJobResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this GetAutopilotOneJobResponse.

        **参数解释**： API版本 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： v2 

        :return: The api_version of this GetAutopilotOneJobResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this GetAutopilotOneJobResponse.

        **参数解释**： API版本 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： v2 

        :param api_version: The api_version of this GetAutopilotOneJobResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        r"""Gets the metadata of this GetAutopilotOneJobResponse.

        :return: The metadata of this GetAutopilotOneJobResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.V2JobTypeObject`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this GetAutopilotOneJobResponse.

        :param metadata: The metadata of this GetAutopilotOneJobResponse.
        :type metadata: :class:`huaweicloudsdkcce.v3.V2JobTypeObject`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this GetAutopilotOneJobResponse.

        :return: The spec of this GetAutopilotOneJobResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.V2JobSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this GetAutopilotOneJobResponse.

        :param spec: The spec of this GetAutopilotOneJobResponse.
        :type spec: :class:`huaweicloudsdkcce.v3.V2JobSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this GetAutopilotOneJobResponse.

        :return: The status of this GetAutopilotOneJobResponse.
        :rtype: :class:`huaweicloudsdkcce.v3.V2JobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetAutopilotOneJobResponse.

        :param status: The status of this GetAutopilotOneJobResponse.
        :type status: :class:`huaweicloudsdkcce.v3.V2JobStatus`
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("GetAutopilotOneJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetAutopilotOneJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
