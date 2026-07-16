# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepExecutionAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name': 'str',
        'data_requirements': 'list[DataRequirement]',
        'parameters': 'list[WorkflowParameter]'
    }

    attribute_map = {
        'action_name': 'action_name',
        'data_requirements': 'data_requirements',
        'parameters': 'parameters'
    }

    def __init__(self, action_name=None, data_requirements=None, parameters=None):
        r"""StepExecutionAction

        The model defined in huaweicloud sdk

        :param action_name: 操作名称，枚举如下:  - retry 重试  - stop 停止  - continue 继续
        :type action_name: str
        :param data_requirements: 
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        :param parameters: 
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        
        

        self._action_name = None
        self._data_requirements = None
        self._parameters = None
        self.discriminator = None

        self.action_name = action_name
        if data_requirements is not None:
            self.data_requirements = data_requirements
        if parameters is not None:
            self.parameters = parameters

    @property
    def action_name(self):
        r"""Gets the action_name of this StepExecutionAction.

        操作名称，枚举如下:  - retry 重试  - stop 停止  - continue 继续

        :return: The action_name of this StepExecutionAction.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this StepExecutionAction.

        操作名称，枚举如下:  - retry 重试  - stop 停止  - continue 继续

        :param action_name: The action_name of this StepExecutionAction.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def data_requirements(self):
        r"""Gets the data_requirements of this StepExecutionAction.

        :return: The data_requirements of this StepExecutionAction.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        return self._data_requirements

    @data_requirements.setter
    def data_requirements(self, data_requirements):
        r"""Sets the data_requirements of this StepExecutionAction.

        :param data_requirements: The data_requirements of this StepExecutionAction.
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        self._data_requirements = data_requirements

    @property
    def parameters(self):
        r"""Gets the parameters of this StepExecutionAction.

        :return: The parameters of this StepExecutionAction.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this StepExecutionAction.

        :param parameters: The parameters of this StepExecutionAction.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        self._parameters = parameters

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
        if not isinstance(other, StepExecutionAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
