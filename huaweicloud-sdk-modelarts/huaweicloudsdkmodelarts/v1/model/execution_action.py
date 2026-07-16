# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionAction:

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
        'policies': 'ExecutionActionPolicy',
        'parameters': 'list[WorkflowParameter]',
        'data_requirements': 'list[DataRequirement]'
    }

    attribute_map = {
        'action_name': 'action_name',
        'policies': 'policies',
        'parameters': 'parameters',
        'data_requirements': 'data_requirements'
    }

    def __init__(self, action_name=None, policies=None, parameters=None, data_requirements=None):
        r"""ExecutionAction

        The model defined in huaweicloud sdk

        :param action_name: 操作名称，枚举如下: - stop 停止 - rerun 重跑
        :type action_name: str
        :param policies: 
        :type policies: :class:`huaweicloudsdkmodelarts.v1.ExecutionActionPolicy`
        :param parameters: 参数。
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        :param data_requirements: 需要的数据。
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        
        

        self._action_name = None
        self._policies = None
        self._parameters = None
        self._data_requirements = None
        self.discriminator = None

        self.action_name = action_name
        if policies is not None:
            self.policies = policies
        if parameters is not None:
            self.parameters = parameters
        if data_requirements is not None:
            self.data_requirements = data_requirements

    @property
    def action_name(self):
        r"""Gets the action_name of this ExecutionAction.

        操作名称，枚举如下: - stop 停止 - rerun 重跑

        :return: The action_name of this ExecutionAction.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this ExecutionAction.

        操作名称，枚举如下: - stop 停止 - rerun 重跑

        :param action_name: The action_name of this ExecutionAction.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def policies(self):
        r"""Gets the policies of this ExecutionAction.

        :return: The policies of this ExecutionAction.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ExecutionActionPolicy`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ExecutionAction.

        :param policies: The policies of this ExecutionAction.
        :type policies: :class:`huaweicloudsdkmodelarts.v1.ExecutionActionPolicy`
        """
        self._policies = policies

    @property
    def parameters(self):
        r"""Gets the parameters of this ExecutionAction.

        参数。

        :return: The parameters of this ExecutionAction.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ExecutionAction.

        参数。

        :param parameters: The parameters of this ExecutionAction.
        :type parameters: list[:class:`huaweicloudsdkmodelarts.v1.WorkflowParameter`]
        """
        self._parameters = parameters

    @property
    def data_requirements(self):
        r"""Gets the data_requirements of this ExecutionAction.

        需要的数据。

        :return: The data_requirements of this ExecutionAction.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        return self._data_requirements

    @data_requirements.setter
    def data_requirements(self, data_requirements):
        r"""Sets the data_requirements of this ExecutionAction.

        需要的数据。

        :param data_requirements: The data_requirements of this ExecutionAction.
        :type data_requirements: list[:class:`huaweicloudsdkmodelarts.v1.DataRequirement`]
        """
        self._data_requirements = data_requirements

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
        if not isinstance(other, ExecutionAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
