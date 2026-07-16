# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodePoolResponse(SdkResponse):

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
        'metadata': 'NodePoolMetadata',
        'spec': 'NodePoolSpec',
        'status': 'NodePoolStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        r"""ShowNodePoolResponse

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**： API版本。 **取值范围**： 可选值如下： - v2
        :type api_version: str
        :param kind: **参数解释**：节点池类型。 **取值范围**： 可选值如下： - NodePool：节点池
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodePoolMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodePoolStatus`
        """
        
        super().__init__()

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
        r"""Gets the api_version of this ShowNodePoolResponse.

        **参数解释**： API版本。 **取值范围**： 可选值如下： - v2

        :return: The api_version of this ShowNodePoolResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ShowNodePoolResponse.

        **参数解释**： API版本。 **取值范围**： 可选值如下： - v2

        :param api_version: The api_version of this ShowNodePoolResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ShowNodePoolResponse.

        **参数解释**：节点池类型。 **取值范围**： 可选值如下： - NodePool：节点池

        :return: The kind of this ShowNodePoolResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ShowNodePoolResponse.

        **参数解释**：节点池类型。 **取值范围**： 可选值如下： - NodePool：节点池

        :param kind: The kind of this ShowNodePoolResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowNodePoolResponse.

        :return: The metadata of this ShowNodePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodePoolMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowNodePoolResponse.

        :param metadata: The metadata of this ShowNodePoolResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodePoolMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this ShowNodePoolResponse.

        :return: The spec of this ShowNodePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowNodePoolResponse.

        :param spec: The spec of this ShowNodePoolResponse.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodePoolSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this ShowNodePoolResponse.

        :return: The status of this ShowNodePoolResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodePoolStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowNodePoolResponse.

        :param status: The status of this ShowNodePoolResponse.
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodePoolStatus`
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("ShowNodePoolResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowNodePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
