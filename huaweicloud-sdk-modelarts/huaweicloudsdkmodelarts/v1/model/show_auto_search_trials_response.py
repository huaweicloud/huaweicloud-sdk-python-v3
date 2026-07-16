# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSearchTrialsResponse(SdkResponse):

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
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'group_by': 'str',
        'items': 'ListAutoSearchTrialsItems'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'group_by': 'group_by',
        'items': 'items'
    }

    def __init__(self, total=None, count=None, limit=None, offset=None, group_by=None, items=None):
        r"""ShowAutoSearchTrialsResponse

        The model defined in huaweicloud sdk

        :param total: 超参搜索所有trial结果的个数。
        :type total: int
        :param count: 超参搜索所有trial结果的当前页展示个数。
        :type count: int
        :param limit: 超参搜索所有trial结果的当前页展示个数最大值。
        :type limit: int
        :param offset: 超参搜索所有trial结果的当前页数。
        :type offset: int
        :param group_by: 分类。
        :type group_by: str
        :param items: 
        :type items: :class:`huaweicloudsdkmodelarts.v1.ListAutoSearchTrialsItems`
        """
        
        super().__init__()

        self._total = None
        self._count = None
        self._limit = None
        self._offset = None
        self._group_by = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if group_by is not None:
            self.group_by = group_by
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的个数。

        :return: The total of this ShowAutoSearchTrialsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的个数。

        :param total: The total of this ShowAutoSearchTrialsResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        r"""Gets the count of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页展示个数。

        :return: The count of this ShowAutoSearchTrialsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页展示个数。

        :param count: The count of this ShowAutoSearchTrialsResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页展示个数最大值。

        :return: The limit of this ShowAutoSearchTrialsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页展示个数最大值。

        :param limit: The limit of this ShowAutoSearchTrialsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页数。

        :return: The offset of this ShowAutoSearchTrialsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAutoSearchTrialsResponse.

        超参搜索所有trial结果的当前页数。

        :param offset: The offset of this ShowAutoSearchTrialsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowAutoSearchTrialsResponse.

        分类。

        :return: The group_by of this ShowAutoSearchTrialsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowAutoSearchTrialsResponse.

        分类。

        :param group_by: The group_by of this ShowAutoSearchTrialsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def items(self):
        r"""Gets the items of this ShowAutoSearchTrialsResponse.

        :return: The items of this ShowAutoSearchTrialsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ListAutoSearchTrialsItems`
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ShowAutoSearchTrialsResponse.

        :param items: The items of this ShowAutoSearchTrialsResponse.
        :type items: :class:`huaweicloudsdkmodelarts.v1.ListAutoSearchTrialsItems`
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ShowAutoSearchTrialsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAutoSearchTrialsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
