# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'deployment_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'deployment_id': 'deployment_id'
    }

    def __init__(self, type=None, status=None, log_group_id=None, log_stream_id=None, deployment_id=None):
        r"""LogConfigResponse

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 日志输出类型。 **取值范围：** - STDOUT：日志输出到控制台或终端。 - EVENT：k8s事件。
        :type type: str
        :param status: **参数解释：** 日志服务状态。 **取值范围：** - ON：开启。 - OFF：关闭。
        :type status: str
        :param log_group_id: **参数解释：** 日志组ID，用户选择自己已有的日志组，不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type log_group_id: str
        :param log_stream_id: **参数解释：** 日志流id，用户选择自己已有的日志组。不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type log_stream_id: str
        :param deployment_id: **参数解释：** 日志流对应的部署ID。当日志策略为default或pool时有值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type deployment_id: str
        """
        
        

        self._type = None
        self._status = None
        self._log_group_id = None
        self._log_stream_id = None
        self._deployment_id = None
        self.discriminator = None

        self.type = type
        self.status = status
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if deployment_id is not None:
            self.deployment_id = deployment_id

    @property
    def type(self):
        r"""Gets the type of this LogConfigResponse.

        **参数解释：** 日志输出类型。 **取值范围：** - STDOUT：日志输出到控制台或终端。 - EVENT：k8s事件。

        :return: The type of this LogConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LogConfigResponse.

        **参数解释：** 日志输出类型。 **取值范围：** - STDOUT：日志输出到控制台或终端。 - EVENT：k8s事件。

        :param type: The type of this LogConfigResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this LogConfigResponse.

        **参数解释：** 日志服务状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :return: The status of this LogConfigResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LogConfigResponse.

        **参数解释：** 日志服务状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :param status: The status of this LogConfigResponse.
        :type status: str
        """
        self._status = status

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LogConfigResponse.

        **参数解释：** 日志组ID，用户选择自己已有的日志组，不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The log_group_id of this LogConfigResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LogConfigResponse.

        **参数解释：** 日志组ID，用户选择自己已有的日志组，不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param log_group_id: The log_group_id of this LogConfigResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LogConfigResponse.

        **参数解释：** 日志流id，用户选择自己已有的日志组。不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The log_stream_id of this LogConfigResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LogConfigResponse.

        **参数解释：** 日志流id，用户选择自己已有的日志组。不填时，会自动创建。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param log_stream_id: The log_stream_id of this LogConfigResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this LogConfigResponse.

        **参数解释：** 日志流对应的部署ID。当日志策略为default或pool时有值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The deployment_id of this LogConfigResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this LogConfigResponse.

        **参数解释：** 日志流对应的部署ID。当日志策略为default或pool时有值。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param deployment_id: The deployment_id of this LogConfigResponse.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

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
        if not isinstance(other, LogConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
