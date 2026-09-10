# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperateRecordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'operate_type': 'str',
        'user_name': 'str',
        'level': 'str',
        'offset': 'str',
        'limit': 'str',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'operate_type': 'operate_type',
        'user_name': 'user_name',
        'level': 'level',
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, start_time=None, end_time=None, operate_type=None, user_name=None, level=None, offset=None, limit=None, sort=None, order=None):
        r"""ListOperateRecordRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 查询开始时间，格式为毫秒级时间戳。
        :type start_time: int
        :param end_time: 查询结束时间，格式为毫秒级时间戳。
        :type end_time: int
        :param operate_type: 操作类型
        :type operate_type: str
        :param user_name: 用户名称
        :type user_name: str
        :param level: 事件等级
        :type level: str
        :param offset: 查询偏移量，默认为0。
        :type offset: str
        :param limit: 查询数量，默认为10。
        :type limit: str
        :param sort: 排序字段，默认为operate_time。取值范围：operate_type、user_name、operate_time、level。
        :type sort: str
        :param order: 排序方式，默认为desc（倒序）。取值范围：desc（倒序）、asc（正序）。
        :type order: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._operate_type = None
        self._user_name = None
        self._level = None
        self._offset = None
        self._limit = None
        self._sort = None
        self._order = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if operate_type is not None:
            self.operate_type = operate_type
        if user_name is not None:
            self.user_name = user_name
        if level is not None:
            self.level = level
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOperateRecordRequestBody.

        查询开始时间，格式为毫秒级时间戳。

        :return: The start_time of this ListOperateRecordRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOperateRecordRequestBody.

        查询开始时间，格式为毫秒级时间戳。

        :param start_time: The start_time of this ListOperateRecordRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOperateRecordRequestBody.

        查询结束时间，格式为毫秒级时间戳。

        :return: The end_time of this ListOperateRecordRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOperateRecordRequestBody.

        查询结束时间，格式为毫秒级时间戳。

        :param end_time: The end_time of this ListOperateRecordRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ListOperateRecordRequestBody.

        操作类型

        :return: The operate_type of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ListOperateRecordRequestBody.

        操作类型

        :param operate_type: The operate_type of this ListOperateRecordRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def user_name(self):
        r"""Gets the user_name of this ListOperateRecordRequestBody.

        用户名称

        :return: The user_name of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListOperateRecordRequestBody.

        用户名称

        :param user_name: The user_name of this ListOperateRecordRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def level(self):
        r"""Gets the level of this ListOperateRecordRequestBody.

        事件等级

        :return: The level of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListOperateRecordRequestBody.

        事件等级

        :param level: The level of this ListOperateRecordRequestBody.
        :type level: str
        """
        self._level = level

    @property
    def offset(self):
        r"""Gets the offset of this ListOperateRecordRequestBody.

        查询偏移量，默认为0。

        :return: The offset of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOperateRecordRequestBody.

        查询偏移量，默认为0。

        :param offset: The offset of this ListOperateRecordRequestBody.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOperateRecordRequestBody.

        查询数量，默认为10。

        :return: The limit of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOperateRecordRequestBody.

        查询数量，默认为10。

        :param limit: The limit of this ListOperateRecordRequestBody.
        :type limit: str
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this ListOperateRecordRequestBody.

        排序字段，默认为operate_time。取值范围：operate_type、user_name、operate_time、level。

        :return: The sort of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListOperateRecordRequestBody.

        排序字段，默认为operate_time。取值范围：operate_type、user_name、operate_time、level。

        :param sort: The sort of this ListOperateRecordRequestBody.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        r"""Gets the order of this ListOperateRecordRequestBody.

        排序方式，默认为desc（倒序）。取值范围：desc（倒序）、asc（正序）。

        :return: The order of this ListOperateRecordRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListOperateRecordRequestBody.

        排序方式，默认为desc（倒序）。取值范围：desc（倒序）、asc（正序）。

        :param order: The order of this ListOperateRecordRequestBody.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListOperateRecordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
