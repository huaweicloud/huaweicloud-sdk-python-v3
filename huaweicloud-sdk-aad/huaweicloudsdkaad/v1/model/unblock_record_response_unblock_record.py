# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnblockRecordResponseUnblockRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'executor': 'str',
        'block_id': 'int',
        'blocking_time': 'int',
        'unblocking_time': 'int',
        'unblock_type': 'str',
        'status': 'str',
        'sort_time': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'executor': 'executor',
        'block_id': 'block_id',
        'blocking_time': 'blocking_time',
        'unblocking_time': 'unblocking_time',
        'unblock_type': 'unblock_type',
        'status': 'status',
        'sort_time': 'sort_time'
    }

    def __init__(self, ip=None, executor=None, block_id=None, blocking_time=None, unblocking_time=None, unblock_type=None, status=None, sort_time=None):
        r"""UnblockRecordResponseUnblockRecord

        The model defined in huaweicloud sdk

        :param ip: ip地址
        :type ip: str
        :param executor: 执行者
        :type executor: str
        :param block_id: 封堵id
        :type block_id: int
        :param blocking_time: 封堵时间
        :type blocking_time: int
        :param unblocking_time: 解封时间
        :type unblocking_time: int
        :param unblock_type: 解封类型。manual：人工；automatic：自动
        :type unblock_type: str
        :param status: 状态。unblocking：解封中；success：成功；failed：失败
        :type status: str
        :param sort_time: 时间
        :type sort_time: int
        """
        
        

        self._ip = None
        self._executor = None
        self._block_id = None
        self._blocking_time = None
        self._unblocking_time = None
        self._unblock_type = None
        self._status = None
        self._sort_time = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if executor is not None:
            self.executor = executor
        if block_id is not None:
            self.block_id = block_id
        if blocking_time is not None:
            self.blocking_time = blocking_time
        if unblocking_time is not None:
            self.unblocking_time = unblocking_time
        if unblock_type is not None:
            self.unblock_type = unblock_type
        if status is not None:
            self.status = status
        if sort_time is not None:
            self.sort_time = sort_time

    @property
    def ip(self):
        r"""Gets the ip of this UnblockRecordResponseUnblockRecord.

        ip地址

        :return: The ip of this UnblockRecordResponseUnblockRecord.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this UnblockRecordResponseUnblockRecord.

        ip地址

        :param ip: The ip of this UnblockRecordResponseUnblockRecord.
        :type ip: str
        """
        self._ip = ip

    @property
    def executor(self):
        r"""Gets the executor of this UnblockRecordResponseUnblockRecord.

        执行者

        :return: The executor of this UnblockRecordResponseUnblockRecord.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this UnblockRecordResponseUnblockRecord.

        执行者

        :param executor: The executor of this UnblockRecordResponseUnblockRecord.
        :type executor: str
        """
        self._executor = executor

    @property
    def block_id(self):
        r"""Gets the block_id of this UnblockRecordResponseUnblockRecord.

        封堵id

        :return: The block_id of this UnblockRecordResponseUnblockRecord.
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        r"""Sets the block_id of this UnblockRecordResponseUnblockRecord.

        封堵id

        :param block_id: The block_id of this UnblockRecordResponseUnblockRecord.
        :type block_id: int
        """
        self._block_id = block_id

    @property
    def blocking_time(self):
        r"""Gets the blocking_time of this UnblockRecordResponseUnblockRecord.

        封堵时间

        :return: The blocking_time of this UnblockRecordResponseUnblockRecord.
        :rtype: int
        """
        return self._blocking_time

    @blocking_time.setter
    def blocking_time(self, blocking_time):
        r"""Sets the blocking_time of this UnblockRecordResponseUnblockRecord.

        封堵时间

        :param blocking_time: The blocking_time of this UnblockRecordResponseUnblockRecord.
        :type blocking_time: int
        """
        self._blocking_time = blocking_time

    @property
    def unblocking_time(self):
        r"""Gets the unblocking_time of this UnblockRecordResponseUnblockRecord.

        解封时间

        :return: The unblocking_time of this UnblockRecordResponseUnblockRecord.
        :rtype: int
        """
        return self._unblocking_time

    @unblocking_time.setter
    def unblocking_time(self, unblocking_time):
        r"""Sets the unblocking_time of this UnblockRecordResponseUnblockRecord.

        解封时间

        :param unblocking_time: The unblocking_time of this UnblockRecordResponseUnblockRecord.
        :type unblocking_time: int
        """
        self._unblocking_time = unblocking_time

    @property
    def unblock_type(self):
        r"""Gets the unblock_type of this UnblockRecordResponseUnblockRecord.

        解封类型。manual：人工；automatic：自动

        :return: The unblock_type of this UnblockRecordResponseUnblockRecord.
        :rtype: str
        """
        return self._unblock_type

    @unblock_type.setter
    def unblock_type(self, unblock_type):
        r"""Sets the unblock_type of this UnblockRecordResponseUnblockRecord.

        解封类型。manual：人工；automatic：自动

        :param unblock_type: The unblock_type of this UnblockRecordResponseUnblockRecord.
        :type unblock_type: str
        """
        self._unblock_type = unblock_type

    @property
    def status(self):
        r"""Gets the status of this UnblockRecordResponseUnblockRecord.

        状态。unblocking：解封中；success：成功；failed：失败

        :return: The status of this UnblockRecordResponseUnblockRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UnblockRecordResponseUnblockRecord.

        状态。unblocking：解封中；success：成功；failed：失败

        :param status: The status of this UnblockRecordResponseUnblockRecord.
        :type status: str
        """
        self._status = status

    @property
    def sort_time(self):
        r"""Gets the sort_time of this UnblockRecordResponseUnblockRecord.

        时间

        :return: The sort_time of this UnblockRecordResponseUnblockRecord.
        :rtype: int
        """
        return self._sort_time

    @sort_time.setter
    def sort_time(self, sort_time):
        r"""Sets the sort_time of this UnblockRecordResponseUnblockRecord.

        时间

        :param sort_time: The sort_time of this UnblockRecordResponseUnblockRecord.
        :type sort_time: int
        """
        self._sort_time = sort_time

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
        if not isinstance(other, UnblockRecordResponseUnblockRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
