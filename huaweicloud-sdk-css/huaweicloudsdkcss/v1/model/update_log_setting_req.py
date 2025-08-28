# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogSettingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency': 'str',
        'log_base_path': 'str',
        'log_bucket': 'str',
        'index_prefix': 'str',
        'keep_days': 'int',
        'target_cluster_id': 'str',
        'auto_enable': 'bool',
        'period': 'str'
    }

    attribute_map = {
        'agency': 'agency',
        'log_base_path': 'log_base_path',
        'log_bucket': 'log_bucket',
        'index_prefix': 'index_prefix',
        'keep_days': 'keep_days',
        'target_cluster_id': 'target_cluster_id',
        'auto_enable': 'auto_enable',
        'period': 'period'
    }

    def __init__(self, agency=None, log_base_path=None, log_bucket=None, index_prefix=None, keep_days=None, target_cluster_id=None, auto_enable=None, period=None):
        r"""UpdateLogSettingReq

        The model defined in huaweicloud sdk

        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param log_base_path: 日志在OBS桶中的备份路径。
        :type log_base_path: str
        :param log_bucket: 用于存储日志的OBS桶的桶名。
        :type log_bucket: str
        :param index_prefix: 设置保存日志的索引前缀。
        :type index_prefix: str
        :param keep_days: 修改日志保存的天数。
        :type keep_days: int
        :param target_cluster_id: 设置保存日志的目标集群ID。
        :type target_cluster_id: str
        :param auto_enable: 集群日志是否开启自动备份。
        :type auto_enable: bool
        :param period: 集群日志备份开始时间。
        :type period: str
        """
        
        

        self._agency = None
        self._log_base_path = None
        self._log_bucket = None
        self._index_prefix = None
        self._keep_days = None
        self._target_cluster_id = None
        self._auto_enable = None
        self._period = None
        self.discriminator = None

        self.agency = agency
        self.log_base_path = log_base_path
        self.log_bucket = log_bucket
        if index_prefix is not None:
            self.index_prefix = index_prefix
        if keep_days is not None:
            self.keep_days = keep_days
        if target_cluster_id is not None:
            self.target_cluster_id = target_cluster_id
        if auto_enable is not None:
            self.auto_enable = auto_enable
        if period is not None:
            self.period = period

    @property
    def agency(self):
        r"""Gets the agency of this UpdateLogSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpdateLogSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpdateLogSettingReq.
        :type agency: str
        """
        self._agency = agency

    @property
    def log_base_path(self):
        r"""Gets the log_base_path of this UpdateLogSettingReq.

        日志在OBS桶中的备份路径。

        :return: The log_base_path of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._log_base_path

    @log_base_path.setter
    def log_base_path(self, log_base_path):
        r"""Sets the log_base_path of this UpdateLogSettingReq.

        日志在OBS桶中的备份路径。

        :param log_base_path: The log_base_path of this UpdateLogSettingReq.
        :type log_base_path: str
        """
        self._log_base_path = log_base_path

    @property
    def log_bucket(self):
        r"""Gets the log_bucket of this UpdateLogSettingReq.

        用于存储日志的OBS桶的桶名。

        :return: The log_bucket of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._log_bucket

    @log_bucket.setter
    def log_bucket(self, log_bucket):
        r"""Sets the log_bucket of this UpdateLogSettingReq.

        用于存储日志的OBS桶的桶名。

        :param log_bucket: The log_bucket of this UpdateLogSettingReq.
        :type log_bucket: str
        """
        self._log_bucket = log_bucket

    @property
    def index_prefix(self):
        r"""Gets the index_prefix of this UpdateLogSettingReq.

        设置保存日志的索引前缀。

        :return: The index_prefix of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._index_prefix

    @index_prefix.setter
    def index_prefix(self, index_prefix):
        r"""Sets the index_prefix of this UpdateLogSettingReq.

        设置保存日志的索引前缀。

        :param index_prefix: The index_prefix of this UpdateLogSettingReq.
        :type index_prefix: str
        """
        self._index_prefix = index_prefix

    @property
    def keep_days(self):
        r"""Gets the keep_days of this UpdateLogSettingReq.

        修改日志保存的天数。

        :return: The keep_days of this UpdateLogSettingReq.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this UpdateLogSettingReq.

        修改日志保存的天数。

        :param keep_days: The keep_days of this UpdateLogSettingReq.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def target_cluster_id(self):
        r"""Gets the target_cluster_id of this UpdateLogSettingReq.

        设置保存日志的目标集群ID。

        :return: The target_cluster_id of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._target_cluster_id

    @target_cluster_id.setter
    def target_cluster_id(self, target_cluster_id):
        r"""Sets the target_cluster_id of this UpdateLogSettingReq.

        设置保存日志的目标集群ID。

        :param target_cluster_id: The target_cluster_id of this UpdateLogSettingReq.
        :type target_cluster_id: str
        """
        self._target_cluster_id = target_cluster_id

    @property
    def auto_enable(self):
        r"""Gets the auto_enable of this UpdateLogSettingReq.

        集群日志是否开启自动备份。

        :return: The auto_enable of this UpdateLogSettingReq.
        :rtype: bool
        """
        return self._auto_enable

    @auto_enable.setter
    def auto_enable(self, auto_enable):
        r"""Sets the auto_enable of this UpdateLogSettingReq.

        集群日志是否开启自动备份。

        :param auto_enable: The auto_enable of this UpdateLogSettingReq.
        :type auto_enable: bool
        """
        self._auto_enable = auto_enable

    @property
    def period(self):
        r"""Gets the period of this UpdateLogSettingReq.

        集群日志备份开始时间。

        :return: The period of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this UpdateLogSettingReq.

        集群日志备份开始时间。

        :param period: The period of this UpdateLogSettingReq.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, UpdateLogSettingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
