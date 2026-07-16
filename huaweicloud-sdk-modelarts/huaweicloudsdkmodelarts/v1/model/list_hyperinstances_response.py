# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHyperinstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current': 'int',
        'data': 'list[ServerHyperinstanceResponse]',
        'pages': 'int',
        'size': 'int',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'current': 'current',
        'data': 'data',
        'pages': 'pages',
        'size': 'size',
        'total': 'total',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, current=None, data=None, pages=None, size=None, total=None, x_request_id=None):
        r"""ListHyperinstancesResponse

        The model defined in huaweicloud sdk

        :param current: **参数解释**：当前页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type current: int
        :param data: **参数解释**：Lite Server超节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.ServerHyperinstanceResponse`]
        :param pages: **参数解释**：总的页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pages: int
        :param size: **参数解释**：每一页的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type size: int
        :param total: **参数解释**：总的记录数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._current = None
        self._data = None
        self._pages = None
        self._size = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if current is not None:
            self.current = current
        if data is not None:
            self.data = data
        if pages is not None:
            self.pages = pages
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def current(self):
        r"""Gets the current of this ListHyperinstancesResponse.

        **参数解释**：当前页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The current of this ListHyperinstancesResponse.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        r"""Sets the current of this ListHyperinstancesResponse.

        **参数解释**：当前页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param current: The current of this ListHyperinstancesResponse.
        :type current: int
        """
        self._current = current

    @property
    def data(self):
        r"""Gets the data of this ListHyperinstancesResponse.

        **参数解释**：Lite Server超节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The data of this ListHyperinstancesResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerHyperinstanceResponse`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListHyperinstancesResponse.

        **参数解释**：Lite Server超节点实例列表。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param data: The data of this ListHyperinstancesResponse.
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.ServerHyperinstanceResponse`]
        """
        self._data = data

    @property
    def pages(self):
        r"""Gets the pages of this ListHyperinstancesResponse.

        **参数解释**：总的页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pages of this ListHyperinstancesResponse.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this ListHyperinstancesResponse.

        **参数解释**：总的页数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pages: The pages of this ListHyperinstancesResponse.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        r"""Gets the size of this ListHyperinstancesResponse.

        **参数解释**：每一页的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The size of this ListHyperinstancesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListHyperinstancesResponse.

        **参数解释**：每一页的数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param size: The size of this ListHyperinstancesResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListHyperinstancesResponse.

        **参数解释**：总的记录数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The total of this ListHyperinstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHyperinstancesResponse.

        **参数解释**：总的记录数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param total: The total of this ListHyperinstancesResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListHyperinstancesResponse.

        :return: The x_request_id of this ListHyperinstancesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListHyperinstancesResponse.

        :param x_request_id: The x_request_id of this ListHyperinstancesResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListHyperinstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListHyperinstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
