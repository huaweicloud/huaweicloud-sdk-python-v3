# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'module': 'int',
        'start_at': 'int',
        'end_at': 'int',
        'per_page': 'int',
        'cur_page': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'module': 'module',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'per_page': 'per_page',
        'cur_page': 'cur_page',
        'x_language': 'X-Language'
    }

    def __init__(self, connection_id=None, module=None, start_at=None, end_at=None, per_page=None, cur_page=None, x_language=None):
        r"""ListSnapshotsRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接id
        :type connection_id: str
        :param module: 锁类型， 检查死锁为2
        :type module: int
        :param start_at: 开始时间
        :type start_at: int
        :param end_at: 结束时间
        :type end_at: int
        :param per_page: 每页返回的数量，默认值为10
        :type per_page: int
        :param cur_page: 当前页码，第一次查询的时候默认值为1
        :type cur_page: int
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._connection_id = None
        self._module = None
        self._start_at = None
        self._end_at = None
        self._per_page = None
        self._cur_page = None
        self._x_language = None
        self.discriminator = None

        self.connection_id = connection_id
        self.module = module
        self.start_at = start_at
        self.end_at = end_at
        if per_page is not None:
            self.per_page = per_page
        if cur_page is not None:
            self.cur_page = cur_page
        if x_language is not None:
            self.x_language = x_language

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSnapshotsRequest.

        连接id

        :return: The connection_id of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSnapshotsRequest.

        连接id

        :param connection_id: The connection_id of this ListSnapshotsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def module(self):
        r"""Gets the module of this ListSnapshotsRequest.

        锁类型， 检查死锁为2

        :return: The module of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this ListSnapshotsRequest.

        锁类型， 检查死锁为2

        :param module: The module of this ListSnapshotsRequest.
        :type module: int
        """
        self._module = module

    @property
    def start_at(self):
        r"""Gets the start_at of this ListSnapshotsRequest.

        开始时间

        :return: The start_at of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListSnapshotsRequest.

        开始时间

        :param start_at: The start_at of this ListSnapshotsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListSnapshotsRequest.

        结束时间

        :return: The end_at of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListSnapshotsRequest.

        结束时间

        :param end_at: The end_at of this ListSnapshotsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def per_page(self):
        r"""Gets the per_page of this ListSnapshotsRequest.

        每页返回的数量，默认值为10

        :return: The per_page of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListSnapshotsRequest.

        每页返回的数量，默认值为10

        :param per_page: The per_page of this ListSnapshotsRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListSnapshotsRequest.

        当前页码，第一次查询的时候默认值为1

        :return: The cur_page of this ListSnapshotsRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListSnapshotsRequest.

        当前页码，第一次查询的时候默认值为1

        :param cur_page: The cur_page of this ListSnapshotsRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSnapshotsRequest.

        语言

        :return: The x_language of this ListSnapshotsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSnapshotsRequest.

        语言

        :param x_language: The x_language of this ListSnapshotsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
