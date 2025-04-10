# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmsDetailsRequest:

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
        'offset': 'int',
        'cid': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'cid': 'cid',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, limit=None, offset=None, cid=None, start_time=None, end_time=None):
        r"""ListSmsDetailsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        :param cid: 容器ID
        :type cid: str
        :param start_time: 开始时间
        :type start_time: datetime
        :param end_time: 结束时间
        :type end_time: datetime
        """
        
        

        self._limit = None
        self._offset = None
        self._cid = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if cid is not None:
            self.cid = cid
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListSmsDetailsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListSmsDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSmsDetailsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListSmsDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSmsDetailsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListSmsDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSmsDetailsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListSmsDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def cid(self):
        r"""Gets the cid of this ListSmsDetailsRequest.

        容器ID

        :return: The cid of this ListSmsDetailsRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        r"""Sets the cid of this ListSmsDetailsRequest.

        容器ID

        :param cid: The cid of this ListSmsDetailsRequest.
        :type cid: str
        """
        self._cid = cid

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSmsDetailsRequest.

        开始时间

        :return: The start_time of this ListSmsDetailsRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSmsDetailsRequest.

        开始时间

        :param start_time: The start_time of this ListSmsDetailsRequest.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSmsDetailsRequest.

        结束时间

        :return: The end_time of this ListSmsDetailsRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSmsDetailsRequest.

        结束时间

        :param end_time: The end_time of this ListSmsDetailsRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

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
        if not isinstance(other, ListSmsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
