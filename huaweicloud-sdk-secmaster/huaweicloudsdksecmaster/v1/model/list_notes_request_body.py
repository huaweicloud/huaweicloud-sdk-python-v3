# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'war_room_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'war_room_id': 'war_room_id'
    }

    def __init__(self, limit=None, offset=None, sort_by=None, order=None, from_date=None, to_date=None, war_room_id=None):
        r"""ListNotesRequestBody

        The model defined in huaweicloud sdk

        :param limit: 分页查询参数，用于指定一次查询最多的结果数，从1开始。
        :type limit: int
        :param offset: 分页查询参数。用于指定查询结果的起始位置，从0开始。
        :type offset: int
        :param sort_by: 排序字段
        :type sort_by: str
        :param order: 升序/降序
        :type order: str
        :param from_date: 搜索起始时间
        :type from_date: str
        :param to_date: 搜索结束时间
        :type to_date: str
        :param war_room_id: 评论的对象ID
        :type war_room_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._from_date = None
        self._to_date = None
        self._war_room_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if war_room_id is not None:
            self.war_room_id = war_room_id

    @property
    def limit(self):
        r"""Gets the limit of this ListNotesRequestBody.

        分页查询参数，用于指定一次查询最多的结果数，从1开始。

        :return: The limit of this ListNotesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNotesRequestBody.

        分页查询参数，用于指定一次查询最多的结果数，从1开始。

        :param limit: The limit of this ListNotesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListNotesRequestBody.

        分页查询参数。用于指定查询结果的起始位置，从0开始。

        :return: The offset of this ListNotesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNotesRequestBody.

        分页查询参数。用于指定查询结果的起始位置，从0开始。

        :param offset: The offset of this ListNotesRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListNotesRequestBody.

        排序字段

        :return: The sort_by of this ListNotesRequestBody.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListNotesRequestBody.

        排序字段

        :param sort_by: The sort_by of this ListNotesRequestBody.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this ListNotesRequestBody.

        升序/降序

        :return: The order of this ListNotesRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListNotesRequestBody.

        升序/降序

        :param order: The order of this ListNotesRequestBody.
        :type order: str
        """
        self._order = order

    @property
    def from_date(self):
        r"""Gets the from_date of this ListNotesRequestBody.

        搜索起始时间

        :return: The from_date of this ListNotesRequestBody.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ListNotesRequestBody.

        搜索起始时间

        :param from_date: The from_date of this ListNotesRequestBody.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ListNotesRequestBody.

        搜索结束时间

        :return: The to_date of this ListNotesRequestBody.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ListNotesRequestBody.

        搜索结束时间

        :param to_date: The to_date of this ListNotesRequestBody.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def war_room_id(self):
        r"""Gets the war_room_id of this ListNotesRequestBody.

        评论的对象ID

        :return: The war_room_id of this ListNotesRequestBody.
        :rtype: str
        """
        return self._war_room_id

    @war_room_id.setter
    def war_room_id(self, war_room_id):
        r"""Sets the war_room_id of this ListNotesRequestBody.

        评论的对象ID

        :param war_room_id: The war_room_id of this ListNotesRequestBody.
        :type war_room_id: str
        """
        self._war_room_id = war_room_id

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
        if not isinstance(other, ListNotesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
