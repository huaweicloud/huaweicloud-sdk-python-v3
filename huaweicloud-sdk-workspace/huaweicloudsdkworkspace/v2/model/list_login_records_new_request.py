# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoginRecordsNewRequest:

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
        'user_name': 'str',
        'computer_name': 'str',
        'terminal_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'min_network_rtt': 'int',
        'max_network_rtt': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'user_name': 'user_name',
        'computer_name': 'computer_name',
        'terminal_type': 'terminal_type',
        'offset': 'offset',
        'limit': 'limit',
        'min_network_rtt': 'min_network_rtt',
        'max_network_rtt': 'max_network_rtt'
    }

    def __init__(self, start_time=None, end_time=None, user_name=None, computer_name=None, terminal_type=None, offset=None, limit=None, min_network_rtt=None, max_network_rtt=None):
        r"""ListLoginRecordsNewRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。
        :type start_time: str
        :param end_time: 查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。
        :type end_time: str
        :param user_name: 登录桌面的用户名。
        :type user_name: str
        :param computer_name: 计算机名（操作系统信息中可见）。
        :type computer_name: str
        :param terminal_type: 登录桌面的终端系统类型，当前支持：WI（云桌面客户端）。
        :type terminal_type: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回登录记录数量限制,取值范围0-1000。如果不指定，默认为20。
        :type limit: int
        :param min_network_rtt: 查询端到端时延的最小值。
        :type min_network_rtt: int
        :param max_network_rtt: 查询端到端时延的最大值。
        :type max_network_rtt: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._user_name = None
        self._computer_name = None
        self._terminal_type = None
        self._offset = None
        self._limit = None
        self._min_network_rtt = None
        self._max_network_rtt = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if user_name is not None:
            self.user_name = user_name
        if computer_name is not None:
            self.computer_name = computer_name
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if min_network_rtt is not None:
            self.min_network_rtt = min_network_rtt
        if max_network_rtt is not None:
            self.max_network_rtt = max_network_rtt

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLoginRecordsNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。

        :return: The start_time of this ListLoginRecordsNewRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLoginRecordsNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。

        :param start_time: The start_time of this ListLoginRecordsNewRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLoginRecordsNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。

        :return: The end_time of this ListLoginRecordsNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLoginRecordsNewRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。

        :param end_time: The end_time of this ListLoginRecordsNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def user_name(self):
        r"""Gets the user_name of this ListLoginRecordsNewRequest.

        登录桌面的用户名。

        :return: The user_name of this ListLoginRecordsNewRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListLoginRecordsNewRequest.

        登录桌面的用户名。

        :param user_name: The user_name of this ListLoginRecordsNewRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def computer_name(self):
        r"""Gets the computer_name of this ListLoginRecordsNewRequest.

        计算机名（操作系统信息中可见）。

        :return: The computer_name of this ListLoginRecordsNewRequest.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this ListLoginRecordsNewRequest.

        计算机名（操作系统信息中可见）。

        :param computer_name: The computer_name of this ListLoginRecordsNewRequest.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def terminal_type(self):
        r"""Gets the terminal_type of this ListLoginRecordsNewRequest.

        登录桌面的终端系统类型，当前支持：WI（云桌面客户端）。

        :return: The terminal_type of this ListLoginRecordsNewRequest.
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        r"""Sets the terminal_type of this ListLoginRecordsNewRequest.

        登录桌面的终端系统类型，当前支持：WI（云桌面客户端）。

        :param terminal_type: The terminal_type of this ListLoginRecordsNewRequest.
        :type terminal_type: str
        """
        self._terminal_type = terminal_type

    @property
    def offset(self):
        r"""Gets the offset of this ListLoginRecordsNewRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListLoginRecordsNewRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLoginRecordsNewRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListLoginRecordsNewRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLoginRecordsNewRequest.

        用于分页查询，返回登录记录数量限制,取值范围0-1000。如果不指定，默认为20。

        :return: The limit of this ListLoginRecordsNewRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLoginRecordsNewRequest.

        用于分页查询，返回登录记录数量限制,取值范围0-1000。如果不指定，默认为20。

        :param limit: The limit of this ListLoginRecordsNewRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def min_network_rtt(self):
        r"""Gets the min_network_rtt of this ListLoginRecordsNewRequest.

        查询端到端时延的最小值。

        :return: The min_network_rtt of this ListLoginRecordsNewRequest.
        :rtype: int
        """
        return self._min_network_rtt

    @min_network_rtt.setter
    def min_network_rtt(self, min_network_rtt):
        r"""Sets the min_network_rtt of this ListLoginRecordsNewRequest.

        查询端到端时延的最小值。

        :param min_network_rtt: The min_network_rtt of this ListLoginRecordsNewRequest.
        :type min_network_rtt: int
        """
        self._min_network_rtt = min_network_rtt

    @property
    def max_network_rtt(self):
        r"""Gets the max_network_rtt of this ListLoginRecordsNewRequest.

        查询端到端时延的最大值。

        :return: The max_network_rtt of this ListLoginRecordsNewRequest.
        :rtype: int
        """
        return self._max_network_rtt

    @max_network_rtt.setter
    def max_network_rtt(self, max_network_rtt):
        r"""Sets the max_network_rtt of this ListLoginRecordsNewRequest.

        查询端到端时延的最大值。

        :param max_network_rtt: The max_network_rtt of this ListLoginRecordsNewRequest.
        :type max_network_rtt: int
        """
        self._max_network_rtt = max_network_rtt

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
        if not isinstance(other, ListLoginRecordsNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
