# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'datetime',
        'page': 'int',
        'size': 'int',
        'start_time': 'datetime'
    }

    attribute_map = {
        'end_time': 'end_time',
        'page': 'page',
        'size': 'size',
        'start_time': 'start_time'
    }

    def __init__(self, end_time=None, page=None, size=None, start_time=None):
        r"""BackupPageRequest

        The model defined in huaweicloud sdk

        :param end_time: 结束时间
        :type end_time: datetime
        :param page: 当前页码
        :type page: int
        :param size: 分页大小
        :type size: int
        :param start_time: 开始时间,yyyy-MM-dd HH:mm:ss
        :type start_time: datetime
        """
        
        

        self._end_time = None
        self._page = None
        self._size = None
        self._start_time = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        self.page = page
        self.size = size
        if start_time is not None:
            self.start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BackupPageRequest.

        结束时间

        :return: The end_time of this BackupPageRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BackupPageRequest.

        结束时间

        :param end_time: The end_time of this BackupPageRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def page(self):
        r"""Gets the page of this BackupPageRequest.

        当前页码

        :return: The page of this BackupPageRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this BackupPageRequest.

        当前页码

        :param page: The page of this BackupPageRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this BackupPageRequest.

        分页大小

        :return: The size of this BackupPageRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackupPageRequest.

        分页大小

        :param size: The size of this BackupPageRequest.
        :type size: int
        """
        self._size = size

    @property
    def start_time(self):
        r"""Gets the start_time of this BackupPageRequest.

        开始时间,yyyy-MM-dd HH:mm:ss

        :return: The start_time of this BackupPageRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BackupPageRequest.

        开始时间,yyyy-MM-dd HH:mm:ss

        :param start_time: The start_time of this BackupPageRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

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
        if not isinstance(other, BackupPageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
