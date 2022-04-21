# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLatelyGroupStatisticsV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'msg': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'list': 'list[StatisticsGroup]'
    }

    attribute_map = {
        'code': 'code',
        'msg': 'msg',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'list': 'list'
    }

    def __init__(self, code=None, msg=None, start_time=None, end_time=None, list=None):
        """ListLatelyGroupStatisticsV2Response

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param msg: 返回消息
        :type msg: str
        :param start_time: 开始时间的UTC的时间戳
        :type start_time: int
        :param end_time: 截止时间的UTC的时间戳
        :type end_time: int
        :param list: 统计指标的数据结构结构体
        :type list: list[:class:`huaweicloudsdkapig.v2.StatisticsGroup`]
        """
        
        super(ListLatelyGroupStatisticsV2Response, self).__init__()

        self._code = None
        self._msg = None
        self._start_time = None
        self._end_time = None
        self._list = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if list is not None:
            self.list = list

    @property
    def code(self):
        """Gets the code of this ListLatelyGroupStatisticsV2Response.

        响应码

        :return: The code of this ListLatelyGroupStatisticsV2Response.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListLatelyGroupStatisticsV2Response.

        响应码

        :param code: The code of this ListLatelyGroupStatisticsV2Response.
        :type code: str
        """
        self._code = code

    @property
    def msg(self):
        """Gets the msg of this ListLatelyGroupStatisticsV2Response.

        返回消息

        :return: The msg of this ListLatelyGroupStatisticsV2Response.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this ListLatelyGroupStatisticsV2Response.

        返回消息

        :param msg: The msg of this ListLatelyGroupStatisticsV2Response.
        :type msg: str
        """
        self._msg = msg

    @property
    def start_time(self):
        """Gets the start_time of this ListLatelyGroupStatisticsV2Response.

        开始时间的UTC的时间戳

        :return: The start_time of this ListLatelyGroupStatisticsV2Response.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListLatelyGroupStatisticsV2Response.

        开始时间的UTC的时间戳

        :param start_time: The start_time of this ListLatelyGroupStatisticsV2Response.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListLatelyGroupStatisticsV2Response.

        截止时间的UTC的时间戳

        :return: The end_time of this ListLatelyGroupStatisticsV2Response.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListLatelyGroupStatisticsV2Response.

        截止时间的UTC的时间戳

        :param end_time: The end_time of this ListLatelyGroupStatisticsV2Response.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def list(self):
        """Gets the list of this ListLatelyGroupStatisticsV2Response.

        统计指标的数据结构结构体

        :return: The list of this ListLatelyGroupStatisticsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.StatisticsGroup`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ListLatelyGroupStatisticsV2Response.

        统计指标的数据结构结构体

        :param list: The list of this ListLatelyGroupStatisticsV2Response.
        :type list: list[:class:`huaweicloudsdkapig.v2.StatisticsGroup`]
        """
        self._list = list

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
        if not isinstance(other, ListLatelyGroupStatisticsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
