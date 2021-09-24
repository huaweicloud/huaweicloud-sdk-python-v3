# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainStatsResponse(SdkResponse):


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
        'interval': 'int',
        'action': 'str',
        'stat_type': 'str',
        'group_by': 'str',
        'result': 'dict(str, object)'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'interval': 'interval',
        'action': 'action',
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'result': 'result'
    }

    def __init__(self, start_time=None, end_time=None, interval=None, action=None, stat_type=None, group_by=None, result=None):
        """ShowDomainStatsResponse - a model defined in huaweicloud sdk"""
        
        super(ShowDomainStatsResponse, self).__init__()

        self._start_time = None
        self._end_time = None
        self._interval = None
        self._action = None
        self._stat_type = None
        self._group_by = None
        self._result = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if interval is not None:
            self.interval = interval
        if action is not None:
            self.action = action
        if stat_type is not None:
            self.stat_type = stat_type
        if group_by is not None:
            self.group_by = group_by
        if result is not None:
            self.result = result

    @property
    def start_time(self):
        """Gets the start_time of this ShowDomainStatsResponse.

        数据起始时间戳，可能不返回

        :return: The start_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowDomainStatsResponse.

        数据起始时间戳，可能不返回

        :param start_time: The start_time of this ShowDomainStatsResponse.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowDomainStatsResponse.

        数据结束时间戳，可能不返回

        :return: The end_time of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowDomainStatsResponse.

        数据结束时间戳，可能不返回

        :param end_time: The end_time of this ShowDomainStatsResponse.
        :type: int
        """
        self._end_time = end_time

    @property
    def interval(self):
        """Gets the interval of this ShowDomainStatsResponse.

        查询间隔，可能不返回

        :return: The interval of this ShowDomainStatsResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowDomainStatsResponse.

        查询间隔，可能不返回

        :param interval: The interval of this ShowDomainStatsResponse.
        :type: int
        """
        self._interval = interval

    @property
    def action(self):
        """Gets the action of this ShowDomainStatsResponse.

        查询类型，可能不返回

        :return: The action of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowDomainStatsResponse.

        查询类型，可能不返回

        :param action: The action of this ShowDomainStatsResponse.
        :type: str
        """
        self._action = action

    @property
    def stat_type(self):
        """Gets the stat_type of this ShowDomainStatsResponse.

        指标类型，可能不返回

        :return: The stat_type of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this ShowDomainStatsResponse.

        指标类型，可能不返回

        :param stat_type: The stat_type of this ShowDomainStatsResponse.
        :type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        """Gets the group_by of this ShowDomainStatsResponse.

        分组类型，可能不返回

        :return: The group_by of this ShowDomainStatsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ShowDomainStatsResponse.

        分组类型，可能不返回

        :param group_by: The group_by of this ShowDomainStatsResponse.
        :type: str
        """
        self._group_by = group_by

    @property
    def result(self):
        """Gets the result of this ShowDomainStatsResponse.

        返回数据体

        :return: The result of this ShowDomainStatsResponse.
        :rtype: dict(str, object)
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowDomainStatsResponse.

        返回数据体

        :param result: The result of this ShowDomainStatsResponse.
        :type: dict(str, object)
        """
        self._result = result

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
        if not isinstance(other, ShowDomainStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
