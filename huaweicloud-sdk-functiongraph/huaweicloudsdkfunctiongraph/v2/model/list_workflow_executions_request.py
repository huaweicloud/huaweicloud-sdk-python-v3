# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowExecutionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'limit': 'int',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'limit': 'limit',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, workflow_id=None, limit=None, status=None, start_time=None, end_time=None):
        """ListWorkflowExecutionsRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数工作流ID
        :type workflow_id: str
        :param limit: 分页查询，每页显示的条目数量，最大数量200，超过200后只返回200
        :type limit: int
        :param status: 需要过滤的流程实例状态
        :type status: str
        :param start_time: 查询开始时间，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间
        :type start_time: str
        :param end_time: 查询开始时间，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。
        :type end_time: str
        """
        
        

        self._workflow_id = None
        self._limit = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.workflow_id = workflow_id
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ListWorkflowExecutionsRequest.

        函数工作流ID

        :return: The workflow_id of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ListWorkflowExecutionsRequest.

        函数工作流ID

        :param workflow_id: The workflow_id of this ListWorkflowExecutionsRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def limit(self):
        """Gets the limit of this ListWorkflowExecutionsRequest.

        分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :return: The limit of this ListWorkflowExecutionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkflowExecutionsRequest.

        分页查询，每页显示的条目数量，最大数量200，超过200后只返回200

        :param limit: The limit of this ListWorkflowExecutionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        """Gets the status of this ListWorkflowExecutionsRequest.

        需要过滤的流程实例状态

        :return: The status of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListWorkflowExecutionsRequest.

        需要过滤的流程实例状态

        :param status: The status of this ListWorkflowExecutionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this ListWorkflowExecutionsRequest.

        查询开始时间，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间

        :return: The start_time of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListWorkflowExecutionsRequest.

        查询开始时间，UTC时间。若起始时间未填写，以终止时间前推3天为起始时间

        :param start_time: The start_time of this ListWorkflowExecutionsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListWorkflowExecutionsRequest.

        查询开始时间，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :return: The end_time of this ListWorkflowExecutionsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListWorkflowExecutionsRequest.

        查询开始时间，UTC时间。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :param end_time: The end_time of this ListWorkflowExecutionsRequest.
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
        if not isinstance(other, ListWorkflowExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
