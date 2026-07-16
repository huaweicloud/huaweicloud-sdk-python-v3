# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreToolsLogsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'group_id': 'str',
        'stream_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'group_id': 'group_id',
        'stream_id': 'stream_id'
    }

    def __init__(self, enabled=None, group_id=None, stream_id=None):
        r"""CoreToolsLogsConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释：** 是否开启日志采集。 - 未开启，工具运行过程产生的日志无法上报至云日志服务(LTS)。 - 开启后，工具运行过程产生的日志会上报至云日志服务(LTS)。  **约束限制：** 不涉及。 **取值范围：** - true打开。 - false关闭。  **默认取值：** false。
        :type enabled: bool
        :param group_id: **参数解释：** 工具的日志组ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。
        :type group_id: str
        :param stream_id: **参数解释：** 工具的日志流ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。
        :type stream_id: str
        """
        
        

        self._enabled = None
        self._group_id = None
        self._stream_id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if group_id is not None:
            self.group_id = group_id
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def enabled(self):
        r"""Gets the enabled of this CoreToolsLogsConfig.

        **参数解释：** 是否开启日志采集。 - 未开启，工具运行过程产生的日志无法上报至云日志服务(LTS)。 - 开启后，工具运行过程产生的日志会上报至云日志服务(LTS)。  **约束限制：** 不涉及。 **取值范围：** - true打开。 - false关闭。  **默认取值：** false。

        :return: The enabled of this CoreToolsLogsConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CoreToolsLogsConfig.

        **参数解释：** 是否开启日志采集。 - 未开启，工具运行过程产生的日志无法上报至云日志服务(LTS)。 - 开启后，工具运行过程产生的日志会上报至云日志服务(LTS)。  **约束限制：** 不涉及。 **取值范围：** - true打开。 - false关闭。  **默认取值：** false。

        :param enabled: The enabled of this CoreToolsLogsConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def group_id(self):
        r"""Gets the group_id of this CoreToolsLogsConfig.

        **参数解释：** 工具的日志组ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :return: The group_id of this CoreToolsLogsConfig.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CoreToolsLogsConfig.

        **参数解释：** 工具的日志组ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :param group_id: The group_id of this CoreToolsLogsConfig.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        r"""Gets the stream_id of this CoreToolsLogsConfig.

        **参数解释：** 工具的日志流ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :return: The stream_id of this CoreToolsLogsConfig.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this CoreToolsLogsConfig.

        **参数解释：** 工具的日志流ID。 **约束限制：** 当前不支持更新、指定。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :param stream_id: The stream_id of this CoreToolsLogsConfig.
        :type stream_id: str
        """
        self._stream_id = stream_id

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
        if not isinstance(other, CoreToolsLogsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
