# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'int',
        'page_num': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_num': 'page_num',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, page_size=None, page_num=None, start_time=None, end_time=None):
        r"""ShowAuditLogRequest

        The model defined in huaweicloud sdk

        :param page_size: 指定查询返回记录条数，默认值10
        :type page_size: int
        :param page_num: 索引位置，从page_num指定的下一条数据开始查询默认值为0
        :type page_num: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._page_size = None
        self._page_num = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_num is not None:
            self.page_num = page_num
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowAuditLogRequest.

        指定查询返回记录条数，默认值10

        :return: The page_size of this ShowAuditLogRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowAuditLogRequest.

        指定查询返回记录条数，默认值10

        :param page_size: The page_size of this ShowAuditLogRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowAuditLogRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :return: The page_num of this ShowAuditLogRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowAuditLogRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :param page_num: The page_num of this ShowAuditLogRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAuditLogRequest.

        开始时间

        :return: The start_time of this ShowAuditLogRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAuditLogRequest.

        开始时间

        :param start_time: The start_time of this ShowAuditLogRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAuditLogRequest.

        结束时间

        :return: The end_time of this ShowAuditLogRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAuditLogRequest.

        结束时间

        :param end_time: The end_time of this ShowAuditLogRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowAuditLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
