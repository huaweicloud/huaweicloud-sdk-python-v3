# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppUserAccessDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'username': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'username': 'username',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, username=None, sort_field=None, sort_type=None, offset=None, limit=None):
        r"""ListAppUserAccessDataRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间，格式为：UTC格式，例如\&quot;2022-05-11T11:45:42Z。\&quot;
        :type start_time: str
        :param end_time: 查询截至时间，格式为：UTC格式，例如\&quot;2022-05-11T11:45:42Z。\&quot;
        :type end_time: str
        :param username: 用户名(模糊匹配)。
        :type username: str
        :param sort_field: 按照指标进行排序 * &#x60;access_failed_count&#x60; -  按照接入失败数排序 * &#x60;last_access_failed_time&#x60; -  按照最近接入失败时间排序
        :type sort_field: str
        :param sort_type: 按照指标进行排序的方向;需配合sort_field一起使用 * &#x60;DESC&#x60; - 降序返回数据 * &#x60;ASC&#x60; -  升序返回数据
        :type sort_type: str
        :param offset: 查询的偏移量,默认值0。
        :type offset: int
        :param limit: limit范围[1-100],默认值10。
        :type limit: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._username = None
        self._sort_field = None
        self._sort_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if username is not None:
            self.username = username
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAppUserAccessDataRequest.

        查询起始时间，格式为：UTC格式，例如\"2022-05-11T11:45:42Z。\"

        :return: The start_time of this ListAppUserAccessDataRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAppUserAccessDataRequest.

        查询起始时间，格式为：UTC格式，例如\"2022-05-11T11:45:42Z。\"

        :param start_time: The start_time of this ListAppUserAccessDataRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAppUserAccessDataRequest.

        查询截至时间，格式为：UTC格式，例如\"2022-05-11T11:45:42Z。\"

        :return: The end_time of this ListAppUserAccessDataRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAppUserAccessDataRequest.

        查询截至时间，格式为：UTC格式，例如\"2022-05-11T11:45:42Z。\"

        :param end_time: The end_time of this ListAppUserAccessDataRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def username(self):
        r"""Gets the username of this ListAppUserAccessDataRequest.

        用户名(模糊匹配)。

        :return: The username of this ListAppUserAccessDataRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListAppUserAccessDataRequest.

        用户名(模糊匹配)。

        :param username: The username of this ListAppUserAccessDataRequest.
        :type username: str
        """
        self._username = username

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListAppUserAccessDataRequest.

        按照指标进行排序 * `access_failed_count` -  按照接入失败数排序 * `last_access_failed_time` -  按照最近接入失败时间排序

        :return: The sort_field of this ListAppUserAccessDataRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListAppUserAccessDataRequest.

        按照指标进行排序 * `access_failed_count` -  按照接入失败数排序 * `last_access_failed_time` -  按照最近接入失败时间排序

        :param sort_field: The sort_field of this ListAppUserAccessDataRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListAppUserAccessDataRequest.

        按照指标进行排序的方向;需配合sort_field一起使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :return: The sort_type of this ListAppUserAccessDataRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListAppUserAccessDataRequest.

        按照指标进行排序的方向;需配合sort_field一起使用 * `DESC` - 降序返回数据 * `ASC` -  升序返回数据

        :param sort_type: The sort_type of this ListAppUserAccessDataRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def offset(self):
        r"""Gets the offset of this ListAppUserAccessDataRequest.

        查询的偏移量,默认值0。

        :return: The offset of this ListAppUserAccessDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppUserAccessDataRequest.

        查询的偏移量,默认值0。

        :param offset: The offset of this ListAppUserAccessDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAppUserAccessDataRequest.

        limit范围[1-100],默认值10。

        :return: The limit of this ListAppUserAccessDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppUserAccessDataRequest.

        limit范围[1-100],默认值10。

        :param limit: The limit of this ListAppUserAccessDataRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAppUserAccessDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
