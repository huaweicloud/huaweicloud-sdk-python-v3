# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockAnalysisResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'dead_lock_id': 'str',
        'job_id': 'str',
        'transaction_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'dead_lock_id': 'dead_lock_id',
        'job_id': 'job_id',
        'transaction_id': 'transaction_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, dead_lock_id=None, job_id=None, transaction_id=None, offset=None, limit=None):
        r"""ShowDeadLockAnalysisResultRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param dead_lock_id: 死锁唯一标识
        :type dead_lock_id: str
        :param job_id: 死锁分析任务唯一标识
        :type job_id: str
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 单次返回数量
        :type limit: int
        """
        
        

        self._instance_id = None
        self._dead_lock_id = None
        self._job_id = None
        self._transaction_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.dead_lock_id = dead_lock_id
        if job_id is not None:
            self.job_id = job_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDeadLockAnalysisResultRequest.

        实例ID

        :return: The instance_id of this ShowDeadLockAnalysisResultRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDeadLockAnalysisResultRequest.

        实例ID

        :param instance_id: The instance_id of this ShowDeadLockAnalysisResultRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this ShowDeadLockAnalysisResultRequest.

        死锁唯一标识

        :return: The dead_lock_id of this ShowDeadLockAnalysisResultRequest.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this ShowDeadLockAnalysisResultRequest.

        死锁唯一标识

        :param dead_lock_id: The dead_lock_id of this ShowDeadLockAnalysisResultRequest.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDeadLockAnalysisResultRequest.

        死锁分析任务唯一标识

        :return: The job_id of this ShowDeadLockAnalysisResultRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDeadLockAnalysisResultRequest.

        死锁分析任务唯一标识

        :param job_id: The job_id of this ShowDeadLockAnalysisResultRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowDeadLockAnalysisResultRequest.

        事务ID

        :return: The transaction_id of this ShowDeadLockAnalysisResultRequest.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowDeadLockAnalysisResultRequest.

        事务ID

        :param transaction_id: The transaction_id of this ShowDeadLockAnalysisResultRequest.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowDeadLockAnalysisResultRequest.

        偏移量

        :return: The offset of this ShowDeadLockAnalysisResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDeadLockAnalysisResultRequest.

        偏移量

        :param offset: The offset of this ShowDeadLockAnalysisResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDeadLockAnalysisResultRequest.

        单次返回数量

        :return: The limit of this ShowDeadLockAnalysisResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDeadLockAnalysisResultRequest.

        单次返回数量

        :param limit: The limit of this ShowDeadLockAnalysisResultRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowDeadLockAnalysisResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
