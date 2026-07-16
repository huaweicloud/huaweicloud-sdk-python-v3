# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Node:

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
        'metadata': 'NodeMetadata',
        'spec': 'NodeSpec',
        'status': 'NodeStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        r"""Node

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。
        :type api_version: str
        :param kind: **参数解释**：资源的类型。 **取值范围**：可选值如下： - Node：节点。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodeStatus`
        """
        
        

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec
        self.status = status

    @property
    def api_version(self):
        r"""Gets the api_version of this Node.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。

        :return: The api_version of this Node.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this Node.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。

        :param api_version: The api_version of this Node.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this Node.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - Node：节点。

        :return: The kind of this Node.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this Node.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - Node：节点。

        :param kind: The kind of this Node.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this Node.

        :return: The metadata of this Node.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Node.

        :param metadata: The metadata of this Node.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeMetadata`
        """
        self._metadata = metadata

    @property
    def spec(self):
        r"""Gets the spec of this Node.

        :return: The spec of this Node.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this Node.

        :param spec: The spec of this Node.
        :type spec: :class:`huaweicloudsdkmodelarts.v1.NodeSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this Node.

        :return: The status of this Node.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Node.

        :param status: The status of this Node.
        :type status: :class:`huaweicloudsdkmodelarts.v1.NodeStatus`
        """
        self._status = status

    def to_dict(self):
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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
