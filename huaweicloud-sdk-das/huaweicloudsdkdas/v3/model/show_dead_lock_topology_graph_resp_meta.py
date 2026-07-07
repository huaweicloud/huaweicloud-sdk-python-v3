# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockTopologyGraphRespMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dead_lock_id': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'occur_time': 'int',
        'total_transactions_in_cycle': 'int',
        'total_transactions_returned': 'int',
        'truncated': 'bool'
    }

    attribute_map = {
        'dead_lock_id': 'dead_lock_id',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'occur_time': 'occur_time',
        'total_transactions_in_cycle': 'total_transactions_in_cycle',
        'total_transactions_returned': 'total_transactions_returned',
        'truncated': 'truncated'
    }

    def __init__(self, dead_lock_id=None, instance_id=None, project_id=None, occur_time=None, total_transactions_in_cycle=None, total_transactions_returned=None, truncated=None):
        r"""ShowDeadLockTopologyGraphRespMeta

        The model defined in huaweicloud sdk

        :param dead_lock_id: 死锁唯一标识
        :type dead_lock_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param occur_time: 死锁的发生时间，Unix 毫秒时间戳
        :type occur_time: int
        :param total_transactions_in_cycle: 死锁的事务总数
        :type total_transactions_in_cycle: int
        :param total_transactions_returned: 本次实际返回的事务数
        :type total_transactions_returned: int
        :param truncated: 是否裁剪（&gt;10 事务只返回 10 个）
        :type truncated: bool
        """
        
        

        self._dead_lock_id = None
        self._instance_id = None
        self._project_id = None
        self._occur_time = None
        self._total_transactions_in_cycle = None
        self._total_transactions_returned = None
        self._truncated = None
        self.discriminator = None

        self.dead_lock_id = dead_lock_id
        self.instance_id = instance_id
        self.project_id = project_id
        self.occur_time = occur_time
        self.total_transactions_in_cycle = total_transactions_in_cycle
        self.total_transactions_returned = total_transactions_returned
        self.truncated = truncated

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this ShowDeadLockTopologyGraphRespMeta.

        死锁唯一标识

        :return: The dead_lock_id of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this ShowDeadLockTopologyGraphRespMeta.

        死锁唯一标识

        :param dead_lock_id: The dead_lock_id of this ShowDeadLockTopologyGraphRespMeta.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDeadLockTopologyGraphRespMeta.

        实例ID

        :return: The instance_id of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDeadLockTopologyGraphRespMeta.

        实例ID

        :param instance_id: The instance_id of this ShowDeadLockTopologyGraphRespMeta.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowDeadLockTopologyGraphRespMeta.

        项目ID

        :return: The project_id of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowDeadLockTopologyGraphRespMeta.

        项目ID

        :param project_id: The project_id of this ShowDeadLockTopologyGraphRespMeta.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def occur_time(self):
        r"""Gets the occur_time of this ShowDeadLockTopologyGraphRespMeta.

        死锁的发生时间，Unix 毫秒时间戳

        :return: The occur_time of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this ShowDeadLockTopologyGraphRespMeta.

        死锁的发生时间，Unix 毫秒时间戳

        :param occur_time: The occur_time of this ShowDeadLockTopologyGraphRespMeta.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def total_transactions_in_cycle(self):
        r"""Gets the total_transactions_in_cycle of this ShowDeadLockTopologyGraphRespMeta.

        死锁的事务总数

        :return: The total_transactions_in_cycle of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: int
        """
        return self._total_transactions_in_cycle

    @total_transactions_in_cycle.setter
    def total_transactions_in_cycle(self, total_transactions_in_cycle):
        r"""Sets the total_transactions_in_cycle of this ShowDeadLockTopologyGraphRespMeta.

        死锁的事务总数

        :param total_transactions_in_cycle: The total_transactions_in_cycle of this ShowDeadLockTopologyGraphRespMeta.
        :type total_transactions_in_cycle: int
        """
        self._total_transactions_in_cycle = total_transactions_in_cycle

    @property
    def total_transactions_returned(self):
        r"""Gets the total_transactions_returned of this ShowDeadLockTopologyGraphRespMeta.

        本次实际返回的事务数

        :return: The total_transactions_returned of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: int
        """
        return self._total_transactions_returned

    @total_transactions_returned.setter
    def total_transactions_returned(self, total_transactions_returned):
        r"""Sets the total_transactions_returned of this ShowDeadLockTopologyGraphRespMeta.

        本次实际返回的事务数

        :param total_transactions_returned: The total_transactions_returned of this ShowDeadLockTopologyGraphRespMeta.
        :type total_transactions_returned: int
        """
        self._total_transactions_returned = total_transactions_returned

    @property
    def truncated(self):
        r"""Gets the truncated of this ShowDeadLockTopologyGraphRespMeta.

        是否裁剪（>10 事务只返回 10 个）

        :return: The truncated of this ShowDeadLockTopologyGraphRespMeta.
        :rtype: bool
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        r"""Sets the truncated of this ShowDeadLockTopologyGraphRespMeta.

        是否裁剪（>10 事务只返回 10 个）

        :param truncated: The truncated of this ShowDeadLockTopologyGraphRespMeta.
        :type truncated: bool
        """
        self._truncated = truncated

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
        if not isinstance(other, ShowDeadLockTopologyGraphRespMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
