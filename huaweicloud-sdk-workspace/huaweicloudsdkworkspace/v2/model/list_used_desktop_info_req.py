# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsedDesktopInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'desktop_username': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'desktop_username': 'desktop_username',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, desktop_ids=None, start_time=None, end_time=None, desktop_username=None, offset=None, limit=None):
        """ListUsedDesktopInfoReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面id集合。
        :type desktop_ids: list[str]
        :param start_time: 开始时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。
        :type start_time: str
        :param end_time: 结束时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。
        :type end_time: str
        :param desktop_username: 若传桌面的用户名，则查询使用时间只有该用户的使用时间。
        :type desktop_username: str
        :param offset: 从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。
        :type offset: int
        :param limit: 查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-100，默认值100。
        :type limit: int
        """
        
        

        self._desktop_ids = None
        self._start_time = None
        self._end_time = None
        self._desktop_username = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if desktop_username is not None:
            self.desktop_username = desktop_username
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def desktop_ids(self):
        """Gets the desktop_ids of this ListUsedDesktopInfoReq.

        桌面id集合。

        :return: The desktop_ids of this ListUsedDesktopInfoReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        """Sets the desktop_ids of this ListUsedDesktopInfoReq.

        桌面id集合。

        :param desktop_ids: The desktop_ids of this ListUsedDesktopInfoReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def start_time(self):
        """Gets the start_time of this ListUsedDesktopInfoReq.

        开始时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。

        :return: The start_time of this ListUsedDesktopInfoReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListUsedDesktopInfoReq.

        开始时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。

        :param start_time: The start_time of this ListUsedDesktopInfoReq.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListUsedDesktopInfoReq.

        结束时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。

        :return: The end_time of this ListUsedDesktopInfoReq.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListUsedDesktopInfoReq.

        结束时间，格式：yyyy-MM-dd（UTC时间，不传查默认最近15天）最多查31天数据。

        :param end_time: The end_time of this ListUsedDesktopInfoReq.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def desktop_username(self):
        """Gets the desktop_username of this ListUsedDesktopInfoReq.

        若传桌面的用户名，则查询使用时间只有该用户的使用时间。

        :return: The desktop_username of this ListUsedDesktopInfoReq.
        :rtype: str
        """
        return self._desktop_username

    @desktop_username.setter
    def desktop_username(self, desktop_username):
        """Sets the desktop_username of this ListUsedDesktopInfoReq.

        若传桌面的用户名，则查询使用时间只有该用户的使用时间。

        :param desktop_username: The desktop_username of this ListUsedDesktopInfoReq.
        :type desktop_username: str
        """
        self._desktop_username = desktop_username

    @property
    def offset(self):
        """Gets the offset of this ListUsedDesktopInfoReq.

        从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。

        :return: The offset of this ListUsedDesktopInfoReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUsedDesktopInfoReq.

        从查询结果中的第几条数据开始返回,用于分页查询，取值范围0-2000，默认从0开始。

        :param offset: The offset of this ListUsedDesktopInfoReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListUsedDesktopInfoReq.

        查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-100，默认值100。

        :return: The limit of this ListUsedDesktopInfoReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsedDesktopInfoReq.

        查询结果中想要返回的信息条目数量,用于分页查询，取值范围0-100，默认值100。

        :param limit: The limit of this ListUsedDesktopInfoReq.
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
        if not isinstance(other, ListUsedDesktopInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
