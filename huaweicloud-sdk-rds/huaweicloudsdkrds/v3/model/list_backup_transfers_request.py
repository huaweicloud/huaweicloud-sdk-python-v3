# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupTransfersRequest:

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
        'order_field': 'str',
        'order_rule': 'str',
        'filter_field': 'str',
        'filter_content': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'x_language': 'str',
        'transfer_type': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'order_field': 'order_field',
        'order_rule': 'order_rule',
        'filter_field': 'filter_field',
        'filter_content': 'filter_content',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'x_language': 'X-Language',
        'transfer_type': 'transfer_type',
        'offset': 'offset'
    }

    def __init__(self, limit=None, order_field=None, order_rule=None, filter_field=None, filter_content=None, begin_time=None, end_time=None, x_language=None, transfer_type=None, offset=None):
        r"""ListBackupTransfersRequest

        The model defined in huaweicloud sdk

        :param limit: 查询记录数
        :type limit: int
        :param order_field: 排序字段
        :type order_field: str
        :param order_rule: 排序规则
        :type order_rule: str
        :param filter_field: 筛选字段
        :type filter_field: str
        :param filter_content: 筛选关键字
        :type filter_content: str
        :param begin_time: 开始时间戳
        :type begin_time: int
        :param end_time: 结束时间戳
        :type end_time: int
        :param x_language: 语言
        :type x_language: str
        :param transfer_type: 转储任务类型，默认为manual manual:手动转储任务 auto:自动转储任务
        :type transfer_type: str
        :param offset: 分页页码
        :type offset: int
        """
        
        

        self._limit = None
        self._order_field = None
        self._order_rule = None
        self._filter_field = None
        self._filter_content = None
        self._begin_time = None
        self._end_time = None
        self._x_language = None
        self._transfer_type = None
        self._offset = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if order_field is not None:
            self.order_field = order_field
        if order_rule is not None:
            self.order_rule = order_rule
        if filter_field is not None:
            self.filter_field = filter_field
        if filter_content is not None:
            self.filter_content = filter_content
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if x_language is not None:
            self.x_language = x_language
        if transfer_type is not None:
            self.transfer_type = transfer_type
        if offset is not None:
            self.offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackupTransfersRequest.

        查询记录数

        :return: The limit of this ListBackupTransfersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackupTransfersRequest.

        查询记录数

        :param limit: The limit of this ListBackupTransfersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_field(self):
        r"""Gets the order_field of this ListBackupTransfersRequest.

        排序字段

        :return: The order_field of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        r"""Sets the order_field of this ListBackupTransfersRequest.

        排序字段

        :param order_field: The order_field of this ListBackupTransfersRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_rule(self):
        r"""Gets the order_rule of this ListBackupTransfersRequest.

        排序规则

        :return: The order_rule of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._order_rule

    @order_rule.setter
    def order_rule(self, order_rule):
        r"""Sets the order_rule of this ListBackupTransfersRequest.

        排序规则

        :param order_rule: The order_rule of this ListBackupTransfersRequest.
        :type order_rule: str
        """
        self._order_rule = order_rule

    @property
    def filter_field(self):
        r"""Gets the filter_field of this ListBackupTransfersRequest.

        筛选字段

        :return: The filter_field of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._filter_field

    @filter_field.setter
    def filter_field(self, filter_field):
        r"""Sets the filter_field of this ListBackupTransfersRequest.

        筛选字段

        :param filter_field: The filter_field of this ListBackupTransfersRequest.
        :type filter_field: str
        """
        self._filter_field = filter_field

    @property
    def filter_content(self):
        r"""Gets the filter_content of this ListBackupTransfersRequest.

        筛选关键字

        :return: The filter_content of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._filter_content

    @filter_content.setter
    def filter_content(self, filter_content):
        r"""Sets the filter_content of this ListBackupTransfersRequest.

        筛选关键字

        :param filter_content: The filter_content of this ListBackupTransfersRequest.
        :type filter_content: str
        """
        self._filter_content = filter_content

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListBackupTransfersRequest.

        开始时间戳

        :return: The begin_time of this ListBackupTransfersRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListBackupTransfersRequest.

        开始时间戳

        :param begin_time: The begin_time of this ListBackupTransfersRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBackupTransfersRequest.

        结束时间戳

        :return: The end_time of this ListBackupTransfersRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBackupTransfersRequest.

        结束时间戳

        :param end_time: The end_time of this ListBackupTransfersRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListBackupTransfersRequest.

        语言

        :return: The x_language of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListBackupTransfersRequest.

        语言

        :param x_language: The x_language of this ListBackupTransfersRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this ListBackupTransfersRequest.

        转储任务类型，默认为manual manual:手动转储任务 auto:自动转储任务

        :return: The transfer_type of this ListBackupTransfersRequest.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this ListBackupTransfersRequest.

        转储任务类型，默认为manual manual:手动转储任务 auto:自动转储任务

        :param transfer_type: The transfer_type of this ListBackupTransfersRequest.
        :type transfer_type: str
        """
        self._transfer_type = transfer_type

    @property
    def offset(self):
        r"""Gets the offset of this ListBackupTransfersRequest.

        分页页码

        :return: The offset of this ListBackupTransfersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackupTransfersRequest.

        分页页码

        :param offset: The offset of this ListBackupTransfersRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBackupTransfersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
