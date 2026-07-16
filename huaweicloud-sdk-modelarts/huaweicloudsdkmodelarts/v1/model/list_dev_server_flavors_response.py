# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevServerFlavorsResponse(SdkResponse):

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
        'data': 'list[ServerFlavorinstanceResponse]',
        'pages': 'int',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'current': 'current',
        'data': 'data',
        'pages': 'pages',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, current=None, data=None, pages=None, size=None, total=None):
        r"""ListDevServerFlavorsResponse

        The model defined in huaweicloud sdk

        :param current: **参数解释**：当前页数。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type current: int
        :param data: **参数解释**：Lite Server规格列表。
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.ServerFlavorinstanceResponse`]
        :param pages: **参数解释**：总的页数。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type pages: int
        :param size: **参数解释**：每一页的数量。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type size: int
        :param total: **参数解释**：总的记录数量。 **约束限制**：不涉及。 **默认取值**：不涉及。
        :type total: int
        """
        
        super().__init__()

        self._current = None
        self._data = None
        self._pages = None
        self._size = None
        self._total = None
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

    @property
    def current(self):
        r"""Gets the current of this ListDevServerFlavorsResponse.

        **参数解释**：当前页数。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The current of this ListDevServerFlavorsResponse.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        r"""Sets the current of this ListDevServerFlavorsResponse.

        **参数解释**：当前页数。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param current: The current of this ListDevServerFlavorsResponse.
        :type current: int
        """
        self._current = current

    @property
    def data(self):
        r"""Gets the data of this ListDevServerFlavorsResponse.

        **参数解释**：Lite Server规格列表。

        :return: The data of this ListDevServerFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerFlavorinstanceResponse`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListDevServerFlavorsResponse.

        **参数解释**：Lite Server规格列表。

        :param data: The data of this ListDevServerFlavorsResponse.
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.ServerFlavorinstanceResponse`]
        """
        self._data = data

    @property
    def pages(self):
        r"""Gets the pages of this ListDevServerFlavorsResponse.

        **参数解释**：总的页数。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The pages of this ListDevServerFlavorsResponse.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this ListDevServerFlavorsResponse.

        **参数解释**：总的页数。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param pages: The pages of this ListDevServerFlavorsResponse.
        :type pages: int
        """
        self._pages = pages

    @property
    def size(self):
        r"""Gets the size of this ListDevServerFlavorsResponse.

        **参数解释**：每一页的数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The size of this ListDevServerFlavorsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListDevServerFlavorsResponse.

        **参数解释**：每一页的数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param size: The size of this ListDevServerFlavorsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListDevServerFlavorsResponse.

        **参数解释**：总的记录数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :return: The total of this ListDevServerFlavorsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDevServerFlavorsResponse.

        **参数解释**：总的记录数量。 **约束限制**：不涉及。 **默认取值**：不涉及。

        :param total: The total of this ListDevServerFlavorsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListDevServerFlavorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDevServerFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
