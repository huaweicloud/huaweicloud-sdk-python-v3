# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodesResponse(SdkResponse):

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
        'items': 'list[Node]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'items': 'items'
    }

    def __init__(self, kind=None, api_version=None, items=None):
        r"""ListNodesResponse

        The model defined in huaweicloud sdk

        :param kind: **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： List 
        :type kind: str
        :param api_version: **参数解释**： API版本 **约束限制**： 固定值,不允许修改 **取值范围**： 不涉及 **默认取值**： v3 
        :type api_version: str
        :param items: **参数解释**： 节点对象列表，包含了当前集群下所有节点的详细信息。可通过items.metadata.name下的值来找到对应的节点。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type items: list[:class:`huaweicloudsdkcce.v3.Node`]
        """
        
        super().__init__()

        self._kind = None
        self._api_version = None
        self._items = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items

    @property
    def kind(self):
        r"""Gets the kind of this ListNodesResponse.

        **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： List 

        :return: The kind of this ListNodesResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ListNodesResponse.

        **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： List 

        :param kind: The kind of this ListNodesResponse.
        :type kind: str
        """
        self._kind = kind

    @property
    def api_version(self):
        r"""Gets the api_version of this ListNodesResponse.

        **参数解释**： API版本 **约束限制**： 固定值,不允许修改 **取值范围**： 不涉及 **默认取值**： v3 

        :return: The api_version of this ListNodesResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ListNodesResponse.

        **参数解释**： API版本 **约束限制**： 固定值,不允许修改 **取值范围**： 不涉及 **默认取值**： v3 

        :param api_version: The api_version of this ListNodesResponse.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def items(self):
        r"""Gets the items of this ListNodesResponse.

        **参数解释**： 节点对象列表，包含了当前集群下所有节点的详细信息。可通过items.metadata.name下的值来找到对应的节点。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The items of this ListNodesResponse.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Node`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListNodesResponse.

        **参数解释**： 节点对象列表，包含了当前集群下所有节点的详细信息。可通过items.metadata.name下的值来找到对应的节点。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param items: The items of this ListNodesResponse.
        :type items: list[:class:`huaweicloudsdkcce.v3.Node`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListNodesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
