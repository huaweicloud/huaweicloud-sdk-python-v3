# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRecordRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, project_id=None, task_id=None, offset=None, limit=None, start_time=None, end_time=None):
        """CheckRecordRequest - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._task_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.project_id = project_id
        self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def project_id(self):
        """Gets the project_id of this CheckRecordRequest.

        项目ID

        :return: The project_id of this CheckRecordRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CheckRecordRequest.

        项目ID

        :param project_id: The project_id of this CheckRecordRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        """Gets the task_id of this CheckRecordRequest.

        任务ID

        :return: The task_id of this CheckRecordRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CheckRecordRequest.

        任务ID

        :param task_id: The task_id of this CheckRecordRequest.
        :type: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        """Gets the offset of this CheckRecordRequest.

        分页索引，偏移量

        :return: The offset of this CheckRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CheckRecordRequest.

        分页索引，偏移量

        :param offset: The offset of this CheckRecordRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this CheckRecordRequest.

        每页显示的数量,每页最多显示100条

        :return: The limit of this CheckRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CheckRecordRequest.

        每页显示的数量,每页最多显示100条

        :param limit: The limit of this CheckRecordRequest.
        :type: int
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this CheckRecordRequest.

        开始时间

        :return: The start_time of this CheckRecordRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CheckRecordRequest.

        开始时间

        :param start_time: The start_time of this CheckRecordRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CheckRecordRequest.

        结束时间

        :return: The end_time of this CheckRecordRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CheckRecordRequest.

        结束时间

        :param end_time: The end_time of this CheckRecordRequest.
        :type: str
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
        if not isinstance(other, CheckRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
