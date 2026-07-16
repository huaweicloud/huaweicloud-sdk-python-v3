# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_time': 'int',
        'concurrency': 'int',
        'continue_on_exception': 'bool'
    }

    attribute_map = {
        'execution_time': 'execution_time',
        'concurrency': 'concurrency',
        'continue_on_exception': 'continue_on_exception'
    }

    def __init__(self, execution_time=None, concurrency=None, continue_on_exception=None):
        r"""RuntimeConfig

        The model defined in huaweicloud sdk

        :param execution_time: **参数解释：** 任务的预定执行时间（Unix 时间戳）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type execution_time: int
        :param concurrency: **参数解释：** 任务执行的并发数配置。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 - 100。 **默认取值：** 不涉及。 
        :type concurrency: int
        :param continue_on_exception: **参数解释：** 异常处理策略，是否在遇到非致命异常时继续。 **约束限制：** 不涉及。 **取值范围：** true, false。 **默认取值：** 不涉及。 
        :type continue_on_exception: bool
        """
        
        

        self._execution_time = None
        self._concurrency = None
        self._continue_on_exception = None
        self.discriminator = None

        self.execution_time = execution_time
        if concurrency is not None:
            self.concurrency = concurrency
        if continue_on_exception is not None:
            self.continue_on_exception = continue_on_exception

    @property
    def execution_time(self):
        r"""Gets the execution_time of this RuntimeConfig.

        **参数解释：** 任务的预定执行时间（Unix 时间戳）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The execution_time of this RuntimeConfig.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this RuntimeConfig.

        **参数解释：** 任务的预定执行时间（Unix 时间戳）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param execution_time: The execution_time of this RuntimeConfig.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def concurrency(self):
        r"""Gets the concurrency of this RuntimeConfig.

        **参数解释：** 任务执行的并发数配置。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 - 100。 **默认取值：** 不涉及。 

        :return: The concurrency of this RuntimeConfig.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        r"""Sets the concurrency of this RuntimeConfig.

        **参数解释：** 任务执行的并发数配置。 **约束限制：** 1到100之间的整数。 **取值范围：** 1 - 100。 **默认取值：** 不涉及。 

        :param concurrency: The concurrency of this RuntimeConfig.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def continue_on_exception(self):
        r"""Gets the continue_on_exception of this RuntimeConfig.

        **参数解释：** 异常处理策略，是否在遇到非致命异常时继续。 **约束限制：** 不涉及。 **取值范围：** true, false。 **默认取值：** 不涉及。 

        :return: The continue_on_exception of this RuntimeConfig.
        :rtype: bool
        """
        return self._continue_on_exception

    @continue_on_exception.setter
    def continue_on_exception(self, continue_on_exception):
        r"""Sets the continue_on_exception of this RuntimeConfig.

        **参数解释：** 异常处理策略，是否在遇到非致命异常时继续。 **约束限制：** 不涉及。 **取值范围：** true, false。 **默认取值：** 不涉及。 

        :param continue_on_exception: The continue_on_exception of this RuntimeConfig.
        :type continue_on_exception: bool
        """
        self._continue_on_exception = continue_on_exception

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
        if not isinstance(other, RuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
