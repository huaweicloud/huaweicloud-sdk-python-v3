# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'min_wait_time': 'int',
        'default_wait_time': 'int',
        'min_exec_time': 'int',
        'default_exec_time': 'int'
    }

    attribute_map = {
        'action': 'action',
        'min_wait_time': 'min_wait_time',
        'default_wait_time': 'default_wait_time',
        'min_exec_time': 'min_exec_time',
        'default_exec_time': 'default_exec_time'
    }

    def __init__(self, action=None, min_wait_time=None, default_wait_time=None, min_exec_time=None, default_exec_time=None):
        r"""ActionConfig

        The model defined in huaweicloud sdk

        :param action: 动作名称。STOP：关机，HIBERNATE：休眠，REBOOT：重启，EXECUTE_SCRIPT：执行脚本。
        :type action: str
        :param min_wait_time: 最小等待时长，单位分钟。如果不填，则使用父级的 min_wait_time。
        :type min_wait_time: int
        :param default_wait_time: 默认等待时长，单位分钟。如果不填，则使用父级的 default_wait_time。
        :type default_wait_time: int
        :param min_exec_time: 最小执行周期，单位分钟。如果不填，则使用父级的 min_exec_time。
        :type min_exec_time: int
        :param default_exec_time: 默认执行周期，单位分钟。如果不填，则使用父级的 default_exec_time。
        :type default_exec_time: int
        """
        
        

        self._action = None
        self._min_wait_time = None
        self._default_wait_time = None
        self._min_exec_time = None
        self._default_exec_time = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if min_wait_time is not None:
            self.min_wait_time = min_wait_time
        if default_wait_time is not None:
            self.default_wait_time = default_wait_time
        if min_exec_time is not None:
            self.min_exec_time = min_exec_time
        if default_exec_time is not None:
            self.default_exec_time = default_exec_time

    @property
    def action(self):
        r"""Gets the action of this ActionConfig.

        动作名称。STOP：关机，HIBERNATE：休眠，REBOOT：重启，EXECUTE_SCRIPT：执行脚本。

        :return: The action of this ActionConfig.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ActionConfig.

        动作名称。STOP：关机，HIBERNATE：休眠，REBOOT：重启，EXECUTE_SCRIPT：执行脚本。

        :param action: The action of this ActionConfig.
        :type action: str
        """
        self._action = action

    @property
    def min_wait_time(self):
        r"""Gets the min_wait_time of this ActionConfig.

        最小等待时长，单位分钟。如果不填，则使用父级的 min_wait_time。

        :return: The min_wait_time of this ActionConfig.
        :rtype: int
        """
        return self._min_wait_time

    @min_wait_time.setter
    def min_wait_time(self, min_wait_time):
        r"""Sets the min_wait_time of this ActionConfig.

        最小等待时长，单位分钟。如果不填，则使用父级的 min_wait_time。

        :param min_wait_time: The min_wait_time of this ActionConfig.
        :type min_wait_time: int
        """
        self._min_wait_time = min_wait_time

    @property
    def default_wait_time(self):
        r"""Gets the default_wait_time of this ActionConfig.

        默认等待时长，单位分钟。如果不填，则使用父级的 default_wait_time。

        :return: The default_wait_time of this ActionConfig.
        :rtype: int
        """
        return self._default_wait_time

    @default_wait_time.setter
    def default_wait_time(self, default_wait_time):
        r"""Sets the default_wait_time of this ActionConfig.

        默认等待时长，单位分钟。如果不填，则使用父级的 default_wait_time。

        :param default_wait_time: The default_wait_time of this ActionConfig.
        :type default_wait_time: int
        """
        self._default_wait_time = default_wait_time

    @property
    def min_exec_time(self):
        r"""Gets the min_exec_time of this ActionConfig.

        最小执行周期，单位分钟。如果不填，则使用父级的 min_exec_time。

        :return: The min_exec_time of this ActionConfig.
        :rtype: int
        """
        return self._min_exec_time

    @min_exec_time.setter
    def min_exec_time(self, min_exec_time):
        r"""Sets the min_exec_time of this ActionConfig.

        最小执行周期，单位分钟。如果不填，则使用父级的 min_exec_time。

        :param min_exec_time: The min_exec_time of this ActionConfig.
        :type min_exec_time: int
        """
        self._min_exec_time = min_exec_time

    @property
    def default_exec_time(self):
        r"""Gets the default_exec_time of this ActionConfig.

        默认执行周期，单位分钟。如果不填，则使用父级的 default_exec_time。

        :return: The default_exec_time of this ActionConfig.
        :rtype: int
        """
        return self._default_exec_time

    @default_exec_time.setter
    def default_exec_time(self, default_exec_time):
        r"""Sets the default_exec_time of this ActionConfig.

        默认执行周期，单位分钟。如果不填，则使用父级的 default_exec_time。

        :param default_exec_time: The default_exec_time of this ActionConfig.
        :type default_exec_time: int
        """
        self._default_exec_time = default_exec_time

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
        if not isinstance(other, ActionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
