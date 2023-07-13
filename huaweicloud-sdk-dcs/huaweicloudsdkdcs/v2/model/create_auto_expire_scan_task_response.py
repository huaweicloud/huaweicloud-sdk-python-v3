# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAutoExpireScanTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'instance_id': 'str',
        'status': 'str',
        'scan_type': 'str',
        'created_at': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'scan_type': 'scan_type',
        'created_at': 'created_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at'
    }

    def __init__(self, id=None, instance_id=None, status=None, scan_type=None, created_at=None, started_at=None, finished_at=None):
        """CreateAutoExpireScanTaskResponse

        The model defined in huaweicloud sdk

        :param id: 过期key扫描记录ID
        :type id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param status: 扫描任务状态
        :type status: str
        :param scan_type: 扫描方式
        :type scan_type: str
        :param created_at: 扫描任务创建时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;
        :type created_at: str
        :param started_at: 扫描任务开始时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;（创建扫描任务时此值为null，不返回）
        :type started_at: str
        :param finished_at: 扫描任务结束时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;（创建扫描任务时此值为null，不返回）
        :type finished_at: str
        """
        
        super(CreateAutoExpireScanTaskResponse, self).__init__()

        self._id = None
        self._instance_id = None
        self._status = None
        self._scan_type = None
        self._created_at = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if scan_type is not None:
            self.scan_type = scan_type
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this CreateAutoExpireScanTaskResponse.

        过期key扫描记录ID

        :return: The id of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAutoExpireScanTaskResponse.

        过期key扫描记录ID

        :param id: The id of this CreateAutoExpireScanTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateAutoExpireScanTaskResponse.

        实例ID

        :return: The instance_id of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateAutoExpireScanTaskResponse.

        实例ID

        :param instance_id: The instance_id of this CreateAutoExpireScanTaskResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this CreateAutoExpireScanTaskResponse.

        扫描任务状态

        :return: The status of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateAutoExpireScanTaskResponse.

        扫描任务状态

        :param status: The status of this CreateAutoExpireScanTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def scan_type(self):
        """Gets the scan_type of this CreateAutoExpireScanTaskResponse.

        扫描方式

        :return: The scan_type of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this CreateAutoExpireScanTaskResponse.

        扫描方式

        :param scan_type: The scan_type of this CreateAutoExpireScanTaskResponse.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def created_at(self):
        """Gets the created_at of this CreateAutoExpireScanTaskResponse.

        扫描任务创建时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :return: The created_at of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateAutoExpireScanTaskResponse.

        扫描任务创建时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :param created_at: The created_at of this CreateAutoExpireScanTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def started_at(self):
        """Gets the started_at of this CreateAutoExpireScanTaskResponse.

        扫描任务开始时间,格式为：\"2020-06-15T02:21:18.669Z\"（创建扫描任务时此值为null，不返回）

        :return: The started_at of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this CreateAutoExpireScanTaskResponse.

        扫描任务开始时间,格式为：\"2020-06-15T02:21:18.669Z\"（创建扫描任务时此值为null，不返回）

        :param started_at: The started_at of this CreateAutoExpireScanTaskResponse.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this CreateAutoExpireScanTaskResponse.

        扫描任务结束时间,格式为：\"2020-06-15T02:21:18.669Z\"（创建扫描任务时此值为null，不返回）

        :return: The finished_at of this CreateAutoExpireScanTaskResponse.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this CreateAutoExpireScanTaskResponse.

        扫描任务结束时间,格式为：\"2020-06-15T02:21:18.669Z\"（创建扫描任务时此值为null，不返回）

        :param finished_at: The finished_at of this CreateAutoExpireScanTaskResponse.
        :type finished_at: str
        """
        self._finished_at = finished_at

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
        if not isinstance(other, CreateAutoExpireScanTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
