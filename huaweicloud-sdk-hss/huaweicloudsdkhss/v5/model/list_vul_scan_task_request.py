# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulScanTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'scan_type': 'str',
        'task_id': 'str',
        'min_start_time': 'int',
        'max_start_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'scan_type': 'scan_type',
        'task_id': 'task_id',
        'min_start_time': 'min_start_time',
        'max_start_time': 'max_start_time'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, scan_type=None, task_id=None, min_start_time=None, max_start_time=None):
        """ListVulScanTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param scan_type: 扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务
        :type scan_type: str
        :param task_id: 扫描任务ID
        :type task_id: str
        :param min_start_time: 扫描任务开始时间的最小值
        :type min_start_time: int
        :param max_start_time: 扫描任务开始时间的最大值
        :type max_start_time: int
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._scan_type = None
        self._task_id = None
        self._min_start_time = None
        self._max_start_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if scan_type is not None:
            self.scan_type = scan_type
        if task_id is not None:
            self.task_id = task_id
        if min_start_time is not None:
            self.min_start_time = min_start_time
        if max_start_time is not None:
            self.max_start_time = max_start_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVulScanTaskRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListVulScanTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVulScanTaskRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListVulScanTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListVulScanTaskRequest.

        每页显示个数

        :return: The limit of this ListVulScanTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVulScanTaskRequest.

        每页显示个数

        :param limit: The limit of this ListVulScanTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVulScanTaskRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListVulScanTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVulScanTaskRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListVulScanTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def scan_type(self):
        """Gets the scan_type of this ListVulScanTaskRequest.

        扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务

        :return: The scan_type of this ListVulScanTaskRequest.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this ListVulScanTaskRequest.

        扫描任务的类型，包含如下：   -manual : 手动扫描任务   -schedule : 定时扫描任务

        :param scan_type: The scan_type of this ListVulScanTaskRequest.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def task_id(self):
        """Gets the task_id of this ListVulScanTaskRequest.

        扫描任务ID

        :return: The task_id of this ListVulScanTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListVulScanTaskRequest.

        扫描任务ID

        :param task_id: The task_id of this ListVulScanTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def min_start_time(self):
        """Gets the min_start_time of this ListVulScanTaskRequest.

        扫描任务开始时间的最小值

        :return: The min_start_time of this ListVulScanTaskRequest.
        :rtype: int
        """
        return self._min_start_time

    @min_start_time.setter
    def min_start_time(self, min_start_time):
        """Sets the min_start_time of this ListVulScanTaskRequest.

        扫描任务开始时间的最小值

        :param min_start_time: The min_start_time of this ListVulScanTaskRequest.
        :type min_start_time: int
        """
        self._min_start_time = min_start_time

    @property
    def max_start_time(self):
        """Gets the max_start_time of this ListVulScanTaskRequest.

        扫描任务开始时间的最大值

        :return: The max_start_time of this ListVulScanTaskRequest.
        :rtype: int
        """
        return self._max_start_time

    @max_start_time.setter
    def max_start_time(self, max_start_time):
        """Sets the max_start_time of this ListVulScanTaskRequest.

        扫描任务开始时间的最大值

        :param max_start_time: The max_start_time of this ListVulScanTaskRequest.
        :type max_start_time: int
        """
        self._max_start_time = max_start_time

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
        if not isinstance(other, ListVulScanTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
