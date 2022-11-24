# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowInstanceRequest:

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
        'graph_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'graph_name': 'graph_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'offset': 'offset'
    }

    def __init__(self, limit=None, graph_name=None, start_time=None, end_time=None, status=None, offset=None):
        """ListWorkflowInstanceRequest

        The model defined in huaweicloud sdk

        :param limit: 请求返回的最大记录条数。分页查询，每页显示的条目数量，最大数量200，超过200后只返回200
        :type limit: int
        :param graph_name: 工作流名称。
        :type graph_name: str
        :param start_time: 查询开始时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间
        :type start_time: str
        :param end_time: 查询终止时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。
        :type end_time: str
        :param status: 需要过滤的流程实例状态  最小长度：0  最大长度：64  枚举值：  success  fail  running  timeout  cancel
        :type status: str
        :param offset: 查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。
        :type offset: int
        """
        
        

        self._limit = None
        self._graph_name = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._offset = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        self.graph_name = graph_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListWorkflowInstanceRequest.

        请求返回的最大记录条数。分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :return: The limit of this ListWorkflowInstanceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkflowInstanceRequest.

        请求返回的最大记录条数。分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :param limit: The limit of this ListWorkflowInstanceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def graph_name(self):
        """Gets the graph_name of this ListWorkflowInstanceRequest.

        工作流名称。

        :return: The graph_name of this ListWorkflowInstanceRequest.
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this ListWorkflowInstanceRequest.

        工作流名称。

        :param graph_name: The graph_name of this ListWorkflowInstanceRequest.
        :type graph_name: str
        """
        self._graph_name = graph_name

    @property
    def start_time(self):
        """Gets the start_time of this ListWorkflowInstanceRequest.

        查询开始时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间

        :return: The start_time of this ListWorkflowInstanceRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListWorkflowInstanceRequest.

        查询开始时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间

        :param start_time: The start_time of this ListWorkflowInstanceRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListWorkflowInstanceRequest.

        查询终止时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :return: The end_time of this ListWorkflowInstanceRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListWorkflowInstanceRequest.

        查询终止时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :param end_time: The end_time of this ListWorkflowInstanceRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListWorkflowInstanceRequest.

        需要过滤的流程实例状态  最小长度：0  最大长度：64  枚举值：  success  fail  running  timeout  cancel

        :return: The status of this ListWorkflowInstanceRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListWorkflowInstanceRequest.

        需要过滤的流程实例状态  最小长度：0  最大长度：64  枚举值：  success  fail  running  timeout  cancel

        :param status: The status of this ListWorkflowInstanceRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        """Gets the offset of this ListWorkflowInstanceRequest.

        查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。

        :return: The offset of this ListWorkflowInstanceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkflowInstanceRequest.

        查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。

        :param offset: The offset of this ListWorkflowInstanceRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListWorkflowInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
