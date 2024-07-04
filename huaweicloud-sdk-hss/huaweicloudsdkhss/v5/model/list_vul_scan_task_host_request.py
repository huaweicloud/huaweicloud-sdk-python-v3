# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulScanTaskHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'scan_status': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'scan_status': 'scan_status'
    }

    def __init__(self, task_id=None, enterprise_project_id=None, limit=None, offset=None, scan_status=None):
        """ListVulScanTaskHostRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param enterprise_project_id: 企业租户ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param scan_status: 主机的扫描状态，包含如下：   -scanning : 扫描中   -success : 扫描成功   -failed : 扫描失败
        :type scan_status: str
        """
        
        

        self._task_id = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._scan_status = None
        self.discriminator = None

        self.task_id = task_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if scan_status is not None:
            self.scan_status = scan_status

    @property
    def task_id(self):
        """Gets the task_id of this ListVulScanTaskHostRequest.

        任务ID

        :return: The task_id of this ListVulScanTaskHostRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListVulScanTaskHostRequest.

        任务ID

        :param task_id: The task_id of this ListVulScanTaskHostRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVulScanTaskHostRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListVulScanTaskHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVulScanTaskHostRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListVulScanTaskHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListVulScanTaskHostRequest.

        每页显示个数

        :return: The limit of this ListVulScanTaskHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVulScanTaskHostRequest.

        每页显示个数

        :param limit: The limit of this ListVulScanTaskHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVulScanTaskHostRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListVulScanTaskHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVulScanTaskHostRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListVulScanTaskHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def scan_status(self):
        """Gets the scan_status of this ListVulScanTaskHostRequest.

        主机的扫描状态，包含如下：   -scanning : 扫描中   -success : 扫描成功   -failed : 扫描失败

        :return: The scan_status of this ListVulScanTaskHostRequest.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ListVulScanTaskHostRequest.

        主机的扫描状态，包含如下：   -scanning : 扫描中   -success : 扫描成功   -failed : 扫描失败

        :param scan_status: The scan_status of this ListVulScanTaskHostRequest.
        :type scan_status: str
        """
        self._scan_status = scan_status

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
        if not isinstance(other, ListVulScanTaskHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
