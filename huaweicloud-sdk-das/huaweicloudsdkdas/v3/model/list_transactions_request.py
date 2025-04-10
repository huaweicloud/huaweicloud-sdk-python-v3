# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransactionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'datastore_type': 'str',
        'x_language': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'order': 'str',
        'order_by': 'str',
        'last_sec_min': 'int',
        'last_sec_max': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'datastore_type': 'datastore_type',
        'x_language': 'X-Language',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'order': 'order',
        'order_by': 'order_by',
        'last_sec_min': 'last_sec_min',
        'last_sec_max': 'last_sec_max'
    }

    def __init__(self, instance_id=None, datastore_type=None, x_language=None, start_at=None, end_at=None, page_num=None, page_size=None, order=None, order_by=None, last_sec_min=None, last_sec_max=None):
        r"""ListTransactionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param datastore_type: 数据库类型。仅支持MySQL
        :type datastore_type: str
        :param x_language: 语言
        :type x_language: str
        :param start_at: 采集开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 采集结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param page_num: 页数
        :type page_num: int
        :param page_size: 页大小
        :type page_size: int
        :param order: 排序字段
        :type order: str
        :param order_by: 升序|降序
        :type order_by: str
        :param last_sec_min: 持续时间下限
        :type last_sec_min: int
        :param last_sec_max: 持续时间上限
        :type last_sec_max: int
        """
        
        

        self._instance_id = None
        self._datastore_type = None
        self._x_language = None
        self._start_at = None
        self._end_at = None
        self._page_num = None
        self._page_size = None
        self._order = None
        self._order_by = None
        self._last_sec_min = None
        self._last_sec_max = None
        self.discriminator = None

        self.instance_id = instance_id
        self.datastore_type = datastore_type
        if x_language is not None:
            self.x_language = x_language
        self.start_at = start_at
        self.end_at = end_at
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if order is not None:
            self.order = order
        if order_by is not None:
            self.order_by = order_by
        if last_sec_min is not None:
            self.last_sec_min = last_sec_min
        if last_sec_max is not None:
            self.last_sec_max = last_sec_max

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTransactionsRequest.

        实例ID

        :return: The instance_id of this ListTransactionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTransactionsRequest.

        实例ID

        :param instance_id: The instance_id of this ListTransactionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListTransactionsRequest.

        数据库类型。仅支持MySQL

        :return: The datastore_type of this ListTransactionsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListTransactionsRequest.

        数据库类型。仅支持MySQL

        :param datastore_type: The datastore_type of this ListTransactionsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ListTransactionsRequest.

        语言

        :return: The x_language of this ListTransactionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListTransactionsRequest.

        语言

        :param x_language: The x_language of this ListTransactionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_at(self):
        r"""Gets the start_at of this ListTransactionsRequest.

        采集开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ListTransactionsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListTransactionsRequest.

        采集开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ListTransactionsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListTransactionsRequest.

        采集结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ListTransactionsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListTransactionsRequest.

        采集结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ListTransactionsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def page_num(self):
        r"""Gets the page_num of this ListTransactionsRequest.

        页数

        :return: The page_num of this ListTransactionsRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ListTransactionsRequest.

        页数

        :param page_num: The page_num of this ListTransactionsRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTransactionsRequest.

        页大小

        :return: The page_size of this ListTransactionsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTransactionsRequest.

        页大小

        :param page_size: The page_size of this ListTransactionsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def order(self):
        r"""Gets the order of this ListTransactionsRequest.

        排序字段

        :return: The order of this ListTransactionsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListTransactionsRequest.

        排序字段

        :param order: The order of this ListTransactionsRequest.
        :type order: str
        """
        self._order = order

    @property
    def order_by(self):
        r"""Gets the order_by of this ListTransactionsRequest.

        升序|降序

        :return: The order_by of this ListTransactionsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListTransactionsRequest.

        升序|降序

        :param order_by: The order_by of this ListTransactionsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def last_sec_min(self):
        r"""Gets the last_sec_min of this ListTransactionsRequest.

        持续时间下限

        :return: The last_sec_min of this ListTransactionsRequest.
        :rtype: int
        """
        return self._last_sec_min

    @last_sec_min.setter
    def last_sec_min(self, last_sec_min):
        r"""Sets the last_sec_min of this ListTransactionsRequest.

        持续时间下限

        :param last_sec_min: The last_sec_min of this ListTransactionsRequest.
        :type last_sec_min: int
        """
        self._last_sec_min = last_sec_min

    @property
    def last_sec_max(self):
        r"""Gets the last_sec_max of this ListTransactionsRequest.

        持续时间上限

        :return: The last_sec_max of this ListTransactionsRequest.
        :rtype: int
        """
        return self._last_sec_max

    @last_sec_max.setter
    def last_sec_max(self, last_sec_max):
        r"""Sets the last_sec_max of this ListTransactionsRequest.

        持续时间上限

        :param last_sec_max: The last_sec_max of this ListTransactionsRequest.
        :type last_sec_max: int
        """
        self._last_sec_max = last_sec_max

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
        if not isinstance(other, ListTransactionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
