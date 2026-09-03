# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBinlogFilesRequestBody:

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
        'cur_page': 'int',
        'per_page': 'int',
        'binlog_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'binlog_type': 'binlog_type'
    }

    def __init__(self, start_time=None, end_time=None, cur_page=None, per_page=None, binlog_type=None):
        r"""ListBinlogFilesRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param cur_page: 当前页
        :type cur_page: int
        :param per_page: 分页大小
        :type per_page: int
        :param binlog_type: binlog类型
        :type binlog_type: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._cur_page = None
        self._per_page = None
        self._binlog_type = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        self.binlog_type = binlog_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBinlogFilesRequestBody.

        开始时间

        :return: The start_time of this ListBinlogFilesRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBinlogFilesRequestBody.

        开始时间

        :param start_time: The start_time of this ListBinlogFilesRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBinlogFilesRequestBody.

        结束时间

        :return: The end_time of this ListBinlogFilesRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBinlogFilesRequestBody.

        结束时间

        :param end_time: The end_time of this ListBinlogFilesRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListBinlogFilesRequestBody.

        当前页

        :return: The cur_page of this ListBinlogFilesRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListBinlogFilesRequestBody.

        当前页

        :param cur_page: The cur_page of this ListBinlogFilesRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListBinlogFilesRequestBody.

        分页大小

        :return: The per_page of this ListBinlogFilesRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListBinlogFilesRequestBody.

        分页大小

        :param per_page: The per_page of this ListBinlogFilesRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def binlog_type(self):
        r"""Gets the binlog_type of this ListBinlogFilesRequestBody.

        binlog类型

        :return: The binlog_type of this ListBinlogFilesRequestBody.
        :rtype: str
        """
        return self._binlog_type

    @binlog_type.setter
    def binlog_type(self, binlog_type):
        r"""Sets the binlog_type of this ListBinlogFilesRequestBody.

        binlog类型

        :param binlog_type: The binlog_type of this ListBinlogFilesRequestBody.
        :type binlog_type: str
        """
        self._binlog_type = binlog_type

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
        if not isinstance(other, ListBinlogFilesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
