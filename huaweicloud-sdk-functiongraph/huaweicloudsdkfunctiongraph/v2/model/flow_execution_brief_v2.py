# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowExecutionBriefV2:

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
        'execution_id': 'str',
        'status': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'last_update_time': 'datetime',
        'created_by': 'str',
        'workflow_urn': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_update_time': 'last_update_time',
        'created_by': 'created_by',
        'workflow_urn': 'workflow_urn'
    }

    def __init__(self, workflow_id=None, execution_id=None, status=None, begin_time=None, end_time=None, last_update_time=None, created_by=None, workflow_urn=None):
        r"""FlowExecutionBriefV2

        The model defined in huaweicloud sdk

        :param workflow_id: 函数流ID
        :type workflow_id: str
        :param execution_id: 函数流执行ID
        :type execution_id: str
        :param status: 函数流执行状态
        :type status: str
        :param begin_time: 开始时间（格式为yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;,UTC时间）。
        :type begin_time: datetime
        :param end_time: 结束时间（格式为yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;,UTC时间）。
        :type end_time: datetime
        :param last_update_time: 结束时间（格式为yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;,UTC时间）。
        :type last_update_time: datetime
        :param created_by: 
        :type created_by: str
        :param workflow_urn: 函数流执行urn
        :type workflow_urn: str
        """
        
        

        self._workflow_id = None
        self._execution_id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._last_update_time = None
        self._created_by = None
        self._workflow_urn = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if created_by is not None:
            self.created_by = created_by
        if workflow_urn is not None:
            self.workflow_urn = workflow_urn

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this FlowExecutionBriefV2.

        函数流ID

        :return: The workflow_id of this FlowExecutionBriefV2.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this FlowExecutionBriefV2.

        函数流ID

        :param workflow_id: The workflow_id of this FlowExecutionBriefV2.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this FlowExecutionBriefV2.

        函数流执行ID

        :return: The execution_id of this FlowExecutionBriefV2.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this FlowExecutionBriefV2.

        函数流执行ID

        :param execution_id: The execution_id of this FlowExecutionBriefV2.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        r"""Gets the status of this FlowExecutionBriefV2.

        函数流执行状态

        :return: The status of this FlowExecutionBriefV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlowExecutionBriefV2.

        函数流执行状态

        :param status: The status of this FlowExecutionBriefV2.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this FlowExecutionBriefV2.

        开始时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :return: The begin_time of this FlowExecutionBriefV2.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this FlowExecutionBriefV2.

        开始时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :param begin_time: The begin_time of this FlowExecutionBriefV2.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FlowExecutionBriefV2.

        结束时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :return: The end_time of this FlowExecutionBriefV2.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FlowExecutionBriefV2.

        结束时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :param end_time: The end_time of this FlowExecutionBriefV2.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this FlowExecutionBriefV2.

        结束时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :return: The last_update_time of this FlowExecutionBriefV2.
        :rtype: datetime
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this FlowExecutionBriefV2.

        结束时间（格式为yyyy-MM-dd'T'HH:mm:ss'Z',UTC时间）。

        :param last_update_time: The last_update_time of this FlowExecutionBriefV2.
        :type last_update_time: datetime
        """
        self._last_update_time = last_update_time

    @property
    def created_by(self):
        r"""Gets the created_by of this FlowExecutionBriefV2.

        :return: The created_by of this FlowExecutionBriefV2.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this FlowExecutionBriefV2.

        :param created_by: The created_by of this FlowExecutionBriefV2.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def workflow_urn(self):
        r"""Gets the workflow_urn of this FlowExecutionBriefV2.

        函数流执行urn

        :return: The workflow_urn of this FlowExecutionBriefV2.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        r"""Sets the workflow_urn of this FlowExecutionBriefV2.

        函数流执行urn

        :param workflow_urn: The workflow_urn of this FlowExecutionBriefV2.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

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
        if not isinstance(other, FlowExecutionBriefV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
