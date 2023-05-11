# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowExecutionForPageRequest:

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
        'offset': 'int',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, workflow_id=None, offset=None, limit=None, start_time=None, end_time=None):
        """ShowWorkflowExecutionForPageRequest

        The model defined in huaweicloud sdk

        :param workflow_id: 函数工作流ID
        :type workflow_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 分页查询，每页查询数据条数，取值范围：1,2,3...100
        :type limit: int
        :param start_time: 查询开始时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若起始时间未填写，以终止时间前推3天为起始时间。
        :type start_time: str
        :param end_time: 查询结束时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。
        :type end_time: str
        """
        
        

        self._workflow_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.offset = offset
        self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ShowWorkflowExecutionForPageRequest.

        函数工作流ID

        :return: The workflow_id of this ShowWorkflowExecutionForPageRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ShowWorkflowExecutionForPageRequest.

        函数工作流ID

        :param workflow_id: The workflow_id of this ShowWorkflowExecutionForPageRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def offset(self):
        """Gets the offset of this ShowWorkflowExecutionForPageRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ShowWorkflowExecutionForPageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowWorkflowExecutionForPageRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ShowWorkflowExecutionForPageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowWorkflowExecutionForPageRequest.

        分页查询，每页查询数据条数，取值范围：1,2,3...100

        :return: The limit of this ShowWorkflowExecutionForPageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowWorkflowExecutionForPageRequest.

        分页查询，每页查询数据条数，取值范围：1,2,3...100

        :param limit: The limit of this ShowWorkflowExecutionForPageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ShowWorkflowExecutionForPageRequest.

        查询开始时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若起始时间未填写，以终止时间前推3天为起始时间。

        :return: The start_time of this ShowWorkflowExecutionForPageRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowWorkflowExecutionForPageRequest.

        查询开始时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若起始时间未填写，以终止时间前推3天为起始时间。

        :param start_time: The start_time of this ShowWorkflowExecutionForPageRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowWorkflowExecutionForPageRequest.

        查询结束时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :return: The end_time of this ShowWorkflowExecutionForPageRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowWorkflowExecutionForPageRequest.

        查询结束时间，UTC时间，格式：YYYY-MM-DD hh:mm:ss。若终止时间未填写，以起始时间后退3天未终止时间。若均未填写，默认查询最近3天数据。

        :param end_time: The end_time of this ShowWorkflowExecutionForPageRequest.
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
        if not isinstance(other, ShowWorkflowExecutionForPageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
