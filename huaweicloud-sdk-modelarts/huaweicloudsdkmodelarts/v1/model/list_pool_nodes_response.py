# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolNodesResponse(SdkResponse):

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
        'metadata': 'NodeListMetadata',
        'items': 'list[Node]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'items': 'items'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, items=None):
        r"""ListPoolNodesResponse

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。
        :type api_version: str
        :param kind: **参数解释**：资源的类型。 **取值范围**：可选值如下： - NodeList：节点列表。
        :type kind: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeListMetadata`
        :param items: **参数解释**：节点资源列表。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.Node`]
        """
        
        super().__init__()

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._items = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if items is not None:
            self.items = items

    @property
    def api_version(self):
        r"""Gets the api_version of this ListPoolNodesResponse.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。

        :return: The api_version of this ListPoolNodesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListPoolNodesResponse.

        **参数解释**：资源的API版本。 **取值范围**：可选值如下： - v2：当前资源版本为v2。

        :param api_version: The api_version of this ListPoolNodesResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ListPoolNodesResponse.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - NodeList：节点列表。

        :return: The kind of this ListPoolNodesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListPoolNodesResponse.

        **参数解释**：资源的类型。 **取值范围**：可选值如下： - NodeList：节点列表。

        :param kind: The kind of this ListPoolNodesResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def metadata(self):
        r"""Gets the metadata of this ListPoolNodesResponse.

        :return: The metadata of this ListPoolNodesResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeListMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListPoolNodesResponse.

        :param metadata: The metadata of this ListPoolNodesResponse.
        :type metadata: :class:`huaweicloudsdkmodelarts.v1.NodeListMetadata`
        """
        self._metadata = metadata

    @property
    def items(self):
        r"""Gets the items of this ListPoolNodesResponse.

        **参数解释**：节点资源列表。

        :return: The items of this ListPoolNodesResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Node`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListPoolNodesResponse.

        **参数解释**：节点资源列表。

        :param items: The items of this ListPoolNodesResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.Node`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListPoolNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListPoolNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
