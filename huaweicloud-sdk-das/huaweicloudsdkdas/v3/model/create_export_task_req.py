# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExportTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'file_path': 'str',
        'time_zone': 'str',
        'order': 'str',
        'order_by': 'str',
        'last_sec_min': 'int',
        'last_sec_max': 'int'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'file_path': 'file_path',
        'time_zone': 'time_zone',
        'order': 'order',
        'order_by': 'order_by',
        'last_sec_min': 'last_sec_min',
        'last_sec_max': 'last_sec_max'
    }

    def __init__(self, bucket_name=None, start_at=None, end_at=None, file_path=None, time_zone=None, order=None, order_by=None, last_sec_min=None, last_sec_max=None):
        r"""CreateExportTaskReq

        The model defined in huaweicloud sdk

        :param bucket_name: OBS桶名
        :type bucket_name: str
        :param start_at: 开始时间(Unix timestamp),单位:毫秒。
        :type start_at: int
        :param end_at: 结束时间(Unix timestamp),单位:毫秒。
        :type end_at: int
        :param file_path: OBS文件目录
        :type file_path: str
        :param time_zone: 时区
        :type time_zone: str
        :param order: 排序字段。 - collectTime 收集时间 - occurrenceTime 发生时间 - lastSec 事务持续时间 - waitLockStructCount 持有锁数量 - holdLockStructCount 等待锁数量
        :type order: str
        :param order_by: 排序规则。 - asc 升序 - desc 降序
        :type order_by: str
        :param last_sec_min: 持续时间下限
        :type last_sec_min: int
        :param last_sec_max: 持续时间上限
        :type last_sec_max: int
        """
        
        

        self._bucket_name = None
        self._start_at = None
        self._end_at = None
        self._file_path = None
        self._time_zone = None
        self._order = None
        self._order_by = None
        self._last_sec_min = None
        self._last_sec_max = None
        self.discriminator = None

        self.bucket_name = bucket_name
        self.start_at = start_at
        self.end_at = end_at
        if file_path is not None:
            self.file_path = file_path
        if time_zone is not None:
            self.time_zone = time_zone
        if order is not None:
            self.order = order
        if order_by is not None:
            self.order_by = order_by
        if last_sec_min is not None:
            self.last_sec_min = last_sec_min
        if last_sec_max is not None:
            self.last_sec_max = last_sec_max

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateExportTaskReq.

        OBS桶名

        :return: The bucket_name of this CreateExportTaskReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateExportTaskReq.

        OBS桶名

        :param bucket_name: The bucket_name of this CreateExportTaskReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def start_at(self):
        r"""Gets the start_at of this CreateExportTaskReq.

        开始时间(Unix timestamp),单位:毫秒。

        :return: The start_at of this CreateExportTaskReq.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this CreateExportTaskReq.

        开始时间(Unix timestamp),单位:毫秒。

        :param start_at: The start_at of this CreateExportTaskReq.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this CreateExportTaskReq.

        结束时间(Unix timestamp),单位:毫秒。

        :return: The end_at of this CreateExportTaskReq.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this CreateExportTaskReq.

        结束时间(Unix timestamp),单位:毫秒。

        :param end_at: The end_at of this CreateExportTaskReq.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def file_path(self):
        r"""Gets the file_path of this CreateExportTaskReq.

        OBS文件目录

        :return: The file_path of this CreateExportTaskReq.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CreateExportTaskReq.

        OBS文件目录

        :param file_path: The file_path of this CreateExportTaskReq.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateExportTaskReq.

        时区

        :return: The time_zone of this CreateExportTaskReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateExportTaskReq.

        时区

        :param time_zone: The time_zone of this CreateExportTaskReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def order(self):
        r"""Gets the order of this CreateExportTaskReq.

        排序字段。 - collectTime 收集时间 - occurrenceTime 发生时间 - lastSec 事务持续时间 - waitLockStructCount 持有锁数量 - holdLockStructCount 等待锁数量

        :return: The order of this CreateExportTaskReq.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this CreateExportTaskReq.

        排序字段。 - collectTime 收集时间 - occurrenceTime 发生时间 - lastSec 事务持续时间 - waitLockStructCount 持有锁数量 - holdLockStructCount 等待锁数量

        :param order: The order of this CreateExportTaskReq.
        :type order: str
        """
        self._order = order

    @property
    def order_by(self):
        r"""Gets the order_by of this CreateExportTaskReq.

        排序规则。 - asc 升序 - desc 降序

        :return: The order_by of this CreateExportTaskReq.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this CreateExportTaskReq.

        排序规则。 - asc 升序 - desc 降序

        :param order_by: The order_by of this CreateExportTaskReq.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def last_sec_min(self):
        r"""Gets the last_sec_min of this CreateExportTaskReq.

        持续时间下限

        :return: The last_sec_min of this CreateExportTaskReq.
        :rtype: int
        """
        return self._last_sec_min

    @last_sec_min.setter
    def last_sec_min(self, last_sec_min):
        r"""Sets the last_sec_min of this CreateExportTaskReq.

        持续时间下限

        :param last_sec_min: The last_sec_min of this CreateExportTaskReq.
        :type last_sec_min: int
        """
        self._last_sec_min = last_sec_min

    @property
    def last_sec_max(self):
        r"""Gets the last_sec_max of this CreateExportTaskReq.

        持续时间上限

        :return: The last_sec_max of this CreateExportTaskReq.
        :rtype: int
        """
        return self._last_sec_max

    @last_sec_max.setter
    def last_sec_max(self, last_sec_max):
        r"""Sets the last_sec_max of this CreateExportTaskReq.

        持续时间上限

        :param last_sec_max: The last_sec_max of this CreateExportTaskReq.
        :type last_sec_max: int
        """
        self._last_sec_max = last_sec_max

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
        if not isinstance(other, CreateExportTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
