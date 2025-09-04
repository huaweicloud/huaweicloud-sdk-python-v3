# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySnapshotsRespItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'int',
        'create_at': 'int',
        'find_lock': 'int',
        'happen_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'create_at': 'create_at',
        'find_lock': 'find_lock',
        'happen_at': 'happen_at'
    }

    def __init__(self, id=None, status=None, create_at=None, find_lock=None, happen_at=None):
        r"""QuerySnapshotsRespItems

        The model defined in huaweicloud sdk

        :param id: snapshot编号
        :type id: int
        :param status: 表示状态，0表示等待，1表示正在运行，2表示失败，3表示成功
        :type status: int
        :param create_at: 创建时间
        :type create_at: int
        :param find_lock: 是否发现锁，1表示发现了锁，0表示没有
        :type find_lock: int
        :param happen_at: 发生锁的时间
        :type happen_at: int
        """
        
        

        self._id = None
        self._status = None
        self._create_at = None
        self._find_lock = None
        self._happen_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_at is not None:
            self.create_at = create_at
        if find_lock is not None:
            self.find_lock = find_lock
        if happen_at is not None:
            self.happen_at = happen_at

    @property
    def id(self):
        r"""Gets the id of this QuerySnapshotsRespItems.

        snapshot编号

        :return: The id of this QuerySnapshotsRespItems.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QuerySnapshotsRespItems.

        snapshot编号

        :param id: The id of this QuerySnapshotsRespItems.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this QuerySnapshotsRespItems.

        表示状态，0表示等待，1表示正在运行，2表示失败，3表示成功

        :return: The status of this QuerySnapshotsRespItems.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QuerySnapshotsRespItems.

        表示状态，0表示等待，1表示正在运行，2表示失败，3表示成功

        :param status: The status of this QuerySnapshotsRespItems.
        :type status: int
        """
        self._status = status

    @property
    def create_at(self):
        r"""Gets the create_at of this QuerySnapshotsRespItems.

        创建时间

        :return: The create_at of this QuerySnapshotsRespItems.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this QuerySnapshotsRespItems.

        创建时间

        :param create_at: The create_at of this QuerySnapshotsRespItems.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def find_lock(self):
        r"""Gets the find_lock of this QuerySnapshotsRespItems.

        是否发现锁，1表示发现了锁，0表示没有

        :return: The find_lock of this QuerySnapshotsRespItems.
        :rtype: int
        """
        return self._find_lock

    @find_lock.setter
    def find_lock(self, find_lock):
        r"""Sets the find_lock of this QuerySnapshotsRespItems.

        是否发现锁，1表示发现了锁，0表示没有

        :param find_lock: The find_lock of this QuerySnapshotsRespItems.
        :type find_lock: int
        """
        self._find_lock = find_lock

    @property
    def happen_at(self):
        r"""Gets the happen_at of this QuerySnapshotsRespItems.

        发生锁的时间

        :return: The happen_at of this QuerySnapshotsRespItems.
        :rtype: int
        """
        return self._happen_at

    @happen_at.setter
    def happen_at(self, happen_at):
        r"""Sets the happen_at of this QuerySnapshotsRespItems.

        发生锁的时间

        :param happen_at: The happen_at of this QuerySnapshotsRespItems.
        :type happen_at: int
        """
        self._happen_at = happen_at

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
        if not isinstance(other, QuerySnapshotsRespItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
