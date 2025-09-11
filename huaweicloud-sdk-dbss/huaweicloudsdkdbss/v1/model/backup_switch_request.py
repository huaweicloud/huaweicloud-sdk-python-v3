# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupSwitchRequest:

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
        'bucket_root_path': 'str',
        'cycle': 'str',
        'mode': 'str',
        'status': 'int',
        'trigger_time': 'datetime'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'bucket_root_path': 'bucket_root_path',
        'cycle': 'cycle',
        'mode': 'mode',
        'status': 'status',
        'trigger_time': 'trigger_time'
    }

    def __init__(self, bucket_name=None, bucket_root_path=None, cycle=None, mode=None, status=None, trigger_time=None):
        r"""BackupSwitchRequest

        The model defined in huaweicloud sdk

        :param bucket_name: OBS桶名称
        :type bucket_name: str
        :param bucket_root_path: 备份根路径
        :type bucket_root_path: str
        :param cycle: 备份周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟
        :type cycle: str
        :param mode: 备份模式  - AUTO：自动备份
        :type mode: str
        :param status: 开关状态  - 0：关闭  - 1：开启
        :type status: int
        :param trigger_time: 触发时间，yyyy-MM-dd HH:mm:ss
        :type trigger_time: datetime
        """
        
        

        self._bucket_name = None
        self._bucket_root_path = None
        self._cycle = None
        self._mode = None
        self._status = None
        self._trigger_time = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if bucket_root_path is not None:
            self.bucket_root_path = bucket_root_path
        self.cycle = cycle
        self.mode = mode
        self.status = status
        self.trigger_time = trigger_time

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this BackupSwitchRequest.

        OBS桶名称

        :return: The bucket_name of this BackupSwitchRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this BackupSwitchRequest.

        OBS桶名称

        :param bucket_name: The bucket_name of this BackupSwitchRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_root_path(self):
        r"""Gets the bucket_root_path of this BackupSwitchRequest.

        备份根路径

        :return: The bucket_root_path of this BackupSwitchRequest.
        :rtype: str
        """
        return self._bucket_root_path

    @bucket_root_path.setter
    def bucket_root_path(self, bucket_root_path):
        r"""Sets the bucket_root_path of this BackupSwitchRequest.

        备份根路径

        :param bucket_root_path: The bucket_root_path of this BackupSwitchRequest.
        :type bucket_root_path: str
        """
        self._bucket_root_path = bucket_root_path

    @property
    def cycle(self):
        r"""Gets the cycle of this BackupSwitchRequest.

        备份周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟

        :return: The cycle of this BackupSwitchRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this BackupSwitchRequest.

        备份周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟

        :param cycle: The cycle of this BackupSwitchRequest.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def mode(self):
        r"""Gets the mode of this BackupSwitchRequest.

        备份模式  - AUTO：自动备份

        :return: The mode of this BackupSwitchRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this BackupSwitchRequest.

        备份模式  - AUTO：自动备份

        :param mode: The mode of this BackupSwitchRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def status(self):
        r"""Gets the status of this BackupSwitchRequest.

        开关状态  - 0：关闭  - 1：开启

        :return: The status of this BackupSwitchRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupSwitchRequest.

        开关状态  - 0：关闭  - 1：开启

        :param status: The status of this BackupSwitchRequest.
        :type status: int
        """
        self._status = status

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this BackupSwitchRequest.

        触发时间，yyyy-MM-dd HH:mm:ss

        :return: The trigger_time of this BackupSwitchRequest.
        :rtype: datetime
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this BackupSwitchRequest.

        触发时间，yyyy-MM-dd HH:mm:ss

        :param trigger_time: The trigger_time of this BackupSwitchRequest.
        :type trigger_time: datetime
        """
        self._trigger_time = trigger_time

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
        if not isinstance(other, BackupSwitchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
