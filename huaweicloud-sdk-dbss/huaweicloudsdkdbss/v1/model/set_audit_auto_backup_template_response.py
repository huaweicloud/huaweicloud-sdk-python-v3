# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetAuditAutoBackupTemplateResponse(SdkResponse):

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
        'latest_backup_time': 'datetime',
        'status': 'int',
        'trigger_time': 'datetime',
        'triggered': 'bool'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'bucket_root_path': 'bucket_root_path',
        'cycle': 'cycle',
        'latest_backup_time': 'latest_backup_time',
        'status': 'status',
        'trigger_time': 'trigger_time',
        'triggered': 'triggered'
    }

    def __init__(self, bucket_name=None, bucket_root_path=None, cycle=None, latest_backup_time=None, status=None, trigger_time=None, triggered=None):
        r"""SetAuditAutoBackupTemplateResponse

        The model defined in huaweicloud sdk

        :param bucket_name: OBS桶名称
        :type bucket_name: str
        :param bucket_root_path: OBS备份根路径
        :type bucket_root_path: str
        :param cycle: 周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟
        :type cycle: str
        :param latest_backup_time: 最近备份时间
        :type latest_backup_time: datetime
        :param status: 备份开关  - 0：关闭  - 1：开启
        :type status: int
        :param trigger_time: 触发时间
        :type trigger_time: datetime
        :param triggered: 是否已触发
        :type triggered: bool
        """
        
        super(SetAuditAutoBackupTemplateResponse, self).__init__()

        self._bucket_name = None
        self._bucket_root_path = None
        self._cycle = None
        self._latest_backup_time = None
        self._status = None
        self._trigger_time = None
        self._triggered = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_root_path is not None:
            self.bucket_root_path = bucket_root_path
        if cycle is not None:
            self.cycle = cycle
        if latest_backup_time is not None:
            self.latest_backup_time = latest_backup_time
        if status is not None:
            self.status = status
        if trigger_time is not None:
            self.trigger_time = trigger_time
        if triggered is not None:
            self.triggered = triggered

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetAuditAutoBackupTemplateResponse.

        OBS桶名称

        :return: The bucket_name of this SetAuditAutoBackupTemplateResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetAuditAutoBackupTemplateResponse.

        OBS桶名称

        :param bucket_name: The bucket_name of this SetAuditAutoBackupTemplateResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_root_path(self):
        r"""Gets the bucket_root_path of this SetAuditAutoBackupTemplateResponse.

        OBS备份根路径

        :return: The bucket_root_path of this SetAuditAutoBackupTemplateResponse.
        :rtype: str
        """
        return self._bucket_root_path

    @bucket_root_path.setter
    def bucket_root_path(self, bucket_root_path):
        r"""Sets the bucket_root_path of this SetAuditAutoBackupTemplateResponse.

        OBS备份根路径

        :param bucket_root_path: The bucket_root_path of this SetAuditAutoBackupTemplateResponse.
        :type bucket_root_path: str
        """
        self._bucket_root_path = bucket_root_path

    @property
    def cycle(self):
        r"""Gets the cycle of this SetAuditAutoBackupTemplateResponse.

        周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟

        :return: The cycle of this SetAuditAutoBackupTemplateResponse.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this SetAuditAutoBackupTemplateResponse.

        周期 - PER_DAY：每天 - PER_WEEK：每周 - PER_MONTH：每月 - PER_HOUR：每小时 - FIVE_MIN：每5分钟

        :param cycle: The cycle of this SetAuditAutoBackupTemplateResponse.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def latest_backup_time(self):
        r"""Gets the latest_backup_time of this SetAuditAutoBackupTemplateResponse.

        最近备份时间

        :return: The latest_backup_time of this SetAuditAutoBackupTemplateResponse.
        :rtype: datetime
        """
        return self._latest_backup_time

    @latest_backup_time.setter
    def latest_backup_time(self, latest_backup_time):
        r"""Sets the latest_backup_time of this SetAuditAutoBackupTemplateResponse.

        最近备份时间

        :param latest_backup_time: The latest_backup_time of this SetAuditAutoBackupTemplateResponse.
        :type latest_backup_time: datetime
        """
        self._latest_backup_time = latest_backup_time

    @property
    def status(self):
        r"""Gets the status of this SetAuditAutoBackupTemplateResponse.

        备份开关  - 0：关闭  - 1：开启

        :return: The status of this SetAuditAutoBackupTemplateResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SetAuditAutoBackupTemplateResponse.

        备份开关  - 0：关闭  - 1：开启

        :param status: The status of this SetAuditAutoBackupTemplateResponse.
        :type status: int
        """
        self._status = status

    @property
    def trigger_time(self):
        r"""Gets the trigger_time of this SetAuditAutoBackupTemplateResponse.

        触发时间

        :return: The trigger_time of this SetAuditAutoBackupTemplateResponse.
        :rtype: datetime
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        r"""Sets the trigger_time of this SetAuditAutoBackupTemplateResponse.

        触发时间

        :param trigger_time: The trigger_time of this SetAuditAutoBackupTemplateResponse.
        :type trigger_time: datetime
        """
        self._trigger_time = trigger_time

    @property
    def triggered(self):
        r"""Gets the triggered of this SetAuditAutoBackupTemplateResponse.

        是否已触发

        :return: The triggered of this SetAuditAutoBackupTemplateResponse.
        :rtype: bool
        """
        return self._triggered

    @triggered.setter
    def triggered(self, triggered):
        r"""Sets the triggered of this SetAuditAutoBackupTemplateResponse.

        是否已触发

        :param triggered: The triggered of this SetAuditAutoBackupTemplateResponse.
        :type triggered: bool
        """
        self._triggered = triggered

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
        if not isinstance(other, SetAuditAutoBackupTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
