# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleKeyScanRecord:

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
        'num': 'int',
        'created_at': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'scan_type': 'scan_type',
        'num': 'num',
        'created_at': 'created_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at'
    }

    def __init__(self, id=None, instance_id=None, status=None, scan_type=None, num=None, created_at=None, started_at=None, finished_at=None):
        r"""SimpleKeyScanRecord

        The model defined in huaweicloud sdk

        :param id: 扫描ID
        :type id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param status: 状态
        :type status: str
        :param scan_type: 扫描类型
        :type scan_type: str
        :param num: 数量
        :type num: int
        :param created_at: 创建时间, 格式为: 2023-06-13T13:46:14.771Z
        :type created_at: str
        :param started_at: 开始时间, 格式为: 2023-06-13T13:46:14.771Z
        :type started_at: str
        :param finished_at: 完成时间, 格式为：2020-06-15T02:21:18.669Z
        :type finished_at: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._status = None
        self._scan_type = None
        self._num = None
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
        if num is not None:
            self.num = num
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def id(self):
        r"""Gets the id of this SimpleKeyScanRecord.

        扫描ID

        :return: The id of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleKeyScanRecord.

        扫描ID

        :param id: The id of this SimpleKeyScanRecord.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SimpleKeyScanRecord.

        实例ID

        :return: The instance_id of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SimpleKeyScanRecord.

        实例ID

        :param instance_id: The instance_id of this SimpleKeyScanRecord.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this SimpleKeyScanRecord.

        状态

        :return: The status of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimpleKeyScanRecord.

        状态

        :param status: The status of this SimpleKeyScanRecord.
        :type status: str
        """
        self._status = status

    @property
    def scan_type(self):
        r"""Gets the scan_type of this SimpleKeyScanRecord.

        扫描类型

        :return: The scan_type of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this SimpleKeyScanRecord.

        扫描类型

        :param scan_type: The scan_type of this SimpleKeyScanRecord.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def num(self):
        r"""Gets the num of this SimpleKeyScanRecord.

        数量

        :return: The num of this SimpleKeyScanRecord.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this SimpleKeyScanRecord.

        数量

        :param num: The num of this SimpleKeyScanRecord.
        :type num: int
        """
        self._num = num

    @property
    def created_at(self):
        r"""Gets the created_at of this SimpleKeyScanRecord.

        创建时间, 格式为: 2023-06-13T13:46:14.771Z

        :return: The created_at of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SimpleKeyScanRecord.

        创建时间, 格式为: 2023-06-13T13:46:14.771Z

        :param created_at: The created_at of this SimpleKeyScanRecord.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def started_at(self):
        r"""Gets the started_at of this SimpleKeyScanRecord.

        开始时间, 格式为: 2023-06-13T13:46:14.771Z

        :return: The started_at of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this SimpleKeyScanRecord.

        开始时间, 格式为: 2023-06-13T13:46:14.771Z

        :param started_at: The started_at of this SimpleKeyScanRecord.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this SimpleKeyScanRecord.

        完成时间, 格式为：2020-06-15T02:21:18.669Z

        :return: The finished_at of this SimpleKeyScanRecord.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this SimpleKeyScanRecord.

        完成时间, 格式为：2020-06-15T02:21:18.669Z

        :param finished_at: The finished_at of this SimpleKeyScanRecord.
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
        if not isinstance(other, SimpleKeyScanRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
