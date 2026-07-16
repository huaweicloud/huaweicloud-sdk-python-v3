# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreIngressesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'items': 'list[CoreIngressResponse]'
    }

    attribute_map = {
        'total': 'total',
        'items': 'items'
    }

    def __init__(self, total=None, items=None):
        r"""ListCoreIngressesResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: Ingress总数。
        :type total: int
        :param items: **参数解释**: Ingress列表。
        :type items: list[:class:`huaweicloudsdkagentarts.v1.CoreIngressResponse`]
        """
        
        super().__init__()

        self._total = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListCoreIngressesResponse.

        **参数解释**: Ingress总数。

        :return: The total of this ListCoreIngressesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCoreIngressesResponse.

        **参数解释**: Ingress总数。

        :param total: The total of this ListCoreIngressesResponse.
        :type total: int
        """
        self._total = total

    @property
    def items(self):
        r"""Gets the items of this ListCoreIngressesResponse.

        **参数解释**: Ingress列表。

        :return: The items of this ListCoreIngressesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreIngressResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListCoreIngressesResponse.

        **参数解释**: Ingress列表。

        :param items: The items of this ListCoreIngressesResponse.
        :type items: list[:class:`huaweicloudsdkagentarts.v1.CoreIngressResponse`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreIngressesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreIngressesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
