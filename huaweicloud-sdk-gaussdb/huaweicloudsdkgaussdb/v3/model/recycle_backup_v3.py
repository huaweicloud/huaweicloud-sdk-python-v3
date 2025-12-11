# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleBackupV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_level': 'str',
        'backup_id': 'str',
        'backup_name': 'str',
        'size': 'int',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'backup_level': 'backup_level',
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'size': 'size',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, backup_level=None, backup_id=None, backup_name=None, size=None, status=None, begin_time=None, end_time=None):
        r"""RecycleBackupV3

        The model defined in huaweicloud sdk

        :param backup_level: 备份级别。
        :type backup_level: str
        :param backup_id: 备份ID。
        :type backup_id: str
        :param backup_name: 备份名称。
        :type backup_name: str
        :param size: 备份大小，单位是字节。
        :type size: int
        :param status: 回收状态。
        :type status: str
        :param begin_time: 备份开始时间。
        :type begin_time: str
        :param end_time: 备份结束时间。
        :type end_time: str
        """
        
        

        self._backup_level = None
        self._backup_id = None
        self._backup_name = None
        self._size = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if backup_level is not None:
            self.backup_level = backup_level
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def backup_level(self):
        r"""Gets the backup_level of this RecycleBackupV3.

        备份级别。

        :return: The backup_level of this RecycleBackupV3.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this RecycleBackupV3.

        备份级别。

        :param backup_level: The backup_level of this RecycleBackupV3.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RecycleBackupV3.

        备份ID。

        :return: The backup_id of this RecycleBackupV3.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RecycleBackupV3.

        备份ID。

        :param backup_id: The backup_id of this RecycleBackupV3.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        r"""Gets the backup_name of this RecycleBackupV3.

        备份名称。

        :return: The backup_name of this RecycleBackupV3.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this RecycleBackupV3.

        备份名称。

        :param backup_name: The backup_name of this RecycleBackupV3.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def size(self):
        r"""Gets the size of this RecycleBackupV3.

        备份大小，单位是字节。

        :return: The size of this RecycleBackupV3.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RecycleBackupV3.

        备份大小，单位是字节。

        :param size: The size of this RecycleBackupV3.
        :type size: int
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this RecycleBackupV3.

        回收状态。

        :return: The status of this RecycleBackupV3.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RecycleBackupV3.

        回收状态。

        :param status: The status of this RecycleBackupV3.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this RecycleBackupV3.

        备份开始时间。

        :return: The begin_time of this RecycleBackupV3.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this RecycleBackupV3.

        备份开始时间。

        :param begin_time: The begin_time of this RecycleBackupV3.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RecycleBackupV3.

        备份结束时间。

        :return: The end_time of this RecycleBackupV3.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RecycleBackupV3.

        备份结束时间。

        :param end_time: The end_time of this RecycleBackupV3.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, RecycleBackupV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
