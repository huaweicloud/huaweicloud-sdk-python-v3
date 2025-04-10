# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonitorItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'env_id': 'int',
        'collector_id': 'int',
        'collector_name': 'str',
        'display_name': 'str',
        'collect_interval': 'int',
        'disabled': 'bool',
        'status_change_user_id': 'str',
        'status_change_user_name': 'str',
        'status_change_time': 'str',
        'config_change_user_id': 'str',
        'config_change_user_name': 'str',
        'config_change_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'env_id': 'env_id',
        'collector_id': 'collector_id',
        'collector_name': 'collector_name',
        'display_name': 'display_name',
        'collect_interval': 'collect_interval',
        'disabled': 'disabled',
        'status_change_user_id': 'status_change_user_id',
        'status_change_user_name': 'status_change_user_name',
        'status_change_time': 'status_change_time',
        'config_change_user_id': 'config_change_user_id',
        'config_change_user_name': 'config_change_user_name',
        'config_change_time': 'config_change_time'
    }

    def __init__(self, id=None, env_id=None, collector_id=None, collector_name=None, display_name=None, collect_interval=None, disabled=None, status_change_user_id=None, status_change_user_name=None, status_change_time=None, config_change_user_id=None, config_change_user_name=None, config_change_time=None):
        r"""MonitorItem

        The model defined in huaweicloud sdk

        :param id: 监控项id。
        :type id: int
        :param env_id: 环境id。
        :type env_id: int
        :param collector_id: 采集器id。
        :type collector_id: int
        :param collector_name: 采集器名称。
        :type collector_name: str
        :param display_name: 采集器展示名称。
        :type display_name: str
        :param collect_interval: 采集间隔。
        :type collect_interval: int
        :param disabled: 是否禁用。
        :type disabled: bool
        :param status_change_user_id: 修改采集状态用户id。
        :type status_change_user_id: str
        :param status_change_user_name: 修改采集状态用户名称。
        :type status_change_user_name: str
        :param status_change_time: 修改采集状态时间。
        :type status_change_time: str
        :param config_change_user_id: 修改采集配置用户id。
        :type config_change_user_id: str
        :param config_change_user_name: 修改采集配置用户名称。
        :type config_change_user_name: str
        :param config_change_time: 修改采集配置时间。
        :type config_change_time: str
        """
        
        

        self._id = None
        self._env_id = None
        self._collector_id = None
        self._collector_name = None
        self._display_name = None
        self._collect_interval = None
        self._disabled = None
        self._status_change_user_id = None
        self._status_change_user_name = None
        self._status_change_time = None
        self._config_change_user_id = None
        self._config_change_user_name = None
        self._config_change_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if env_id is not None:
            self.env_id = env_id
        if collector_id is not None:
            self.collector_id = collector_id
        if collector_name is not None:
            self.collector_name = collector_name
        if display_name is not None:
            self.display_name = display_name
        if collect_interval is not None:
            self.collect_interval = collect_interval
        if disabled is not None:
            self.disabled = disabled
        if status_change_user_id is not None:
            self.status_change_user_id = status_change_user_id
        if status_change_user_name is not None:
            self.status_change_user_name = status_change_user_name
        if status_change_time is not None:
            self.status_change_time = status_change_time
        if config_change_user_id is not None:
            self.config_change_user_id = config_change_user_id
        if config_change_user_name is not None:
            self.config_change_user_name = config_change_user_name
        if config_change_time is not None:
            self.config_change_time = config_change_time

    @property
    def id(self):
        r"""Gets the id of this MonitorItem.

        监控项id。

        :return: The id of this MonitorItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MonitorItem.

        监控项id。

        :param id: The id of this MonitorItem.
        :type id: int
        """
        self._id = id

    @property
    def env_id(self):
        r"""Gets the env_id of this MonitorItem.

        环境id。

        :return: The env_id of this MonitorItem.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this MonitorItem.

        环境id。

        :param env_id: The env_id of this MonitorItem.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def collector_id(self):
        r"""Gets the collector_id of this MonitorItem.

        采集器id。

        :return: The collector_id of this MonitorItem.
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        r"""Sets the collector_id of this MonitorItem.

        采集器id。

        :param collector_id: The collector_id of this MonitorItem.
        :type collector_id: int
        """
        self._collector_id = collector_id

    @property
    def collector_name(self):
        r"""Gets the collector_name of this MonitorItem.

        采集器名称。

        :return: The collector_name of this MonitorItem.
        :rtype: str
        """
        return self._collector_name

    @collector_name.setter
    def collector_name(self, collector_name):
        r"""Sets the collector_name of this MonitorItem.

        采集器名称。

        :param collector_name: The collector_name of this MonitorItem.
        :type collector_name: str
        """
        self._collector_name = collector_name

    @property
    def display_name(self):
        r"""Gets the display_name of this MonitorItem.

        采集器展示名称。

        :return: The display_name of this MonitorItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this MonitorItem.

        采集器展示名称。

        :param display_name: The display_name of this MonitorItem.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def collect_interval(self):
        r"""Gets the collect_interval of this MonitorItem.

        采集间隔。

        :return: The collect_interval of this MonitorItem.
        :rtype: int
        """
        return self._collect_interval

    @collect_interval.setter
    def collect_interval(self, collect_interval):
        r"""Sets the collect_interval of this MonitorItem.

        采集间隔。

        :param collect_interval: The collect_interval of this MonitorItem.
        :type collect_interval: int
        """
        self._collect_interval = collect_interval

    @property
    def disabled(self):
        r"""Gets the disabled of this MonitorItem.

        是否禁用。

        :return: The disabled of this MonitorItem.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this MonitorItem.

        是否禁用。

        :param disabled: The disabled of this MonitorItem.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def status_change_user_id(self):
        r"""Gets the status_change_user_id of this MonitorItem.

        修改采集状态用户id。

        :return: The status_change_user_id of this MonitorItem.
        :rtype: str
        """
        return self._status_change_user_id

    @status_change_user_id.setter
    def status_change_user_id(self, status_change_user_id):
        r"""Sets the status_change_user_id of this MonitorItem.

        修改采集状态用户id。

        :param status_change_user_id: The status_change_user_id of this MonitorItem.
        :type status_change_user_id: str
        """
        self._status_change_user_id = status_change_user_id

    @property
    def status_change_user_name(self):
        r"""Gets the status_change_user_name of this MonitorItem.

        修改采集状态用户名称。

        :return: The status_change_user_name of this MonitorItem.
        :rtype: str
        """
        return self._status_change_user_name

    @status_change_user_name.setter
    def status_change_user_name(self, status_change_user_name):
        r"""Sets the status_change_user_name of this MonitorItem.

        修改采集状态用户名称。

        :param status_change_user_name: The status_change_user_name of this MonitorItem.
        :type status_change_user_name: str
        """
        self._status_change_user_name = status_change_user_name

    @property
    def status_change_time(self):
        r"""Gets the status_change_time of this MonitorItem.

        修改采集状态时间。

        :return: The status_change_time of this MonitorItem.
        :rtype: str
        """
        return self._status_change_time

    @status_change_time.setter
    def status_change_time(self, status_change_time):
        r"""Sets the status_change_time of this MonitorItem.

        修改采集状态时间。

        :param status_change_time: The status_change_time of this MonitorItem.
        :type status_change_time: str
        """
        self._status_change_time = status_change_time

    @property
    def config_change_user_id(self):
        r"""Gets the config_change_user_id of this MonitorItem.

        修改采集配置用户id。

        :return: The config_change_user_id of this MonitorItem.
        :rtype: str
        """
        return self._config_change_user_id

    @config_change_user_id.setter
    def config_change_user_id(self, config_change_user_id):
        r"""Sets the config_change_user_id of this MonitorItem.

        修改采集配置用户id。

        :param config_change_user_id: The config_change_user_id of this MonitorItem.
        :type config_change_user_id: str
        """
        self._config_change_user_id = config_change_user_id

    @property
    def config_change_user_name(self):
        r"""Gets the config_change_user_name of this MonitorItem.

        修改采集配置用户名称。

        :return: The config_change_user_name of this MonitorItem.
        :rtype: str
        """
        return self._config_change_user_name

    @config_change_user_name.setter
    def config_change_user_name(self, config_change_user_name):
        r"""Sets the config_change_user_name of this MonitorItem.

        修改采集配置用户名称。

        :param config_change_user_name: The config_change_user_name of this MonitorItem.
        :type config_change_user_name: str
        """
        self._config_change_user_name = config_change_user_name

    @property
    def config_change_time(self):
        r"""Gets the config_change_time of this MonitorItem.

        修改采集配置时间。

        :return: The config_change_time of this MonitorItem.
        :rtype: str
        """
        return self._config_change_time

    @config_change_time.setter
    def config_change_time(self, config_change_time):
        r"""Sets the config_change_time of this MonitorItem.

        修改采集配置时间。

        :param config_change_time: The config_change_time of this MonitorItem.
        :type config_change_time: str
        """
        self._config_change_time = config_change_time

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
        if not isinstance(other, MonitorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
