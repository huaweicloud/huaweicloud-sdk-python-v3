# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Results:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eps_id': 'str',
        'log_group_name': 'str',
        'log_group_name_alias': 'str',
        'log_stream_name': 'str',
        'log_stream_name_alias': 'str',
        'time': 'str'
    }

    attribute_map = {
        'eps_id': 'eps_id',
        'log_group_name': 'log_group_name',
        'log_group_name_alias': 'log_group_name_alias',
        'log_stream_name': 'log_stream_name',
        'log_stream_name_alias': 'log_stream_name_alias',
        'time': 'time'
    }

    def __init__(self, eps_id=None, log_group_name=None, log_group_name_alias=None, log_stream_name=None, log_stream_name_alias=None, time=None):
        r"""Results

        The model defined in huaweicloud sdk

        :param eps_id: **参数解释：** 企业项目ID。 **取值范围：** 不涉及。
        :type eps_id: str
        :param log_group_name: **参数解释：** 日志组名称。 **取值范围：** 不涉及。
        :type log_group_name: str
        :param log_group_name_alias: **参数解释：** 日志组别名。 **取值范围：** 不涉及。
        :type log_group_name_alias: str
        :param log_stream_name: **参数解释：** 日志流名称。 **取值范围：** 不涉及。
        :type log_stream_name: str
        :param log_stream_name_alias: **参数解释：** 日志流别名。 **取值范围：** 不涉及。
        :type log_stream_name_alias: str
        :param time: **参数解释：** 告警统计周期，例如：1小时。 **取值范围：** 不涉及。
        :type time: str
        """
        
        

        self._eps_id = None
        self._log_group_name = None
        self._log_group_name_alias = None
        self._log_stream_name = None
        self._log_stream_name_alias = None
        self._time = None
        self.discriminator = None

        self.eps_id = eps_id
        self.log_group_name = log_group_name
        self.log_group_name_alias = log_group_name_alias
        self.log_stream_name = log_stream_name
        self.log_stream_name_alias = log_stream_name_alias
        self.time = time

    @property
    def eps_id(self):
        r"""Gets the eps_id of this Results.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :return: The eps_id of this Results.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this Results.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :param eps_id: The eps_id of this Results.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this Results.

        **参数解释：** 日志组名称。 **取值范围：** 不涉及。

        :return: The log_group_name of this Results.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this Results.

        **参数解释：** 日志组名称。 **取值范围：** 不涉及。

        :param log_group_name: The log_group_name of this Results.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_group_name_alias(self):
        r"""Gets the log_group_name_alias of this Results.

        **参数解释：** 日志组别名。 **取值范围：** 不涉及。

        :return: The log_group_name_alias of this Results.
        :rtype: str
        """
        return self._log_group_name_alias

    @log_group_name_alias.setter
    def log_group_name_alias(self, log_group_name_alias):
        r"""Sets the log_group_name_alias of this Results.

        **参数解释：** 日志组别名。 **取值范围：** 不涉及。

        :param log_group_name_alias: The log_group_name_alias of this Results.
        :type log_group_name_alias: str
        """
        self._log_group_name_alias = log_group_name_alias

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this Results.

        **参数解释：** 日志流名称。 **取值范围：** 不涉及。

        :return: The log_stream_name of this Results.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this Results.

        **参数解释：** 日志流名称。 **取值范围：** 不涉及。

        :param log_stream_name: The log_stream_name of this Results.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_stream_name_alias(self):
        r"""Gets the log_stream_name_alias of this Results.

        **参数解释：** 日志流别名。 **取值范围：** 不涉及。

        :return: The log_stream_name_alias of this Results.
        :rtype: str
        """
        return self._log_stream_name_alias

    @log_stream_name_alias.setter
    def log_stream_name_alias(self, log_stream_name_alias):
        r"""Sets the log_stream_name_alias of this Results.

        **参数解释：** 日志流别名。 **取值范围：** 不涉及。

        :param log_stream_name_alias: The log_stream_name_alias of this Results.
        :type log_stream_name_alias: str
        """
        self._log_stream_name_alias = log_stream_name_alias

    @property
    def time(self):
        r"""Gets the time of this Results.

        **参数解释：** 告警统计周期，例如：1小时。 **取值范围：** 不涉及。

        :return: The time of this Results.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Results.

        **参数解释：** 告警统计周期，例如：1小时。 **取值范围：** 不涉及。

        :param time: The time of this Results.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, Results):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
