# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveMonitorItemParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'monitor_item_id': 'int',
        'interval': 'int',
        'env_id': 'int',
        'config_value_list': 'list[ConfigItem]'
    }

    attribute_map = {
        'monitor_item_id': 'monitor_item_id',
        'interval': 'interval',
        'env_id': 'env_id',
        'config_value_list': 'config_value_list'
    }

    def __init__(self, monitor_item_id=None, interval=None, env_id=None, config_value_list=None):
        r"""SaveMonitorItemParam

        The model defined in huaweicloud sdk

        :param monitor_item_id: 监控项id。
        :type monitor_item_id: int
        :param interval: 采集间隔。
        :type interval: int
        :param env_id: 环境id。
        :type env_id: int
        :param config_value_list: 配置项列表。
        :type config_value_list: list[:class:`huaweicloudsdkapm.v1.ConfigItem`]
        """
        
        

        self._monitor_item_id = None
        self._interval = None
        self._env_id = None
        self._config_value_list = None
        self.discriminator = None

        self.monitor_item_id = monitor_item_id
        if interval is not None:
            self.interval = interval
        self.env_id = env_id
        if config_value_list is not None:
            self.config_value_list = config_value_list

    @property
    def monitor_item_id(self):
        r"""Gets the monitor_item_id of this SaveMonitorItemParam.

        监控项id。

        :return: The monitor_item_id of this SaveMonitorItemParam.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        r"""Sets the monitor_item_id of this SaveMonitorItemParam.

        监控项id。

        :param monitor_item_id: The monitor_item_id of this SaveMonitorItemParam.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def interval(self):
        r"""Gets the interval of this SaveMonitorItemParam.

        采集间隔。

        :return: The interval of this SaveMonitorItemParam.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this SaveMonitorItemParam.

        采集间隔。

        :param interval: The interval of this SaveMonitorItemParam.
        :type interval: int
        """
        self._interval = interval

    @property
    def env_id(self):
        r"""Gets the env_id of this SaveMonitorItemParam.

        环境id。

        :return: The env_id of this SaveMonitorItemParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this SaveMonitorItemParam.

        环境id。

        :param env_id: The env_id of this SaveMonitorItemParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def config_value_list(self):
        r"""Gets the config_value_list of this SaveMonitorItemParam.

        配置项列表。

        :return: The config_value_list of this SaveMonitorItemParam.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ConfigItem`]
        """
        return self._config_value_list

    @config_value_list.setter
    def config_value_list(self, config_value_list):
        r"""Sets the config_value_list of this SaveMonitorItemParam.

        配置项列表。

        :param config_value_list: The config_value_list of this SaveMonitorItemParam.
        :type config_value_list: list[:class:`huaweicloudsdkapm.v1.ConfigItem`]
        """
        self._config_value_list = config_value_list

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
        if not isinstance(other, SaveMonitorItemParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
