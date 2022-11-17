# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOnlineInfoNewRequest:

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
        'query_type': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'query_type': 'query_type'
    }

    def __init__(self, start_time=None, end_time=None, query_type=None):
        """ListHistoryOnlineInfoNewRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。
        :type start_time: str
        :param end_time: 查询的结束时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。
        :type end_time: str
        :param query_type: 查询类型，类型查询优先于时间查询。类型查询和时间查询必须有一个存在。 -MONTH：按月查询。 -WEEK：按周查询。 -DAY：按天查询。
        :type query_type: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._query_type = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if query_type is not None:
            self.query_type = query_type

    @property
    def start_time(self):
        """Gets the start_time of this ListHistoryOnlineInfoNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。

        :return: The start_time of this ListHistoryOnlineInfoNewRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListHistoryOnlineInfoNewRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。

        :param start_time: The start_time of this ListHistoryOnlineInfoNewRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListHistoryOnlineInfoNewRequest.

        查询的结束时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。

        :return: The end_time of this ListHistoryOnlineInfoNewRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListHistoryOnlineInfoNewRequest.

        查询的结束时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数。类型查询优先于时间查询。类型查询和时间查询必须有一个存在。

        :param end_time: The end_time of this ListHistoryOnlineInfoNewRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def query_type(self):
        """Gets the query_type of this ListHistoryOnlineInfoNewRequest.

        查询类型，类型查询优先于时间查询。类型查询和时间查询必须有一个存在。 -MONTH：按月查询。 -WEEK：按周查询。 -DAY：按天查询。

        :return: The query_type of this ListHistoryOnlineInfoNewRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListHistoryOnlineInfoNewRequest.

        查询类型，类型查询优先于时间查询。类型查询和时间查询必须有一个存在。 -MONTH：按月查询。 -WEEK：按周查询。 -DAY：按天查询。

        :param query_type: The query_type of this ListHistoryOnlineInfoNewRequest.
        :type query_type: str
        """
        self._query_type = query_type

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
        if not isinstance(other, ListHistoryOnlineInfoNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
