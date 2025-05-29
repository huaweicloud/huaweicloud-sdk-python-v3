# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBuildInfoRecordByJobIdRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'page_index': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page_index': 'page_index',
        'page_size': 'page_size'
    }

    def __init__(self, job_id=None, start_time=None, end_time=None, page_index=None, page_size=None):
        r"""ListBuildInfoRecordByJobIdRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param start_time: 区间开始时间，格式yyyy-MM-dd HH:mm:ss。
        :type start_time: str
        :param end_time: 区间结束时间，格式yyyy-MM-dd HH:mm:ss。
        :type end_time: str
        :param page_index: 分页页码，表示从此页开始查询， page_index大于等于0
        :type page_index: int
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        """
        
        

        self._job_id = None
        self._start_time = None
        self._end_time = None
        self._page_index = None
        self._page_size = None
        self.discriminator = None

        self.job_id = job_id
        self.start_time = start_time
        self.end_time = end_time
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size

    @property
    def job_id(self):
        r"""Gets the job_id of this ListBuildInfoRecordByJobIdRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ListBuildInfoRecordByJobIdRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListBuildInfoRecordByJobIdRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ListBuildInfoRecordByJobIdRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListBuildInfoRecordByJobIdRequest.

        区间开始时间，格式yyyy-MM-dd HH:mm:ss。

        :return: The start_time of this ListBuildInfoRecordByJobIdRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListBuildInfoRecordByJobIdRequest.

        区间开始时间，格式yyyy-MM-dd HH:mm:ss。

        :param start_time: The start_time of this ListBuildInfoRecordByJobIdRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBuildInfoRecordByJobIdRequest.

        区间结束时间，格式yyyy-MM-dd HH:mm:ss。

        :return: The end_time of this ListBuildInfoRecordByJobIdRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBuildInfoRecordByJobIdRequest.

        区间结束时间，格式yyyy-MM-dd HH:mm:ss。

        :param end_time: The end_time of this ListBuildInfoRecordByJobIdRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def page_index(self):
        r"""Gets the page_index of this ListBuildInfoRecordByJobIdRequest.

        分页页码，表示从此页开始查询， page_index大于等于0

        :return: The page_index of this ListBuildInfoRecordByJobIdRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListBuildInfoRecordByJobIdRequest.

        分页页码，表示从此页开始查询， page_index大于等于0

        :param page_index: The page_index of this ListBuildInfoRecordByJobIdRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListBuildInfoRecordByJobIdRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListBuildInfoRecordByJobIdRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListBuildInfoRecordByJobIdRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListBuildInfoRecordByJobIdRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListBuildInfoRecordByJobIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
