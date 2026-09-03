# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Snapshot:

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
        'find_lock': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'create_at': 'create_at',
        'find_lock': 'find_lock'
    }

    def __init__(self, id=None, status=None, create_at=None, find_lock=None):
        r"""Snapshot

        The model defined in huaweicloud sdk

        :param id: 快照ID
        :type id: int
        :param status: 快照状态。取值范围：0（等待中）、1（运行中）、2（失败）、3（成功）
        :type status: int
        :param create_at: 锁快照创建时间
        :type create_at: int
        :param find_lock: 是否找到有锁。取值范围：0（否）、1（是）
        :type find_lock: int
        """
        
        

        self._id = None
        self._status = None
        self._create_at = None
        self._find_lock = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_at is not None:
            self.create_at = create_at
        if find_lock is not None:
            self.find_lock = find_lock

    @property
    def id(self):
        r"""Gets the id of this Snapshot.

        快照ID

        :return: The id of this Snapshot.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Snapshot.

        快照ID

        :param id: The id of this Snapshot.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this Snapshot.

        快照状态。取值范围：0（等待中）、1（运行中）、2（失败）、3（成功）

        :return: The status of this Snapshot.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Snapshot.

        快照状态。取值范围：0（等待中）、1（运行中）、2（失败）、3（成功）

        :param status: The status of this Snapshot.
        :type status: int
        """
        self._status = status

    @property
    def create_at(self):
        r"""Gets the create_at of this Snapshot.

        锁快照创建时间

        :return: The create_at of this Snapshot.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this Snapshot.

        锁快照创建时间

        :param create_at: The create_at of this Snapshot.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def find_lock(self):
        r"""Gets the find_lock of this Snapshot.

        是否找到有锁。取值范围：0（否）、1（是）

        :return: The find_lock of this Snapshot.
        :rtype: int
        """
        return self._find_lock

    @find_lock.setter
    def find_lock(self, find_lock):
        r"""Sets the find_lock of this Snapshot.

        是否找到有锁。取值范围：0（否）、1（是）

        :param find_lock: The find_lock of this Snapshot.
        :type find_lock: int
        """
        self._find_lock = find_lock

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
