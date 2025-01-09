# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryOnlineInfoRequest:

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
        'query_type': 'str',
        'client_hour': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'query_type': 'query_type',
        'client_hour': 'client_hour'
    }

    def __init__(self, start_time=None, end_time=None, query_type=None, client_hour=None):
        """ListHistoryOnlineInfoRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数
        :type start_time: str
        :param end_time: 查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数
        :type end_time: str
        :param query_type: 查询类型，合法取值有三个:MONTH按月查询 WEEK：按周查询DAY：按天查询
        :type query_type: str
        :param client_hour: 客户端所在操作系统时间的小时数
        :type client_hour: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._query_type = None
        self._client_hour = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if query_type is not None:
            self.query_type = query_type
        if client_hour is not None:
            self.client_hour = client_hour

    @property
    def start_time(self):
        """Gets the start_time of this ListHistoryOnlineInfoRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数

        :return: The start_time of this ListHistoryOnlineInfoRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListHistoryOnlineInfoRequest.

        查询的起始时间。指定该参数后，返回的结果为此时间之后的所有登录记录。时间格式如：“2016-08-20T21:11Z”。终止时间不为空时，起始时间为必填参数

        :param start_time: The start_time of this ListHistoryOnlineInfoRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListHistoryOnlineInfoRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数

        :return: The end_time of this ListHistoryOnlineInfoRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListHistoryOnlineInfoRequest.

        查询的终止时间。指定该参数后，返回的结果为此时间之前的所有登录记录。时间格式如：“2016-08-20T21:11Z”。起始时间不为空时，终止时间为必填参数

        :param end_time: The end_time of this ListHistoryOnlineInfoRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def query_type(self):
        """Gets the query_type of this ListHistoryOnlineInfoRequest.

        查询类型，合法取值有三个:MONTH按月查询 WEEK：按周查询DAY：按天查询

        :return: The query_type of this ListHistoryOnlineInfoRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListHistoryOnlineInfoRequest.

        查询类型，合法取值有三个:MONTH按月查询 WEEK：按周查询DAY：按天查询

        :param query_type: The query_type of this ListHistoryOnlineInfoRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def client_hour(self):
        """Gets the client_hour of this ListHistoryOnlineInfoRequest.

        客户端所在操作系统时间的小时数

        :return: The client_hour of this ListHistoryOnlineInfoRequest.
        :rtype: int
        """
        return self._client_hour

    @client_hour.setter
    def client_hour(self, client_hour):
        """Sets the client_hour of this ListHistoryOnlineInfoRequest.

        客户端所在操作系统时间的小时数

        :param client_hour: The client_hour of this ListHistoryOnlineInfoRequest.
        :type client_hour: int
        """
        self._client_hour = client_hour

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
        if not isinstance(other, ListHistoryOnlineInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
