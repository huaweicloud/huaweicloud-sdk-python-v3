# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfiguration:

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
        'cluster_id': 'str',
        'obs_bucket': 'str',
        'agency': 'str',
        'update_at': 'int',
        'base_path': 'str',
        'auto_enable': 'bool',
        'period': 'str',
        'log_switch': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'clusterId',
        'obs_bucket': 'obsBucket',
        'agency': 'agency',
        'update_at': 'updateAt',
        'base_path': 'basePath',
        'auto_enable': 'autoEnable',
        'period': 'period',
        'log_switch': 'logSwitch'
    }

    def __init__(self, id=None, cluster_id=None, obs_bucket=None, agency=None, update_at=None, base_path=None, auto_enable=None, period=None, log_switch=None):
        r"""LogConfiguration

        The model defined in huaweicloud sdk

        :param id: 日志备份ID，通过系统UUID生成。
        :type id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param obs_bucket: 用于存储日志的OBS桶的桶名。
        :type obs_bucket: str
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param update_at: 更新时间。格式为：Unix时间戳格式。
        :type update_at: int
        :param base_path: 日志在OBS桶中的备份路径。
        :type base_path: str
        :param auto_enable: 自动备份开关。 - true: 自动备份开启。 - false: 自动备份关闭。
        :type auto_enable: bool
        :param period: 自动备份日志开始时间。当autoEnable为false时该字段为null。格式为：格林威治标准时间。
        :type period: str
        :param log_switch: 日志开关。 - true: 日志开启。 - false: 日志关闭。
        :type log_switch: bool
        """
        
        

        self._id = None
        self._cluster_id = None
        self._obs_bucket = None
        self._agency = None
        self._update_at = None
        self._base_path = None
        self._auto_enable = None
        self._period = None
        self._log_switch = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if agency is not None:
            self.agency = agency
        if update_at is not None:
            self.update_at = update_at
        if base_path is not None:
            self.base_path = base_path
        if auto_enable is not None:
            self.auto_enable = auto_enable
        if period is not None:
            self.period = period
        if log_switch is not None:
            self.log_switch = log_switch

    @property
    def id(self):
        r"""Gets the id of this LogConfiguration.

        日志备份ID，通过系统UUID生成。

        :return: The id of this LogConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogConfiguration.

        日志备份ID，通过系统UUID生成。

        :param id: The id of this LogConfiguration.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this LogConfiguration.

        集群ID。

        :return: The cluster_id of this LogConfiguration.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this LogConfiguration.

        集群ID。

        :param cluster_id: The cluster_id of this LogConfiguration.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this LogConfiguration.

        用于存储日志的OBS桶的桶名。

        :return: The obs_bucket of this LogConfiguration.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this LogConfiguration.

        用于存储日志的OBS桶的桶名。

        :param obs_bucket: The obs_bucket of this LogConfiguration.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def agency(self):
        r"""Gets the agency of this LogConfiguration.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this LogConfiguration.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this LogConfiguration.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this LogConfiguration.
        :type agency: str
        """
        self._agency = agency

    @property
    def update_at(self):
        r"""Gets the update_at of this LogConfiguration.

        更新时间。格式为：Unix时间戳格式。

        :return: The update_at of this LogConfiguration.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this LogConfiguration.

        更新时间。格式为：Unix时间戳格式。

        :param update_at: The update_at of this LogConfiguration.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def base_path(self):
        r"""Gets the base_path of this LogConfiguration.

        日志在OBS桶中的备份路径。

        :return: The base_path of this LogConfiguration.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        r"""Sets the base_path of this LogConfiguration.

        日志在OBS桶中的备份路径。

        :param base_path: The base_path of this LogConfiguration.
        :type base_path: str
        """
        self._base_path = base_path

    @property
    def auto_enable(self):
        r"""Gets the auto_enable of this LogConfiguration.

        自动备份开关。 - true: 自动备份开启。 - false: 自动备份关闭。

        :return: The auto_enable of this LogConfiguration.
        :rtype: bool
        """
        return self._auto_enable

    @auto_enable.setter
    def auto_enable(self, auto_enable):
        r"""Sets the auto_enable of this LogConfiguration.

        自动备份开关。 - true: 自动备份开启。 - false: 自动备份关闭。

        :param auto_enable: The auto_enable of this LogConfiguration.
        :type auto_enable: bool
        """
        self._auto_enable = auto_enable

    @property
    def period(self):
        r"""Gets the period of this LogConfiguration.

        自动备份日志开始时间。当autoEnable为false时该字段为null。格式为：格林威治标准时间。

        :return: The period of this LogConfiguration.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this LogConfiguration.

        自动备份日志开始时间。当autoEnable为false时该字段为null。格式为：格林威治标准时间。

        :param period: The period of this LogConfiguration.
        :type period: str
        """
        self._period = period

    @property
    def log_switch(self):
        r"""Gets the log_switch of this LogConfiguration.

        日志开关。 - true: 日志开启。 - false: 日志关闭。

        :return: The log_switch of this LogConfiguration.
        :rtype: bool
        """
        return self._log_switch

    @log_switch.setter
    def log_switch(self, log_switch):
        r"""Sets the log_switch of this LogConfiguration.

        日志开关。 - true: 日志开启。 - false: 日志关闭。

        :param log_switch: The log_switch of this LogConfiguration.
        :type log_switch: bool
        """
        self._log_switch = log_switch

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
        if not isinstance(other, LogConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
