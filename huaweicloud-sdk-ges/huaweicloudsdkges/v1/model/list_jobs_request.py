# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'end_time': 'str',
        'graph_name': 'str',
        'limit': 'str',
        'offset': 'str',
        'start_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'end_time': 'endTime',
        'graph_name': 'graph_name',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'startTime',
        'status': 'status'
    }

    def __init__(self, end_time=None, graph_name=None, limit=None, offset=None, start_time=None, status=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param end_time: 任务结束日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。
        :type end_time: str
        :param graph_name: 关联的图名称
        :type graph_name: str
        :param limit: 每页资源数量的最大值，默认为10。
        :type limit: str
        :param offset: 本次请求的起始位置，默认为0。
        :type offset: str
        :param start_time: 任务开始日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。
        :type start_time: str
        :param status: 任务状态。取值为：  - running - waiting - success - failed
        :type status: str
        """
        
        

        self._end_time = None
        self._graph_name = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if graph_name is not None:
            self.graph_name = graph_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status

    @property
    def end_time(self):
        """Gets the end_time of this ListJobsRequest.

        任务结束日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。

        :return: The end_time of this ListJobsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListJobsRequest.

        任务结束日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。

        :param end_time: The end_time of this ListJobsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def graph_name(self):
        """Gets the graph_name of this ListJobsRequest.

        关联的图名称

        :return: The graph_name of this ListJobsRequest.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this ListJobsRequest.

        关联的图名称

        :param graph_name: The graph_name of this ListJobsRequest.
        :type graph_name: str
        """
        self._graph_name = graph_name

    @property
    def limit(self):
        """Gets the limit of this ListJobsRequest.

        每页资源数量的最大值，默认为10。

        :return: The limit of this ListJobsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJobsRequest.

        每页资源数量的最大值，默认为10。

        :param limit: The limit of this ListJobsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListJobsRequest.

        本次请求的起始位置，默认为0。

        :return: The offset of this ListJobsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJobsRequest.

        本次请求的起始位置，默认为0。

        :param offset: The offset of this ListJobsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def start_time(self):
        """Gets the start_time of this ListJobsRequest.

        任务开始日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。

        :return: The start_time of this ListJobsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListJobsRequest.

        任务开始日期，当前只支持日期，不支持时间。格式为：yyyy-MM-dd，比如2019-03-27。

        :param start_time: The start_time of this ListJobsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListJobsRequest.

        任务状态。取值为：  - running - waiting - success - failed

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsRequest.

        任务状态。取值为：  - running - waiting - success - failed

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
