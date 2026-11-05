# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchNodeConfigResponse(SdkResponse):

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
        'metadata': 'NodeconfigMeta',
        'spec': 'NodeconfigSpec',
        'status': 'NodeconfigStatus',
        'x_request_id': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None, x_request_id=None):
        r"""PatchNodeConfigResponse

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**： 固定为v2。 **取值范围**： 不涉及。
        :type api_version: str
        :param kind: **参数解释**： 固定为NodeConfig。 **取值范围**： 不涉及。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeconfigMeta`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatus`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self._x_request_id = None
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
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def api_version(self):
        r"""Gets the api_version of this PatchNodeConfigResponse.

        **参数解释**： 固定为v2。 **取值范围**： 不涉及。

        :return: The api_version of this PatchNodeConfigResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this PatchNodeConfigResponse.

        **参数解释**： 固定为v2。 **取值范围**： 不涉及。

        :param api_version: The api_version of this PatchNodeConfigResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this PatchNodeConfigResponse.

        **参数解释**： 固定为NodeConfig。 **取值范围**： 不涉及。

        :return: The kind of this PatchNodeConfigResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this PatchNodeConfigResponse.

        **参数解释**： 固定为NodeConfig。 **取值范围**： 不涉及。

        :param kind: The kind of this PatchNodeConfigResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this PatchNodeConfigResponse.

        :return: The metadata of this PatchNodeConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigMeta`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this PatchNodeConfigResponse.

        :param metadata: The metadata of this PatchNodeConfigResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeconfigMeta`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this PatchNodeConfigResponse.

        :return: The spec of this PatchNodeConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this PatchNodeConfigResponse.

        :param spec: The spec of this PatchNodeConfigResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeconfigSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this PatchNodeConfigResponse.

        :return: The status of this PatchNodeConfigResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PatchNodeConfigResponse.

        :param status: The status of this PatchNodeConfigResponse.
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatus`
        """
        self._status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this PatchNodeConfigResponse.

        :return: The x_request_id of this PatchNodeConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this PatchNodeConfigResponse.

        :param x_request_id: The x_request_id of this PatchNodeConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("PatchNodeConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, PatchNodeConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
