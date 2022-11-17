# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowListPeriodHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, job_id=None, offset=None, limit=None, start_time=None, end_time=None):
        """ShowListPeriodHistoryRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID [获取项目下构建任务列表](https://support.huaweicloud.com/api-codeci/ShowJobListByProjectId.html)； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param offset: 分页页码， 表示从此页开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量，limit小于等于100
        :type limit: int
        :param start_time: 区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天
        :type start_time: str
        :param end_time: 区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天
        :type end_time: str
        """
        
        

        self._job_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.job_id = job_id
        self.offset = offset
        self.limit = limit
        self.start_time = start_time
        self.end_time = end_time

    @property
    def job_id(self):
        """Gets the job_id of this ShowListPeriodHistoryRequest.

        构建的任务ID [获取项目下构建任务列表](https://support.huaweicloud.com/api-codeci/ShowJobListByProjectId.html)； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowListPeriodHistoryRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowListPeriodHistoryRequest.

        构建的任务ID [获取项目下构建任务列表](https://support.huaweicloud.com/api-codeci/ShowJobListByProjectId.html)； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowListPeriodHistoryRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def offset(self):
        """Gets the offset of this ShowListPeriodHistoryRequest.

        分页页码， 表示从此页开始查询， offset大于等于0

        :return: The offset of this ShowListPeriodHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowListPeriodHistoryRequest.

        分页页码， 表示从此页开始查询， offset大于等于0

        :param offset: The offset of this ShowListPeriodHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowListPeriodHistoryRequest.

        每页显示的条目数量，limit小于等于100

        :return: The limit of this ShowListPeriodHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowListPeriodHistoryRequest.

        每页显示的条目数量，limit小于等于100

        :param limit: The limit of this ShowListPeriodHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ShowListPeriodHistoryRequest.

        区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :return: The start_time of this ShowListPeriodHistoryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowListPeriodHistoryRequest.

        区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :param start_time: The start_time of this ShowListPeriodHistoryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowListPeriodHistoryRequest.

        区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :return: The end_time of this ShowListPeriodHistoryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowListPeriodHistoryRequest.

        区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :param end_time: The end_time of this ShowListPeriodHistoryRequest.
        :type end_time: str
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
        if not isinstance(other, ShowListPeriodHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
