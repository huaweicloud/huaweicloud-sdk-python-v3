# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupTransferInfo:

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
        'name': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'status': 'str',
        'size': 'float',
        'instance_id': 'str',
        'file_name': 'str',
        'destination': 'str',
        'backup_begin_time': 'int',
        'backup_end_time': 'int',
        'transfer_type': 'str',
        'prefix': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'size': 'size',
        'instance_id': 'instance_id',
        'file_name': 'file_name',
        'destination': 'destination',
        'backup_begin_time': 'backup_begin_time',
        'backup_end_time': 'backup_end_time',
        'transfer_type': 'transfer_type',
        'prefix': 'prefix',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, begin_time=None, end_time=None, status=None, size=None, instance_id=None, file_name=None, destination=None, backup_begin_time=None, backup_end_time=None, transfer_type=None, prefix=None, type=None):
        r"""BackupTransferInfo

        The model defined in huaweicloud sdk

        :param id: 备份id
        :type id: str
        :param name: 备份名称
        :type name: str
        :param begin_time: 开始时间
        :type begin_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param status: 任务状态
        :type status: str
        :param size: 对象大小,单位为KByte
        :type size: float
        :param instance_id: 实例id
        :type instance_id: str
        :param file_name: 目标对象名称
        :type file_name: str
        :param destination: 目标桶名
        :type destination: str
        :param backup_begin_time: 转储备份起始时间
        :type backup_begin_time: int
        :param backup_end_time: 转储备份结束时间
        :type backup_end_time: int
        :param transfer_type: 转储任务类型
        :type transfer_type: str
        :param prefix: 转储目标前缀
        :type prefix: str
        :param type: 转储备份类型
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._size = None
        self._instance_id = None
        self._file_name = None
        self._destination = None
        self._backup_begin_time = None
        self._backup_end_time = None
        self._transfer_type = None
        self._prefix = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if size is not None:
            self.size = size
        if instance_id is not None:
            self.instance_id = instance_id
        if file_name is not None:
            self.file_name = file_name
        if destination is not None:
            self.destination = destination
        if backup_begin_time is not None:
            self.backup_begin_time = backup_begin_time
        if backup_end_time is not None:
            self.backup_end_time = backup_end_time
        if transfer_type is not None:
            self.transfer_type = transfer_type
        if prefix is not None:
            self.prefix = prefix
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this BackupTransferInfo.

        备份id

        :return: The id of this BackupTransferInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupTransferInfo.

        备份id

        :param id: The id of this BackupTransferInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupTransferInfo.

        备份名称

        :return: The name of this BackupTransferInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupTransferInfo.

        备份名称

        :param name: The name of this BackupTransferInfo.
        :type name: str
        """
        self._name = name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BackupTransferInfo.

        开始时间

        :return: The begin_time of this BackupTransferInfo.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BackupTransferInfo.

        开始时间

        :param begin_time: The begin_time of this BackupTransferInfo.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BackupTransferInfo.

        结束时间

        :return: The end_time of this BackupTransferInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BackupTransferInfo.

        结束时间

        :param end_time: The end_time of this BackupTransferInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this BackupTransferInfo.

        任务状态

        :return: The status of this BackupTransferInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupTransferInfo.

        任务状态

        :param status: The status of this BackupTransferInfo.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        r"""Gets the size of this BackupTransferInfo.

        对象大小,单位为KByte

        :return: The size of this BackupTransferInfo.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackupTransferInfo.

        对象大小,单位为KByte

        :param size: The size of this BackupTransferInfo.
        :type size: float
        """
        self._size = size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BackupTransferInfo.

        实例id

        :return: The instance_id of this BackupTransferInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BackupTransferInfo.

        实例id

        :param instance_id: The instance_id of this BackupTransferInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def file_name(self):
        r"""Gets the file_name of this BackupTransferInfo.

        目标对象名称

        :return: The file_name of this BackupTransferInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this BackupTransferInfo.

        目标对象名称

        :param file_name: The file_name of this BackupTransferInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def destination(self):
        r"""Gets the destination of this BackupTransferInfo.

        目标桶名

        :return: The destination of this BackupTransferInfo.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this BackupTransferInfo.

        目标桶名

        :param destination: The destination of this BackupTransferInfo.
        :type destination: str
        """
        self._destination = destination

    @property
    def backup_begin_time(self):
        r"""Gets the backup_begin_time of this BackupTransferInfo.

        转储备份起始时间

        :return: The backup_begin_time of this BackupTransferInfo.
        :rtype: int
        """
        return self._backup_begin_time

    @backup_begin_time.setter
    def backup_begin_time(self, backup_begin_time):
        r"""Sets the backup_begin_time of this BackupTransferInfo.

        转储备份起始时间

        :param backup_begin_time: The backup_begin_time of this BackupTransferInfo.
        :type backup_begin_time: int
        """
        self._backup_begin_time = backup_begin_time

    @property
    def backup_end_time(self):
        r"""Gets the backup_end_time of this BackupTransferInfo.

        转储备份结束时间

        :return: The backup_end_time of this BackupTransferInfo.
        :rtype: int
        """
        return self._backup_end_time

    @backup_end_time.setter
    def backup_end_time(self, backup_end_time):
        r"""Sets the backup_end_time of this BackupTransferInfo.

        转储备份结束时间

        :param backup_end_time: The backup_end_time of this BackupTransferInfo.
        :type backup_end_time: int
        """
        self._backup_end_time = backup_end_time

    @property
    def transfer_type(self):
        r"""Gets the transfer_type of this BackupTransferInfo.

        转储任务类型

        :return: The transfer_type of this BackupTransferInfo.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type):
        r"""Sets the transfer_type of this BackupTransferInfo.

        转储任务类型

        :param transfer_type: The transfer_type of this BackupTransferInfo.
        :type transfer_type: str
        """
        self._transfer_type = transfer_type

    @property
    def prefix(self):
        r"""Gets the prefix of this BackupTransferInfo.

        转储目标前缀

        :return: The prefix of this BackupTransferInfo.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this BackupTransferInfo.

        转储目标前缀

        :param prefix: The prefix of this BackupTransferInfo.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def type(self):
        r"""Gets the type of this BackupTransferInfo.

        转储备份类型

        :return: The type of this BackupTransferInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BackupTransferInfo.

        转储备份类型

        :param type: The type of this BackupTransferInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BackupTransferInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
