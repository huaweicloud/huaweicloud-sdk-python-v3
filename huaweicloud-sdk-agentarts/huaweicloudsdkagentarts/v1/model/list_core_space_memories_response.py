# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpaceMemoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[MemoryRecord]',
        'total': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'items': 'items',
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, items=None, total=None, limit=None, offset=None):
        r"""ListCoreSpaceMemoriesResponse

        The model defined in huaweicloud sdk

        :param items: **参数解释：**  记忆记录列表，包含当前页的所有记忆记录。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type items: list[:class:`huaweicloudsdkagentarts.v1.MemoryRecord`]
        :param total: **参数解释：**  符合条件的记录总数，用于计算总页数。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type total: int
        :param limit: **参数解释：**  每页返回的记录数量，用于分页查询。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type limit: int
        :param offset: **参数解释：**  偏移量，用于分页查询时指定起始位置，从0开始。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type offset: int
        """
        
        super().__init__()

        self._items = None
        self._total = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def items(self):
        r"""Gets the items of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  记忆记录列表，包含当前页的所有记忆记录。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The items of this ListCoreSpaceMemoriesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.MemoryRecord`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  记忆记录列表，包含当前页的所有记忆记录。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param items: The items of this ListCoreSpaceMemoriesResponse.
        :type items: list[:class:`huaweicloudsdkagentarts.v1.MemoryRecord`]
        """
        self._items = items

    @property
    def total(self):
        r"""Gets the total of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  符合条件的记录总数，用于计算总页数。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The total of this ListCoreSpaceMemoriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  符合条件的记录总数，用于计算总页数。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param total: The total of this ListCoreSpaceMemoriesResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  每页返回的记录数量，用于分页查询。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The limit of this ListCoreSpaceMemoriesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  每页返回的记录数量，用于分页查询。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param limit: The limit of this ListCoreSpaceMemoriesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  偏移量，用于分页查询时指定起始位置，从0开始。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The offset of this ListCoreSpaceMemoriesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreSpaceMemoriesResponse.

        **参数解释：**  偏移量，用于分页查询时指定起始位置，从0开始。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param offset: The offset of this ListCoreSpaceMemoriesResponse.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreSpaceMemoriesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreSpaceMemoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
