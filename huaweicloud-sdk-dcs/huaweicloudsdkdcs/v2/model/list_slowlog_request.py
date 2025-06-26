# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowlogRequest:

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
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'role': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'role': 'role'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, start_time=None, end_time=None, role=None):
        r"""ListSlowlogRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param sort_key: 返回结果按该关键字排序，支持start_time，duration，默认为“start_time”
        :type sort_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为“desc”）
        :type sort_dir: str
        :param start_time: 查询开始时间，时间为UTC时间的Unix时间戳。如：1598803200000。
        :type start_time: str
        :param end_time: 查询结束时间，时间为UTC时间的Unix时间戳。如：1599494399000。
        :type end_time: str
        :param role: 查询节点，分为proxy和server。
        :type role: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._start_time = None
        self._end_time = None
        self._role = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        self.start_time = start_time
        self.end_time = end_time
        if role is not None:
            self.role = role

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSlowlogRequest.

        实例ID。

        :return: The instance_id of this ListSlowlogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSlowlogRequest.

        实例ID。

        :param instance_id: The instance_id of this ListSlowlogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSlowlogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListSlowlogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSlowlogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListSlowlogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSlowlogRequest.

        每页显示的条目数量。

        :return: The limit of this ListSlowlogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSlowlogRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListSlowlogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSlowlogRequest.

        返回结果按该关键字排序，支持start_time，duration，默认为“start_time”

        :return: The sort_key of this ListSlowlogRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSlowlogRequest.

        返回结果按该关键字排序，支持start_time，duration，默认为“start_time”

        :param sort_key: The sort_key of this ListSlowlogRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSlowlogRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）

        :return: The sort_dir of this ListSlowlogRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSlowlogRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）

        :param sort_dir: The sort_dir of this ListSlowlogRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSlowlogRequest.

        查询开始时间，时间为UTC时间的Unix时间戳。如：1598803200000。

        :return: The start_time of this ListSlowlogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSlowlogRequest.

        查询开始时间，时间为UTC时间的Unix时间戳。如：1598803200000。

        :param start_time: The start_time of this ListSlowlogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSlowlogRequest.

        查询结束时间，时间为UTC时间的Unix时间戳。如：1599494399000。

        :return: The end_time of this ListSlowlogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSlowlogRequest.

        查询结束时间，时间为UTC时间的Unix时间戳。如：1599494399000。

        :param end_time: The end_time of this ListSlowlogRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def role(self):
        r"""Gets the role of this ListSlowlogRequest.

        查询节点，分为proxy和server。

        :return: The role of this ListSlowlogRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ListSlowlogRequest.

        查询节点，分为proxy和server。

        :param role: The role of this ListSlowlogRequest.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, ListSlowlogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
