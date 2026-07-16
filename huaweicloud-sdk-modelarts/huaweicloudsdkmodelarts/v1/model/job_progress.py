# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'step': 'int',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'step': 'step',
        'description': 'description'
    }

    def __init__(self, status=None, step=None, description=None):
        r"""JobProgress

        The model defined in huaweicloud sdk

        :param status: **参数解释**：任务某个步骤的状态。 **取值范围**：枚举类型，取值如下： - WAITING：等待中 - PROCESSING：处理中 - FAILED：任务失败 - COMPLETED：任务完成
        :type status: str
        :param step: **参数解释**：任务的步骤。 **取值范围**：枚举类型，取值如下： - 1：准备存储 - 2：准备计算资源 - 3：配置网络 - 4：初始化实例
        :type step: int
        :param description: **参数解释**：任务某个步骤的描述。 **取值范围**：不涉及。
        :type description: str
        """
        
        

        self._status = None
        self._step = None
        self._description = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if step is not None:
            self.step = step
        if description is not None:
            self.description = description

    @property
    def status(self):
        r"""Gets the status of this JobProgress.

        **参数解释**：任务某个步骤的状态。 **取值范围**：枚举类型，取值如下： - WAITING：等待中 - PROCESSING：处理中 - FAILED：任务失败 - COMPLETED：任务完成

        :return: The status of this JobProgress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobProgress.

        **参数解释**：任务某个步骤的状态。 **取值范围**：枚举类型，取值如下： - WAITING：等待中 - PROCESSING：处理中 - FAILED：任务失败 - COMPLETED：任务完成

        :param status: The status of this JobProgress.
        :type status: str
        """
        self._status = status

    @property
    def step(self):
        r"""Gets the step of this JobProgress.

        **参数解释**：任务的步骤。 **取值范围**：枚举类型，取值如下： - 1：准备存储 - 2：准备计算资源 - 3：配置网络 - 4：初始化实例

        :return: The step of this JobProgress.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this JobProgress.

        **参数解释**：任务的步骤。 **取值范围**：枚举类型，取值如下： - 1：准备存储 - 2：准备计算资源 - 3：配置网络 - 4：初始化实例

        :param step: The step of this JobProgress.
        :type step: int
        """
        self._step = step

    @property
    def description(self):
        r"""Gets the description of this JobProgress.

        **参数解释**：任务某个步骤的描述。 **取值范围**：不涉及。

        :return: The description of this JobProgress.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobProgress.

        **参数解释**：任务某个步骤的描述。 **取值范围**：不涉及。

        :param description: The description of this JobProgress.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, JobProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
