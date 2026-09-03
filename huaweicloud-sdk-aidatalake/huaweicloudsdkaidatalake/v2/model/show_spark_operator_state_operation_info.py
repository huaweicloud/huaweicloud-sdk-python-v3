# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkOperatorStateOperationInfo:

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
        'endpoint_name': 'str',
        'restart_strategy': 'str'
    }

    attribute_map = {
        'type': 'type',
        'endpoint_name': 'endpoint_name',
        'restart_strategy': 'restart_strategy'
    }

    def __init__(self, type=None, endpoint_name=None, restart_strategy=None):
        r"""ShowSparkOperatorStateOperationInfo

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param endpoint_name: **参数解释**：SparkSql端点名称。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 
        :type endpoint_name: str
        :param restart_strategy: **参数解释**：集群重启策略，用于指定重启方式。 **取值范围**：         - FORCE：强制重启，不等待正在运行的作业完成。 - GRACEFUL：优雅重启，等待所有正在运行的作业完成后再重启。 
        :type restart_strategy: str
        """
        
        

        self._type = None
        self._endpoint_name = None
        self._restart_strategy = None
        self.discriminator = None

        self.type = type
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if restart_strategy is not None:
            self.restart_strategy = restart_strategy

    @property
    def type(self):
        r"""Gets the type of this ShowSparkOperatorStateOperationInfo.

        :return: The type of this ShowSparkOperatorStateOperationInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSparkOperatorStateOperationInfo.

        :param type: The type of this ShowSparkOperatorStateOperationInfo.
        :type type: str
        """
        self._type = type

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ShowSparkOperatorStateOperationInfo.

        **参数解释**：SparkSql端点名称。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 

        :return: The endpoint_name of this ShowSparkOperatorStateOperationInfo.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ShowSparkOperatorStateOperationInfo.

        **参数解释**：SparkSql端点名称。 **取值范围**：只能由小写字母、数字及中划线组成，必须以小写字母开头，以小写字母或数字结尾，且长度为1~63个字符。 

        :param endpoint_name: The endpoint_name of this ShowSparkOperatorStateOperationInfo.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def restart_strategy(self):
        r"""Gets the restart_strategy of this ShowSparkOperatorStateOperationInfo.

        **参数解释**：集群重启策略，用于指定重启方式。 **取值范围**：         - FORCE：强制重启，不等待正在运行的作业完成。 - GRACEFUL：优雅重启，等待所有正在运行的作业完成后再重启。 

        :return: The restart_strategy of this ShowSparkOperatorStateOperationInfo.
        :rtype: str
        """
        return self._restart_strategy

    @restart_strategy.setter
    def restart_strategy(self, restart_strategy):
        r"""Sets the restart_strategy of this ShowSparkOperatorStateOperationInfo.

        **参数解释**：集群重启策略，用于指定重启方式。 **取值范围**：         - FORCE：强制重启，不等待正在运行的作业完成。 - GRACEFUL：优雅重启，等待所有正在运行的作业完成后再重启。 

        :param restart_strategy: The restart_strategy of this ShowSparkOperatorStateOperationInfo.
        :type restart_strategy: str
        """
        self._restart_strategy = restart_strategy

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
        if not isinstance(other, ShowSparkOperatorStateOperationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
